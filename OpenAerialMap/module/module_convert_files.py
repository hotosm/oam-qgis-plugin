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

"""
def reproject(self,filename):
    # to avoid repetition of "EPSG3857" in filename:
    if not "EPSG3857" in filename:
        reproject_filename = os.path.splitext(filename)[0]+'_EPSG3857.tif'
    os.system("gdalwarp -of GTiff -t_srs epsg:3857 %s %s" % (filename,reproject_filename))
    QgsMessageLog.logMessage(
        'Reprojected to EPSG:3857',
        'OAM',
        level=QgsMessageLog.INFO)
    return reproject_filename

def convert(self,filename):
    tif_filename = os.path.splitext(filename)[0]+".tif"
    #Open existing dataset
    src_ds = gdal.Open(filename)
    driver = gdal.GetDriverByName("GTiff")
    dst_ds = driver.CreateCopy(tif_filename, src_ds, 0 )
    #Properly close the datasets to flush to disk
    dst_ds = None
    src_ds = None
"""
