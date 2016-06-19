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
import os, sys

from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtCore import QThread, Qt #,QObject
import json, time, math, imghdr, tempfile

from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer, QgsMessageLog

import boto
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import traceback
import requests, json
from ast import literal_eval
"""
import sys, os, time
from PyQt4 import QtCore
# modify this part?
from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, pyqtSignal

class S3UploadProgressWindow(QWidget):

    #MAX_WINDOW_WIDTH = 600
    MAX_WINDOW_HEIGHT_PER_PROGRESS_BAR = 50
    POSITION_WINDOW_FROM_RIGHT = 10
    POSITION_WINDOW_FROM_BOTTOM = 50

    #progress = pyqtSignal(int, int)
    # count success cancel failed
    finished = pyqtSignal(int, int, int)
    #error = pyqtSignal(Exception, basestring)

    def __init__(self, bucketKey, bucketSecret, bucketName, uploadOptions):
        QWidget.__init__(self)
        self.setWindowTitle('Upload Progress')
        self.vLayout = QVBoxLayout(self)

        self.bucketKey = bucketKey
        self.bucketSecret = bucketSecret
        self.bucketName = bucketName
        self.uploadOptions = uploadOptions

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
        self.move(left,top)
        self.activateWindow()

    def startUpload(self, uploadFileAbspaths):
        #print(str(uploadFileAbspaths))
        #for i in range(0, len(uploadFileAbspaths)):
        #    self.progress.emit(i, len(uploadFileAbspaths))
        #print(str(self.activeId))

        for i in range(self.activeId, self.activeId + len(uploadFileAbspaths)):

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
            indexFileAbsPath = i-self.activeId
            fileName = os.path.basename(uploadFileAbspaths[indexFileAbsPath])
            self.qLabels[i].setText(fileName)

            self.uwThreads.append(S3UploadWorker(uploadFileAbspaths[indexFileAbsPath], 'aaaaa', self.uploadOptions, i))

            self.cancelButtons[i].clicked.connect(self.cancelUpload)
            self.uwThreads[i].started.connect(self.uploadStarted)
            self.uwThreads[i].valueChanged.connect(self.updateProgressBar)
            self.uwThreads[i].finished.connect(self.uploadFinished)
            self.uwThreads[i].error.connect(self.displayError)

            self.uwThreads[i].start()
            #self.uwThread.run()
            #self.uwThread.wait()
            #self.uwThread.terminate()


        self.activeId += len(uploadFileAbspaths)
        self.numTotal += len(uploadFileAbspaths)

        self.show()
        self.setWindowPosition()

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
        pass

    def updateProgressBar(self, valueChanged, index):
        #print(str(valueChanged))
        self.progressBars[index].setValue(valueChanged)

    def uploadFinished(self, result, index):
        #self.thread.quit()
        self.uwThreads[index].quit()
        #print('Result: ' + result)
        try: #make sure if the labels still exist
            if result == 'success':
                self.qLabels[index].setText("Successfully uploaded.")
                self.numSuccess += 1
            elif result == 'cancelled':
                self.qLabels[index].setText("Upload cancelled.")
                self.numCancelled += 1
            else:
                self.qLabels[index].setText("Unexpected incident occurred.")
                self.numFailed += 1
        except:
            pass

        if (self.numSuccess + self.numCancelled + self.numFailed) == self.numTotal:
            self.finished.emit(self.numSuccess, self.numCancelled, self.numFailed)

    def displayError(self, errMsg, index):
        pass
        #print(str(errMsg))
        #self.qLabels[index].setText("Error: " + str(errMsg))


class S3UploadWorker(QThread):

    started = pyqtSignal(bool)
    #valueChanged = pyqtSignal(float, int)
    valueChanged = pyqtSignal(int, int)
    finished = pyqtSignal(str, int)
    error = pyqtSignal(Exception, int)

    def __init__(self, fileAbsPath, bucket, uploadOptions, index, delay=0.10):
        QThread.__init__(self)
        #self.fileAbsPath = fileAbsPath
        #self.bucket = bucket
        #self.uploadOptions = uploadOptions
        self.index = index
        #self.killed = False
        self.isRunning = True

        self.delay = delay

    def run(self):
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

        #self.uploadMetadata()
        #self.uploadImageFile()

    def stop(self):
        self.isRunning = False


"""
class S3UploadWorker(QThread):

    finished = pyqtSignal(bool, int)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float, int)

    def __init__(self, fileAbsPath, bucket, options, index):
        QThread.__init__(self)
        self.fileAbsPath = fileAbsPath
        self.bucket = bucket
        self.killed = False
        self.options = options
        self.index = index

    def sendMetadata(self):
        jsonfile = os.path.splitext(self.fileAbsPath)[0]+'.json'
        try:
            k = Key(self.bucket)
            k.key = os.path.basename(jsonfile)
            k.set_contents_from_filename(jsonfile)
            QgsMessageLog.logMessage(
                'Sent %s\n' % jsonfile,
                'OAM',
                level=QgsMessageLog.INFO)
        except:
            QgsMessageLog.logMessage(
                'Could not send %s\n' % jsonfile,
                'OAM',
                level=QgsMessageLog.CRITICAL)

    def sendImageFiles(self):

        success = False

        try:
            file_size = os.stat(self.fileAbsPath).st_size
            chunk_size = 5242880
            chunk_count = int(math.ceil(file_size / float(chunk_size)))
            progress_count = 0

            multipart = self.bucket.initiate_multipart_upload(os.path.basename(self.fileAbsPath))

            QgsMessageLog.logMessage(
                'Preparing to send %s chunks in total\n' % chunk_count,
                'OAM',
                level=QgsMessageLog.INFO)

            for i in range(chunk_count):

                if self.killed is True:
                    # kill request received, exit loop early
                    break

                offset = chunk_size * i
                # bytes are set to never exceed the original file size.
                bytes = min(chunk_size, file_size - offset)
                with FileChunkIO(self.fileAbsPath, 'r', offset=offset, bytes=bytes) as fp:
                    multipart.upload_part_from_file(fp, part_num=i + 1)
                progress_count += 1
                QgsMessageLog.logMessage(
                    'Sent chunk #%d\n' % progress_count,
                    'OAM',
                    level=QgsMessageLog.INFO)
                self.progress.emit(progress_count / float(chunk_count)*100, self.index)
                QgsMessageLog.logMessage(
                    'Progress = %f' % (progress_count / float(chunk_count)),
                    'OAM',
                    level=QgsMessageLog.INFO)

            if self.killed is False:

                multipart.complete_upload()
                self.progress.emit(100, self.index)
                success = True

                # need to modify this part?
                if "notify_oam" in self.options:
                    self.notifyOAM()
                if "trigger_tiling" in self.options:
                    self.triggerTileService()

        except Exception, e:
            # forward the exception upstream (or try to...)
            # chunk size smaller than 5MB can cause an error, server does not expect it
            self.error.emit(e, traceback.format_exc())

        self.finished.emit(success, self.index)

    #for option
    def notifyOAM(self):

        '''Just a stub method, not needed at the moment
        because indexing happens every 10 mins'''
        QgsMessageLog.logMessage(
            'AOM notified of new resource',
            'OAM',
            level=QgsMessageLog.INFO)

    #for options
    def triggerTileService(self):
        url = "http://hotosm-oam-server-stub.herokuapp.com/tile"
        h = {'content-type':'application/json'}
        uri = "s3://%s/%s" % (self.bucket.name,os.path.basename(self.fileAbsPath))
        QgsMessageLog.logMessage(
            'Imagery uri %s\n' % uri,
            'OAM',
            level=QgsMessageLog.INFO)
        d = json.dumps({'sources':[uri]})
        p = requests.post(url,headers=h,data=d)
        post_dict = json.loads(p.text)
        QgsMessageLog.logMessage(
            'Post response: %s' % post_dict,
            'OAM',
            level=QgsMessageLog.INFO)

        if u'id' in post_dict.keys():
            ts_id = post_dict[u'id']
            time = post_dict[u'queued_at']
            QgsMessageLog.logMessage(
                'Tile service #%s triggered on %s\n' % (ts_id,time),
                'OAM',
                level=QgsMessageLog.INFO)
        else:
            QgsMessageLog.logMessage(
                'Tile service could not be created\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        return(0)

    def run(self):
        self.sendMetadata()
        self.sendImageFiles()

    def kill(self):
        self.killed = True
"""
