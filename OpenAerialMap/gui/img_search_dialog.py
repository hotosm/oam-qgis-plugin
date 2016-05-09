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
from PyQt4 import QtCore

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

        self.initializeGui()

        # event handling
        self.connect(self.buttonBox, QtCore.SIGNAL('accepted()'), self.execOk)
        self.connect(self.buttonBox, QtCore.SIGNAL('rejected()'), self.execCancel)

        self.pushButtonSearch.clicked.connect(self.startSearch)
        self.pushButtonBrowseLatest.clicked.connect(self.browseLatest)
        self.pushButtonBrowseLocation.clicked.connect(self.browseLocation)

        #self.buttonBox.clicked.connect(lambda: self.test(self.buttonBox))
        #self.connect(self.buttonBox, QtCore.SIGNAL('clicked(QAbstractButton*)'), lambda: self.test(self.buttonBox))
        #self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.execOk)
        #self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.execCancel)
        #self.buttonBox.accepted.connect(self.execOk)
        #self.buttonBox.rejected.connect(self.execCancel)

    def test(self, *argv):
        print(str(argv))

    def initializeGui(self):
        item = QListWidgetItem()
        item.setText("Please set the conditions and press 'Search' button.")
        self.listWidget.addItem(item)

        scene = QGraphicsScene()
        icon_abspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icon/icon.png')
        scene.addPixmap(QPixmap(icon_abspath))
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

        self.lineEditLocation.setText("Enter location")
        self.dateEditStart.setDateTime(QDateTime.currentDateTime())
        self.dateEditEnd.setDateTime(QDateTime.currentDateTime())
        self.lineEditResolution.setText("Enter resolution")

    def startSearch(self):
        queries = []
        queries.append(self.lineEditLocation.text())
        queries.append(self.dateEditStart.dateTime().toString(Qt.ISODate))
        queries.append(self.dateEditEnd.dateTime().toString(Qt.ISODate))
        queries.append(self.lineEditResolution.text())

        print("Search has started..." + repr(queries))

    def browseLatest(self):
        print("Browse latest imagery...")

    def browseLocation(self):
        print("Browse location of loaded layer...")

    def execOk(self):
        print("OK")

    def execCancel(self):
        print("Canceled")
