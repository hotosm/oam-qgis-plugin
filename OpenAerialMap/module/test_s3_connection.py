from Tkinter import * #only for testing purpose
import sys #only for testing purpose

from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback

def connect_s3():
    conn = S3Connection('', '')
    myBucket = conn.get_bucket('oam-qgis-plugin-test')

    listStr = ""
    for key in myBucket.list():
        listStr += str(key) + "\n"
        
    return listStr
