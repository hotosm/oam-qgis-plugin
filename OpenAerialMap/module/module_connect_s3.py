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
    #inherit from S3 Connection later
    #def __init__(self, bucket_key_id, bucket_secret_key, parent=None):
    #    super(S3Manager, self).__init__(bucket_key_id, bucket_secret_key, parent)

    def test(self, bucket_key_id, bucket_secret_key, bucket_name, file_path):

        outStr = str(bucket_key_id) + ", " + str(bucket_secret_key) + ", " + str(bucket_name) + ", " + str(file_path)

        return outStr
