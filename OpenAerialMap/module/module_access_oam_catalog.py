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
import pycurl
import urllib
import json
from StringIO import StringIO

class OAMCatalogAccess:

    def __init__(self, hostUrl, action=None, dictQueries=None, parent=None):
        #probably need to make a textbox for editing hostUrl later
        self.hostUrl = hostUrl
        self.action = action
        self.dictQueries = dictQueries
        self.endPoint = None

    def getMetadataInList(self):
        jMetadata = self.downloadMetadata()
        metadadaInDic = json.loads(jMetadata)
        metadataInList = metadadaInDic[u'results']
        return metadataInList

    def downloadMetadata(self):
        print(str(self.dictQueries))

        if self.action == None or self.action == '':
            self.endPoint = self.hostUrl
        else:
            """need to modify this part later"""
            self.endPoint = self.hostUrl + '/' + self.action
            #if self.dictQueries.get('location') != '':
            #    self.endPoint += '?location=' + self.dictQueries['location']
            if self.dictQueries.get('dateAcquisitionFrom') != '':
                self.endPoint += '?acquisition_from=' + self.dictQueries['dateAcquisitionFrom']
            if self.dictQueries.get('dateAcquisitionTo') != '':
                self.endPoint += '&acquisition_to=' + self.dictQueries['dateAcquisitionTo']
            #if self.dictQueries.get('resolution') != '':
            #    self.endPoint += '&gsd_to=' + int(self.dictQueries['resolution'])

        print(str(self.endPoint))

        strBuffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.endPoint)
        c.setopt(c.WRITEDATA, strBuffer)
        c.perform()
        c.close()
        jMetadata = strBuffer.getvalue()
        return jMetadata

    def uploadMetaData(self):
        #access to self.hostUrl and upload metadata
        #invoked form uploader wizard in the future
        print("Under construction")
