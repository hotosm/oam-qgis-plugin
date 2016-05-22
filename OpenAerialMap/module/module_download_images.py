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
import urllib, urllib2
import json
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import QObject, QThread, pyqtSignal


class ThumbnailManager:

    def __init__(self, parent=None):
        pass

    @staticmethod
    def downloadThumbnail(urlThumbnail):
        imgDirAbspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
        print(urlThumbnail)
        imgFileName = urlThumbnail.split('/')[-1]
        imgAbspath = os.path.join(imgDirAbspath, imgFileName)
        print(imgAbspath)
        if not os.path.exists(imgAbspath):
            f = open(imgAbspath,'wb')
            f.write(urllib2.urlopen(urlThumbnail).read())
            f.close()
        return imgAbspath


class DownloadProgressWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        #self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('Download Progress')

        self.vLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)
        self.vLayout.addLayout(self.hLayout)

        self.qLabel = QLabel()
        self.progressBar = QProgressBar()
        self.cancelButton = QPushButton('Cancel')
        self.hLayout.addWidget(self.qLabel)
        self.hLayout.addWidget(self.progressBar)
        self.hLayout.addWidget(self.cancelButton)

        self.cancelButton.clicked.connect(self.cancelDownload)

        self.setMaximumHeight(60)
        screenShape = QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = self.frameGeometry().width(), self.frameGeometry().height()
        left = width - (winW + 10)
        top = height - (winH + 50)
        self.move(left,top)
        self.show()
        self.activateWindow()

        self.url = None
        self.fileAbsPath = None


    def startDownload(self, url=None, fileAbsPath=None):
        self.url = url
        self.fileAbsPath = fileAbsPath

        fileName = os.path.basename(self.fileAbsPath)
        self.qLabel.setText(fileName)

        self.dwThread = DownloadWorker(self.url, self.fileAbsPath)
        self.dwThread.started.connect(self.downloadStarted)
        self.dwThread.valueChanged.connect(self.updateProgressBar)
        self.dwThread.finished.connect(self.downloadFinished)
        self.dwThread.error.connect(self.displayError)
        self.dwThread.start()
        #self.dwThread.run()
        #self.dwThread.wait()
        #self.dwThread.terminate()

        #self.thread = QThread()
        #self.dw.moveToThread(self.thread)
        #self.thread.started.connect(self.dw.run)
        #self.thread.start()
        #self.thread.wait()
        #self.thread.terminate()

    def cancelDownload(self):
        self.dwThread.stop()

    def downloadStarted(self, hasStarted):
        #print('Download Start: ' + str(hasStarted))
        pass

    def updateProgressBar(self,valueChanged):
        #print(str(valueChanged))
        self.progressBar.setValue(valueChanged)

    def downloadFinished(self, result):
        #self.thread.quit()
        self.dwThread.quit()
        #print('Result: ' + result)
        if result == 'success':
            self.qLabel.setText("Successfully completed.")
        elif result == 'cancelled':
            self.qLabel.setText("Download cancelled.")
        else:
            self.qLabel.setText("Unexpected incident occurred.")

    def displayError(self, errMsg):
        #print(str(errMsg))
        self.qLabel.setText("Error: " + str(errMsg))

#class DownloadWorker(QObject):
class DownloadWorker(QThread):

    started = pyqtSignal(bool)
    valueChanged = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(Exception)

    def __init__(self, url, fileAbsPath, parent=None):
        #QObject.__init__(self)
        QThread.__init__(self)
        self.url = url
        self.fileAbsPath = fileAbsPath
        self.isRunning = True
        #self.delay = 0.02
    def run(self):
        """
        count = 0
        while count <= 100 and self.isRunning == True:
            try:
                time.sleep(self.delay)
                self.valueChanged.emit(count)
                #print(str(count))
                count+=1
            except Exception as e:
                self.isRunning = False
                self.error.emit(e)

        if self.isRunning == True:
            self.finished.emit('success')
        else:
            self.finished.emit('cancelled')
        """
        try:
            self.started.emit(True)
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
                self.valueChanged.emit(int(p*100))
            f.close()

        except Exception as e:
            self.error.emit(e)
            self.finished.emit('failed')

        if self.isRunning == True:
            self.finished.emit('success')
        else:
            self.finished.emit('cancelled')

    def stop(self):
        self.isRunning = False
