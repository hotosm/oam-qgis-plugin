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
from ast import literal_eval

class ImgMetadataHandler:

    def __init__(self, imgFileAbspath):
        self.imgFileAbspath = imgFileAbspath
        self.metaInImagery = {}

        self.gdalDataset = None
        self.projInfo = None
        self.spatialRef = None

    def getMetaInImagery(self):
        return self.metaInImagery

    def openGdalDataset(self):
        #print('Open GDAL Dataset...')
        self.gdalDataset = gdal.Open(self.imgFileAbspath, gdal.GA_ReadOnly)
        if self.gdalDataset:
            return True
        else:
            return False

    def closeGdalDataset(self):
        self.gdalDataset = None

    def extractMetaInImagery(self):
        #print('Extracting metadata from Imagery...')
        # is it better to use exception handling?
        self.metaInImagery['file_size'] = os.stat(self.imgFileAbspath).st_size
        if self.openGdalDataset():
            self.extractProjName()
            self.extractBBox()
            self.extractFootprint()
            self.extractGsd()
            return True
        else:
            print "Error: could not open the gdaldataset."
            return False

    def extractProjName(self):
        # extract projection in WKT format
        self.projInfo = self.gdalDataset.GetProjection()
        self.metaInImagery['projection'] = str(self.projInfo)

        # create an spatial reference object for bbox extraction
        #self.spatialRef = osr.SpatialReference()
        #self.spatialRef.ImportFromWkt(self.projInfo)
        # Export to Proj4 format
        #spatialRefProj = self.spatialRef.ExportToProj4()
        #self.metaInImagery['projection'] = str(spatialRefProj)

    def extractBBox(self):

        self.spatialRef = osr.SpatialReference()
        self.spatialRef.ImportFromWkt(self.projInfo)

        listBBoxNodes = []
        listBBoxNodes.append(self.affineGeoTransform(
        self.gdalDataset, 0.0, 0.0)[0])
        listBBoxNodes.append(self.affineGeoTransform(
        self.gdalDataset, 0.0, 0.0)[1])
        listBBoxNodes.append(self.affineGeoTransform(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,
            self.gdalDataset.RasterYSize )[0])
        listBBoxNodes.append(self.affineGeoTransform(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,
            self.gdalDataset.RasterYSize )[1])
        self.metaInImagery['bbox'] = str(listBBoxNodes)

    def extractFootprint(self):
        """Temporarily use bbox values"""
        node1 = self.affineGeoTransform(
            self.gdalDataset,0.0,0.0 )
        node2 = self.affineGeoTransform(
            self.gdalDataset,0.0,
            self.gdalDataset.RasterYSize)
        node3 = self.affineGeoTransform(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,0.0 )
        node4 = self.affineGeoTransform(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,
            self.gdalDataset.RasterYSize )
        self.metaInImagery['footprint'] = 'POLYGON' + \
            str((node1, node2, node3, node4, node1))

    def extractGsd(self):
        #print("Message: " + repr(self.gdalDataset))

        geotransform = self.gdalDataset.GetGeoTransform()
        if not geotransform is None:
            gsdAvg = (abs(geotransform[1]) + abs(geotransform[5]))/2
            self.metaInImagery['gsd'] = str(gsdAvg)
        else:
            self.metaInImagery['gsd'] = "n.a."

    def affineGeoTransform(self, hDataset, x, y):

        geoTransform = hDataset.GetGeoTransform(can_return_null = True)
        if geoTransform is not None:
            geoX = geoTransform[0] + geoTransform[1] * x + geoTransform[2] * y
            geoY = geoTransform[3] + geoTransform[4] * x + geoTransform[5] * y
        else:
            print "BBOX might be wrong. Transformation coefficient " + \
                "could not be fetched from raster"
            return (x,y)

        # Report the georeferenced coordinates
        if abs(geoX) < 181 and abs(geoY) < 91:
            return literal_eval(("(%12.7f,%12.7f) " % (geoX, geoY )))
        else:
            return literal_eval(("(%12.3f,%12.3f) " % (geoX, geoY )))
