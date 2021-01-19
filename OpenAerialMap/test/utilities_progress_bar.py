"""
This class can be used for testing progress bar.
It generates incrementing integer values from 0 to 100, and
emit signals, using PyQt singal.
"""

import sys, os, time
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QThread, pyqtSignal

class S3UploadWorker(QThread):

    started = pyqtSignal(bool)
    #valueChanged = pyqtSignal(float, int)
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

    def run(self):

        self.started.emit(True)
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
