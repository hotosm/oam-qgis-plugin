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

    def __init__(self, hostUrl, action=None, dicQueries=None, parent=None):
        self.hostUrl = hostUrl
        self.action = action
        self.dicQueries = dicQueries
        self.endPoint = None

    def test(self):
        print str(self.dicQueries)
        if self.action is None:
            self.endPoint = self.hostUrl
        else:
            self.endPoint = self.hostUrl + '/' + self.action
        strBuffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.endPoint)
        c.setopt(c.WRITEDATA, strBuffer)
        c.perform()
        c.close()
        jMetadata = strBuffer.getvalue()
        metadadaInDic = json.loads(jMetadata)
        metadataInList = metadadaInDic[u'results']
        return metadataInList

    """probably this function should move to another class, since this is not using oam catalog"""
    @staticmethod
    def getThumbnail(urlThumbnail):
        img_dir_abspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
        print(urlThumbnail)
        img_file_name = urlThumbnail.split('/')[-1]
        img_abspath = os.path.join(img_dir_abspath, img_file_name)
        print (img_abspath)
        f = open(img_abspath,'wb')
        f.write(urllib.urlopen(urlThumbnail).read())
        f.close()
        return img_abspath
