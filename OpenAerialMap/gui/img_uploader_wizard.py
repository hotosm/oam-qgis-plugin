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
import json, time, math, imghdr, tempfile

# Modules needed for upload
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import traceback
import requests, json
from ast import literal_eval

from module.module_handle_metadata import MetadataHandler
from module.module_access_s3 import S3Manager
from module.module_gdal_utilities import reproject, convert_to_tif
from module.module_validate_files import validate_layer, validate_file

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

        # Initialize the object for S3Manager and upload options and filenames
        self.s3Mgr = None
        self.upload_options = []
        self.upload_filenames = []

        # Initialize layers and default settings
        self.loadLayers()
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()

        # register event handlers
        self.button(QWizard.BackButton).clicked.connect(self.previousPage)
        self.button(QWizard.NextButton).clicked.connect(self.nextPage)
        self.button(QWizard.FinishButton).clicked.connect(self.finishWizard)
        self.button(QWizard.CancelButton).clicked.connect(self.cancelWizard)

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

        # Temporarily hide the reload button
        self.reload_button.hide()
        self.reload_button.clicked.connect(self.loadSavedMetadata)

        # temporarily disable notify_oam_check and trigger_tiling_check
        self.notify_oam_check.setEnabled(False)
        self.trigger_tiling_check.setEnabled(False)


        # Upload tab connections (wizard page 3)
        self.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)
        self.customButtonClicked.connect(self.startUpload)

    # handlers for navigation
    def nextPage(self):
        if self.currentId() == 1:
            #print "Page ID: " + str(self.currentId())
            pass
        elif self.currentId() == 2:
            #print "Page ID: " + str(self.currentId())
            self.loadMetadataReviewBox()
        else:
            pass

    def previousPage(self):
        if self.currentId() == 0:
            #print "Page ID: " + str(self.currentId())
            pass
        elif self.currentId() == 1:
            #print "Page ID: " + str(self.currentId())
            pass
        else:
            pass

    def finishWizard(self):
        print "finish wizard button was clicked."
        if self.s3Mgr != None:
            self.s3Mgr.cancelAllUploads()

    def cancelWizard(self):
        print "cancel wizard button was clicked."
        if self.s3Mgr != None:
            self.s3Mgr.cancelAllUploads()

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
                result_val = validate_file(filename)
                if result_val["val"]:
                    if not self.sources_list_widget.findItems(filename,Qt.MatchExactly):
                        item = QListWidgetItem()
                        item.setText(os.path.basename(filename))
                        item.setData(Qt.UserRole, filename)
                        self.sources_list_widget.addItem(item)
                        self.added_sources_list_widget.addItem(item.clone())
                        self.source_file_edit.setText('')
                        added = True
                else:
                    msg = result_val["msg"]
                    self.bar0.clearWidgets()
                    self.bar0.pushMessage("CRITICAL", msg, level=QgsMessageBar.CRITICAL)
                    QgsMessageLog.logMessage("CRITICAL", msg, level=QgsMessageLog.INFO)

            if selected_layers:
                for item in selected_layers:
                    if validate_layer(item.text(), self.iface):
                        if not self.sources_list_widget.findItems(item.text(),Qt.MatchExactly):
                            self.layers_list_widget.takeItem(self.layers_list_widget.row(item))
                            self.sources_list_widget.addItem(item)
                            self.added_sources_list_widget.addItem(item.clone())
                            added = True
                    else:
                        self.bar0.clearWidgets()
                        self.bar0.pushMessage(
                            "CRITICAL",
                            "Vector layers cannot be selected for upload",
                            level=QgsMessageBar.CRITICAL)
            if added:
                self.bar0.clearWidgets()
                self.bar0.pushMessage(
                    'INFO',
                    'Source(s) added to the upload queue',
                    level=QgsMessageBar.INFO)

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
    # load default values
    def loadMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.title_edit.setText(self.settings.value('TITLE'))
        if self.settings.value('PLATFORM') == None:
            self.platform_combo_box.setCurrentIndex(0)
        else:
            self.platform_combo_box.setCurrentIndex(
                int(self.settings.value('PLATFORM')))
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
            QDateTime().fromString('1970-01-01T00:00:00',
            Qt.ISODate).date())
        self.sense_end_edit.setTime(
            QDateTime().fromString('1970-01-01T00:00:00',
            Qt.ISODate).time())
        self.tags_edit.setText('')
        self.provider_edit.setText('')
        self.contact_edit.setText('')
        self.website_edit.setText('')
        self.license_check_box.setCheckState(0)
        self.reproject_check_box.setCheckState(0)

    def saveMetadata(self):
        flag = False
        if self.reproject_check_box.isChecked():
            qMsgBox = QMessageBox()
            qMsgBox.setWindowTitle("Confirmation")
            qMsgBox.setText("You checked the reprojection option, which can require significant \
amount of time. Are you sure to continue?")
            qMsgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #qMsgBox.setDefaultButton(QMessageBox.Cancel)

            if qMsgBox.exec_() == QMessageBox.Ok:
                flag = True
        else:
            flag = True

        if flag:
            # get metadata from GUI, and store them in a dictionary
            metaInputInDic = {}
            metaInputInDic['title'] = self.title_edit.text()
            metaInputInDic['platform'] = self.platform_combo_box.currentIndex()
            metaInputInDic['sensor'] = self.sensor_edit.text()
            metaInputInDic['acquisition_start'] = self.sense_start_edit.dateTime().toString(Qt.ISODate)
            metaInputInDic['acquisition_end'] = self.sense_end_edit.dateTime().toString(Qt.ISODate)
            metaInputInDic['provider'] = self.provider_edit.text()
            metaInputInDic['contact'] =  self.contact_edit.text()
            metaInputInDic['properties'] =  self.tags_edit.text() #change name later?
            metaInputInDic['uuid'] = self.website_edit.text() #change name later?

            # declare list for MetadataHandler object
            metaHdlrs = []
            num_selected_layers = 0
            count = 0

            """Open python console. I haven't indentified the exact reason, but
            messagebar doesn't work properly without opening python console
            and some print statements"""
            pluginMenu = self.iface.pluginMenu()
            #print(repr(pluginMenu))
            for action in pluginMenu.actions():
                if 'Python Console' in action.text():
                    action.trigger()

            selected_layers = self.added_sources_list_widget.selectedItems()
            if selected_layers:
                num_selected_layers = len(selected_layers)
                for each_layer in selected_layers:
                    file_abspath = each_layer.data(Qt.UserRole)

                    if self.reproject_check_box.isChecked():
                        self.bar1.clearWidgets()
                        # this message doesn't show up without opening python console
                        # need to identify the reason
                        self.bar1.pushMessage(
                            'INFO',
                            'Reprojecting files: %sth image out of %s is being processed...'\
                             % (str(count+1), str(num_selected_layers)),
                            level=QgsMessageBar.INFO)
                        # Isn't it better to use thread?
                        print('Reprojecting {0}'.format(str(os.path.basename(file_abspath))))
                        file_abspath = reproject(file_abspath)
                    else:
                        self.bar1.clearWidgets()
                        self.bar1.pushMessage(
                            'INFO',
                            '%sth image out of %s is processed.'\
                             % (str(count+1), str(num_selected_layers)),
                            level=QgsMessageBar.INFO)

                    # Isn't it better to use thread?
                    # probably no need to make list in this part
                    metaHdlrs.append(MetadataHandler(metaInputInDic, file_abspath))
                    metaHdlrs[count].createMetaForUpload()
                    str_meta = str(json.dumps(metaHdlrs[count].getMetaForUpload()))
                    #print str_meta
                    json_file_abspath = os.path.splitext(file_abspath)[0] + '.json'
                    #print json_file_abspath
                    f = open(json_file_abspath,'w')
                    f.write(str_meta)
                    f.close()
                    count += 1

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

    def loadSavedMetadata(self):

        qMsgBox = QMessageBox()
        qMsgBox.setText('Under construction:\nMessage from loadSavedMetadata function.')
        qMsgBox.exec_()

    # event handling for wizard page 3
    # please also see startUpload function for event handling of Start Upload button
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

        """
        if str(self.settings.value('NOTIFY_OAM')).lower() == 'true':
            self.notify_oam_check.setCheckState(2)
        if str(self.settings.value('TRIGGER_OAM_TS')).lower() == 'true':
            self.trigger_tiling_check.setCheckState(2)
        """

        # This part is for temporal use.
        self.notify_oam_check.setCheckState(0)
        self.trigger_tiling_check.setCheckState(0)

        self.settings.endGroup()


    def loadMetadataReviewBox(self):
        json_file_abspaths = []
        for index in xrange(self.sources_list_widget.count()):
            file_abspath = str(self.sources_list_widget.item(index).data(Qt.UserRole))
            json_file_abspath = ''
            if self.reproject_check_box.isChecked():
                json_file_abspath = os.path.splitext(file_abspath)[0]+'_EPSG3857.json'
            else:
                json_file_abspath = os.path.splitext(file_abspath)[0]+'.json'

            #print str(json_file_abspath)
            json_file_abspaths.append(json_file_abspath)

        temp = QTemporaryFile()
        temp.open()
        for json_file_abspath in json_file_abspaths:
            if os.path.exists(json_file_abspath):
                with open(json_file_abspath) as infile:
                    temp.write(infile.read() + '\n\n')
            else:
                temp.write('%s was not found. Please save it in advance.\n\n'
                    % str(json_file_abspath))
        temp.flush()
        temp.seek(0)

        stream = QTextStream(temp)
        self.review_metadata_box.setText(stream.readAll())

    def startUploadPreprocessing(self):

        """Probably it is better to let the users to confirm all the metadata and
        reprojected files are saved before starting upload."""

        """don't know why this message doesn't show up..."""
        self.bar2.clearWidgets()
        self.bar2.pushMessage(
            'INFO',
            'Preprocessing....',
            level=QgsMessageBar.INFO)

        for index in xrange(self.sources_list_widget.count()):
            upload_filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))

            if self.reproject_check_box.isChecked():
                upload_filename = reproject(upload_filename)
                QgsMessageLog.logMessage(
                    'Created reprojected file: %s' % upload_filename,
                    'OAM',
                    level=QgsMessageLog.INFO)
            """
            if not (imghdr.what(upload_filename) == 'tiff'):
                upload_filename = self.convert_to_tif(upload_filename)
                QgsMessageLog.logMessage(
                    'Converted file to tiff: %s' % upload_filename,
                    'OAM',
                    level=QgsMessageLog.INFO)
            """

            self.upload_filenames.append(upload_filename)

    #event handler for upload button
    def startUpload(self):

        #get the information of upload options
        if self.notify_oam_check.isChecked():
            self.upload_options.append("notify_oam")
        if self.trigger_tiling_check.isChecked():
            self.upload_options.append("trigger_tiling")

        if not self.license_check_box.isChecked():
            self.bar2.clearWidgets()
            self.bar2.pushMessage(
                'CRITICAL',
                'Please check the lisence term.',
                level=QgsMessageBar.WARNING)
        else:
            # conversion of file format, reprojection, creation of file paths
            self.startUploadPreprocessing()

            # get login information for bucket
            bucket_name = None
            bucket_key = None
            bucket_secret = None

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

            #create S3Manager Object and start upload
            self.s3Mgr = S3Manager( bucket_key,
                                    bucket_secret,
                                    bucket_name,
                                    self.upload_filenames,
                                    self.upload_options,
                                    self.page(2) )

            if self.s3Mgr.getBucket():
                self.bar2.clearWidgets()
                #msg = repr(self.s3Mgr.getAllKeys())
                #msg = repr(self.s3Mgr.test())
                #print msg
                result = repr(self.s3Mgr.uploadFiles())
                print result
            else:
                self.bar2.clearWidgets()
                self.bar2.pushMessage(
                    'CRITICAL',
                    'No connection to the server',
                    level=QgsMessageBar.CRITICAL)
                QgsMessageLog.logMessage(
                    'No connection to the server\n',
                    'OAM',
                    level=QgsMessageLog.CRITICAL)
