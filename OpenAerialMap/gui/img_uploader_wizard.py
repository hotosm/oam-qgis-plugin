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
from osgeo import gdal, osr, ogr
import json, time
import math, imghdr

# Modules needed for upload
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import traceback
import requests, json
from ast import literal_eval

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_uploader_wizard.ui'))

class ImgUploaderWizard(QtGui.QWizard, FORM_CLASS):

    def __init__(self, iface, settings, parent=None):
        """Constructor."""
        super(ImgUploaderWizard, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        # Message bars need to be attached to pages, since the wizard object
        # does not have a layout. It doesn't work to attach the same bar
        # object to all pages (it is only shown in the last one). The only way
        # I could make it work was to create different QgsMessageBar objects,
        # one per page, but it is very to keep track of those references
        # along the code. It is messy, there should be a better solution.

        self.bar0 = QgsMessageBar()
        self.bar0.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.page(0).layout().addWidget(self.bar0)

        self.bar1 = QgsMessageBar()
        self.bar1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.page(1).layout().addWidget(self.bar1)

        self.bar2 = QgsMessageBar()
        self.bar2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.page(2).layout().addWidget(self.bar2)

        self.setButtonText(QtGui.QWizard.CustomButton1, self.tr("&Start upload"));
        self.setOption(QtGui.QWizard.HaveCustomButton1, True);

        self.settings = settings

        # Dictionaries to save imagery info (todo: defined as a classes in the future)
        self.metadata = {}
        self.reprojected = []
        self.licensed = []

        # Initialize layers and default settings
        self.loadLayers()
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()

        # register event handlers
        """ List of page navigation buttons in QWizard, for reference.
        Please comment out and implement following functions if necessary."""
        #self.button(QWizard.BackButton).clicked.connect(self.previousPage)
        #self.button(QWizard.NextButton).clicked.connect(self.nextPage)
        #self.button(QWizard.FinishButton).clicked.connect(self.finishWizard)
        #self.button(QWizard.CancelButton).clicked.connect(self.cancelWizard)

        # Imagery connections (wizard page 1)
        self.layers_tool_button.clicked.connect(self.loadLayers)
        self.file_tool_button.clicked.connect(self.selectFile)
        self.add_source_button.clicked.connect(self.addSources)
        self.remove_source_button.clicked.connect(self.removeSources)
        self.up_source_button.clicked.connect(self.upSource)
        self.down_source_button.clicked.connect(self.downSource)

        # Metadata connections (wizard page 2)
        self.sense_start_edit.setCalendarPopup(1)
        self.sense_start_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.sense_end_edit.setCalendarPopup(1)
        self.sense_end_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.default_button.clicked.connect(self.loadMetadataSettings)
        self.clean_button.clicked.connect(self.cleanMetadataSettings)
        self.save_button.clicked.connect(self.saveMetadata)

        # Upload tab connections (wizard page 3)
        self.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)
        self.customButtonClicked.connect(self.startUploader)

    # event handling for wizard page 1
    def loadLayers(self):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if not self.layers_list_widget.findItems(layer.name(),Qt.MatchExactly):
                item = QListWidgetItem()
                item.setText(layer.name())
                item.setData(Qt.UserRole, layer.dataProvider().dataSourceUri())
                self.layers_list_widget.addItem(item)

    def selectFile(self):
        selected_file = QFileDialog.getOpenFileName(
            self,
            'Select imagery file',
            os.path.expanduser("~"))
        self.source_file_edit.setText(selected_file)

    def addSources(self):
        filename = self.source_file_edit.text()
        selected_layers = self.layers_list_widget.selectedItems()
        if not filename and not selected_layers:
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                'WARNING',
                'Either a layer or file should be selected to be added',
                level=QgsMessageBar.WARNING)
        else:
            added = False
            if filename:
                if self.validateFile(filename):
                    if not self.sources_list_widget.findItems(filename,Qt.MatchExactly):
                        item = QListWidgetItem()
                        item.setText(os.path.basename(filename))
                        item.setData(Qt.UserRole, filename)
                        self.sources_list_widget.addItem(item)
                        self.added_sources_list_widget.addItem(item.clone())
                        self.source_file_edit.setText('')
                        added = True
            if selected_layers:
                for item in selected_layers:
                    if self.validateLayer(item.text()):
                        if not self.sources_list_widget.findItems(item.text(),Qt.MatchExactly):
                            self.layers_list_widget.takeItem(self.layers_list_widget.row(item))
                            self.sources_list_widget.addItem(item)
                            self.added_sources_list_widget.addItem(item.clone())
                            added = True
            if added:
                self.bar0.clearWidgets()
                self.bar0.pushMessage(
                    'INFO',
                    'Source(s) added to the upload queue',
                    level=QgsMessageBar.INFO)
                self.loadMetadataReviewBox()

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
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
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

    # event handling for wizard page 2
    def loadMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.title_edit.setText(self.settings.value('TITLE'))

        if self.settings.value('PLATFORM') == None:
            self.platform_combo_box.setCurrentIndex(0)
        else:
            self.platform_combo_box.setCurrentIndex(int(self.settings.value('PLATFORM')))

        self.sensor_edit.setText(self.settings.value('SENSOR'))
        self.sensor_edit.setCursorPosition(0)

        """
        self.sense_start_edit.setDateTime(QDateTime(self.settings.value('SENSE_START')))
        self.sense_end_edit.setDateTime(QDateTime(self.settings.value('SENSE_END')))

        """
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

        self.tags_edit.setText(self.settings.value('TAGS'))
        self.tags_edit.setCursorPosition(0)
        self.provider_edit.setText(self.settings.value('PROVIDER'))
        self.provider_edit.setCursorPosition(0)
        self.contact_edit.setText(self.settings.value('CONTACT'))
        self.contact_edit.setCursorPosition(0)
        self.website_edit.setText(self.settings.value('WEBSITE'))
        self.website_edit.setCursorPosition(0)

        """
        Boolean values are converted into string and lower case for
        'if' statement, since PyQt sometimes returns 'true', just like C++,
        instead of 'True', Python style.
        Maybe we can use integer values (0 or 1), instead of using string.
        """
        if str(self.settings.value('LICENSE')).lower() == 'true':
            self.license_check_box.setCheckState(2)
        if str(self.settings.value('REPROJECT')).lower() == 'true':
            self.reproject_check_box.setCheckState(2)

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
        self.license_check_box.setCheckState(0)
        self.reproject_check_box.setCheckState(0)

    def saveMetadata(self):
        selected_layers = self.added_sources_list_widget.selectedItems()
        if selected_layers:
            for item in selected_layers:
                filename = item.data(Qt.UserRole)
                self.loadImageryInfo(filename)
                json_string = json.dumps(self.metadata[filename],indent=4,separators=(',', ': '))
                if filename not in self.reprojected:
                    json_filename = os.path.splitext(filename)[0]+'.json'
                else:
                    # to avoid repetition of "EPSG3857" in filename:
                    if not "EPSG3857" in filename:
                        json_filename = os.path.splitext(filename)[0]+'_EPSG3857.json'
                json_file = open(json_filename, 'w')
                print >> json_file, json_string
                json_file.close()

            self.loadMetadataReviewBox()
            self.bar1.clearWidgets()
            self.bar1.pushMessage(
                'INFO',
                'Metadata for the selected sources were saved',
                level=QgsMessageBar.INFO)
        else:
            self.bar1.clearWidgets()
            self.bar1.pushMessage(
                'WARNING',
                'One or more source imagery should be selected to have the metadata saved',
                level=QgsMessageBar.WARNING)

    # event handling for wizard page 3
    # also see multi-thread for startUploader function
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

        """
        Boolean values are converted into string and lower case for
        'if' statement, since PyQt sometimes returns 'true', just like C++,
        instead of 'True', Python style.
        Maybe we can use integer values (0 or 1), instead of using string.
        """
        if str(self.settings.value('NOTIFY_OAM')).lower() == 'true':
            self.notify_oam_check.setCheckState(2)
        if str(self.settings.value('TRIGGER_OAM_TS')).lower() == 'true':
            self.trigger_tiling_check.setCheckState(2)

        self.settings.endGroup()

    # other functions
    def validateFile(self,filename):
        # check that file exists
        if not os.path.exists(filename):
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                "CRITICAL",
                "The file %s does not exist" % filename,
                level=QgsMessageBar.CRITICAL)
            return False
        # check that file is an image
        if imghdr.what(filename) is None:
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                "CRITICAL",
                "The file %s is not a supported data source" % filename,
                level=QgsMessageBar.CRITICAL)
            return False
        # check if gdal can read file
        try:
            raster = gdal.Open(filename,gdal.GA_ReadOnly)
        except:
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                "CRITICAL",
                "GDAL could not read file %s" % filename,
                level=QgsMessageBar.CRITICAL)
            return False
        # check that image has at least 3 bands
        if raster.RasterCount < 3:
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                "CRITICAL",
                "The file %s has less than 3 raster bands" % filename,
                level=QgsMessageBar.CRITICAL)
            return False
        # check if projection is set
        if raster.GetProjection() is '':
            self.bar0.clearWidgets()
            self.bar0.pushMessage(
                "CRITICAL",
                "Could not extract projection from file %s" % filename,
                level=QgsMessageBar.CRITICAL)
            return False
        # finally, check if bbox has valid data
        xy_points = [(0.0,0.0),(0.0,raster.RasterYSize),(raster.RasterXSize,0.0),(raster.RasterXSize,raster.RasterYSize)]
        for point in xy_points:
            if point != self.GDALInfoReportCorner(raster,point[0],point[1]):
                QgsMessageLog.logMessage(
                    'File %s is a valid data source' % filename,
                    'OAM',
                    level=QgsMessageLog.INFO)
                return True

    def validateLayer(self,layer_name):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if layer_name == layer.name():
                if layer.type() == QgsMapLayer.VectorLayer:
                    self.bar0.clearWidgets()
                    self.bar0.pushMessage(
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
            self.bar1.clearWidgets()
            self.bar1.pushMessage(
                'CRITICAL',
                'Extraction of raster metadata failed',
                level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage(
                'Failed to extract metadata',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        else:
            # extract projection
            projInfo = datafile.GetProjection()
            # WKT format
            spatialRef = osr.SpatialReference()
            spatialRef.ImportFromWkt(projInfo)
            # Proj4 format
            spatialRefProj = spatialRef.ExportToProj4()

            self.metadata[filename]['Projection'] = str(spatialRefProj)

            # original bbox
            upper_left = self.GDALInfoReportCorner(datafile,0.0,0.0 );
            lower_left = self.GDALInfoReportCorner(datafile,0.0,datafile.RasterYSize);
            upper_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,0.0 );
            lower_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,datafile.RasterYSize );
            center = self.GDALInfoReportCorner(datafile,datafile.RasterXSize/2.0,datafile.RasterYSize/2.0 );

            # get new bbox values if reprojection will happen
            try:
                if filename in self.reprojected:
                    self.metadata[filename]['Projection'] = "EPSG:3857"
                    target = osr.SpatialReference()
                    target.ImportFromEPSG(3857)
                    transform = osr.CoordinateTransformation(spatialRef,target)

                    point = ogr.CreateGeometryFromWkt("POINT (%f %f)" % (upper_left[0],upper_left[1]))
                    point.Transform(transform)
                    upper_left = json.loads(point.ExportToJson())['coordinates']

                    point = ogr.CreateGeometryFromWkt("POINT (%f %f)" % (lower_left[0],lower_left[1]))
                    point.Transform(transform)
                    lower_left = json.loads(point.ExportToJson())['coordinates']

                    point = ogr.CreateGeometryFromWkt("POINT (%f %f)" % (upper_right[0],upper_right[1]))
                    point.Transform(transform)
                    upper_right = json.loads(point.ExportToJson())['coordinates']

                    point = ogr.CreateGeometryFromWkt("POINT (%f %f)" % (lower_right[0],lower_right[1]))
                    point.Transform(transform)
                    lower_right = json.loads(point.ExportToJson())['coordinates']
            except (RuntimeError, TypeError, NameError) as error:
                print error
            except:
                print "Unexpected error:", sys.exc_info()[0]

            self.metadata[filename]['BBOX'] = (upper_left,lower_left,upper_right,lower_right)

    def GDALInfoReportCorner(self,hDataset,x,y):
        """GDALInfoReportCorner: extracted and adapted from the python port of gdalinfo"""

        # Transform the point into georeferenced coordinates
        adfGeoTransform = hDataset.GetGeoTransform(can_return_null = True)
        if adfGeoTransform is not None:
            dfGeoX = adfGeoTransform[0] + adfGeoTransform[1] * x + adfGeoTransform[2] * y
            dfGeoY = adfGeoTransform[3] + adfGeoTransform[4] * x + adfGeoTransform[5] * y
        else:
            self.bar1.clearWidgets()
            self.bar1.pushMessage(
                'WARNING',
                'BBOX might be wrong. Transformation coefficient could not be fetched from raster',
                level=QgsMessageBar.WARNING)
            return (x,y)

        # Report the georeferenced coordinates
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            return literal_eval(("(%12.7f,%12.7f) " % (dfGeoX, dfGeoY )))
        else:
            return literal_eval(("(%12.3f,%12.3f) " % (dfGeoX, dfGeoY )))

    def loadImageryInfoForm(self, filename):
        pass

    def loadImageryInfo(self, filename):
        self.metadata[filename] = {}
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

        if self.reproject_check_box.isChecked():
            if filename not in self.reprojected:
                self.reprojected.append(filename)
        else:
            while filename in self.reprojected:
                self.reprojected.remove(filename)

        if self.license_check_box.isChecked():
            self.metadata[filename]['License'] = "Licensed under CC-BY 4.0 and allow tracing in OSM"
            if filename not in self.licensed:
                self.licensed.append(filename)
        else:
            while filename in self.licensed:
                self.licensed.remove(filename)

        self.extractMetadata(filename)

    def loadMetadataReviewBox(self):
        json_filenames = []
        for index in xrange(self.sources_list_widget.count()):
            filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))
            if filename not in self.reprojected:
                f = os.path.splitext(filename)[0]+'.json'
            else:
                f = os.path.splitext(filename)[0]+'_EPSG3857.json'
            json_filenames.append(f)

        with open('/tmp/full_metadata', 'w') as tmpfile:
            for f in json_filenames:
                if os.path.exists(f):
                    with open(f) as infile:
                        tmpfile.write(infile.read())

        metadata = QFile('/tmp/full_metadata')
        metadata.open(QIODevice.ReadOnly)
        stream = QTextStream(metadata)
        self.review_metadata_box.setText(stream.readAll())

    #functions for threading purpose
    def startConnection(self):
        if self.storage_combo_box.currentIndex() == 0:
            bucket_name = 'oam-qgis-plugin-test'
        else:
            bucket_name = str(self.specify_edit.text())
            if not bucket_name:
                self.bar2.clearWidgets()
                self.bar2.pushMessage(
                    'WARNING',
                    'The bucket for upload must be provided',
                    level=QgsMessageBar.WARNING)

        bucket_key = str(self.key_id_edit.text())
        bucket_secret = str(self.secret_key_edit.text())

        self.bucket = None
        for trial in xrange(3):
            if self.bucket: break
            try:
                connection = S3Connection(bucket_key,bucket_secret)
                self.bucket = connection.get_bucket(bucket_name)
                QgsMessageLog.logMessage(
                    'Connection established' % trial,
                    'OAM',
                    level=QgsMessageLog.INFO)
            except:
                if trial == 2:
                   QgsMessageLog.logMessage(
                    'Failed to connect after 3 attempts',
                    'OAM',
                    level=QgsMessageLog.CRITICAL)
        return self.bucket

    def reproject(self,filename):
        # to avoid repetition of "EPSG3857" in filename:
        if not "EPSG3857" in filename:
            reproject_filename = os.path.splitext(filename)[0]+'_EPSG3857.tif'
        os.system("gdalwarp -of GTiff -t_srs epsg:3857 %s %s" % (filename,reproject_filename))
        QgsMessageLog.logMessage(
            'Reprojected to EPSG:3857',
            'OAM',
            level=QgsMessageLog.INFO)
        return reproject_filename

    def convert(self,filename):
        tif_filename = os.path.splitext(filename)[0]+".tif"
        #Open existing dataset
        src_ds = gdal.Open(filename)
        driver = gdal.GetDriverByName("GTiff")
        dst_ds = driver.CreateCopy(tif_filename, src_ds, 0 )
        #Properly close the datasets to flush to disk
        dst_ds = None
        src_ds = None

    def startUploader(self):
        # initialize options
        self.upload_options = []
        if self.notify_oam_check.isChecked():
            self.upload_options.append("notify_oam")
        if self.trigger_tiling_check.isChecked():
            self.upload_options.append("trigger_tiling")

        if self.startConnection():
            for index in xrange(self.sources_list_widget.count()):
                filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))

                self.bar2.clearWidgets()
                self.bar2.pushMessage(
                    'INFO',
                    'Pre-upload image processing...',
                    level=QgsMessageBar.INFO)

                # Perfom reprojection
                if filename in self.reprojected:
                    filename = self.reproject(filename)
                    QgsMessageLog.logMessage(
                        'Created reprojected file: %s' % filename,
                        'OAM',
                        level=QgsMessageLog.INFO)

                # Convert file format
                if not (imghdr.what(filename) == 'tiff'):
                    filename = self.convert(filename)
                    QgsMessageLog.logMessage(
                        'Converted file to tiff: %s' % filename,
                        'OAM',
                        level=QgsMessageLog.INFO)

                # create a new uploader instance
                uploader = Uploader(filename,self.bucket,self.upload_options)
                QgsMessageLog.logMessage(
                    'Uploader started\n',
                    'OAM',
                    level=QgsMessageLog.INFO)
                # configure the QgsMessageBar
                messageBar = self.bar2.createMessage('INFO: Performing upload...', )
                progressBar = QProgressBar()
                progressBar.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
                messageBar.layout().addWidget(progressBar)
                cancelButton = QPushButton()
                cancelButton.setText('Cancel')
                cancelButton.clicked.connect(self.cancelUpload)
                messageBar.layout().addWidget(cancelButton)
                self.bar2.clearWidgets()
                self.bar2.pushWidget(messageBar, level=QgsMessageBar.INFO)
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
                QgsMessageLog.logMessage(
                    'No connection to the server\n',
                    'OAM',
                    level=QgsMessageLog.CRITICAL)

    def cancelUpload(self):
        self.uploader.kill()
        self.bar2.clearWidgets()
        self.bar2.pushMessage(
            'WARNING',
            'Canceling upload...',
            level=QgsMessageBar.WARNING)

    def uploaderFinished(self, success):
        # clean up the uploader and thread
        try:
            self.uploader.deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting uploader\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        self.thread.quit()
        self.thread.wait()
        try:
            self.thread.deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting thread\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        # remove widget from message bar
        self.bar2.popWidget(self.messageBar)
        if success:
            # report the result
            self.bar2.clearWidgets()
            self.bar2.pushMessage(
                'INFO',
                'Upload completed with success',
                level=QgsMessageBar.INFO)
            QgsMessageLog.logMessage(
                'Upload succeeded',
                'OAM',
                level=QgsMessageLog.INFO)
        else:
            # notify the user that something went wrong
            self.bar2.pushMessage(
                'CRITICAL',
                'Upload was interrupted',
                level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage(
                'Upload was interrupted',
                'OAM',
                level=QgsMessageLog.CRITICAL)

    def uploaderError(self, e, exception_string):
        QgsMessageLog.logMessage(
            'Uploader thread raised an exception:\n'.format(exception_string),
            'OAM',
            level=QgsMessageLog.CRITICAL)


class Uploader(QObject):
    '''Handle uploads in a separate thread'''

    finished = pyqtSignal(bool)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float)

    def __init__(self,filename,bucket,options):
        QObject.__init__(self)
        self.filename = filename
        self.bucket = bucket
        self.killed = False
        self.options = options

    def sendMetadata(self):
        jsonfile = os.path.splitext(self.filename)[0]+'.json'
        try:
            k = Key(self.bucket)
            k.key = os.path.basename(jsonfile)
            k.set_contents_from_filename(jsonfile)
            QgsMessageLog.logMessage(
                'Sent %s\n' % jsonfile,
                'OAM',
                level=QgsMessageLog.INFO)
        except:
            QgsMessageLog.logMessage(
                'Could not send %s\n' % jsonfile,
                'OAM',
                level=QgsMessageLog.CRITICAL)

    def notifyOAM(self):
        '''Just a stub method, not needed at the moment because indexing happens every 10 mins'''
        QgsMessageLog.logMessage(
            'AOM notified of new resource',
            'OAM',
            level=QgsMessageLog.INFO)

    def triggerTileService(self):
        url = "http://hotosm-oam-server-stub.herokuapp.com/tile"
        h = {'content-type':'application/json'}
        uri = "s3://%s/%s" % (self.bucket.name,os.path.basename(self.filename))
        QgsMessageLog.logMessage(
            'Imagery uri %s\n' % uri,
            'OAM',
            level=QgsMessageLog.INFO)
        d = json.dumps({'sources':[uri]})
        p = requests.post(url,headers=h,data=d)
        post_dict = json.loads(p.text)
        QgsMessageLog.logMessage(
            'Post response: %s' % post_dict,
            'OAM',
            level=QgsMessageLog.INFO)

        if u'id' in post_dict.keys():
            ts_id = post_dict[u'id']
            time = post_dict[u'queued_at']
            QgsMessageLog.logMessage(
                'Tile service #%s triggered on %s\n' % (ts_id,time),
                'OAM',
                level=QgsMessageLog.INFO)
        else:
            QgsMessageLog.logMessage(
                'Tile service could not be created\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        return(0)

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
                'Preparing to send %s chunks in total\n' % chunk_count,
                'OAM',
                level=QgsMessageLog.INFO)

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
                    'Sent chunk #%d\n' % progress_count,
                    'OAM',
                    level=QgsMessageLog.INFO)
                self.progress.emit(progress_count / float(chunk_count)*100)
                QgsMessageLog.logMessage(
                    'Progress = %f' % (progress_count / float(chunk_count)),
                    'OAM',
                    level=QgsMessageLog.INFO)
            if self.killed is False:
                multipart.complete_upload()
                self.progress.emit(100)
                success = True
                if "notify_oam" in self.options:
                    self.notifyOAM()
                if "trigger_tiling" in self.options:
                    self.triggerTileService()
        except Exception, e:
            # forward the exception upstream (or try to...)
            # chunk size smaller than 5MB can cause an error, server does not expect it
            self.error.emit(e, traceback.format_exc())

        self.finished.emit(success)

    def kill(self):
        self.killed = True
