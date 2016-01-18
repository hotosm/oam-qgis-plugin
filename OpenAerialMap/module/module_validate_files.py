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


def validateLayer(self,layer_name):
    all_layers = self.iface.mapCanvas().layers()
    for layer in all_layers:
        if layer_name == layer.name():
            if layer.type() == QgsMapLayer.VectorLayer:
                self.bar0.clearWidgets()
                self.bar0.pushMessage(
                    "CRITICAL",
                    "Vector layers cannot be selected for upload",
                    level=QgsMessageBar.CRITICAL)
                return 0
            else:
                return 1

def validateFile(self,filename):
    # check that file exists
    if not os.path.exists(filename):
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "The file %s does not exist" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # check that file is an image
    if imghdr.what(filename) is None:
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "The file %s is not a supported data source" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # check if gdal can read file
    try:
        raster = gdal.Open(filename,gdal.GA_ReadOnly)
    except:
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "GDAL could not read file %s" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # check if there is an object raster
    if not raster:
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "GDAL could not read file %s" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # check that image has at least 3 bands
    if raster.RasterCount < 3:
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "The file %s has less than 3 raster bands" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # check if projection is set
    if raster.GetProjection() is '':
        self.bar0.clearWidgets()
        self.bar0.pushMessage(
            "CRITICAL",
            "Could not extract projection from file %s" % filename,
            level=QgsMessageBar.CRITICAL)
        return False
    # finally, check if bbox has valid data
    xy_points = [(0.0,0.0),(0.0,raster.RasterYSize),(raster.RasterXSize,0.0),(raster.RasterXSize,raster.RasterYSize)]
    for point in xy_points:
        if point != self.GDALInfoReportCorner(raster,point[0],point[1]):
            QgsMessageLog.logMessage(
                'File %s is a valid data source' % filename,
                'OAM',
                level=QgsMessageLog.INFO)
            return True
