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
from osgeo import gdal, osr, ogr
from qgis.core import QgsMessageLog

def reproject(file_abspath):
    """make sure if we need to -overwrite option"""
    # to avoid repetition of "EPSG3857" in filename:
    if not "EPSG3857" in file_abspath:
        reprojected_file_abspath = os.path.splitext(file_abspath)[0]+'_EPSG3857.tif'
    os.system("gdalwarp -of GTiff -t_srs epsg:3857 %s %s"
        % (file_abspath, reprojected_file_abspath))

    QgsMessageLog.logMessage(
        'Reprojected to EPSG:3857',
        'OAM',
        level=QgsMessageLog.INFO)
    return reprojected_file_abspath


"""Probably this function is not necessary, since reproject function
    automatically convert the non-tiff file into tiff file."""
def convert_to_tif(file_abspath):
    if not ".tif" in file_abspath:
        converted_file_abspath = os.path.splitext(file_abspath)[0]+".tif"
    src_ds = gdal.Open(file_abspath)
    conversion_driver = gdal.GetDriverByName("GTiff")
    converted_ds = conversion_driver.CreateCopy(converted_file_abspath, src_ds, 0)
    src_ds = None
    converted_ds = None
    QgsMessageLog.logMessage(
        'Converted to Tiff format',
        'OAM',
        level=QgsMessageLog.INFO)
    return converted_file_abspath
