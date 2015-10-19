"""
/***************************************************************************
 OpenAerialMap QGIS plugin
 Module for accessing s3
 ***************************************************************************/
"""
import os, sys

from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtCore import QThread
#import threading
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

class S3Manager(S3Connection):

    def __init__(self, access_key_id, secret_access_key, bucket_name, filenames, upload_options, qMsgBar, parent=None):

        S3Connection.__init__(self, access_key_id, secret_access_key)
        self.upload_options = upload_options
        self.bucket_name = bucket_name
        self.bucket = None
        self.filenames = filenames
        self.bar2 = qMsgBar
        #self.uploaders = []
        self.threads = []
        self.count_uploaded_images = 0
        self.num_uploading_images = 0

    def get_bucket(self):

        for trial in xrange(3):
            if self.bucket: break
            try:
                self.bucket = super(S3Manager,self).get_bucket(self.bucket_name)
                QgsMessageLog.logMessage(
                    'Connection established' % trial,
                    'OAM',
                    level=QgsMessageLog.INFO)
            except:
                if trial == 2:
                   QgsMessageLog.logMessage(
                    'Failed to connect after 3 attempts',
                    'OAM',
                    level=QgsMessageLog.CRITICAL)

        return self.bucket

        """
        rsKeys = []
        for key in self.bucket.list():
            rsKeys.append(repr(key))
        return rsKeys
        """

    #functions for threading purpose
    def upload_files(self):

        # configure the QgsMessageBar
        messageBar = self.bar2.createMessage('INFO: Performing upload...', )
        progressBar = QProgressBar()
        progressBar.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        messageBar.layout().addWidget(progressBar)
        cancelButton = QPushButton()
        cancelButton.setText('Cancel')
        cancelButton.clicked.connect(self.cancelUpload)
        messageBar.layout().addWidget(cancelButton)
        self.bar2.clearWidgets()
        self.bar2.pushWidget(messageBar, level=QgsMessageBar.INFO)
        self.messageBar = messageBar

        #strFileNames = ''
        #testQThreads = []
        self.num_uploading_images = len(self.filenames)

        for i in range(0, self.num_uploading_images):
            filename = self.filenames[i]
            #strFileNames += filename

            """
            self.bar2.clearWidgets()
            self.bar2.pushMessage(
                'INFO',
                'Pre-upload image processing...',
                level=QgsMessageBar.INFO)

            # Perfom reprojection
            if filename in self.reprojected:
                filename = self.reproject(filename)
                QgsMessageLog.logMessage(
                    'Created reprojected file: %s' % filename,
                    'OAM',
                    level=QgsMessageLog.INFO)

            # Convert file format
            if not (imghdr.what(filename) == 'tiff'):
                filename = self.convert(filename)
                QgsMessageLog.logMessage(
                    'Converted file to tiff: %s' % filename,
                    'OAM',
                    level=QgsMessageLog.INFO)
            """

            # create a new uploader instance
            #self.uploaders.append(Uploader(filename,self.bucket,self.upload_options, i))
            uploader = Uploader(filename,self.bucket,self.upload_options, i)
            self.uploader = uploader

            try:
                # start the worker in a new thread
                self.threads.append(QThread())
                #self.thread = thread

                uploader.moveToThread(self.threads[i])
                uploader.finished.connect(self.uploaderFinished)
                uploader.error.connect(self.uploaderError)
                #uploader.progress.connect(progressBar.setValue)
                uploader.progress.connect(progressBar.setValue)
                self.threads[i].started.connect(uploader.run)
                self.threads[i].start()

                print repr(self.threads[i])
                print str(i+1)

            except Exception, e:
                return repr(e)

            #testQThreads.append(TestQThread(filename, self.bucket, self.upload_options))

    def cancelUpload(self):
        #delete list by loop?
        self.uploader.kill()
        self.bar2.clearWidgets()
        self.bar2.pushMessage(
            'WARNING',
            'Canceling upload...',
            level=QgsMessageBar.WARNING)

    def uploaderFinished(self, success, index):
        # clean up the uploader and thread
        try:
            self.uploader.deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting uploader\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        self.threads[index].quit()
        self.threads[index].wait()
        #self.thread.quit()
        #self.thread.wait()
        try:
            self.threads[index].deleteLater()
            #self.thread.deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting thread\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        # remove widget from message bar
        self.bar2.popWidget(self.messageBar)
        if success:
            self.count_uploaded_images += 1
            print str(self.count_uploaded_images)
            # report the result
            self.bar2.clearWidgets()
            self.bar2.pushMessage(
                'INFO',
                str(self.count_uploaded_images) + ' image(s) out of ' + str(self.num_uploading_images) + ' was(were) uploaded.',
                level=QgsMessageBar.INFO)
            QgsMessageLog.logMessage(
                'Upload succeeded',
                'OAM',
                level=QgsMessageLog.INFO)
        else:
            # notify the user that something went wrong
            self.bar2.pushMessage(
                'CRITICAL',
                'Upload was interrupted',
                level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage(
                'Upload was interrupted',
                'OAM',
                level=QgsMessageLog.CRITICAL)

    def uploaderError(self, e, exception_string):
        QgsMessageLog.logMessage(
            'Uploader thread raised an exception:\n'.format(exception_string),
            'OAM',
            level=QgsMessageLog.CRITICAL)


    #Testing purpose only
    def test(self):
        strResult = repr(self.upload_options) + repr(self.bucket_name) + repr(self.bucket) + repr(self.filenames)
        return strResult

    #Testing purpose only
    def get_all_keys(self):
        rsKeys = []
        try:
            myBucket = super(S3Manager,self).get_bucket(self.bucket_name)
            #convert botoList into normal python list
            for key in myBucket.list():
                rsKeys.append(repr(key))
        except:
            rsKeys = None

        return rsKeys


class Uploader(QObject):
    '''Handle uploads in a separate thread'''

    finished = pyqtSignal(bool, int)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float)

    def __init__(self,filename,bucket,options, index):
        QObject.__init__(self)
        self.filename = filename
        self.bucket = bucket
        self.killed = False
        self.options = options
        self.index = index

    def sendMetadata(self):
        jsonfile = os.path.splitext(self.filename)[0]+'.json'
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

    def notifyOAM(self):
        '''Just a stub method, not needed at the moment because indexing happens every 10 mins'''
        QgsMessageLog.logMessage(
            'AOM notified of new resource',
            'OAM',
            level=QgsMessageLog.INFO)

    def triggerTileService(self):
        url = "http://hotosm-oam-server-stub.herokuapp.com/tile"
        h = {'content-type':'application/json'}
        uri = "s3://%s/%s" % (self.bucket.name,os.path.basename(self.filename))
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
        success = False
        try:
            file_size = os.stat(self.filename).st_size
            chunk_size = 5242880
            chunk_count = int(math.ceil(file_size / float(chunk_size)))
            progress_count = 0

            multipart = self.bucket.initiate_multipart_upload(os.path.basename(self.filename))

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
                with FileChunkIO(self.filename, 'r', offset=offset, bytes=bytes) as fp:
                    multipart.upload_part_from_file(fp, part_num=i + 1)
                progress_count += 1
                QgsMessageLog.logMessage(
                    'Sent chunk #%d\n' % progress_count,
                    'OAM',
                    level=QgsMessageLog.INFO)
                self.progress.emit(progress_count / float(chunk_count)*100)
                QgsMessageLog.logMessage(
                    'Progress = %f' % (progress_count / float(chunk_count)),
                    'OAM',
                    level=QgsMessageLog.INFO)
            if self.killed is False:
                multipart.complete_upload()
                self.progress.emit(100)
                success = True
                if "notify_oam" in self.options:
                    self.notifyOAM()
                if "trigger_tiling" in self.options:
                    self.triggerTileService()
        except Exception, e:
            # forward the exception upstream (or try to...)
            # chunk size smaller than 5MB can cause an error, server does not expect it
            self.error.emit(e, traceback.format_exc())

        self.finished.emit(success, self.index)

    def kill(self):
        self.killed = True
