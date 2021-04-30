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

import sys, os, time, math
# import imghdr, tempfile, requests, json
# import traceback
# from ast import literal_eval

from qgis.PyQt import QtCore
from qgis.PyQt.QtGui import *      # modify this part?
from qgis.PyQt.QtCore import QThread, pyqtSignal

#import boto
#from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO


class S3UploadWorker(QThread):

    started = pyqtSignal(bool, int)
    valueChanged = pyqtSignal(int, int)
    finished = pyqtSignal(str, int)
    error = pyqtSignal(Exception, int)

    def __init__(self,
                 bucket,
                 uploadOptions,
                 fileAbsPath,
                 index,
                 delay=0.10):
        QThread.__init__(self)
        self.bucket = bucket
        self.uploadOptions = uploadOptions
        self.fileAbsPath = fileAbsPath
        self.index = index
        self.isRunning = True

        self.delay = delay

    def uploadMetadata(self):

        metaFileAbsPath = self.fileAbsPath + '_meta.json'
        keyForMetaUp = Key(self.bucket)
        metaFileName = os.path.basename(metaFileAbsPath)
        keyForMetaUp.key = metaFileName
        try:
            keyForMetaUp.set_contents_from_filename(metaFileAbsPath)
        except Exception as e:
            self.error.emit(e, self.index)
            self.finished.emit('failed', self.index)

    def uploadThumbnail(self):

        thumbnailFileAbsPath = self.fileAbsPath + '.thumb.png'
        if os.path.exists(thumbnailFileAbsPath):
            keyForMetaUp = Key(self.bucket)
            thumbnailFileName = os.path.basename(thumbnailFileAbsPath)
            keyForMetaUp.key = thumbnailFileName
            try:
                keyForMetaUp.set_contents_from_filename(thumbnailFileAbsPath)
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
            # for i in range(chunkCount):
            while self.isRunning and i < chunkCount:
                offset = chunkSize * i
                bytes = min(chunkSize, fileSize - offset)
                with FileChunkIO(self.fileAbsPath,
                                 'r',
                                 offset=offset,
                                 bytes=bytes) as fp:
                    mp.upload_part_from_file(fp, part_num=i + 1)
                i += 1
                # emit progress here
                progress = i / float(chunkCount) * 100
                self.valueChanged.emit(progress, self.index)

            if self.isRunning is True:
                mp.complete_upload()
                self.finished.emit('success', self.index)
            else:
                self.finished.emit('cancelled', self.index)

        except Exception as e:
            self.error.emit(e, self.index)

        """
        if "notify_oam" in self.uploadOptions:
            self.notifyOAM()
        if "trigger_tiling" in self.uploadOptions:
            self.triggerTileService()
        """

    def notifyOAM(self):
        pass

    # need to modify this part
    def triggerTilingService(self):
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

        if u'id' in list(post_dict.keys()):
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
        self.uploadThumbnail()
        self.uploadImageFile()
        # self.notifyOAM()
        # self.triggerTilingService()

    def stop(self):
        self.isRunning = False
