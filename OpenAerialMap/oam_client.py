# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and upload imagery from/to the OAM catalog.
                              -------------------
        begin                : 2015-07-01
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email                : tassia@acaia.ca
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication 
from PyQt4.QtGui import QAction, QIcon, QMessageBox, QFileDialog, QListWidgetItem, QSizePolicy, QGridLayout, QPushButton
from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from oam_client_dialog import OpenAerialMapDialog
import os, sys, math, imghdr
# Import modules needed for upload
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from filechunkio import FileChunkIO

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
        self.dlg = OpenAerialMapDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Open Aerial Map (OAM)')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'OpenAerialMap')
        self.toolbar.setObjectName(u'OpenAerialMap')

        self.dlg.bar = QgsMessageBar()
        self.dlg.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.dlg.layout().addWidget(self.dlg.bar)

    # noinspection PyMethodMayBeStatic
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

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/OpenAerialMap/icon.png'
        search_icon_path = ':/plugins/OpenAerialMap/search_icon.png'
        
        self.add_action(
            icon_path,
            text=self.tr(u'Upload imagery'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.add_action(
            search_icon_path,
            text=self.tr(u'Search imagery'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # Imagery tab
        self.loadLayers()
        self.dlg.file_tool_button.clicked.connect(self.selectFile)
        self.dlg.add_source_button.clicked.connect(self.addSources)
        self.dlg.remove_source_button.clicked.connect(self.removeSources)
        self.dlg.up_source_button.clicked.connect(self.upSource)
        self.dlg.down_source_button.clicked.connect(self.downSource)

        # Upload tab
        self.dlg.upload_button.clicked.connect(self.uploadS3)
        self.dlg.cancel_button.clicked.connect(self.closeDialog)
        self.dlg.storage_combo_box.currentIndexChanged.connect(self.enableUrl)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Open Aerial Map (OAM)'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def loadLayers(self):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            item = QListWidgetItem()
            item.setText(layer.name())
            item.setData(32, layer.dataProvider().dataSourceUri()) # 32 = Qt::UserRole, The first role that can be used for application-specific purposes
            self.dlg.layers_list_widget.addItem(item)
        self.dlg.bar.pushMessage("Loaded layers", "All layer are loaded, please select your sources", level=QgsMessageBar.INFO)

    def closeDialog(self):
        self.dlg.close()

    def selectFile(self):
        selected_file = QFileDialog.getOpenFileName(self.dlg, 'Select File', os.path.expanduser("~"))
        self.dlg.source_file_edit.setText(selected_file)

    def validateFile(self,file_name):
        if not os.path.isfile(file_name):
            self.dlg.bar.pushMessage("Invalid", "The file %s does not exist" % file_name, level=QgsMessageBar.CRITICAL)
            return 0
        elif not imghdr.what(file_name):
            self.dlg.bar.pushMessage("Invalid", "The file %s is not a supported data source" % file_name, level=QgsMessageBar.CRITICAL)
            return 0
        else:
            return 1

    def validateLayer(self,layer_name):
        all_layers = self.iface.mapCanvas().layers()
        for layer in all_layers:
            if layer_name == layer.name():
                if layer.type() == QgsMapLayer.VectorLayer:
                    self.dlg.bar.pushMessage("Invalid", "Vector layers can not be selected for upload", level=QgsMessageBar.CRITICAL)
                    return 0
                else:
                    return 1

    def addSources(self):
        file_name = self.dlg.source_file_edit.text()
        selected_layers = self.dlg.layers_list_widget.selectedItems()
        if not file_name and not selected_layers:
            self.dlg.bar.pushMessage('Invalid', 'Please select a layer or file to be added', level=QgsMessageBar.WARNING)
        if file_name:
            if self.validateFile(file_name):
                item = QListWidgetItem()
                item.setText(os.path.basename(file_name))
                item.setData(32, file_name) # 32 = Qt::UserRole, The first role that can be used for application-specific purposes
                self.dlg.sources_list_widget.addItem(item)
                self.dlg.source_file_edit.setText('')
        if selected_layers:
            for item in selected_layers:
                if self.validateLayer(item.text()):
                    self.dlg.layers_list_widget.takeItem(self.dlg.layers_list_widget.row(item))
                    self.dlg.sources_list_widget.addItem(item)
                   

    def removeSources(self):
        selected_layers = self.dlg.sources_list_widget.selectedItems()
        if selected_layers:
            for item in selected_layers:
                self.dlg.sources_list_widget.takeItem(self.dlg.sources_list_widget.row(item))
                all_layers = self.iface.mapCanvas().layers()
                for layer in all_layers:
                    if item.text() == layer.name():
                        self.dlg.layers_list_widget.addItem(item)
        else:
            self.dlg.bar.pushMessage('Invalid', 'Please select a source to be removed', level=QgsMessageBar.WARNING)

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

    def enableUrl(self):
        if self.dlg.storage_combo_box.currentIndex() == 1:
            self.dlg.url_label.setEnabled(1)
            self.dlg.url_edit.setEnabled(1)
        else:
            self.dlg.url_label.setEnabled(0)
            self.dlg.url_edit.setText('')
            self.dlg.url_edit.setEnabled(0)

    def uploadS3(self):
        if self.dlg.storage_combo_box == 0:
            bucket_name = 'oam-qgis-plugin-test'
        else:
            bucket_name = str(self.dlg.url_edit.text())
            if not bucket_name:
                self.dlg.bar.pushMessage('Missing storage', 'the bucket must be provided in the format s3://name_of_bucket', level=QgsMessageBar.CRITICAL)
        bucket_key = str(self.dlg.key_id_edit.text())
        bucket_secret = str(self.dlg.secret_key_edit.text())
        
        # uncomment the following lines and fill it in with your key info to bypass the plugin form
        #bucket_key = ''
        #bucket_secret = ''
        
        connection = S3Connection(bucket_key,bucket_secret)
        bucket = connection.get_bucket(bucket_name)
        if not bucket:
            self.dlg.bar.pushMessage('Missing connection', 'please check your connectivity and credentials', level=QgsMessageBar.CRITICAL)

        for index in xrange(self.dlg.sources_list_widget.count()):
            file_path = str(self.dlg.sources_list_widget.item(index).data(32))
            self.uploadFile(file_path,bucket)


    def uploadFile(self,file_path,bucket): 
        
        multipart = bucket.initiate_multipart_upload(os.path.basename(file_path))

        # Use a chunk size of 50 MiB
        file_size = os.stat(file_path).st_size
        chunk_size = 52428800
        chunk_count = int(math.ceil(file_size / float(chunk_size)))
        
        # Send the file parts, using FileChunkIO to create a file-like object
        # that points to a certain byte range within the original file. We
        # set bytes to never exceed the original file size.
        for i in range(chunk_count):
            offset = chunk_size * i
            bytes = min(chunk_size, file_size - offset)
            with FileChunkIO(file_path, 'r', offset=offset,
                             bytes=bytes) as fp:
                multipart.upload_part_from_file(fp, part_num=i + 1)
        
        # Finish the upload
        multipart.complete_upload()
        self.dlg.bar.pushMessage('Succeeded:', 'Uploaded file \"%s\"' % file_path, level=QgsMessageBar.SUCCESS)

    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
