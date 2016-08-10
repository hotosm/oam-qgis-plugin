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

import os, sys
from qgis.core import QgsMapLayer, QgsMessageLog
from qgis.gui import QgsMessageBar

import imghdr
from osgeo import gdal, osr, ogr

from module.module_gdal_utilities import gdal_info_report_corner


def validate_layer(layer_name, iface):
    val = True
    all_layers = iface.mapCanvas().layers()
    for layer in all_layers:
        if layer_name == layer.name():
            if layer.type() == QgsMapLayer.VectorLayer:
                val = False
    return val


def validate_file(file_abspath):
    rs = {}
    rs["val"] = True
    rs["msg"] = "File %s is a valid data source" % file_abspath

    if not os.path.exists(file_abspath):
        rs["val"] = False
        rs["msg"] = "The file %s does not exist" % file_abspath
    elif imghdr.what(file_abspath) is None:
        rs["val"] = False
        rs["msg"] = "The file %s is not a supported data source" % file_abspath
    else:
        try:
            raster = gdal.Open(file_abspath, gdal.GA_ReadOnly)
        except:
            rs["val"] = False
            rs["msg"] = "GDAL could not read file %s" % file_abspath
        if not raster:
            rs["val"] = False
            rs["msg"] = "GDAL could not read file %s" % file_abspath
        elif raster.RasterCount < 3:
            rs["val"] = False
            rs["msg"] = "The file %s has less than 3 raster bands" % file_abspath
        elif raster.GetProjection() is '':
            rs["val"] = False
            rs["msg"] = "Could not extract projection from file %s" % file_abspath
        else:
            # check if bbox has valid data
            xy_points = [(0.0, 0.0),
                        (0.0, raster.RasterYSize),
                        (raster.RasterXSize, 0.0),
                        (raster.RasterXSize, raster.RasterYSize)]
            for point in xy_points:
                if point == gdal_info_report_corner(
                                raster, point[0], point[1]):
                    rs["val"] = False
                    rs["msg"] = "BBOX of the file %s does not have a valid data" % file_abspath
    return rs
