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
"""
import json, time, math, imghdr, tempfile
from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer, QgsMessageLog
import traceback
import requests, json
from ast import literal_eval
"""
import sys, os, time, math
from PyQt4 import QtCore
from PyQt4.QtGui import *      # modify this part?
from PyQt4.QtCore import QThread, pyqtSignal

import boto
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO


class S3UploadProgressWindow(QWidget):

    #MAX_WINDOW_WIDTH = 600
    MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR = 50
    POSITION_WINDOW_FROM_RIGHT = 10
    POSITION_WINDOW_FROM_BOTTOM = 50

    started = pyqtSignal(bool)
    startConfirmed = pyqtSignal(str)
    #progress = pyqtSignal(str)
    finished = pyqtSignal(int, int, int)
    #error = pyqtSignal(Exception, basestring)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Upload Progress')
        self.vLayout = QVBoxLayout(self)

        self.activeId = 0

        self.numTotal = 0
        self.numSuccess = 0
        self.numCancelled = 0
        self.numFailed = 0

        self.hLayouts = []
        self.qLabels = []
        self.progressBars = []
        self.cancelButtons = []
        self.uwThreads = []

    def setWindowPosition(self):
        # This part need to be modified...
        maxHeight = int(S3UploadProgressWindow.MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR * len(self.hLayouts))
        #self.setMaximumWidth(S3UploadProgressWindow.MAX_WINDOW_WIDTH)
        self.setMaximumHeight(maxHeight)
        screenShape = QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = self.frameGeometry().width(), self.frameGeometry().height()
        left = width - (winW + S3UploadProgressWindow.POSITION_WINDOW_FROM_RIGHT)
        top = height - (winH + S3UploadProgressWindow.POSITION_WINDOW_FROM_BOTTOM)
        print('ScreenW: ' + str(width) + ' ScreenH:' + str(height))
        print('WinWidth: ' + str(winW) + ' WinHeight: ' + str(winH) + ' maxHeight: ' + str(maxHeight))
        print('Left: ' + str(left) + ' Top: ' + str(top))
        print('')
        self.move(left, top)
        self.activateWindow()

    def startUpload(self, bucketKey, bucketSecret, bucketName, uploadOptions, uploadFileAbspaths):

        # probably need to set timeout
        conn = None
        bucket = None
        try:
            conn = S3Connection(bucketKey, bucketSecret)
            bucket = conn.get_bucket(bucketName)
        except Exception as e:
            self.started.emit(False)

        numFileAbsPaths = len(uploadFileAbspaths)

        if bucket is not None:
            self.started.emit(True)
            for i in range(self.activeId, self.activeId + numFileAbsPaths):

                # Create horizontal layouts and add to the vertical layout
                self.hLayouts.append(QHBoxLayout())
                self.vLayout.addLayout(self.hLayouts[i])

                # Create labes, progressbars, and cancel buttons, and add to hLayouts
                self.qLabels.append(QLabel())
                self.progressBars.append(QProgressBar())
                self.cancelButtons.append(QPushButton('Cancel'))
                self.hLayouts[i].addWidget(self.qLabels[i])
                self.hLayouts[i].addWidget(self.progressBars[i])
                self.hLayouts[i].addWidget(self.cancelButtons[i])

                # Set the file names to labels
                indexFileAbsPath = i - self.activeId
                fileName = os.path.basename(uploadFileAbspaths[indexFileAbsPath])
                self.qLabels[i].setText(fileName)

                s3UpWorker = S3UploadWorker(bucket, uploadOptions, uploadFileAbspaths[indexFileAbsPath], i)
                self.uwThreads.append(s3UpWorker)

                self.cancelButtons[i].clicked.connect(self.cancelUpload)
                self.uwThreads[i].started.connect(self.uploadStarted)
                self.uwThreads[i].valueChanged.connect(self.updateProgressBar)
                self.uwThreads[i].finished.connect(self.uploadFinished)
                self.uwThreads[i].error.connect(self.displayError)

                self.uwThreads[i].start()
                #self.uwThread.run()
                #self.uwThread.wait()
                #self.uwThread.terminate()

            self.activeId += numFileAbsPaths
            self.numTotal += numFileAbsPaths

            self.show()
            self.setWindowPosition()
        else:
            self.started.emit(False)

    def closeEvent(self, closeEvent):
        for eachTread in self.uwThreads:
            eachTread.stop()
            eachTread.quit()

        self.clearLayout(self.vLayout)
        self.numTotal = 0
        self.numSuccess = 0
        self.numCancelled = 0
        self.numFailed = 0

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def cancelUpload(self):
        #print(str(self.sender()))
        for index in range(0, len(self.cancelButtons)):
            if self.cancelButtons[index] == self.sender():
                #print(str(index))
                self.uwThreads[index].stop()

    def cancelAllUploads(self):
        for eachTread in self.uwThreads:
            eachTread.stop()

    def uploadStarted(self, hasStarted, index):
        #print('Index: ' + str(index))
        self.startConfirmed.emit(self.uwThreads[index].fileAbsPath)

    def updateProgressBar(self, valueChanged, index):
        #print(str(valueChanged))
        self.progressBars[index].setValue(valueChanged)

    def uploadFinished(self, result, index):
        #print('Result: ' + result)
        try:  # make sure if the labels still exist
            if result == 'success':
                self.qLabels[index].setText("Successfully uploaded.")
                self.numSuccess += 1
                #self.progress.emit(self.uwThreads[index].fileAbsPath)
            elif result == 'cancelled':
                self.qLabels[index].setText("Upload cancelled.")
                self.numCancelled += 1
            else:
                self.qLabels[index].setText("Unexpected incident occurred.")
                self.numFailed += 1
        except:
            pass

        self.uwThreads[index].quit()

        if (self.numSuccess + self.numCancelled + self.numFailed) == self.numTotal:
            self.finished.emit(self.numSuccess, self.numCancelled, self.numFailed)

        """
        self.threads[index].quit()
        self.threads[index].wait()
        self.threads[index].deleteLater()
        self.threads[index].terminate()
        """

    def displayError(self, exception, index):
        # need to test this part later
        self.qLabels[index].setText("Error: " + str(exception))


class S3UploadWorker(QThread):

    started = pyqtSignal(bool, int)
    valueChanged = pyqtSignal(int, int)
    finished = pyqtSignal(str, int)
    error = pyqtSignal(Exception, int)

    def __init__(self, bucket, uploadOptions, fileAbsPath, index, delay=0.10):
        QThread.__init__(self)
        self.bucket = bucket
        self.uploadOptions = uploadOptions
        self.fileAbsPath = fileAbsPath
        self.index = index
        self.isRunning = True

        self.delay = delay

    def uploadMetadata(self):

        #metaFileAbsPath = os.path.splitext(self.fileAbsPath)[0]  + '.tif_meta.json'
        metaFileAbsPath = self.fileAbsPath + '_meta.json'
        keyForMetaUp = Key(self.bucket)
        metaFileName = os.path.basename(metaFileAbsPath)
        keyForMetaUp.key = metaFileName
        try:
            keyForMetaUp.set_contents_from_filename(metaFileAbsPath)
        except Exception as e:
            self.error.emit(e, self.index)
            self.finished.emit('failed', self.index)

    def uploadImageFile(self):

        fileSize = os.stat(self.fileAbsPath).st_size
        keyName = os.path.basename(self.fileAbsPath)  # make unique id later
        mp = self.bucket.initiate_multipart_upload(keyName)

        chunkSize = 5242880
        chunkCount = int(math.ceil(fileSize / float(chunkSize)))

        self.started.emit(True, self.index)

        try:
            i = 0
            #for i in range(chunkCount):
            while self.isRunning and i < chunkCount:
                offset = chunkSize * i
                bytes = min(chunkSize, fileSize - offset)
                with FileChunkIO(self.fileAbsPath, 'r', offset=offset, bytes=bytes) as fp:
                    mp.upload_part_from_file(fp, part_num=i + 1)
                i += 1
                #emit progress here
                progress = i / float(chunkCount) * 100
                self.valueChanged.emit(progress, self.index)

        except Exception as e:
            self.error.emit(e, self.index)
            self.finished.emit('failed', self.index)

        if self.isRunning is True:
            mp.complete_upload()
            self.finished.emit('success', self.index)
        else:
            self.finished.emit('cancelled', self.index)

        """
        if "notify_oam" in self.uploadOptions:
            self.notifyOAM()
        if "trigger_tiling" in self.uploadOptions:
            self.triggerTileService()
        """

    def run(self):

        """
        #self.started.emit(True)
        count = 0
        while count <= 100 and self.isRunning == True:
            try:
                time.sleep(self.delay)
                self.valueChanged.emit(count, self.index)
                #print(str(count))
                count+=1
            except Exception as e:
                self.isRunning = False
                self.finished.emit('failed', self.index)
                self.error.emit(e, self.index)

        if self.isRunning == True:
            self.finished.emit('success', self.index)
        else:
            self.finished.emit('cancelled', self.index)

        """
        self.uploadMetadata()
        self.uploadImageFile()

    def stop(self):
        self.isRunning = False
