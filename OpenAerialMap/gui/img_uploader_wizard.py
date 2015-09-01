"""
define class to create img_uploader wizard
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

# temp for back-end modules
from module_connect_s3 import S3Manager
from module_edit_metadata import MetadataHandler


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_uploader_wizard.ui'))

class ImgUploaderWizard(QtGui.QWizard, FORM_CLASS):

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(ImgUploaderWizard, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        #metadata = {}
        #storageSettings = {}
        #optionSettings = {}

        #add QGISMessageBar bar on the dialog

        """ need to figure out how to put QgisMessageBar on Wizard"""
        #self.layout = QtGui.QGridLayout()
        self.bar = iface.messageBar()
        #self.bar = QgsMessageBar()
        #self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        #self.layout().addWidget(self.bar)


        """modify this part later!"""
        #img_settings = QSettings('QGIS','oam-qgis-plugin')
        """
        self.settings = imgSettings
        self.metadata = imgMetadata

        self.loadLayers()
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()
        """

        # make sure about this function...
        #self.loadFullMetadata()

        # Registering event handlers for page navigation
        self.button(QWizard.BackButton).clicked.connect(self.previousPage)
        self.button(QWizard.NextButton).clicked.connect(self.nextPage)
        self.button(QWizard.FinishButton).clicked.connect(self.finishWizard)
        self.button(QWizard.CancelButton).clicked.connect(self.cancelWizard)

        """List of page navigation buttons"""
        """
        QWizard.BackButton 	0 	The Back button (Go Back on Mac OS X)
        QWizard.NextButton 	1 	The Next button (Continue on Mac OS X)
        QWizard.CommitButton 	2 	The Commit button
        QWizard.FinishButton 	3 	The Finish button (Done on Mac OS X)
        QWizard.CancelButton 	4 	The Cancel button (see also NoCancelButton)
        QWizard.HelpButton 	5 	The Help button (see also HaveHelpButton)
        QWizard.CustomButton1 	6 	The first user-defined button (see also HaveCustomButton1)
        QWizard.CustomButton2 	7 	The second user-defined button (see also HaveCustomButton2)
        QWizard.CustomButton3 	8 	The third us
        """

        # Registering event handlers for image/layer source
        self.layers_tool_button.clicked.connect(self.loadLayers)
        self.file_tool_button.clicked.connect(self.selectFile)
        self.add_source_button.clicked.connect(self.addSources)
        self.remove_source_button.clicked.connect(self.removeSources)
        self.up_source_button.clicked.connect(self.upSource)
        self.down_source_button.clicked.connect(self.downSource)

        # Registering event handlers for editing metadata
        self.added_sources_list_widget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.default_button.clicked.connect(self.loadMetadataSettings)
        self.clean_button.clicked.connect(self.cleanMetadataSettings)
        self.save_button.clicked.connect(self.saveMetadata)

        #set the format of calendars
        self.sense_start_edit.setCalendarPopup(1)
        self.sense_start_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.sense_end_edit.setCalendarPopup(1)
        self.sense_end_edit.setDisplayFormat('dd.MM.yyyy HH:mm')

        # Registering event handlers for upload
        self.upload_button.clicked.connect(self.startUploader)
        self.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)

        #make sure about this function
        #self.exec_()

    #function for testing
    def test(self):
        #outStr = "" + repr(self.settings.value('locale/userLocale')) + "\n" + str(self.metadata) + "\n" + str(sys.path)
        outStr = "Bonjour!"
        qMsgBox = QMessageBox()
        qMsgBox.setText(outStr)
        qMsgBox.exec_()

    # Event handling for page navigation
    def previousPage(self):

        #qMsgBox = QMessageBox()
        #qMsgBox.setText(str(self.currentId()))
        #qMsgBox.exec_()
        pass

    def nextPage(self):

        if self.currentId() == 1:
            #filename = self.source_file_edit.text()
            self.added_sources_list_widget.clear()

            selected_layers = []

            for i in range(0, self.sources_list_widget.count()):
                each_item = self.sources_list_widget.item(i)
                self.added_sources_list_widget.addItem(each_item.clone()) #why clone?

                data_each_item = each_item.data(Qt.UserRole)
                selected_layers.append(repr(data_each_item))

            #qMsgBox = QMessageBox()
            #qMsgBox.setText(repr(selected_layers))
            #qMsgBox.exec_()

        elif self.currentId() == 2:
            self.button(QWizard.FinishButton).setEnabled(False)
        else:
            pass

    def finishWizard(self):
        #return imgSettigs and imgMetadata?
        #need validation
        pass

    def cancelWizard(self):
        #return imgSettigs and imgMetadata?
        #need confirmation
        pass

    # event handling for image/layer source
    def loadLayers(self):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if not self.layers_list_widget.findItems(layer.name(),Qt.MatchExactly):
                item = QListWidgetItem()
                item.setText(layer.name())
                item.setData(Qt.UserRole, layer.dataProvider().dataSourceUri()) # why using QtUserRole?
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
            pass
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
            #it is better to change item into each_layer?
            for item in selected_layers:
                if self.validateLayer(item.text()):
                    if not self.sources_list_widget.findItems(item.text(),Qt.MatchExactly):
                        self.layers_list_widget.takeItem(self.layers_list_widget.row(item))
                        self.sources_list_widget.addItem(item)
                        #self.added_sources_list_widget.addItem(item.clone()) #why clone?

        self.bar.clearWidgets()
        self.bar.pushMessage(
            'INFO',
            'Select sources were added to the upload queue',
            level=QgsMessageBar.INFO)

        #make sure about this statement later
        #self.loadFullMetadata()

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
            pass

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

    # for validation of files
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

    # for validation of layers
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

    # event handling for editing metadata
    def loadMetadataSettings(self):

        """ need to modify this part! """
        #items_for_metadata = None
        #items_for_metadata = []
        items_for_metadata = self.added_sources_list_widget.selectedItems()
        first_item = items_for_metadata[0]
        file_path = first_item.data(Qt.UserRole)

        mHdl = MetadataHandler()
        fileName = mHdl.extractMetadata(file_path)

        qMsgBox = QMessageBox()
        qMsgBox.setText("Under construction: metadata will be extracted from " + repr(fileName))
        qMsgBox.exec_()

    def cleanMetadataSettings(self):
        qMsgBox = QMessageBox()
        qMsgBox.setText("Under construction: message from cleanMetadataSettings method.")
        qMsgBox.exec_()

    def saveMetadata(self):
        qMsgBox = QMessageBox()
        qMsgBox.setText("Under construction: message from saveMetadata method.")
        qMsgBox.exec_()

    # Event handling for upload
    def startUploader(self):

        """note: please replace this part into module_access_oam_catalog.py,
        when access via oam-catalog"""
        s3Manager = S3Manager()

        if s3Manager.uploadExe():
            self.button(QWizard.FinishButton).setEnabled(True)
            self.button(QWizard.CancelButton).setEnabled(False)
            self.button(QWizard.BackButton).setEnabled(False)
            qMsgBox = QMessageBox()
            qMsgBox.setText("Files were successfully uploaded.")
            qMsgBox.exec_()
        else:
            pass

    def enableSpecify(self):
        if self.storage_combo_box.currentIndex() == 1:
            self.specify_label.setEnabled(1)
            self.specify_edit.setEnabled(1)
        else:
            self.specify_label.setEnabled(0)
            self.specify_edit.setText('')
            self.specify_edit.setEnabled(0)
