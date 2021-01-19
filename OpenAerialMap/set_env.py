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
from builtins import str
from builtins import map
from builtins import object

import os, sys

from qgis.core import *
from osgeo import gdal
from qgis.PyQt.QtCore import QDir


class SetEnvironment(object):

    @staticmethod
    def setPip():
        pass
        # subprocess.call('python',['./ext_libs/get-pip.py'])
        # process = QtCore.QProcess()
        # process.start('python',['./ext_libs/get-pip.py'])

    @staticmethod
    def setSetuptools():
        pass
        # pip.main(['install','setuptools'])

    @staticmethod
    def setGoogleDriveAPI():
        pass
        # pip.main(['install','--upgrade','google-api-python-client'])

    @staticmethod
    def setDropBoxAPI():
        pass
        # pip.main(['install','dropbox'])

    @staticmethod
    def setPaths():
        if sys.platform == 'darwin':

            # QgsApplication.prefixPath() contains the path to qgis executable (i.e. .../Qgis.app/MacOS)
            # get the path to Qgis application folder
            qgis_app = u"%s/.." % QgsApplication.prefixPath()
            qgis_app = QDir(qgis_app).absolutePath()

            # get the path to the GDAL framework within the Qgis application folder (Qgis standalone only)
            qgis_standalone_gdal_path = u"%s/Frameworks/GDAL.framework" % qgis_app

            # get the path to the GDAL framework when installed as external framework
            gdal_versionsplit = str(Version(gdal.VersionInfo("RELEASE_NAME"))).split('.')
            gdal_base_path = u"/Library/Frameworks/GDAL.framework/Versions/%s.%s/Programs" % (gdal_versionsplit[0], gdal_versionsplit[1])

            if os.path.exists(qgis_standalone_gdal_path):  # qgis standalone
                os.environ['PATH'] = os.environ['PATH'] + ':' +  qgis_standalone_gdal_path

            elif os.path.exists(gdal_base_path):
                os.environ['PATH'] = os.environ['PATH'] + ':' +  gdal_base_path

        elif sys.platform == 'linux2':
            pass

        elif sys.platform == 'win32':
            pass


class Version(object):

    def __init__(self, ver):
        self.vers = ('0', '0', '0')

        if isinstance(ver, Version):
            self.vers = ver.vers
        elif isinstance(ver, tuple) or isinstance(ver, list):
            self.vers = list(map(str, ver))
        elif isinstance(ver, str):
            self.vers = self.string2vers(ver)

    @staticmethod
    def string2vers(string):
        vers = ['0', '0', '0']

        nums = str(string).split(".")

        if len(nums) > 0:
            vers[0] = nums[0]
        if len(nums) > 1:
            vers[1] = nums[1]
        if len(nums) > 2:
            vers[2] = nums[2]

        return (vers[0], vers[1], vers[2])

    def __cmp__(self, other):
        if not isinstance(other, Version):
            other = Version(other)

        if self.vers > other.vers:
            return 1
        if self.vers < other.vers:
            return -1
        return 0

    def __str__(self):
        return ".".join(self.vers)
