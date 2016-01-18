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
import json

class MetadataHandler():

    def __init__(self, metaInput, imgFileAbspath):
        self.metaInput = metaInput
        self.imgFileAbspath = imgFileAbspath
        self.metaInImagery = {}
        self.metaForUpload = {}

        self.gdalDataset = None
        self.spatialRef = None

    def getMetaForUpload(self):
        return self.metaForUpload

    def createMetaForUpload(self):
        self.extractMetaInImagery()
        # self.extractMetadata()
        self.metaForUpload = dict(self.metaInput.items() +
            self.metaInImagery.items())
        return True

    def openGdalDataset(self):
        self.gdalDataset = gdal.Open(self.imgFileAbspath, gdal.GA_ReadOnly)
        if self.gdalDataset:
            return True
        else:
            return False

    def closeGdalDataset(self):
        self.gdalDataset = None

    def extractMetaInImagery(self):
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
        projInfo = self.gdalDataset.GetProjection()
        self.metaInImagery['projection'] = str(projInfo)

        # create an spatial reference object for bbox extraction
        self.spatialRef = osr.SpatialReference()
        self.spatialRef.ImportFromWkt(projInfo)

        # Export to Proj4 format
        #spatialRefProj = self.spatialRef.ExportToProj4()
        #self.metaInImagery['projection'] = str(spatialRefProj)

    def extractBBox(self):
        # probably need to convert parentheses into bracket later
        upper_left = self.GDALInfoReportCorner(
            self.gdalDataset,0.0,0.0 )
        lower_left = self.GDALInfoReportCorner(
            self.gdalDataset,0.0,
            self.gdalDataset.RasterYSize)
        upper_right = self.GDALInfoReportCorner(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,0.0 )
        lower_right = self.GDALInfoReportCorner(
            self.gdalDataset,
            self.gdalDataset.RasterXSize,
            self.gdalDataset.RasterYSize )
        center = self.GDALInfoReportCorner(
            self.gdalDataset,
            self.gdalDataset.RasterXSize/2.0,
            self.gdalDataset.RasterYSize/2.0 )

        if "_EPSG3857" in self.imgFileAbspath:

            try:
                target = osr.SpatialReference()
                target.ImportFromEPSG(3857)
                transform = osr.CoordinateTransformation(self.spatialRef,target)

                point = ogr.CreateGeometryFromWkt(
                    "POINT (%f %f)" % (upper_left[0],upper_left[1]))
                point.Transform(transform)
                upper_left = json.loads(point.ExportToJson())['coordinates']

                point = ogr.CreateGeometryFromWkt(
                    "POINT (%f %f)" % (lower_left[0],lower_left[1]))
                point.Transform(transform)
                lower_left = json.loads(point.ExportToJson())['coordinates']

                point = ogr.CreateGeometryFromWkt(
                    "POINT (%f %f)" % (upper_right[0],upper_right[1]))
                point.Transform(transform)
                upper_right = json.loads(point.ExportToJson())['coordinates']

                point = ogr.CreateGeometryFromWkt(
                    "POINT (%f %f)" % (lower_right[0],lower_right[1]))
                point.Transform(transform)
                lower_right = json.loads(point.ExportToJson())['coordinates']

            except (RuntimeError, TypeError, NameError) as error:
                print error
            except:
                print "Unexpected error:", sys.exc_info()[0]

        self.metaInImagery['bbox'] = (
            upper_left,lower_left,upper_right,lower_right)

    def extractFootprint(self):
        self.metaInImagery['footprint'] = "xxxxx"

    def extractGsd(self):
        self.metaInImagery['gsd'] = "xxxxx"

    def GDALInfoReportCorner(self, hDataset, x, y):
        """GDALInfoReportCorner: extracted and adapted
            from the python port of gdalinfo"""

        # Transform the point into georeferenced coordinates
        adfGeoTransform = hDataset.GetGeoTransform(can_return_null = True)
        if adfGeoTransform is not None:
            dfGeoX = adfGeoTransform[0] + adfGeoTransform[1] * x + adfGeoTransform[2] * y
            dfGeoY = adfGeoTransform[3] + adfGeoTransform[4] * x + adfGeoTransform[5] * y
        else:
            print "BBOX might be wrong. Transformation coefficient " + \
                "could not be fetched from raster"
            return (x,y)

        # Report the georeferenced coordinates
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            return literal_eval(("(%12.7f,%12.7f) " % (dfGeoX, dfGeoY )))
        else:
            return literal_eval(("(%12.3f,%12.3f) " % (dfGeoX, dfGeoY )))
