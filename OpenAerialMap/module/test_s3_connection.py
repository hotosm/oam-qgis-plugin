
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback

def connect_s3(accessKeyId, secretAccessKey, bucketName):
    conn = S3Connection(accessKeyId, secretAccessKey)
    myBucket = conn.get_bucket(bucketName)

    listStr = ""
    for key in myBucket.list():
        listStr += str(key) + "\n"

    return listStr
