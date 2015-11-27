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
