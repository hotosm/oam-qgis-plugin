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
import urllib
import json

class ImgDownloader:

    def __init__(self, parent=None):
        pass

    @staticmethod
    def downloadThumbnail(urlThumbnail):
        img_dir_abspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
        print(urlThumbnail)
        img_file_name = urlThumbnail.split('/')[-1]
        img_abspath = os.path.join(img_dir_abspath, img_file_name)
        print (img_abspath)
        #make a buffer - make sure if the image is already downloaded in the folder, first of all
        f = open(img_abspath,'wb')
        f.write(urllib.urlopen(urlThumbnail).read())
        f.close()
        return img_abspath

    @staticmethod
    def downloadFullImage(urlFullImage):
        #use urlib and download full image
        print("Download full image from " + urlFullImage)
