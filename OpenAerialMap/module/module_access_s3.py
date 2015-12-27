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

from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtCore import QThread, Qt
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

    def __init__(self,
                 access_key_id,
                 secret_access_key,
                 bucket_name,
                 filenames,
                 upload_options,
                 wizard_page,
                 parent=None):

        S3Connection.__init__(self, access_key_id, secret_access_key)
        self.upload_options = upload_options
        self.bucket_name = bucket_name
        self.bucket = None
        self.filenames = filenames
        self.s3Uploaders = []
        self.threads = []

        self.count_uploaded_images = 0
        self.num_uploading_images = 0

        #For GUI (messages and progress bars)
        self.wizard_page = wizard_page

        self.uploader_widget = QtGui.QWidget()
        self.uploader_widget.setWindowTitle("Upload Progress Bars")
        self.uploader_widget.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.uploader_widget.move(20,20)
        self.uploader_v_box = QtGui.QVBoxLayout()
        self.uploader_widget.setLayout(self.uploader_v_box)

        self.msg_bar_main = None
        self.msg_bar_main_content = None
        self.cancel_button_main = None

        self.msg_bars = []
        self.msg_bars_content = []
        self.progress_bars = []
        self.cancel_buttons = []

    def getBucket(self):

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

        """for testing purpose"""
        """
        rsKeys = []
        for key in self.bucket.list():
            rsKeys.append(repr(key))
        return rsKeys
        """

    #functions for threading purpose
    def uploadFiles(self):

        """ Testing purpose only """
        if "reprojection" in self.upload_options:
            print "reprojection"
        if "license" in self.upload_options:
            print "license"
        if "notify_oam" in self.upload_options:
            print "notify_oam"
        if "trigger_tiling" in self.upload_options:
            print "trigger_tiling"

        # configure the msg_bar_main (including Cancel button and its container)
        self.msg_bar_main = QgsMessageBar()
        self.msg_bar_main.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.wizard_page.layout().addWidget(self.msg_bar_main)

        self.msg_bar_main_content = self.msg_bar_main.createMessage('Performing upload...', )
        self.cancel_button_main = QPushButton()
        self.cancel_button_main.setText('Cancel')
        self.cancel_button_main.clicked.connect(self.cancelAllUploads)
        self.msg_bar_main_content.layout().addWidget(self.cancel_button_main)
        self.msg_bar_main.clearWidgets()
        self.msg_bar_main.pushWidget(self.msg_bar_main_content, level=QgsMessageBar.INFO)

        self.num_uploading_images = len(self.filenames)

        for i in range(0, self.num_uploading_images):
            filename = self.filenames[i]

            # create a new S3Uploader instance
            self.s3Uploaders.append(S3Uploader(filename, self.bucket, self.upload_options, i))

            try:
                # start the worker in a new thread
                self.threads.append(QThread())
                self.s3Uploaders[i].moveToThread(self.threads[i])
                self.s3Uploaders[i].finished.connect(self.finishUpload)
                self.s3Uploaders[i].error.connect(self.displayUploadError)
                self.threads[i].started.connect(self.s3Uploaders[i].run)
                self.threads[i].start()

                print repr(self.threads[i])

                # configure the msg_bars for progress bar
                self.msg_bars.append(QgsMessageBar())
                self.msg_bars[i].setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
                #self.wizard_page.layout().addWidget(self.msg_bars[i])
                self.uploader_v_box.addWidget(self.msg_bars[i])

                #set the texts of uploading files
                file_basename = str(os.path.basename(str(filename)))
                self.msg_bars_content.append(self.msg_bars[i].createMessage(file_basename, ))
                self.msg_bars[i].clearWidgets()
                self.msg_bars[i].pushWidget(self.msg_bars_content[i], level=QgsMessageBar.INFO)

                #add progress bars in the message bar
                self.progress_bars.append(QProgressBar())
                self.progress_bars[i].setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
                self.msg_bars_content[i].layout().addWidget(self.progress_bars[i])
                self.s3Uploaders[i].progress.connect(self.updateProgressBar)

                #set cancel button in the message bar for each upload file
                """
                self.cancel_buttons.append(QPushButton())
                self.cancel_buttons[i].setText('Cancel')
                self.cancel_buttons[i].clicked.connect(self.cancelAllUploads)
                self.msg_bars_content[i].layout().addWidget(self.cancel_buttons[i])
                #self.cancel_buttons[i].clicked.connect(self.cancelUpload)
                """

            except Exception, e:
                return repr(e)

            #Display upload progress bars in a separate widget
            self.uploader_widget.show()

        return 0

    def updateProgressBar(self, progress_value, index):
        print "Progress: " + str(progress_value) + ", index: " + str(index)
        if self.progress_bars[index] != None:
            self.progress_bars[index].setValue(progress_value)

    def cancelAllUploads(self):

        self.msg_bar_main.clearWidgets()
        self.msg_bar_main.pushMessage(
            'WARNING',
            'Canceling upload...',
            level=QgsMessageBar.WARNING)

        try:
            for i in range(0, self.num_uploading_images):
                # Is it better to use destructor?
                self.s3Uploaders[i].kill()
                self.progress_bars[i] = None
                #self.cancel_buttons[i] = None
                #self.threads[i] = None

        except:
            print "Error: problem occurred to kill uploaders"

    def cancelUpload(self, index):

        print "Cancel button was clicked!"

        """
        try:
            #is it better to use destructor?
            self.s3Uploaders[index].kill()
            self.progress_bars[index] = None
            self.cancel_buttons[index] = None
            #self.threads[index] = None
        except:
            print "Error: problem occurred to kill uploader"
        """

    def finishUpload(self, success, index):
        # clean up the s3Uploader and thread
        try:
            self.s3Uploaders[index].deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting uploader\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)
        self.threads[index].quit()
        self.threads[index].wait()
        try:
            self.threads[index].deleteLater()
        except:
            QgsMessageLog.logMessage(
                'Exception on deleting thread\n',
                'OAM',
                level=QgsMessageLog.CRITICAL)

        # remove widget from message bar
        #self.msg_bar_main.popWidget(self.messageBar)

        if success:
            self.count_uploaded_images += 1
            #print str(self.count_uploaded_images)

            # report the result
            if self.count_uploaded_images < self.num_uploading_images:
                self.msg_bar_main_content.setText(
                    ''
                    + str(self.count_uploaded_images)
                    + ' image out of '
                    + str(self.num_uploading_images)
                    + ' were uploaded.')
                QgsMessageLog.logMessage(
                    'Upload succeeded ('
                    + str(self.count_uploaded_images)
                    + ' out of '
                    + str(self.num_uploading_images) + ')' ,
                    'OAM',
                    level=QgsMessageLog.INFO)
            else:
                self.msg_bar_main.pushMessage(
                    'INFO',
                    'Upload was successfully completed.',
                    level=QgsMessageBar.INFO)
                QgsMessageLog.logMessage(
                    'Upload succeeded',
                    'OAM',
                    level=QgsMessageLog.INFO)
        else:
            # notify the user that something went wrong
            self.msg_bar_main.pushMessage(
                'CRITICAL',
                'Upload was interrupted',
                level=QgsMessageBar.CRITICAL)
            QgsMessageLog.logMessage(
                'Upload was interrupted',
                'OAM',
                level=QgsMessageLog.CRITICAL)

    def displayUploadError(self, e, exception_string):

        self.msg_bar_main.pushMessage(
            'CRITICAL',
            'Uploader thread raised an exception:\n'.format(exception_string),
            level=QgsMessageBar.CRITICAL)

        QgsMessageLog.logMessage(
            'Uploader thread raised an exception:\n'.format(exception_string),
            'OAM',
            level=QgsMessageLog.CRITICAL)

    #Testing purpose only
    def test(self):
        strResult = "Test: " + \
                    repr(self.upload_options) + \
                    repr(self.bucket_name) + \
                    repr(self.bucket) + \
                    repr(self.filenames)
        return strResult

    #Testing purpose only
    def getAllKeys(self):
        rsKeys = []
        try:
            myBucket = super(S3Manager,self).get_bucket(self.bucket_name)
            #convert botoList into normal python list
            for key in myBucket.list():
                rsKeys.append(repr(key))
        except:
            rsKeys = None

        return rsKeys


class S3Uploader(QObject):
    '''Handle uploads in a separate thread'''

    finished = pyqtSignal(bool, int)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float, int)

    def __init__(self, filename, bucket, options, index):
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

    def sendImageFiles(self):

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
                self.progress.emit(progress_count / float(chunk_count)*100, self.index)
                QgsMessageLog.logMessage(
                    'Progress = %f' % (progress_count / float(chunk_count)),
                    'OAM',
                    level=QgsMessageLog.INFO)

            if self.killed is False:

                multipart.complete_upload()
                self.progress.emit(100, self.index)
                success = True

                # need to modify this part.
                """
                if "notify_oam" in self.options:
                    self.notifyOAM()
                if "trigger_tiling" in self.options:
                    #pass
                    self.triggerTileService()
                """

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
        self.sendImageFiles()

    def kill(self):
        self.killed = True
