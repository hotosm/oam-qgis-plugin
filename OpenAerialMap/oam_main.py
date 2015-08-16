# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and 
 upload imagery from/to the OAM catalog.
                              -------------------
        begin                : 2015-07-01
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email                : tassia@acaia.ca / yoji.salut@gmail.com
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
from PyQt4.QtCore import (QSettings, QTranslator, qVersion, QCoreApplication, 
                          pyqtSignal, QObject, QThread)
from PyQt4.QtGui import (QAction, QIcon, QMessageBox, QFileDialog, 
                         QListWidgetItem, QSizePolicy, QGridLayout, QPushButton, 
                         QProgressBar)
from PyQt4.Qt import *
from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer, QgsMessageLog
import resources_rc

from oam_client_dialog import OpenAerialMapDialog

import os, sys, math, imghdr
from osgeo import gdal, osr
import time
import json
# Modules needed for upload
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback


from module_access_local_storage import *


#for testing purpose only
from test_tkinter import HelloTkWindow
from test_s3_connection import *
from test_s3_connection_wizard_class import TestS3ConnectionWizard
from Tkinter import * 
#import sys
 
class OpenAerialMap:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        
        # Save reference to the QGIS interface
        self.iface = iface
        
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'OpenAerialMap_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = ExtendedOAMDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Open Aerial Map (OAM)')
        self.toolbar = self.iface.addToolBar(u'OpenAerialMap')
        self.toolbar.setObjectName(u'OpenAerialMap')
        self.dlg.bar = QgsMessageBar()
        self.dlg.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.dlg.layout().addWidget(self.dlg.bar)
        self.settings = QSettings('QGIS','oam-qgis-plugin')
        self.metadata = {}

    # noinspection PyMethodMayBeStatisc
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('OpenAerialMap', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action
    
    def displayLoadImageryWizard(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            pass
        
    def displaySearchTool(self):
        masterWigt = Tk()
        helloTkWindow = HelloTkWindow(masterWigt, "Hello,world!", "OAM Search Tool")
        helloTkWindow.mainloop()
    
    #Testing purpose only
    def displayPaths(self):
        masterWigt = Tk()
        helloTkWindow = HelloTkWindow(masterWigt, "Hello,world!", str(sys.path))
        helloTkWindow.mainloop()

    #Testing purpose only
    def testS3(self):
        self.testS3 = TestS3ConnectionWizard()
        self.testS3.show()

    #Testing purpose only
    """    
    def renderTest(self, painter):
        masterWigt = Tk()
        helloTkWindow = HelloTkWindow(masterWigt, "Hello,world!", "TestPlugin: renderTest called!")
        helloTkWindow.mainloop()
    """

    def initGui(self):
        
        # Testing purpose only
        self.actionTest1 = QAction(QIcon(":/plugins/testplug/icon.png"), "Test paths", self.iface.mainWindow())
        self.actionTest1.setObjectName("testPaths")
        
        QObject.connect(self.actionTest1, SIGNAL("triggered()"), self.displayPaths)
    
        self.actionTest2 = QAction(QIcon(":/plugins/testplug/icon.png"), "Test S3", self.iface.mainWindow())
        self.actionTest2.setObjectName("testS3")
        QObject.connect(self.actionTest2, SIGNAL("triggered()"), self.testS3)

        self.iface.addPluginToMenu("Test plugins", self.actionTest1)
        self.iface.addPluginToMenu("Test plugins", self.actionTest2)
   
        # connect to signal renderComplete which is emitted when canvas
        # rendering is done
        #QObject.connect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderTest)        

        
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/OpenAerialMap/icon.png'
        search_icon_path = ':/plugins/OpenAerialMap/search_icon.png'

        self.add_action(
            icon_path,
            text=self.tr(u'Upload imagery'),
            callback=self.displayLoadImageryWizard,
            parent=self.iface.mainWindow())

        self.add_action(
            search_icon_path,
            text=self.tr(u'Search imagery'),
            callback=self.displaySearchTool,
            parent=self.iface.mainWindow())

        # Load widgets
        self.loadLayers()
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()
        self.loadFullMetadata()

        # Imagery tab connections
        self.dlg.layers_tool_button.clicked.connect(self.loadLayers)
        self.dlg.file_tool_button.clicked.connect(self.selectFile)
        self.dlg.add_source_button.clicked.connect(self.addSources)
        self.dlg.remove_source_button.clicked.connect(self.removeSources)
        self.dlg.up_source_button.clicked.connect(self.upSource)
        self.dlg.down_source_button.clicked.connect(self.downSource)
        self.dlg.imagery_next_button.clicked.connect(self.nextTab)

        # Metadata tab connections
        self.dlg.sense_start_edit.setCalendarPopup(1)
        self.dlg.sense_start_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.dlg.sense_end_edit.setCalendarPopup(1)
        self.dlg.sense_end_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.dlg.default_button.clicked.connect(self.loadMetadataSettings)
        self.dlg.clean_button.clicked.connect(self.cleanMetadataSettings)
        self.dlg.save_button.clicked.connect(self.saveMetadata)
        self.dlg.metadata_next_button.clicked.connect(self.nextTab)
        self.dlg.metadata_previous_button.clicked.connect(self.previousTab)

        # Upload tab connections
        self.dlg.upload_button.clicked.connect(self.dlg.startUploader)
        self.dlg.quit_button.clicked.connect(self.closeDialog)
        self.dlg.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)
        self.dlg.upload_previous_button.clicked.connect(self.previousTab)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Open Aerial Map (OAM)'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def cleanMetadataSettings(self):
        self.dlg.title_edit.setText('')
        self.dlg.platform_combo_box.setCurrentIndex(0)
        self.dlg.sensor_edit.setText('')
        self.dlg.sense_start_edit.setDate(QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).date())
        self.dlg.sense_start_edit.setTime(QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).time())
        self.dlg.sense_end_edit.setDate(QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).date())
        self.dlg.sense_end_edit.setTime(QDateTime().fromString('1970-01-01T00:00:00',Qt.ISODate).time())
        self.dlg.tags_edit.setText('')
        self.dlg.provider_edit.setText('')
        self.dlg.contact_edit.setText('')
        self.dlg.website_edit.setText('')

    def loadMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.dlg.title_edit.setText(self.settings.value('TITLE'))

        if self.settings.value('PLATFORM') == None:
            self.dlg.title_edit.setCursorPosition(0)
        else:
            self.dlg.platform_combo_box.setCurrentIndex(int(self.settings.value('PLATFORM')))
        
        self.dlg.platform_combo_box.setCurrentIndex(0)
        self.dlg.sensor_edit.setText(self.settings.value('SENSOR'))
        self.dlg.sensor_edit.setCursorPosition(0)
        self.dlg.sense_start_edit.setDate(QDateTime.fromString(self.settings.value('SENSE_START'), Qt.ISODate).date())
        self.dlg.sense_start_edit.setTime(QDateTime.fromString(self.settings.value('SENSE_START'), Qt.ISODate).time())
        self.dlg.sense_end_edit.setDate(QDateTime.fromString(self.settings.value('SENSE_END'), Qt.ISODate).date())
        self.dlg.sense_end_edit.setTime(QDateTime.fromString(self.settings.value('SENSE_END'), Qt.ISODate).time())
        
        if self.settings.value('TAGS') == None:
            self.dlg.tags_edit.setText(', '.join(''))
        else:
            self.dlg.tags_edit.setText(', '.join(self.settings.value('TAGS')))
        
        self.dlg.tags_edit.setCursorPosition(0)
        self.dlg.provider_edit.setText(self.settings.value('PROVIDER'))
        self.dlg.provider_edit.setCursorPosition(0)
        self.dlg.contact_edit.setText(self.settings.value('CONTACT'))
        self.dlg.contact_edit.setCursorPosition(0)
        self.dlg.website_edit.setText(self.settings.value('WEBSITE'))
        self.dlg.website_edit.setCursorPosition(0)
        self.settings.endGroup()

    def loadStorageSettings(self):
        self.settings.beginGroup("Storage")
        bucket = self.settings.value('S3_BUCKET_NAME')
        storage_index = self.dlg.storage_combo_box.findText(bucket,Qt.MatchExactly)
        if not storage_index == -1:
            self.dlg.storage_combo_box.setCurrentIndex(storage_index)
        else:
            self.dlg.storage_combo_box.setCurrentIndex(self.dlg.storage_combo_box.findText(self.tr('other...')))
            self.dlg.specify_label.setEnabled(1)
            self.dlg.specify_edit.setEnabled(1)
            self.dlg.specify_edit.setText(self.settings.value('S3_BUCKET_NAME'))
        self.dlg.key_id_edit.setText(self.settings.value('AWS_ACCESS_KEY_ID'))
        self.dlg.key_id_edit.setCursorPosition(0)
        self.dlg.secret_key_edit.setText(self.settings.value('AWS_SECRET_ACCESS_KEY'))
        self.dlg.secret_key_edit.setCursorPosition(0)
        self.settings.endGroup()

    def loadOptionsSettings(self):
        self.settings.beginGroup("Options")
        if self.settings.value('NOTIFY_OAM'):
            self.dlg.notify_oam_check.setCheckState(2)
        if self.settings.value('TRIGGER_OAM_TS'):
            self.dlg.trigger_tiling_check.setCheckState(2)
        if self.settings.value('REPROJECT'):
            self.dlg.notify_oam_check.setCheckState(2)
        if self.settings.value('CONVERT_GEOTIFF_RGB'):
            self.dlg.notify_oam_check.setCheckState(2)
        self.settings.endGroup()

    def loadLayers(self):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if not self.dlg.layers_list_widget.findItems(layer.name(),Qt.MatchExactly):
                item = QListWidgetItem()
                item.setText(layer.name())
                item.setData(Qt.UserRole, layer.dataProvider().dataSourceUri())
                self.dlg.layers_list_widget.addItem(item)
        self.dlg.bar.clearWidgets()
        self.dlg.bar.pushMessage("INFO", "Source imagery for upload must be selected from layers or files.", level=QgsMessageBar.INFO)

    def closeDialog(self):
        self.dlg.close()

    def selectFile(self):
        selected_file = QFileDialog.getOpenFileName(self.dlg, 'Select File', os.path.expanduser("~"))
        self.dlg.source_file_edit.setText(selected_file)

    def validateFile(self,filename):
        if not os.path.isfile(filename):
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage("CRITICAL", "The file %s does not exist" % filename, level=QgsMessageBar.CRITICAL)
            return 0
        elif imghdr.what(filename) is None:
            print imghdr.what(filename)
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage("CRITICAL", "The file %s is not a supported data source" % filename, level=QgsMessageBar.CRITICAL)
            return 0
        else:
            return 1

    def validateLayer(self,layer_name):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if layer_name == layer.name():
                if layer.type() == QgsMapLayer.VectorLayer:
                    self.dlg.bar.clearWidgets()
                    self.dlg.bar.pushMessage("CRITICAL", "Vector layers cannot be selected for upload", level=QgsMessageBar.CRITICAL)
                    return 0
                else:
                    return 1

    def addSources(self):
        filename = self.dlg.source_file_edit.text()
        selected_layers = self.dlg.layers_list_widget.selectedItems()
        if not filename and not selected_layers:
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('WARNING', 'Either a layer or file must be selected to be added', level=QgsMessageBar.WARNING)
        if filename:
            if self.validateFile(filename):
                if not self.dlg.sources_list_widget.findItems(filename,Qt.MatchExactly):
                    item = QListWidgetItem()
                    item.setText(os.path.basename(filename))
                    item.setData(Qt.UserRole, filename)
                    self.dlg.sources_list_widget.addItem(item)
                    self.dlg.added_sources_list_widget.addItem(item.clone())
                    self.dlg.source_file_edit.setText('')
        if selected_layers:
            for item in selected_layers:
                if self.validateLayer(item.text()):
                    if not self.dlg.sources_list_widget.findItems(item.text(),Qt.MatchExactly):
                        self.dlg.layers_list_widget.takeItem(self.dlg.layers_list_widget.row(item))
                        self.dlg.sources_list_widget.addItem(item)
                        self.dlg.added_sources_list_widget.addItem(item.clone())
        self.dlg.bar.clearWidgets()
        self.dlg.bar.pushMessage('INFO', 'Select sources were added to the upload queue', level=QgsMessageBar.INFO)
        self.loadFullMetadata()

    def removeSources(self):
        selected_sources = self.dlg.sources_list_widget.selectedItems()
        added_sources = self.dlg.added_sources_list_widget.selectedItems()
        if selected_sources:
            for item in selected_sources:
                self.dlg.sources_list_widget.takeItem(self.dlg.sources_list_widget.row(item))
                added_item = self.dlg.added_sources_list_widget.findItems(item.text(),Qt.MatchExactly)
                if added_item:
                    self.dlg.added_sources_list_widget.takeItem(self.dlg.added_sources_list_widget.row(added_item[0]))
                all_layers = self.iface.mapCanvas().layers()
                for layer in all_layers:
                    if item.text() == layer.name():
                        if not self.dlg.layers_list_widget.findItems(item.text(),Qt.MatchExactly):
                            self.dlg.layers_list_widget.addItem(item)
        else:
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('WARNING', 'An imagery source must be selected to be removed', level=QgsMessageBar.WARNING)

    def upSource(self):
        selected_layers = self.dlg.sources_list_widget.selectedItems()
        if selected_layers:
            position = self.dlg.sources_list_widget.row(selected_layers[0])
            if position > 0:
                item = self.dlg.sources_list_widget.takeItem(position)
                self.dlg.sources_list_widget.insertItem(position-1,item)
                item.setSelected(1)

    def downSource(self):
        selected_layers = self.dlg.sources_list_widget.selectedItems()
        if selected_layers:
            position = self.dlg.sources_list_widget.row(selected_layers[0])
            if position < self.dlg.sources_list_widget.count()-1:
                item = self.dlg.sources_list_widget.takeItem(position)
                self.dlg.sources_list_widget.insertItem(position+1,item)
                item.setSelected(1)

    def nextTab(self):
        self.dlg.tab_widget.setCurrentIndex(self.dlg.tab_widget.currentIndex()+1)

    def previousTab(self):
        self.dlg.tab_widget.setCurrentIndex(self.dlg.tab_widget.currentIndex()-1)

    def extractMetadata(self,filename):
        """Extract filesize, projection, bbox and gsd from image file"""

        self.metadata[filename]['File size'] = os.stat(filename).st_size

        datafile = gdal.Open(filename,gdal.GA_ReadOnly)
        if datafile is None:
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('CRITICAL', 'Extraction of raster metadata failed.', level=QgsMessageBar.CRITICAL)

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
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('WARNING', 'BBOX might be wrong. Transformation coefficient could not be fetched from raster.', level=QgsMessageBar.WARNING)
            return (x,y)

        # Report the georeferenced coordinates
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            return ("(%12.7f,%12.7f) " % (dfGeoX, dfGeoY ))
        else:
            return ("(%12.3f,%12.3f) " % (dfGeoX, dfGeoY ))

    def loadInputMetadata(self, filename):
        self.metadata[filename]['Title'] = self.dlg.title_edit.text()
        self.metadata[filename]['Platform'] = self.dlg.platform_combo_box.currentIndex()
        self.metadata[filename]['Sensor'] = self.dlg.sensor_edit.text()
        start = QDateTime()
        start.setDate(self.dlg.sense_start_edit.date())
        start.setTime(self.dlg.sense_start_edit.time())
        self.metadata[filename]['Sensor start'] = start.toString(Qt.ISODate)
        end = QDateTime()
        end.setDate(self.dlg.sense_end_edit.date())
        end.setTime(self.dlg.sense_end_edit.time())
        self.metadata[filename]['Sensor end'] = end.toString(Qt.ISODate)
        self.metadata[filename]['Tags'] = self.dlg.tags_edit.text()
        self.metadata[filename]['Provider'] = self.dlg.provider_edit.text()
        self.metadata[filename]['Contact'] = self.dlg.contact_edit.text()
        self.metadata[filename]['Website'] = self.dlg.website_edit.text()

    def saveMetadata(self):
        selected_layers = self.dlg.added_sources_list_widget.selectedItems()
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
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('INFO', 'Metadata for the selected sources was saved', level=QgsMessageBar.INFO)
        else:
            self.dlg.bar.clearWidgets()
            self.dlg.bar.pushMessage('WARNING', 'One or more source imagery must be selected to have the metadata saved.', level=QgsMessageBar.WARNING)

    def loadFullMetadata(self):
        for index in xrange(self.dlg.sources_list_widget.count()):
            jsonfile = os.path.splitext(str(self.dlg.sources_list_widget.item(index).data(Qt.UserRole)))[0]+'.json'
            self.dlg.metadata_review_browser.setSource(QUrl().fromLocalFile(jsonfile))

    def enableSpecify(self):
        if self.dlg.storage_combo_box.currentIndex() == 1:
            self.dlg.specify_label.setEnabled(1)
            self.dlg.specify_edit.setEnabled(1)
        else:
            self.dlg.specify_label.setEnabled(0)
            self.dlg.specify_edit.setText('')
            self.dlg.specify_edit.setEnabled(0)

    def run(self):
        
        """
        Run method that performs all the real work.
        Please refer to the following functions for details:
        
        def displayLoadImageryWizard(self):
        def displaySearchTool(self):
        def displayPaths(self):
        def testS3(self):
            
        """        

class ExtendedOAMDialog(OpenAerialMapDialog):
    '''Class that extends automated generated OAM dialog, basically for threading purpose'''

    def startConnection(self):
        if self.storage_combo_box.currentIndex() == 0:
            bucket_name = 'oam-qgis-plugin-test'
        else:
            bucket_name = str(self.specify_edit.text())
            if not bucket_name:
                self.bar.clearWidgets()
                self.bar.pushMessage('WARNING', 'The bucket for upload must be provided', level=QgsMessageBar.CRITICAL)
        bucket_key = str(self.key_id_edit.text())
        bucket_secret = str(self.secret_key_edit.text())

        self.bucket = None
        for trial in xrange(3):
            if self.bucket: break
            try:
                connection = S3Connection(bucket_key,bucket_secret)
                self.bucket = connection.get_bucket(bucket_name)
                QgsMessageLog.logMessage('INFO','Connection established' % trial, level=QgsMessageLog.INFO)
            except:
                if trial == 2:
                   QgsMessageLog.logMessage('CRITICAL','Failed to connect after 3 attempts', level=QgsMessageLog.CRITICAL)
        return self.bucket

    def startUploader(self):
        if self.startConnection():
            for index in xrange(self.sources_list_widget.count()):
                filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))

                # create a new uploader instance
                uploader = Uploader(filename,self.bucket)
                QgsMessageLog.logMessage('started uploader\n', level=QgsMessageLog.CRITICAL)
    
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
            self.bar.pushMessage('INFO','Upload completed with success.',level=QgsMessageBar.INFO)
            QgsMessageLog.logMessage('Upload succeeded', level=QgsMessageLog.CRITICAL)
        else:
            # notify the user that something went wrong
            self.bar.pushMessage('CRITICAL','Upload could not be completeded.',level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage('Upload failed', level=QgsMessageLog.CRITICAL)
    
    def uploaderError(self, e, exception_string):
        QgsMessageLog.logMessage('Uploader thread raised an exception:\n'.format(exception_string), level=QgsMessageLog.CRITICAL)


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
            QgsMessageLog.logMessage('Sent %s\n' % jsonfile, level=QgsMessageLog.CRITICAL)
        except:
            QgsMessageLog.logMessage('Could not send %s\n' % jsonfile, level=QgsMessageLog.CRITICAL)


    def run(self):
        self.sendMetadata()
        success = False
        try:
            file_size = os.stat(self.filename).st_size
            chunk_size = 5242880
            chunk_count = int(math.ceil(file_size / float(chunk_size)))
            progress_count = 0

            multipart = self.bucket.initiate_multipart_upload(os.path.basename(self.filename))

            QgsMessageLog.logMessage('About to send %s chunks\n' % chunk_count, level=QgsMessageLog.CRITICAL)
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
                QgsMessageLog.logMessage('chunk %d\n' % progress_count, level=QgsMessageLog.CRITICAL)
                self.progress.emit(progress_count / float(chunk_count)*100)
                QgsMessageLog.logMessage('progress %f' % (progress_count / float(chunk_count)), level=QgsMessageLog.CRITICAL)
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
