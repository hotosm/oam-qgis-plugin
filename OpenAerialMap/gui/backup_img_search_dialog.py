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
import json

from PyQt4 import QtGui, uic
from PyQt4 import QtCore
from PyQt4.Qt import *

from img_browser import ImgBrowser
from module.module_access_oam_catalog import OAMCatalogAccess

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_search_dialog.ui'))


class ImgSearchDialog(QtGui.QDialog, FORM_CLASS):

    def __init__(self, iface, settings, parent=None):
        """Constructor."""
        super(ImgSearchDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        self.settings = settings

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
        self.lineEditLocation.setText('n.a.')
        self.lineEditLocation.setEnabled(False)
        # self.pushButtonBrowseLocation.setEnabled(False)
        self.pushButtonBrowseLocation.hide()

        # add objects for catalog access
        # self.oamCatalogAccess = OAMCatalogAccess(
        #    "https://oam-catalog.herokuapp.com")

        # add objects for catalog access
        self.settings.beginGroup("Storage")

        if self.settings.value('CATALOG_URL') is None or \
            str(self.settings.value('CATALOG_URL')) == '':
            self.catalogUrl = "https://oam-catalog.herokuapp.com"
        else:
            self.catalogUrl = str(self.settings.value('CATALOG_URL'))

        self.settings.endGroup()

        self.oamCatalogAccess = OAMCatalogAccess(self.catalogUrl)
        catalogUrlLabel = self.catalog_url_label.text() + self.catalogUrl
        self.catalog_url_label.setText(catalogUrlLabel)

        self.imgBrowser = None

    def test(self, *argv):
        print(str(argv))

    def createQueriesSettings(self):
        # self.settings.setValue('LOCATION', '')
        self.settings.setValue('ACQUISITION_FROM',
            QDate.currentDate().addMonths(-12).toString(Qt.ISODate))
        self.settings.setValue('ACQUISITION_TO',
            QDate.currentDate().toString(Qt.ISODate))
        self.settings.setValue('GSD_FROM', '')
        self.settings.setValue('GSD_TO', '')
        self.settings.setValue('LIMIT', 20)

    def loadQueriesSettings(self):
        self.settings.beginGroup("ImageSearch")
        # self.lineEditLocation.setText(
        #    self.settings.value('LOCATION'))
        self.dateEditAcquisitionFrom.setDate(QDate.fromString(
            self.settings.value('ACQUISITION_FROM'), Qt.ISODate))
        self.dateEditAcquisitionTo.setDate(QDate.fromString(
            self.settings.value('ACQUISITION_TO'), Qt.ISODate))
        self.lineEditResolutionFrom.setText(
            str(self.settings.value('GSD_FROM')))
        self.lineEditResolutionTo.setText(
            str(self.settings.value('GSD_TO')))
        self.lineEditNumImages.setText(
            str(self.settings.value('LIMIT')))
        self.settings.endGroup()

    def saveQueriesSettings(self):
        self.settings.beginGroup("ImageSearch")
        # self.settings.setValue('LOCATION',
        #     self.lineEditLocation.text())
        self.settings.setValue('ACQUISITION_FROM',
            self.dateEditAcquisitionFrom.date().toString(Qt.ISODate))
        self.settings.setValue('ACQUISITION_TO',
            self.dateEditAcquisitionTo.date().toString(Qt.ISODate))
        if (self.lineEditResolutionFrom.text() != ''
            and self.lineEditResolutionFrom.text() is not None):
            self.settings.setValue('GSD_FROM',
                float(self.lineEditResolutionFrom.text()))
        if (self.lineEditResolutionTo.text() != ''
            and self.lineEditResolutionTo.text() is not None):
            self.settings.setValue('GSD_TO',
                float(self.lineEditResolutionTo.text()))
        if (self.lineEditNumImages.text() != ''
            and self.lineEditNumImages.text() is not None):
            self.settings.setValue('LIMIT',
                int(self.lineEditNumImages.text()))
        self.settings.endGroup()

    def initGui(self):

        item = QListWidgetItem()
        item.setText("Please set the conditions and press 'Search' button.")
        item.setData(Qt.UserRole, "Sample Data")
        self.listWidget.addItem(item)

        # load default queries
        self.settings.beginGroup("ImageSearch")
        if self.settings.value('ACQUISITION_FROM') is None:
            print('create new queries settings')
            self.createQueriesSettings()
        self.settings.endGroup()

        self.loadQueriesSettings()

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
        # save self.defaultQueriesInDict into self.settings
        self.saveQueriesSettings()
        self.close()

    def execCancel(self):
        self.close()
