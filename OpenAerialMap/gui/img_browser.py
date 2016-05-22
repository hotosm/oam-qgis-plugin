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

from module.module_download_images import (ThumbnailManager, DownloadProgressWindow)

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_browser.ui'))

class ImgBrowser(QtGui.QDialog, FORM_CLASS):

    def __init__(self, iface, singleMetaInDic, parent=None):
        """Constructor."""
        super(ImgBrowser, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        screenShape = QtGui.QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = self.frameGeometry().width(), self.frameGeometry().height()
        left = width - (winW + 50)
        top = 100
        self.move(left,top)

        self.connect(self.pushButtonDownload, QtCore.SIGNAL("clicked()"), self.downloadFullImage)

        self.singleMetaInDic = singleMetaInDic
        self.displayThumbnailAndMeta()

    def setSingleMetaInDic(self, singleMetaInDic):
        self.singleMetaInDic = singleMetaInDic
        #self.imgDownloader = ImgDownloader()

    def displayThumbnailAndMeta(self):

        urlThumbnail = self.singleMetaInDic[u'properties'][u'thumbnail']
        imgAbspath = ThumbnailManager.downloadThumbnail(urlThumbnail)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(imgAbspath))
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

        self.lbTest01.setWordWrap(True)
        self.lbTest01.setText(str(self.singleMetaInDic))

    def downloadFullImage(self):
        urlFullImage = self.singleMetaInDic[u'uuid']
        imgFileName = urlFullImage.split('/')[-1]
        defaultDir = os.path.join(os.path.expanduser('~'), 'oam_images')
        imgAbsPath = os.path.join(defaultDir, imgFileName)
        print(str(imgAbsPath))
        if not os.path.exists(defaultDir):
            os.makedirs(defaultDir)
        imgAbsPath = QtGui.QFileDialog.getSaveFileName(self, 'Save file', imgAbsPath, "GeoTiff")
        print(str(imgAbsPath))

        self.d = DownloadProgressWindow()
        self.d.startDownload(urlFullImage, imgAbsPath)
        #ImgDownloader.downloadFullImage(urlFullImage, imgAbsPath)
