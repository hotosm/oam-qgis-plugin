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
from datetime import datetime
from dateutil import parser

from PyQt4 import QtGui, uic
from PyQt4 import QtCore
from PyQt4.Qt import *
# from PyQt4.Qt import QGraphicsScene, QPixmap

from module.module_download_images import (ThumbnailManager,
                                           DownloadProgressWindow,
                                           ImgMetaDownloader)

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/img_browser.ui'))


class ImgBrowser(QtGui.QDialog, FORM_CLASS):

    POSITION_WINDOW_FROM_RIGHT = 50
    POSITION_WINDOW_FROM_TOP = 100

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(ImgBrowser, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint |
                            Qt.WindowMinimizeButtonHint)

        screenShape = QtGui.QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = (self.frameGeometry().width(),
                      self.frameGeometry().height())
        left = width - (winW + ImgBrowser.POSITION_WINDOW_FROM_RIGHT)
        top = ImgBrowser.POSITION_WINDOW_FROM_TOP
        self.move(left, top)

        scene = QGraphicsScene()
        defaultImgAbsPath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'temp', 'oam-logo.png')
        scene.addPixmap(QPixmap(defaultImgAbsPath))
        self.graphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

        self.connect(self.pushButtonDownload,
                     QtCore.SIGNAL("clicked()"),
                     self.downloadFullImage)
        self.checkBoxSaveMeta.setChecked(True)

        self.singleMetaInDic = None
        self.thumbnailManager = ThumbnailManager()

        self.downloadProgressWindow = None

    def setSingleMetaInDic(self, singleMetaInDic):
        self.singleMetaInDic = singleMetaInDic
        # self.imgDownloader = ImgDownloader()

    def setDefaultGraphicsView(self):
        scene = QGraphicsScene()
        defaultImgAbsPath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'temp', 'oam-logo.png')
        scene.addPixmap(QPixmap(defaultImgAbsPath))
        self.graphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

    def displayMetadata(self):
        self.setDefaultGraphicsView()
        aquisitionStart = parser.parse(str(self.singleMetaInDic[u'acquisition_start']))
        strAcquisitionStart = aquisitionStart.strftime('%Y-%m-%d %H:%M (%Z)')
        # print(aquisitionStart.strftime('%Y-%m-%d %I:%M %p (%Z)'))
        aquisitionEnd = parser.parse(str(self.singleMetaInDic[u'acquisition_end']))
        strAcquisitionEnd = aquisitionEnd.strftime('%Y-%m-%d %H:%M (%Z)')
        # print(aquisitionEnd.strftime('%Y-%m-%d %I:%M %p (%Z)'))

        gsdForDisplay = float(int(self.singleMetaInDic[u'gsd'] * 100)) / 100
        fileSizeInMb = float(self.singleMetaInDic[u'file_size']) / (1000 * 1000)
        fileSizeInMb = float(int(fileSizeInMb * 100)) / 100
        # fileSizeInMb = self.singleMetaInDic[u'file_size'] / (1024 * 1024)

        strTitle = 'TITLE:\n' + self.singleMetaInDic[u'title'] + '\n'
        self.lbTitle.setWordWrap(True)
        self.lbTitle.setText(strTitle)

        strPlatform = self.singleMetaInDic[u'platform']
        strGsdForDisplay = str(gsdForDisplay) + ' m'
        strProvider = self.singleMetaInDic[u'provider']
        strFileSizeInMb = str(fileSizeInMb) + ' MB'

        self.lbText0.setText(strPlatform)
        self.lbText1.setText(strAcquisitionStart)
        self.lbText2.setText(strAcquisitionEnd)
        self.lbText3.setText(strGsdForDisplay)
        self.lbText4.setText(strProvider)
        self.lbText5.setText(strFileSizeInMb)

        # print(self.formLayoutMetadata.formAlignment())
        # self.formLayoutMetadata.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.formLayoutMetadata.setLabelAlignment(Qt.AlignLeft)

        return True

    def displayThumbnail(self):
        isDownloadSuccess = False
        urlThumbnail = self.singleMetaInDic[u'properties'][u'thumbnail']
        imageId = self.singleMetaInDic[u'_id']
        prefix = str(imageId) + '_'
        imgAbspath = self.thumbnailManager.downloadThumbnail(urlThumbnail, prefix)

        if imgAbspath != 'failed':
            isDownloadSuccess = True
            scene = QGraphicsScene()
            item = scene.addPixmap(QPixmap(imgAbspath))
            self.graphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
            self.graphicsView.setScene(scene)
            self.graphicsView.show()
        else:
            self.setDefaultGraphicsView()

        return isDownloadSuccess

    def downloadFullImage(self):
        urlFullImage = self.singleMetaInDic[u'uuid']
        imgFileName = urlFullImage.split('/')[-1]
        defaultDir = os.path.join(os.path.expanduser('~'), 'oam_images')
        imgAbsPath = os.path.join(defaultDir, imgFileName)
        if not os.path.exists(defaultDir):
            os.makedirs(defaultDir)

        fdlg = QtGui.QFileDialog()
        fdlg.setAcceptMode(QFileDialog.AcceptSave)
        fdlg.selectFile(imgAbsPath)
        fdlg.setFilter("GEOTiff")

        if fdlg.exec_():
            # excepton handling here?
            if self.downloadProgressWindow is None:
                self.downloadProgressWindow = DownloadProgressWindow(self.iface)

            if self.checkBoxAddLayer.isChecked():
                addLayer = True
            else:
                addLayer = False

            self.downloadProgressWindow.startDownload(
                urlFullImage, imgAbsPath, addLayer)

            if self.checkBoxSaveMeta.isChecked():
                urlImgMeta = self.singleMetaInDic[u'meta_uri']
                imgMetaFilename = urlImgMeta.split('/')[-1]
                imgMetaAbsPath = os.path.join(
                    os.path.dirname(imgAbsPath),
                    imgMetaFilename)
                r = ImgMetaDownloader.downloadImgMeta(
                    urlImgMeta,
                    imgMetaAbsPath)
                # print(str(r))
