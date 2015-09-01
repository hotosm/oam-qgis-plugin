"""
/***************************************************************************
 OpenAerialMap QGIS plugin
 Module for S3 Connection
 ***************************************************************************/
"""
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback

class S3Manager:

    def uploadExe(self):
        return True
