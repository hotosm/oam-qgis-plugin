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
import sys, os, time
import urllib2
import json
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, pyqtSignal


class ThumbnailManager:

    def __init__(self, parent=None):
        pass

    @staticmethod
    def downloadThumbnail(urlThumbnail, prefix):
        imgDirAbspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
        print(urlThumbnail)
        # Concatenate fileName with id to avoid duplicate filename
        imgFileName = urlThumbnail.split('/')[-1]
        imgFileName = prefix + imgFileName
        imgAbspath = os.path.join(imgDirAbspath, imgFileName)
        print(imgAbspath)
        if not os.path.exists(imgAbspath):
            try:
                f = open(imgAbspath,'wb')
                f.write(urllib2.urlopen(urlThumbnail).read())
                f.close()
            except Exception as e:
                print(str(e))
        return imgAbspath

class ImgMetaDownloader:
    def __init__(self, parent=None):
        pass

    @staticmethod
    def downloadImgMeta(urlImgMeta, imgMetaAbsPath):
        try:
            f = open(imgMetaAbsPath,'w')
            f.write(urllib2.urlopen(urlImgMeta).read())
            f.close()
        except Exception as e:
            print(str(e))

        return True

class DownloadProgressWindow(QWidget):

    MAX_NUM_DOWNLOADS = 3
    MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR = 50
    POSITION_WINDOW_FROM_RIGHT = 10
    POSITION_WINDOW_FROM_BOTTOM = 50

    def __init__(self, iface, parent=None):
        QWidget.__init__(self)
        self.iface = iface
        #self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('Download Progress')
        self.vLayout = QVBoxLayout(self)

        self.activeId = -1

    def setWindowPosition(self):
        # This part need to be modified...
        maxHeight = int(DownloadProgressWindow.MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR * len(self.hLayouts))
        self.setMaximumHeight(maxHeight)
        screenShape = QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = self.frameGeometry().width(), self.frameGeometry().height()
        left = width - (winW + DownloadProgressWindow.POSITION_WINDOW_FROM_RIGHT)
        top = height - (winH + DownloadProgressWindow.POSITION_WINDOW_FROM_BOTTOM)
        print('WinWidth: ' + str(winW) + ' WinHeight: ' + str(winH) + ' maxHeight: ' + str(maxHeight))
        self.move(left,top)
        self.show()
        self.activateWindow()

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

        self.activeId +=1

        if self.activeId > DownloadProgressWindow.MAX_NUM_DOWNLOADS -1:
            qMsgBox = QMessageBox()
            qMsgBox.setWindowTitle('Message')
            qMsgBox.setText("The maximum numbers of images for downloading is \
presently set to 3.\nIf you need to download more, please finish \
the current uploading tasks first, and try download again.")
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

            # Create labes, progressbars, and cancel buttons, and add to hLayouts
            self.qLabels.append(QLabel())

            self.progressBars.append(QProgressBar())
            self.cancelButtons.append(QPushButton('Cancel'))
            self.hLayouts[self.activeId].addWidget(self.qLabels[self.activeId])
            self.hLayouts[self.activeId].addWidget(self.progressBars[self.activeId])
            self.hLayouts[self.activeId].addWidget(self.cancelButtons[self.activeId])

            # Set the file names to labels
            fileName = os.path.basename(fileAbsPath)
            self.qLabels[self.activeId].setText(fileName)

            # add event listener and handlers to cancel buttons
            threadIndex = self.activeId
            self.cancelButtons[self.activeId].clicked.connect(lambda: self.cancelDownload(threadIndex))

            self.dwThreads.append(DownloadWorker(url, fileAbsPath, addLayer, threadIndex))
            self.dwThreads[self.activeId].started.connect(self.downloadStarted)
            self.dwThreads[self.activeId].valueChanged.connect(self.updateProgressBar)
            self.dwThreads[self.activeId].finished.connect(self.downloadFinished)
            self.dwThreads[self.activeId].error.connect(self.displayError)
            self.dwThreads[self.activeId].start()
            #self.dwThread.run()
            #self.dwThread.wait()
            #self.dwThread.terminate()

            self.setWindowPosition()

    def cancelDownload(self, btnIndex):
        print('Index: ' + str(btnIndex))
        self.dwThreads[btnIndex].stop()

    def downloadStarted(self, hasStarted, index):
        print('Index: ' + str(index))
        #pass

    def updateProgressBar(self,valueChanged, index):
        #print(str(valueChanged))
        self.progressBars[index].setValue(valueChanged)

    def downloadFinished(self, result, index):
        #self.thread.quit()
        self.dwThreads[index].quit()
        #print('Result: ' + result)
        try: #make sure if the labels still exist
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
        #print(str(errMsg))
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
        #self.delay = 0.02
    def run(self):
        try:
            self.started.emit(True, self.index)
            u = urllib2.urlopen(self.url)
            f = open(self.fileAbsPath, 'wb')
            meta = u.info()
            fileSize = int(meta.getheaders("Content-Length")[0])
            #print("Downloading: {0} Bytes: {1}".format(str(self.url), str(fileSize)))
            fileSizeDownloaded = 0
            blockSize = 8192 #make sure if this block size is apropriate
            while True:
                buffer = u.read(blockSize)
                if not buffer or self.isRunning == False:
                    break
                fileSizeDownloaded += len(buffer)
                f.write(buffer)
                p = float(fileSizeDownloaded) / fileSize
                self.valueChanged.emit(int(p*100), self.index)
            f.close()

        except Exception as e:
            self.error.emit(e, self.index)
            self.finished.emit('failed', self.index)

        if self.isRunning == True:
            self.finished.emit('success', self.index)
        else:
            self.finished.emit('cancelled', self.index)

    def stop(self):
        self.isRunning = False
