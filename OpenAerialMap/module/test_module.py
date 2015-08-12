from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, pyqtSignal, QObject, QThread
from PyQt4.QtGui import QAction, QIcon, QMessageBox, QFileDialog, QListWidgetItem, QSizePolicy, QGridLayout, QPushButton, QProgressBar
from PyQt4.Qt import *
from qgis.gui import QgsMessageBar
from qgis.core import QgsMapLayer, QgsMessageLog
import resources_rc
from oam_client_dialog import OpenAerialMapDialog
import os, sys, math, imghdr
from osgeo import gdal, osr
import time
import json
# Modules needed for upload
from boto.s3.connection import S3Connection, S3ResponseError
from boto.s3.key import Key
from filechunkio import FileChunkIO
import syslog, traceback

