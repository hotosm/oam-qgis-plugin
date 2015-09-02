"""
/***************************************************************************
 OpenAerialMap QGIS plugin
 Module for handling metadata
 ***************************************************************************/
"""
import json

class MetadataHandler:

    def extractMetadata(self,fileName):

        self.fileName = fileName

        """Extract filesize, projection, bbox and gsd from image file"""

        """
        self.metadata[filename]['File size'] = os.stat(filename).st_size

        datafile = gdal.Open(filename,gdal.GA_ReadOnly)
        if datafile is None:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'CRITICAL',
                'Extraction of raster metadata failed.',
                level=QgsMessageBar.CRITICAL)

        # projection
        projInfo = datafile.GetProjection()
        spatialRef = osr.SpatialReference()
        #print "WKT format: " + str(spatialRef)
        spatialRef.ImportFromWkt(projInfo)
        spatialRefProj = spatialRef.ExportToProj4()
        #print "Proj4 format: " + str(spatialRefProj)
        self.metadata[filename]['Projection'] = str(spatialRefProj)

        #bbox
        upper_left = self.GDALInfoReportCorner(datafile,0.0,0.0 );
        lower_left = self.GDALInfoReportCorner(datafile,0.0,datafile.RasterYSize);
        upper_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,0.0 );
        lower_right = self.GDALInfoReportCorner(datafile,datafile.RasterXSize,datafile.RasterYSize );
        center = self.GDALInfoReportCorner(datafile,datafile.RasterXSize/2.0,datafile.RasterYSize/2.0 );
        self.metadata[filename]['BBOX'] = (upper_left,lower_left,upper_right,lower_right)
        """
        return self.fileName

    def GDALInfoReportCorner(self,hDataset,x,y):
        """GDALInfoReportCorner: extracted and adapted from the python port of gdalinfo"""

        # Transform the point into georeferenced coordinates
        adfGeoTransform = hDataset.GetGeoTransform(can_return_null = True)
        if adfGeoTransform is not None:
            dfGeoX = adfGeoTransform[0] + adfGeoTransform[1] * x + adfGeoTransform[2] * y
            dfGeoY = adfGeoTransform[3] + adfGeoTransform[4] * x + adfGeoTransform[5] * y
        else:
            self.bar.clearWidgets()
            self.bar.pushMessage(
                'WARNING',
                'BBOX might be wrong. Transformation coefficient could not be fetched from raster.',
                level=QgsMessageBar.WARNING)
            return (x,y)

        # Report the georeferenced coordinates
        if abs(dfGeoX) < 181 and abs(dfGeoY) < 91:
            return ("(%12.7f,%12.7f) " % (dfGeoX, dfGeoY ))
        else:
            return ("(%12.3f,%12.3f) " % (dfGeoX, dfGeoY ))
