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

import os, sys

from PyQt4 import QtGui, uic
from PyQt4 import QtCore
from PyQt4.Qt import *

from img_browser import ImgBrowser
from module.module_access_oam_catalog import OAMCatalogAccess

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_search_dialog.ui'))


class ImgSearchDialog(QtGui.QDialog, FORM_CLASS):

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(ImgSearchDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint |
                            Qt.WindowMinimizeButtonHint)

        # initialize GUI
        self.initGui()

        # event handling
        self.pushButtonSearch.clicked.connect(self.startSearch)
        self.pushButtonSearchLatest.clicked.connect(self.searchLatest)
        self.pushButtonBrowseLocation.clicked.connect(self.browseLocation)
        self.connect(self.listWidget, QtCore.SIGNAL(
            "itemClicked(QListWidgetItem *)"),
            self.browseThumbnailAndMeta)

        # self.buttonBox.clicked.connect(lambda: self.test(self.buttonBox))
        self.connect(self.buttonBox,
                     QtCore.SIGNAL('accepted()'),
                     self.execOk)
        self.connect(self.buttonBox,
                     QtCore.SIGNAL('rejected()'),
                     self.execCancel)

        # disable some GUIs
        self.label_2.setEnabled(False)
        self.lineEditLocation.setEnabled(False)
        self.pushButtonBrowseLocation.setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        # hide some GUIs
        self.label_2.hide()
        self.lineEditLocation.hide()
        self.pushButtonBrowseLocation.hide()
        self.buttonBox.button(QDialogButtonBox.Ok).hide()

        # add objects for catalog access
        self.oamCatalogAccess = OAMCatalogAccess(
            "https://oam-catalog.herokuapp.com")
            
        # url for test
        #self.oamCatalogAccess = OAMCatalogAccess(
        #    "http://localhost:4000")

        self.imgBrowser = None

    def test(self, *argv):
        print(str(argv))

    def initGui(self):

        item = QListWidgetItem()
        item.setText("Please set the conditions and press 'Search' button.")
        item.setData(Qt.UserRole, "Sample Data")
        self.listWidget.addItem(item)

        self.lineEditLocation.setText("")
        self.dateEditAcquisitionFrom.setDate(QDate.currentDate().addMonths(-6))
        self.dateEditAcquisitionTo.setDate(QDate.currentDate())
        self.lineEditResolutionFrom.setText("")
        self.lineEditResolutionTo.setText("")
        self.lineEditNumImages.setText("20")

    def refreshListWidget(self, metadataInList):

        self.listWidget.clear()

        for singleMetaInDict in metadataInList:
            item = QListWidgetItem()
            item.setText(str(singleMetaInDict['title']))
            item.setData(Qt.UserRole, singleMetaInDict)
            self.listWidget.addItem(item)

    def startSearch(self):
        action = "meta"
        dictQueries = {}

        try:
            # temporarily disable this part
            # dictQueries['location'] = self.lineEditLocation.text()
            dictQueries['acquisition_from'] = \
                self.dateEditAcquisitionFrom.date().toString(Qt.ISODate)
            dictQueries['acquisition_to'] = \
                self.dateEditAcquisitionTo.date().toString(Qt.ISODate)
            if (self.lineEditResolutionFrom.text() != '' and
                    self.lineEditResolutionFrom.text() is not None):
                dictQueries['gsd_from'] = \
                    float(self.lineEditResolutionFrom.text())
            if (self.lineEditResolutionTo.text() != '' and
                    self.lineEditResolutionTo.text() is not None):
                dictQueries['gsd_to'] = \
                    float(self.lineEditResolutionTo.text())
            if (self.lineEditNumImages.text() != '' and
                    self.lineEditNumImages.text() is not None):
                dictQueries['limit'] = int(self.lineEditNumImages.text())

            self.oamCatalogAccess.setAction(action)
            self.oamCatalogAccess.setDictQueries(dictQueries)
            metadataInList = self.oamCatalogAccess.getMetadataInList()

            self.refreshListWidget(metadataInList)

        except Exception as e:
            qMsgBox = QMessageBox()
            qMsgBox.setWindowTitle('Message')
            qMsgBox.setText("Please make sure if you entered valid data" +
                            "/internet connection, and try again.")
            qMsgBox.exec_()

    def searchLatest(self):
        action = "meta"
        dictQueries = {}

        try:
            dictQueries['sort'] = "desc"
            dictQueries['order_by'] = "acquisition_end"
            if (self.lineEditResolutionFrom.text() != '' and
                    self.lineEditResolutionFrom.text() is not None):
                dictQueries['gsd_from'] = float(
                    self.lineEditResolutionFrom.text())
            if (self.lineEditResolutionTo.text() != '' and
                    self.lineEditResolutionTo.text() is not None):
                dictQueries['gsd_to'] = float(
                    self.lineEditResolutionTo.text())
            if (self.lineEditNumImages.text() != '' and
                    self.lineEditNumImages.text() is not None):
                dictQueries['limit'] = int(self.lineEditNumImages.text())

            self.oamCatalogAccess.setAction(action)
            self.oamCatalogAccess.setDictQueries(dictQueries)
            metadataInList = self.oamCatalogAccess.getMetadataInList()

            self.refreshListWidget(metadataInList)

        except Exception as e:
            qMsgBox = QMessageBox()
            qMsgBox.setWindowTitle('Message')
            qMsgBox.setText("Please make sure if you entered " +
                            "valid data/internet connection, and try again.")
            qMsgBox.exec_()

    def browseLocation(self):
        print("Browse location of loaded layer...")

    def browseThumbnailAndMeta(self, item):
        singleMetaInDict = item.data(Qt.UserRole)
        # print(str(singleMetaInDict))

        if type(singleMetaInDict) is dict:

            if self.imgBrowser is None:
                self.imgBrowser = ImgBrowser(self.iface, singleMetaInDict)
            else:
                self.imgBrowser.setSingleMetaInDic(singleMetaInDict)

            if not self.imgBrowser.isVisible():
                self.imgBrowser.show()

            self.imgBrowser.displayThumbnailAndMeta()
            self.imgBrowser.activateWindow()

    def execOk(self):
        # save the setting to QSetting and close the dialog.
        print("OK")

    def execCancel(self):
        # print("Canceled")
        self.close()
