# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMapDialog
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and
 upload imagery from/to the OAM catalog.
                             -------------------
        begin                : 2015-07-01
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email                : tassia@acaia.ca  / yoji.salut@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os, sys

from PyQt4 import QtGui, uic
from PyQt4.Qt import *

from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer, QgsMessageLog
from osgeo import gdal, osr
import json
import time
import math, imghdr

# Modules needed for upload
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/oam_client_dialog_base.ui'))

class ImageUploaderDialog(QtGui.QDialog, FORM_CLASS):

    def __init__(self, iface, imgSettings, imgMetadata, parent=None):
        """Constructor."""
        super(ImageUploaderDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        #add QGISMessageBar bar on the dialog
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout().addWidget(self.bar)

        """modify this part later!"""
        #img_settings = QSettings('QGIS','oam-qgis-plugin')
        self.settings = imgSettings
        self.metadata = imgMetadata

        self.loadLayers()
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()

        # make sure about this function...
        self.loadFullMetadata()

        #register event handlers
        # Imagery tab connections
        self.layers_tool_button.clicked.connect(self.loadLayers)
        self.file_tool_button.clicked.connect(self.selectFile)
        self.add_source_button.clicked.connect(self.addSources)
        self.remove_source_button.clicked.connect(self.removeSources)
        self.up_source_button.clicked.connect(self.upSource)
        self.down_source_button.clicked.connect(self.downSource)
        self.imagery_next_button.clicked.connect(self.nextTab)

        # Metadata tab connections
        self.sense_start_edit.setCalendarPopup(1)
        self.sense_start_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.sense_end_edit.setCalendarPopup(1)
        self.sense_end_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.default_button.clicked.connect(self.loadMetadataSettings)
        self.clean_button.clicked.connect(self.cleanMetadataSettings)
        self.save_button.clicked.connect(self.saveMetadata)
        self.metadata_next_button.clicked.connect(self.nextTab)
        self.metadata_previous_button.clicked.connect(self.previousTab)

        # Upload tab connections
        self.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)
        self.upload_button.clicked.connect(self.startUploader)
        self.quit_button.clicked.connect(self.closeDialog)
        self.upload_previous_button.clicked.connect(self.previousTab)

        #make sure about this function
        #self.exec_()

    # event handling for tab paging
    def nextTab(self):
        self.tab_widget.setCurrentIndex(self.tab_widget.currentIndex()+1)

    def previousTab(self):
        self.tab_widget.setCurrentIndex(self.tab_widget.currentIndex()-1)

    def closeDialog(self):
        #return imgSettigs and imgMetadata?
        self.close()

    # event handling for imagery tab
    def loadLayers(self):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if not self.layers_list_widget.findItems(layer.name(),Qt.MatchExactly):
                item = QListWidgetItem()
                item.setText(layer.name())
                item.setData(Qt.UserRole, layer.dataProvider().dataSourceUri())
                self.layers_list_widget.addItem(item)
        self.bar.clearWidgets()
        self.bar.pushMessage(
            "INFO",
            "Source imagery for upload must be selected from layers or files.",
            level=QgsMessageBar.INFO)

    def selectFile(self):
        selected_file = QFileDialog.getOpenFileName(
            self,
            'Select File',
            os.path.expanduser("~"))
        self.source_file_edit.setText(selected_file)

    def addSources(self):
        filename = self.source_file_edit.text()
        selected_layers = self.layers_list_widget.selectedItems()
        if not filename and not selected_layers:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'WARNING',
                'Either a layer or file must be selected to be added',
                level=QgsMessageBar.WARNING)
        if filename:
            if self.validateFile(filename):
                if not self.sources_list_widget.findItems(filename,Qt.MatchExactly):
                    item = QListWidgetItem()
                    item.setText(os.path.basename(filename))
                    item.setData(Qt.UserRole, filename)
                    self.sources_list_widget.addItem(item)
                    self.added_sources_list_widget.addItem(item.clone())
                    self.source_file_edit.setText('')
        if selected_layers:
            for item in selected_layers:
                if self.validateLayer(item.text()):
                    if not self.sources_list_widget.findItems(item.text(),Qt.MatchExactly):
                        self.layers_list_widget.takeItem(self.layers_list_widget.row(item))
                        self.sources_list_widget.addItem(item)
                        self.added_sources_list_widget.addItem(item.clone())
        self.bar.clearWidgets()
        self.bar.pushMessage(
            'INFO',
            'Select sources were added to the upload queue',
            level=QgsMessageBar.INFO)
        self.loadFullMetadata()

    def removeSources(self):
        selected_sources = self.sources_list_widget.selectedItems()
        added_sources = self.added_sources_list_widget.selectedItems()
        if selected_sources:
            for item in selected_sources:
                self.sources_list_widget.takeItem(self.sources_list_widget.row(item))
                added_item = self.added_sources_list_widget.findItems(item.text(),Qt.MatchExactly)
                if added_item:
                    self.added_sources_list_widget.takeItem(self.added_sources_list_widget.row(added_item[0]))
                all_layers = self.iface.mapCanvas().layers()
                for layer in all_layers:
                    if item.text() == layer.name():
                        if not self.layers_list_widget.findItems(item.text(),Qt.MatchExactly):
                            self.layers_list_widget.addItem(item)
        else:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'WARNING',
                'An imagery source must be selected to be removed',
                level=QgsMessageBar.WARNING)

    def upSource(self):
        selected_layers = self.sources_list_widget.selectedItems()
        if selected_layers:
            position = self.sources_list_widget.row(selected_layers[0])
            if position > 0:
                item = self.sources_list_widget.takeItem(position)
                self.sources_list_widget.insertItem(position-1,item)
                item.setSelected(1)

    def downSource(self):
        selected_layers = self.sources_list_widget.selectedItems()
        if selected_layers:
            position = self.sources_list_widget.row(selected_layers[0])
            if position < self.sources_list_widget.count()-1:
                item = self.sources_list_widget.takeItem(position)
                self.sources_list_widget.insertItem(position+1,item)
                item.setSelected(1)

    # event handling for metadata tab
    def loadMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.title_edit.setText(self.settings.value('TITLE'))

        if self.settings.value('PLATFORM') == None:
            self.title_edit.setCursorPosition(0)
        else:
            self.platform_combo_box.setCurrentIndex(int(self.settings.value('PLATFORM')))

        self.platform_combo_box.setCurrentIndex(0)
        self.sensor_edit.setText(self.settings.value('SENSOR'))
        self.sensor_edit.setCursorPosition(0)
        self.sense_start_edit.setDate(QDateTime.fromString(
            self.settings.value('SENSE_START'),
            Qt.ISODate).date())
        self.sense_start_edit.setTime(
            QDateTime.fromString(self.settings.value('SENSE_START'),
            Qt.ISODate).time())
        self.sense_end_edit.setDate(
            QDateTime.fromString(self.settings.value('SENSE_END'),
            Qt.ISODate).date())
        self.sense_end_edit.setTime(
            QDateTime.fromString(self.settings.value('SENSE_END'),
            Qt.ISODate).time())

        if self.settings.value('TAGS') == None:
            self.tags_edit.setText(', '.join(''))
        else:
            self.tags_edit.setText(', '.join(self.settings.value('TAGS')))

        self.tags_edit.setCursorPosition(0)
        self.provider_edit.setText(self.settings.value('PROVIDER'))
        self.provider_edit.setCursorPosition(0)
        self.contact_edit.setText(self.settings.value('CONTACT'))
        self.contact_edit.setCursorPosition(0)
        self.website_edit.setText(self.settings.value('WEBSITE'))
        self.website_edit.setCursorPosition(0)
        self.settings.endGroup()

    def cleanMetadataSettings(self):
        self.title_edit.setText('')
        self.platform_combo_box.setCurrentIndex(0)
        self.sensor_edit.setText('')
        self.sense_start_edit.setDate(
            QDateTime().fromString('1970-01-01T00:00:00',
            Qt.ISODate).date())
        self.sense_start_edit.setTime(
            QDateTime().fromString('1970-01-01T00:00:00',
            Qt.ISODate).time())
        self.sense_end_edit.setDate(
            QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).date())
        self.sense_end_edit.setTime(
            QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).time())
        self.tags_edit.setText('')
        self.provider_edit.setText('')
        self.contact_edit.setText('')
        self.website_edit.setText('')

    def saveMetadata(self):
        selected_layers = self.added_sources_list_widget.selectedItems()
        if selected_layers:
            for item in selected_layers:
                filename = item.data(Qt.UserRole)
                self.metadata[filename] = {}
                self.extractMetadata(filename)
                self.loadInputMetadata(filename)
                json_string = json.dumps(self.metadata[filename],indent=4,separators=(',', ': '))
                json_filename = os.path.splitext(filename)[0]+'.json'
                json_file = open(json_filename, 'w')
                print >> json_file, json_string
                json_file.close()

            self.loadFullMetadata()
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'INFO',
                'Metadata for the selected sources was saved',
                level=QgsMessageBar.INFO)
        else:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'WARNING',
                'One or more source imagery must be selected to have the metadata saved.',
                level=QgsMessageBar.WARNING)

    # event handling for upload tab
    # also see multi-thred for startUploader function
    def enableSpecify(self):
        if self.storage_combo_box.currentIndex() == 1:
            self.specify_label.setEnabled(1)
            self.specify_edit.setEnabled(1)
        else:
            self.specify_label.setEnabled(0)
            self.specify_edit.setText('')
            self.specify_edit.setEnabled(0)

    def loadStorageSettings(self):
        self.settings.beginGroup("Storage")
        bucket = self.settings.value('S3_BUCKET_NAME')
        storage_index = self.storage_combo_box.findText(bucket,Qt.MatchExactly)
        if not storage_index == -1:
            self.storage_combo_box.setCurrentIndex(storage_index)
        else:
            self.storage_combo_box.setCurrentIndex(self.storage_combo_box.findText(self.tr('other...')))
            self.specify_label.setEnabled(1)
            self.specify_edit.setEnabled(1)
            self.specify_edit.setText(self.settings.value('S3_BUCKET_NAME'))
        self.key_id_edit.setText(self.settings.value('AWS_ACCESS_KEY_ID'))
        self.key_id_edit.setCursorPosition(0)
        self.secret_key_edit.setText(self.settings.value('AWS_SECRET_ACCESS_KEY'))
        self.secret_key_edit.setCursorPosition(0)
        self.settings.endGroup()

    def loadOptionsSettings(self):
        self.settings.beginGroup("Options")
        if self.settings.value('NOTIFY_OAM'):
            self.notify_oam_check.setCheckState(2)
        if self.settings.value('TRIGGER_OAM_TS'):
            self.trigger_tiling_check.setCheckState(2)
        if self.settings.value('REPROJECT'):
            self.notify_oam_check.setCheckState(2)
        if self.settings.value('CONVERT_GEOTIFF_RGB'):
            self.notify_oam_check.setCheckState(2)
        self.settings.endGroup()

    # other functions
    def validateFile(self,filename):
        if not os.path.isfile(filename):
            self.bar.clearWidgets()
            self.bar.pushMessage(
                "CRITICAL",
                "The file %s does not exist" % filename,
                level=QgsMessageBar.CRITICAL)
            return 0
        elif imghdr.what(filename) is None:
            print imghdr.what(filename)
            self.bar.clearWidgets()
            self.bar.pushMessage(
                "CRITICAL",
                "The file %s is not a supported data source" % filename,
                level=QgsMessageBar.CRITICAL)
            return 0
        else:
            return 1

    def validateLayer(self,layer_name):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if layer_name == layer.name():
                if layer.type() == QgsMapLayer.VectorLayer:
                    self.bar.clearWidgets()
                    self.bar.pushMessage(
                        "CRITICAL",
                        "Vector layers cannot be selected for upload",
                        level=QgsMessageBar.CRITICAL)
                    return 0
                else:
                    return 1

    def extractMetadata(self,filename):
        """Extract filesize, projection, bbox and gsd from image file"""

        self.metadata[filename]['File size'] = os.stat(filename).st_size

        datafile = gdal.Open(filename,gdal.GA_ReadOnly)
        if datafile is None:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'CRITICAL',
                'Extraction of raster metadata failed.',
                level=QgsMessageBar.CRITICAL)

        # projection
        projInfo = datafile.GetProjection()
        spatialRef = osr.SpatialReference()
        #print "WKT format: " + str(spatialRef)
        spatialRef.ImportFromWkt(projInfo)
        spatialRefProj = spatialRef.ExportToProj4()
        #print "Proj4 format: " + str(spatialRefProj)
        self.metadata[filename]['Projection'] = str(spatialRefProj)

        #bbox
        upper_left = self.GDALInfoReportCorner(datafile,0.0,0.0 );
        lower_left = self.GDALInfoReportCorner(datafile,0.0,datafile.RasterYSize);
        upper_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,0.0 );
        lower_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,datafile.RasterYSize );
        center = self.GDALInfoReportCorner(datafile,datafile.RasterXSize/2.0,datafile.RasterYSize/2.0 );
        self.metadata[filename]['BBOX'] = (upper_left,lower_left,upper_right,lower_right)

    def GDALInfoReportCorner(self,hDataset,x,y):
        """GDALInfoReportCorner: extracted and adapted from the python port of gdalinfo"""

        # Transform the point into georeferenced coordinates
        adfGeoTransform = hDataset.GetGeoTransform(can_return_null = True)
        if adfGeoTransform is not None:
            dfGeoX = adfGeoTransform[0] + adfGeoTransform[1] * x + adfGeoTransform[2] * y
            dfGeoY = adfGeoTransform[3] + adfGeoTransform[4] * x + adfGeoTransform[5] * y
        else:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'WARNING',
                'BBOX might be wrong. Transformation coefficient could not be fetched from raster.',
                level=QgsMessageBar.WARNING)
            return (x,y)

        # Report the georeferenced coordinates
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            return ("(%12.7f,%12.7f) " % (dfGeoX, dfGeoY ))
        else:
            return ("(%12.3f,%12.3f) " % (dfGeoX, dfGeoY ))

    def loadInputMetadata(self, filename):
        self.metadata[filename]['Title'] = self.title_edit.text()
        self.metadata[filename]['Platform'] = self.platform_combo_box.currentIndex()
        self.metadata[filename]['Sensor'] = self.sensor_edit.text()
        start = QDateTime()
        start.setDate(self.sense_start_edit.date())
        start.setTime(self.sense_start_edit.time())
        self.metadata[filename]['Sensor start'] = start.toString(Qt.ISODate)
        end = QDateTime()
        end.setDate(self.sense_end_edit.date())
        end.setTime(self.sense_end_edit.time())
        self.metadata[filename]['Sensor end'] = end.toString(Qt.ISODate)
        self.metadata[filename]['Tags'] = self.tags_edit.text()
        self.metadata[filename]['Provider'] = self.provider_edit.text()
        self.metadata[filename]['Contact'] = self.contact_edit.text()
        self.metadata[filename]['Website'] = self.website_edit.text()

    def loadFullMetadata(self):
        for index in xrange(self.sources_list_widget.count()):
            jsonfile = os.path.splitext(str(self.sources_list_widget.item(index).data(Qt.UserRole)))[0]+'.json'
            self.metadata_review_browser.setSource(QUrl().fromLocalFile(jsonfile))



    '''functions for threading purpose'''
    def startConnection(self):
        if self.storage_combo_box.currentIndex() == 0:
            bucket_name = 'oam-qgis-plugin-test'
        else:
            bucket_name = str(self.specify_edit.text())
            if not bucket_name:
                self.bar.clearWidgets()
                self.bar.pushMessage(
                    'WARNING',
                    'The bucket for upload must be provided',
                    level=QgsMessageBar.CRITICAL)

        bucket_key = str(self.key_id_edit.text())
        bucket_secret = str(self.secret_key_edit.text())

        self.bucket = None
        for trial in xrange(3):
            if self.bucket: break
            try:
                connection = S3Connection(bucket_key,bucket_secret)
                self.bucket = connection.get_bucket(bucket_name)
                QgsMessageLog.logMessage(
                    'INFO',
                    'Connection established' % trial,
                    level=QgsMessageLog.INFO)
            except:
                if trial == 2:
                   QgsMessageLog.logMessage(
                    'CRITICAL',
                    'Failed to connect after 3 attempts',
                    level=QgsMessageLog.CRITICAL)
        return self.bucket

    def startUploader(self):
        if self.startConnection():
            for index in xrange(self.sources_list_widget.count()):
                filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))

                # create a new uploader instance
                uploader = Uploader(filename,self.bucket)
                QgsMessageLog.logMessage(
                    'started uploader\n',
                    level=QgsMessageLog.CRITICAL)

                # configure the QgsMessageBar
                messageBar = self.bar.createMessage('Performing upload...', )
                progressBar = QProgressBar()
                progressBar.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
                cancelButton = QPushButton()
                cancelButton.setText('Cancel')
                cancelButton.clicked.connect(uploader.kill)
                messageBar.layout().addWidget(progressBar)
                messageBar.layout().addWidget(cancelButton)
                self.bar.clearWidgets()
                self.bar.pushWidget(messageBar, level=QgsMessageBar.INFO)
                self.messageBar = messageBar

                # start the worker in a new thread
                thread = QThread(self)
                uploader.moveToThread(thread)
                uploader.finished.connect(self.uploaderFinished)
                uploader.error.connect(self.uploaderError)
                uploader.progress.connect(progressBar.setValue)
                thread.started.connect(uploader.run)
                thread.start()
                self.thread = thread
                self.uploader = uploader
        else:
            print "error"

    def uploaderFinished(self, success):
        # clean up the uploader and thread
        self.uploader.deleteLater()
        self.thread.quit()
        self.thread.wait()
        self.thread.deleteLater()
        # remove widget from message bar
        self.bar.popWidget(self.messageBar)
        if success:
            # report the result
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'INFO',
                'Upload completed with success.',
                level=QgsMessageBar.INFO)
            QgsMessageLog.logMessage(
                'Upload succeeded',
                level=QgsMessageLog.CRITICAL)
        else:
            # notify the user that something went wrong
            self.bar.pushMessage(
                'CRITICAL',
                'Upload could not be completeded.',
                level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage(
                'Upload failed',
                level=QgsMessageLog.CRITICAL)

    def uploaderError(self, e, exception_string):
        QgsMessageLog.logMessage(
            'Uploader thread raised an exception:\n'.format(exception_string),
            level=QgsMessageLog.CRITICAL)


class Uploader(QObject):
    '''Handle uploads in a separate thread'''

    finished = pyqtSignal(bool)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float)

    def __init__(self,filename,bucket):
        QObject.__init__(self)
        self.filename = filename
        self.bucket = bucket
        self.killed = False

    def sendMetadata(self):
        jsonfile = os.path.splitext(self.filename)[0]+'.json'
        try:
            k = Key(self.bucket)
            k.key = os.path.basename(jsonfile)
            k.set_contents_from_filename(jsonfile)
            QgsMessageLog.logMessage(
                'Sent %s\n' % jsonfile,
                level=QgsMessageLog.CRITICAL)
        except:
            QgsMessageLog.logMessage(
                'Could not send %s\n' % jsonfile,
                level=QgsMessageLog.CRITICAL)

    def run(self):
        self.sendMetadata()
        success = False
        try:
            file_size = os.stat(self.filename).st_size
            chunk_size = 5242880
            chunk_count = int(math.ceil(file_size / float(chunk_size)))
            progress_count = 0

            multipart = self.bucket.initiate_multipart_upload(os.path.basename(self.filename))

            QgsMessageLog.logMessage(
                'About to send %s chunks\n' % chunk_count,
                level=QgsMessageLog.CRITICAL)

            for i in range(chunk_count):
                if self.killed is True:
                    # kill request received, exit loop early
                    break
                offset = chunk_size * i
                # bytes are set to never exceed the original file size.
                bytes = min(chunk_size, file_size - offset)
                with FileChunkIO(self.filename, 'r', offset=offset, bytes=bytes) as fp:
                    multipart.upload_part_from_file(fp, part_num=i + 1)
                progress_count += 1
                QgsMessageLog.logMessage(
                    'chunk %d\n' % progress_count,
                    level=QgsMessageLog.CRITICAL)
                self.progress.emit(progress_count / float(chunk_count)*100)
                QgsMessageLog.logMessage(
                    'progress %f' % (progress_count / float(chunk_count)),
                    level=QgsMessageLog.CRITICAL)
            if self.killed is False:
                multipart.complete_upload()
                self.progress.emit(100)
                success = True
        except Exception, e:
            # forward the exception upstream
            self.error.emit(e, traceback.format_exc())
        self.finished.emit(success)

    def kill(self):
        self.killed = True
