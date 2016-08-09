# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and
 upload imagery from/to the OAM catalog.
                            -------------------
        begin               : 2015-07-01
        copyright           : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email               : tassia@acaia.ca / yoji.salut@gmail.com
        git sha             : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# Qt classes
from PyQt4.Qt import *
from PyQt4.QtCore import (QSettings, QTranslator, qVersion, QCoreApplication,
                          pyqtSignal, QObject, QThread)
from PyQt4.QtGui import (QAction, QIcon, QMessageBox, QFileDialog,
                         QListWidgetItem, QSizePolicy, QGridLayout,
                         QPushButton, QProgressBar)

# icon images
import resources_rc

# classes for GUI
from gui.img_uploader_wizard import ImgUploaderWizard
from gui.img_search_dialog import ImgSearchDialog
from gui.setting_dialog import SettingDialog

# from gui.backuped_img_uploader_wizard import BackupedImgUploaderWizard

import os, sys
import webbrowser


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

        """move this part for tr into __init__.py?"""
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

        # Declare instance attributes
        self.actions = []

        # need to send this setting object to setting dialog.
        self.settings = QSettings('QGIS', 'oam-qgis-plugin')

        # Testing purpose only
        # self.settings.remove('')

        """this part is only for testImgUploader() function"""
        """Please delete these statements when we delete the
            testImgUploader() function"""
        self.currentImgSettings = self.settings
        self.currentImgMetadata = {}

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

    def displayImgUploaderWizard(self):
        pass

        self.imgUploaderWizard = ImgUploaderWizard(self.iface, self.settings)
        self.imgUploaderWizard.show()

    def displaySearchTool(self):

        self.imgSearchDialog = ImgSearchDialog(self.iface)
        self.imgSearchDialog.show()

    def displaySettingDialog(self):

        self.settingDialog = SettingDialog(self.iface, self.settings)
        self.settingDialog.show()

    def displayHelp(self):

        currentAbsPath = os.path.abspath(__file__)
        helpAbsPath = os.path.join(
            os.path.dirname(currentAbsPath),
            'help/index.html')
        url = 'file://' + str(helpAbsPath)
        webbrowser.open_new(url)

    def initGui(self):

        """Create the menu and toolbar inside the QGIS GUI."""

        self.menu = self.tr(u'&Open Aerial Map (OAM)')
        self.toolbar = self.iface.addToolBar(u'OpenAerialMap')
        self.toolbar.setObjectName(u'OpenAerialMap')

        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path_img_wizard = ':/plugins/OpenAerialMap/icon/icon.png'
        icon_path_search_tool = ':/plugins/OpenAerialMap/icon/search_icon.png'
        icon_path_setting_dialog = ':/plugins/OpenAerialMap/icon/settings_icon.png'
        icon_path_help = ':/plugins/OpenAerialMap/icon/help_icon.png'

        self.add_action(
            icon_path_img_wizard,
            text=self.tr(u'Upload Imagery'),
            callback=self.displayImgUploaderWizard,
            parent=self.iface.mainWindow())

        self.add_action(
            icon_path_search_tool,
            text=self.tr(u'Search Imagery'),
            callback=self.displaySearchTool,
            parent=self.iface.mainWindow())

        self.add_action(
            icon_path_setting_dialog,
            text=self.tr(u'Edit Settings'),
            callback=self.displaySettingDialog,
            parent=self.iface.mainWindow())

        self.add_action(
            icon_path_help,
            text=self.tr(u'OAM Help'),
            callback=self.displayHelp,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u'&Open Aerial Map (OAM)'), action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def run(self):
        """
        Please refer to the following functions for details:
        def displayImgUploaderWizard(self):
        def displaySearchTool(self):
        def displaySettingDialog(self):
        def displayHelp(self):
        """
        pass
