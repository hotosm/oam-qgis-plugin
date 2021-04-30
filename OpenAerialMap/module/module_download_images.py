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
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

import sys, os, time
import urllib.request, urllib.error, urllib.parse
import json
# from qgis.PyQt import QtCore
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import QThread, pyqtSignal, QObject
from qgis.PyQt.Qt import *

class ThumbnailManager(QObject):

    statusChanged = pyqtSignal(int)
    error = pyqtSignal(Exception)

    def __init__(self, parent=None):
        QObject.__init__(self)

    def downloadThumbnail(self, urlThumbnail, prefix):
        self.statusChanged.emit(0)
        imgDirAbspath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'temp')
        # print(urlThumbnail)
        # Concatenate fileName with id to avoid duplicate filename
        imgFileName = urlThumbnail.split('/')[-1]
        imgFileName = prefix + imgFileName
        imgAbspath = os.path.join(imgDirAbspath, imgFileName)
        # print(imgAbspath)
        if not os.path.exists(imgAbspath):
            try:
                response = urllib.request.urlopen(urlThumbnail)
                chunkSize = 1024 * 16
                f = open(imgAbspath, 'wb')
                while True:
                    chunk = response.read(chunkSize)
                    if not chunk:
                        break
                    f.write(chunk)
                f.close()
                self.statusChanged.emit(1)
            except Exception as e:
                imgAbspath = 'failed'
                self.error.emit(e)
        return imgAbspath


class ImgMetaDownloader(object):
    def __init__(self, parent=None):
        pass

    @staticmethod
    def downloadImgMeta(urlImgMeta, imgMetaAbsPath):
        try:
            f = open(imgMetaAbsPath, 'w')
            f.write(urllib.request.urlopen(urlImgMeta).read())
            f.close()
        except Exception as e:
            print(str(e))

        return True


class DownloadProgressWindow(QWidget):

    # MAX_WINDOW_WIDTH = 600
    MAX_NUM_DOWNLOADS = 20
    MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR = 50
    POSITION_WINDOW_FROM_RIGHT = 20
    POSITION_WINDOW_FROM_BOTTOM = 75

    def __init__(self, iface, parent=None):
        QWidget.__init__(self)
        self.iface = iface
        # self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('Download Progress')
        self.vLayout = QVBoxLayout(self)

        self.activeId = -1

    def initWindowPosition(self):
        screenShape = QDesktopWidget().screenGeometry()
        screenWidth = screenShape.width()
        screenHeight = screenShape.height()

        winWidth = self.frameGeometry().width()
        winHeight = self.frameGeometry().height()

        posLeft = screenWidth - (winWidth + self.POSITION_WINDOW_FROM_RIGHT)
        posTop = screenHeight - (winHeight + self.POSITION_WINDOW_FROM_BOTTOM)
        self.move(posLeft, posTop)

        # print('Pos_X: {}'.format(posLeft))
        # print('Pos_Y: {}'.format(posTop))
        # print('Win Width: {}'.format(self.frameGeometry().width()))
        # print('Win Height: {}'.format(self.frameGeometry().height()))

    def adjustWindowPosition(self):
        screenShape = QDesktopWidget().screenGeometry()
        screenWidth = screenShape.width()
        screenHeight = screenShape.height()

        winWidth = self.frameGeometry().width()
        winHeight = self.frameGeometry().height()

        winRight = self.pos().x() + winWidth
        winBottom = self.pos().y() + winHeight

        posLeft = self.pos().x()
        posTop = self.pos().y()

        if winRight + self.POSITION_WINDOW_FROM_RIGHT >= screenWidth:
            posLeft = screenWidth - (
                winWidth + self.POSITION_WINDOW_FROM_RIGHT)
            self.move(posLeft, self.pos().y())

        if winBottom + self.POSITION_WINDOW_FROM_BOTTOM >= screenHeight:
            posTop = screenHeight - (
                winHeight + self.POSITION_WINDOW_FROM_BOTTOM)
            self.move(self.pos().x(), posTop)

        # print('ScreenW: ' + str(screenWidth) +
        #       ' ScreenH:' + str(screenHeight))
        # print('WinWidth: ' + str(winWidth) +
        #       ' WinHeight: ' + str(winHeight))
        # print('Left: ' + str(posLeft) + ' Top: ' + str(posTop))
        # print('')

    """
    def setWindowPosition(self):
        # This part need to be modified...
        maxHeight = int(
            DownloadProgressWindow.MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR * len(self.hLayouts))
        # self.setMaximumWidth(DownloadProgressWindow.MAX_WINDOW_WIDTH)
        self.setMaximumHeight(maxHeight)
        screenShape = QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = (self.frameGeometry().width(),
                      self.frameGeometry().height())
        left = width - (
            winW + DownloadProgressWindow.POSITION_WINDOW_FROM_RIGHT)
        top = height - (
            winH + DownloadProgressWindow.POSITION_WINDOW_FROM_BOTTOM)
        # print('ScreenW: ' + str(width) + ' ScreenH:' + str(height))
        # print('WinWidth: ' + str(winW) +
        #     ' WinHeight: ' + str(winH) +
        #     ' MaxHeight: ' + str(maxHeight))
        # print('Left: ' + str(left) + ' Top: ' + str(top))
        # print('')
        self.move(left, top)
        self.activateWindow()
    """

    def closeEvent(self, closeEvent):
        for eachTread in self.dwThreads:
            eachTread.stop()
            eachTread.quit()

        self.clearLayout(self.vLayout)
        self.activeId = -1

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def startDownload(self, url=None, fileAbsPath=None, addLayer=True):

        self.activeId += 1

        if self.activeId > DownloadProgressWindow.MAX_NUM_DOWNLOADS - 1:
            qMsgBox = QMessageBox()
            qMsgBox.setWindowTitle('Message')
            msg = "The maximum numbers of images for downloading " \
                  "is presently set to {0}.\nIf you need to " \
                  "download more, please finish the current " \
                  "uploading tasks first, and try download again" \
                  ".".format(DownloadProgressWindow.MAX_NUM_DOWNLOADS)
            qMsgBox.setText(msg)
            qMsgBox.exec_()
        else:
            # Initialize the lists
            if self.activeId == 0:
                self.hLayouts = []
                self.qLabels = []
                self.progressBars = []
                self.cancelButtons = []
                self.dwThreads = []

            # Create horizontal layouts and add to the vertical layout
            self.hLayouts.append(QHBoxLayout())
            self.vLayout.addLayout(self.hLayouts[self.activeId])

            # Create labes, progressbars, and cancel buttons,
            # and add to hLayouts
            self.qLabels.append(QLabel())

            self.progressBars.append(QProgressBar())
            self.cancelButtons.append(QPushButton('Cancel'))
            self.hLayouts[self.activeId].addWidget(
                self.qLabels[self.activeId], Qt.AlignLeft)
            self.hLayouts[self.activeId].addWidget(
                self.progressBars[self.activeId], Qt.AlignRight)
            self.hLayouts[self.activeId].addWidget(
                self.cancelButtons[self.activeId], Qt.AlignRight)

            self.qLabels[self.activeId].setFixedWidth(220)
            self.progressBars[self.activeId].setFixedWidth(120)
            self.cancelButtons[self.activeId].setFixedWidth(65)

            # Set the file names to labels
            fileName = os.path.basename(fileAbsPath)
            self.qLabels[self.activeId].setText(fileName)

            # add event listener and handlers to cancel buttons
            # threadIndex = self.activeId
            # self.cancelButtons[self.activeId].clicked.connect(
            #  lambda: self.cancelDownload(threadIndex))
            self.cancelButtons[self.activeId].clicked.connect(
                self.cancelDownload)

            # self.dwThreads.append(DownloadWorker(
            #       url, fileAbsPath, addLayer, threadIndex))
            self.dwThreads.append(DownloadWorker(url,
                                  fileAbsPath,
                                  addLayer,
                                  self.activeId))
            self.dwThreads[self.activeId].started.connect(
                self.downloadStarted)
            self.dwThreads[self.activeId].valueChanged.connect(
                self.updateProgressBar)
            self.dwThreads[self.activeId].finished.connect(
                self.downloadFinished)
            self.dwThreads[self.activeId].error.connect(
                self.displayError)
            self.dwThreads[self.activeId].start()
            # self.dwThread.run()
            # self.dwThread.wait()
            # self.dwThread.terminate()

            # self.show()
            # self.setWindowPosition()

            if self.activeId == 0:
                self.show()
                self.initWindowPosition()
            else:
                self.activateWindow()
                self.adjustWindowPosition()

    # def cancelDownload(self, btnIndex):
    def cancelDownload(self):
        for index in range(0, len(self.cancelButtons)):
            if self.cancelButtons[index] == self.sender():
                # print(str(index))
                self.dwThreads[index].stop()

    def downloadStarted(self, hasStarted, index):
        # print('Index: ' + str(index))
        pass

    def updateProgressBar(self, valueChanged, index):
        # print(str(valueChanged))
        self.progressBars[index].setValue(valueChanged)

    def downloadFinished(self, result, index):
        # self.thread.quit()
        self.dwThreads[index].quit()
        # print('Result: ' + result)
        try:  # make sure if the labels still exist
            if result == 'success':
                self.qLabels[index].setText("Successfully downloaded.")
                # add the downloaded image as a raster layer
                if self.dwThreads[index].addLayer:
                    layerAbsPath = self.dwThreads[index].fileAbsPath
                    layerName = str(os.path.basename(layerAbsPath))
                    self.iface.addRasterLayer(layerAbsPath, layerName)
            elif result == 'cancelled':
                self.qLabels[index].setText("Download cancelled.")
            else:
                self.qLabels[index].setText("Unexpected incident occurred.")
        except:
            pass

    def displayError(self, errMsg, index):
        # print(str(errMsg))
        self.qLabels[index].setText("Error: " + str(errMsg))


class DownloadWorker(QThread):

    started = pyqtSignal(bool, int)
    valueChanged = pyqtSignal(int, int)
    finished = pyqtSignal(str, int)
    error = pyqtSignal(Exception, int)

    def __init__(self, url, fileAbsPath, addLayer, index, parent=None):
        QThread.__init__(self)
        self.url = url
        self.fileAbsPath = fileAbsPath
        self.addLayer = addLayer
        self.index = index
        self.isRunning = True
        # self.delay = 0.02

    def run(self):
        try:
            self.started.emit(True, self.index)
            u = urllib.request.urlopen(self.url)
            f = open(self.fileAbsPath, 'wb')
            meta = u.info()
            fileSize = int(meta.getheaders("Content-Length")[0])
            # print("Downloading: {0} Bytes: {1}".format(
            #                    str(self.url), str(fileSize)))
            fileSizeDownloaded = 0
            blockSize = 8192  # make sure if this block size is apropriate
            while True:
                buffer = u.read(blockSize)
                if not buffer or self.isRunning is False:
                    break
                fileSizeDownloaded += len(buffer)
                f.write(buffer)
                p = float(fileSizeDownloaded) / fileSize
                self.valueChanged.emit(int(p * 100), self.index)
            f.close()

            if self.isRunning is True:
                self.finished.emit('success', self.index)
            else:
                self.finished.emit('cancelled', self.index)

        except Exception as e:
            self.error.emit(e, self.index)

    def stop(self):
        self.isRunning = False
