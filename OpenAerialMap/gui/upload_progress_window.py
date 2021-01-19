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
from builtins import str
from builtins import range

import sys, os, time, math
# import imghdr, tempfile, requests, json
# import traceback
# from ast import literal_eval

from qgis.PyQt import QtCore
from qgis.PyQt.QtGui import *      # modify this part?
from qgis.PyQt.QtCore import QThread, pyqtSignal
from PyQt4.Qt import *

from module.module_access_s3 import S3UploadWorker

import boto
from boto.s3.connection import S3Connection, S3ResponseError


class UploadProgressWindow(QWidget):

    # MAX_WINDOW_WIDTH = 600
    MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR = 50
    POSITION_WINDOW_FROM_RIGHT = 10
    POSITION_WINDOW_FROM_BOTTOM = 50

    connected = pyqtSignal(bool)
    started = pyqtSignal(str)
    # progress = pyqtSignal(str)
    finished = pyqtSignal(int, int, int)
    # error = pyqtSignal(Exception, basestring)

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
        maxHeight = int(
            UploadProgressWindow.MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR * len(self.hLayouts))
        # self.setMaximumWidth(UploadProgressWindow.MAX_WINDOW_WIDTH)
        self.setMaximumHeight(maxHeight)
        screenShape = QDesktopWidget().screenGeometry()
        width, height = screenShape.width(), screenShape.height()
        winW, winH = (self.frameGeometry().width(),
                      self.frameGeometry().height())
        left = width - (
            winW + UploadProgressWindow.POSITION_WINDOW_FROM_RIGHT)
        top = height - (
            winH + UploadProgressWindow.POSITION_WINDOW_FROM_BOTTOM)
        # print('ScreenW: ' + str(width) + ' ScreenH:' + str(height))
        # print('WinWidth: ' + str(winW) +
        #       ' WinHeight: ' + str(winH) +
        #       ' maxHeight: ' + str(maxHeight))
        # print('Left: ' + str(left) + ' Top: ' + str(top))
        # print('')
        self.move(left, top)
        self.activateWindow()

    def startUpload(self,
                    storageType,
                    uploadFileAbspaths,
                    uploadOptions,
                    awsBucketKey=None,
                    awsBucketSecret=None,
                    awsBucketName=None,
                    googleClientSecret=None,
                    googleAppName=None,
                    dropboxAccessToken=None):

        # testing purpose only
        print(str(storageType))
        print(str(uploadFileAbspaths))
        print(str(uploadOptions))
        print(str(awsBucketKey))
        print(str(awsBucketSecret))
        print(str(awsBucketName))
        print(str(googleClientSecret))
        print(str(googleAppName))
        print(str(dropboxAccessToken))

        # make sure if it's ready to upload
        startFlag = False

        # for S3 uploader
        conn = None
        bucket = None

        # for google drive

        # for dropbox

        if storageType == 'aws':
            # probably need to set timeout
            try:
                conn = S3Connection(awsBucketKey, awsBucketSecret)
                bucket = conn.get_bucket(awsBucketName)
            except Exception as e:
                self.connected.emit(False)

            if bucket is not None:
                startFlag = True

        elif storageType == 'google':
            pass

        elif storageType == 'dropbox':
            pass


        numFileAbsPaths = len(uploadFileAbspaths)

        if startFlag:
            self.connected.emit(True)
            for i in range(self.activeId, self.activeId + numFileAbsPaths):

                # Create horizontal layouts and add to the vertical layout
                self.hLayouts.append(QHBoxLayout())
                self.vLayout.addLayout(self.hLayouts[i])

                # Create labes, progressbars,
                # and cancel buttons, and add to hLayouts
                self.qLabels.append(QLabel())
                self.progressBars.append(QProgressBar())
                self.cancelButtons.append(QPushButton('Cancel'))
                self.hLayouts[i].addWidget(self.qLabels[i], Qt.AlignLeft)
                self.hLayouts[i].addWidget(self.progressBars[i], Qt.AlignRight)
                self.hLayouts[i].addWidget(self.cancelButtons[i], Qt.AlignRight)

                self.progressBars[i].setFixedWidth(120)
                self.cancelButtons[i].setFixedWidth(65)

                # Set the file names to labels
                indexFileAbsPath = i - self.activeId
                fileName = os.path.basename(
                    uploadFileAbspaths[indexFileAbsPath])
                self.qLabels[i].setText(fileName)

                upWorker = None

                if storageType == 'aws':
                    upWorker = S3UploadWorker(
                        bucket,
                        uploadOptions,
                        uploadFileAbspaths[indexFileAbsPath],
                        i)
                elif storageType == 'google':
                    pass
                elif storageType == 'dropbox':
                    pass

                self.uwThreads.append(upWorker)

                self.cancelButtons[i].clicked.connect(self.cancelUpload)
                self.uwThreads[i].started.connect(self.uploadStarted)
                self.uwThreads[i].valueChanged.connect(self.updateProgressBar)
                self.uwThreads[i].finished.connect(self.uploadFinished)
                self.uwThreads[i].error.connect(self.displayError)

                self.uwThreads[i].start()
                # self.uwThread.run()
                # self.uwThread.wait()
                # self.uwThread.terminate()

            self.activeId += numFileAbsPaths
            self.numTotal += numFileAbsPaths

            self.show()
            self.setWindowPosition()
        else:
            self.connected.emit(False)

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
        # print(str(self.sender()))
        for index in range(0, len(self.cancelButtons)):
            if self.cancelButtons[index] == self.sender():
                # print(str(index))
                self.uwThreads[index].stop()

    def cancelAllUploads(self):
        for eachTread in self.uwThreads:
            eachTread.stop()

    def uploadStarted(self, hasStarted, index):
        # print('Index: ' + str(index))
        self.started.emit(self.uwThreads[index].fileAbsPath)

    def updateProgressBar(self, valueChanged, index):
        # print(str(valueChanged))
        self.progressBars[index].setValue(valueChanged)

    def uploadFinished(self, result, index):
        # print('Result: ' + result)
        try:  # make sure if the labels still exist
            if result == 'success':
                self.qLabels[index].setText("Successfully uploaded.")
                self.numSuccess += 1
                # self.progress.emit(self.uwThreads[index].fileAbsPath)
            elif result == 'cancelled':
                self.qLabels[index].setText("Upload cancelled.")
                self.numCancelled += 1
            else:
                self.qLabels[index].setText("Unexpected incident occurred.")
                self.numFailed += 1
        except:
            pass

        self.uwThreads[index].quit()

        if (self.numSuccess + self.numCancelled +
                    self.numFailed) == self.numTotal:

            self.finished.emit(self.numSuccess,
                               self.numCancelled,
                               self.numFailed)

        """
        self.threads[index].quit()
        self.threads[index].wait()
        self.threads[index].deleteLater()
        self.threads[index].terminate()
        """

    def displayError(self, exception, index):
        # need to test this part later
        self.qLabels[index].setText("Error: " + str(exception))
