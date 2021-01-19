```sh
/home/geopro/.local/bin/qgis2to3 -w /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap
RefactoringTool: Skipping optional fixer: idioms
RefactoringTool: Skipping optional fixer: ws_comma
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/make_package.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/make_package.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/make_package.py	(refactored)
@@ -1,3 +1,4 @@
+from __future__ import print_function
 import os, sys
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py	(refactored)
@@ -22,33 +22,34 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import absolute_import
+from builtins import str
+from builtins import object
 
 # Qt classes
 # from PyQt4.QtCore import *
 # from PyQt4.QtGui import *
 # from qgis.core import *
 
-from PyQt4.QtCore import (QSettings,
-                          QTranslator,
-                          qVersion,
-                          QCoreApplication)
-from PyQt4.QtGui import (QAction, QIcon)
+from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
+from qgis.PyQt.QtWidgets import QAction
+from qgis.PyQt.QtGui import QIcon
 
 # icon images
 import resources_rc
 
 # classes for GUI
-from gui.img_uploader_wizard import ImgUploaderWizard
-from gui.img_search_dialog import ImgSearchDialog
-from gui.setting_dialog import SettingDialog
+from .gui.img_uploader_wizard import ImgUploaderWizard
+from .gui.img_search_dialog import ImgSearchDialog
+from .gui.setting_dialog import SettingDialog
 
 # set os-specific environment
-from set_env import SetEnvironment
+from .set_env import SetEnvironment
 
 import os, sys
 import webbrowser
 
-class OpenAerialMap:
+class OpenAerialMap(object):
     """QGIS Plugin Implementation."""
 
     def __init__(self, iface):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py	(refactored)
@@ -4,10 +4,14 @@
         Authors: A. Pasotti, V. Picavet
         git sha              : $TemplateVCSFormat
 """
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import input
 
 import sys
 import getpass
-import xmlrpclib
+import xmlrpc.client
 from optparse import OptionParser
 
 # Configuration
@@ -31,25 +35,36 @@
         parameters.server,
         parameters.port,
         ENDPOINT)
-    print "Connecting to: %s" % hide_password(address)
+    # fix_print_with_import
+    print("Connecting to: %s" % hide_password(address))
 
-    server = xmlrpclib.ServerProxy(address, verbose=VERBOSE)
+    server = xmlrpc.client.ServerProxy(address, verbose=VERBOSE)
 
     try:
         plugin_id, version_id = server.plugin.upload(
-            xmlrpclib.Binary(open(arguments[0]).read()))
-        print "Plugin ID: %s" % plugin_id
-        print "Version ID: %s" % version_id
-    except xmlrpclib.ProtocolError, err:
-        print "A protocol error occurred"
-        print "URL: %s" % hide_password(err.url, 0)
-        print "HTTP/HTTPS headers: %s" % err.headers
-        print "Error code: %d" % err.errcode
-        print "Error message: %s" % err.errmsg
-    except xmlrpclib.Fault, err:
-        print "A fault occurred"
-        print "Fault code: %d" % err.faultCode
-        print "Fault string: %s" % err.faultString
+            xmlrpc.client.Binary(open(arguments[0]).read()))
+        # fix_print_with_import
+        print("Plugin ID: %s" % plugin_id)
+        # fix_print_with_import
+        print("Version ID: %s" % version_id)
+    except xmlrpc.client.ProtocolError as err:
+        # fix_print_with_import
+        print("A protocol error occurred")
+        # fix_print_with_import
+        print("URL: %s" % hide_password(err.url, 0))
+        # fix_print_with_import
+        print("HTTP/HTTPS headers: %s" % err.headers)
+        # fix_print_with_import
+        print("Error code: %d" % err.errcode)
+        # fix_print_with_import
+        print("Error message: %s" % err.errmsg)
+    except xmlrpc.client.Fault as err:
+        # fix_print_with_import
+        print("A fault occurred")
+        # fix_print_with_import
+        print("Fault code: %d" % err.faultCode)
+        # fix_print_with_import
+        print("Fault string: %s" % err.faultString)
 
 
 def hide_password(url, start=6):
@@ -85,7 +100,8 @@
         help="Specify server name", metavar="plugins.qgis.org")
     options, args = parser.parse_args()
     if len(args) != 1:
-        print "Please specify zip file.\n"
+        # fix_print_with_import
+        print("Please specify zip file.\n")
         parser.print_help()
         sys.exit(1)
     if not options.server:
@@ -95,8 +111,9 @@
     if not options.username:
         # interactive mode
         username = getpass.getuser()
-        print "Please enter user name [%s] :" % username,
-        res = raw_input()
+        # fix_print_with_import
+        print("Please enter user name [%s] :" % username, end=' ')
+        res = input()
         if res != "":
             options.username = res
         else:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py	(refactored)
@@ -22,15 +22,18 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from builtins import str
+from builtins import map
+from builtins import object
 
 import os, sys
 
 from qgis.core import *
 from osgeo import gdal
-from PyQt4.QtCore import QDir
+from qgis.PyQt.QtCore import QDir
 
 
-class SetEnvironment:
+class SetEnvironment(object):
 
     @staticmethod
     def setPip():
@@ -67,7 +70,7 @@
             qgis_standalone_gdal_path = u"%s/Frameworks/GDAL.framework" % qgis_app
 
             # get the path to the GDAL framework when installed as external framework
-            gdal_versionsplit = unicode(Version(gdal.VersionInfo("RELEASE_NAME"))).split('.')
+            gdal_versionsplit = str(Version(gdal.VersionInfo("RELEASE_NAME"))).split('.')
             gdal_base_path = u"/Library/Frameworks/GDAL.framework/Versions/%s.%s/Programs" % (gdal_versionsplit[0], gdal_versionsplit[1])
 
             if os.path.exists(qgis_standalone_gdal_path):  # qgis standalone
@@ -83,7 +86,7 @@
             pass
 
 
-class Version:
+class Version(object):
 
     def __init__(self, ver):
         self.vers = ('0', '0', '0')
@@ -91,7 +94,7 @@
         if isinstance(ver, Version):
             self.vers = ver.vers
         elif isinstance(ver, tuple) or isinstance(ver, list):
-            self.vers = map(str, ver)
+            self.vers = list(map(str, ver))
         elif isinstance(ver, str):
             self.vers = self.string2vers(ver)
 
@@ -99,7 +102,7 @@
     def string2vers(string):
         vers = ['0', '0', '0']
 
-        nums = unicode(string).split(".")
+        nums = str(string).split(".")
 
         if len(nums) > 0:
             vers[0] = nums[0]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py	(refactored)
@@ -21,10 +21,15 @@
  *                                                                         *
  ***************************************************************************/
 """
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
 
 import os, sys
 
-from PyQt4 import QtGui, uic
+from qgis.PyQt import QtGui, uic
 from PyQt4.Qt import *
 
 from qgis.gui import QgsMessageBar
@@ -131,7 +136,7 @@
                 self.layers_list_widget.addItem(item)
 
     def selectFile(self):
-        selected_file = QFileDialog.getOpenFileName(
+        selected_file, __ = QFileDialog.getOpenFileName(RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_search_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py

             self,
             'Select imagery file',
             os.path.expanduser("~"))
@@ -301,7 +306,8 @@
                     if not "EPSG3857" in filename:
                         json_filename = os.path.splitext(filename)[0]+'_EPSG3857.json'
                 json_file = open(json_filename, 'w')
-                print >> json_file, json_string
+                # fix_print_with_import
+                print(json_string, file=json_file)
                 json_file.close()
 
             self.loadMetadataReviewBox()
@@ -495,9 +501,11 @@
                     point.Transform(transform)
                     lower_right = json.loads(point.ExportToJson())['coordinates']
             except (RuntimeError, TypeError, NameError) as error:
-                print error
+                # fix_print_with_import
+                print(error)
             except:
-                print "Unexpected error:", sys.exc_info()[0]
+                # fix_print_with_import
+                print("Unexpected error:", sys.exc_info()[0])
 
             self.metadata[filename]['BBOX'] = (upper_left,lower_left,upper_right,lower_right)
 
@@ -563,7 +571,7 @@
 
     def loadMetadataReviewBox(self):
         json_filenames = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             if filename not in self.reprojected:
                 f = os.path.splitext(filename)[0]+'.json'
@@ -600,7 +608,7 @@
         bucket_secret = str(self.secret_key_edit.text())
 
         self.bucket = None
-        for trial in xrange(3):
+        for trial in range(3):
             if self.bucket: break
             try:
                 connection = S3Connection(bucket_key,bucket_secret)
@@ -647,7 +655,7 @@
             self.upload_options.append("trigger_tiling")
 
         if self.startConnection():
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))
 
                 self.bar2.clearWidgets()
@@ -768,7 +776,7 @@
     '''Handle uploads in a separate thread'''
 
     finished = pyqtSignal(bool)
-    error = pyqtSignal(Exception, basestring)
+    error = pyqtSignal(Exception, str)
     progress = pyqtSignal(float)
 
     def __init__(self,filename,bucket,options):
@@ -817,7 +825,7 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
+        if u'id' in list(post_dict.keys()):
             ts_id = post_dict[u'id']
             time = post_dict[u'queued_at']
             QgsMessageLog.logMessage(
@@ -874,7 +882,7 @@
                     self.notifyOAM()
                 if "trigger_tiling" in self.options:
                     self.triggerTileService()
-        except Exception, e:
+        except Exception as e:
             # forward the exception upstream (or try to...)
             # chunk size smaller than 5MB can cause an error, server does not expect it
             self.error.emit(e, traceback.format_exc())
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_search_dialog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_search_dialog.py	(refactored)
@@ -22,12 +22,14 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from builtins import str
 
 import os, sys
 import json
 
-from PyQt4 import QtGui, uic
-from PyQt4 import QtCore
+from qgis.PyQt import QtGui, uic
+from qgis.PyQt import QtCore
 from PyQt4.Qt import *
 from qgis.gui import QgsMessageBar
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py	(refactored)
@@ -21,10 +21,13 @@
  *                                                                         *
  ***************************************************************************/
 """
+from __future__ import print_function
+from builtins import str
+from builtins import range
 
 import os, sys
 
-from PyQt4 import QtGui, uic
+from qgis.PyQt import QtGui, uic
 from PyQt4.Qt import *
 
 from qgis.gui import QgsMessageBar
@@ -190,7 +193,7 @@
                     self.layers_list_widget.addItem(item)
 
     def selectFile(self):
-        selected_file = QFileDialog.getOpenFileName(
+        selected_file, __ = QFileDialog.getOpenFileName(
             self,
             'Select imagery file',
             os.path.expanduser("~"))
@@ -435,7 +438,7 @@
                     # extract metadata from GeoTiff, and merge with the metadata from textbox
                     imgMetaHdlr = ImgMetadataHandler(file_abspath)
                     imgMetaHdlr.extractMetaInImagery()
-                    metaForUpload = dict(imgMetaHdlr.getMetaInImagery().items() + metaInputInDict.items())
+                    metaForUpload = dict(list(imgMetaHdlr.getMetaInImagery().items()) + list(metaInputInDict.items()))
                     strMetaForUpload = str(json.dumps(metaForUpload))
 
                     #json_file_abspath = os.path.splitext(file_abspath)[0] + '.tif_meta.json'
@@ -535,7 +538,7 @@
 
     def loadMetadataReviewBox(self):
         json_file_abspaths = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             file_abspath = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             json_file_abspath = ''
             #if self.reproject_check_box.isChecked():
@@ -584,7 +587,7 @@
                 'Please check the lisence term.',
                 level=QgsMessageBar.WARNING)
         else:
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 upload_file_abspath = str(self.added_sources_list_widget.item(index).data(Qt.UserRole))
                 upload_file_abspaths.append(upload_file_abspath)
 
@@ -643,7 +646,7 @@
         #print('fileAbsPath: ' + fileAbsPath)
 
         #print(str(self.added_sources_list_widget.count()))
-        for index in xrange(0, self.added_sources_list_widget.count()):
+        for index in range(0, self.added_sources_list_widget.count()):
             refFileAbsPath = str(self.added_sources_list_widget.item(index).data(Qt.UserRole))
             #print('refFileAbsPath: ' + refFileAbsPath)
             if fileAbsPath == refFileAbsPath:
@@ -651,7 +654,7 @@
                 break
 
         #print(str(self.sources_list_widget.count()))
-        for index in xrange(0, self.sources_list_widget.count()):
+        for index in range(0, self.sources_list_widget.count()):
             refFileAbsPath = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             #print('refFileAbsPath: ' + refFileAbsPath)
             if fileAbsPath == refFileAbsPath:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py	(refactored)
@@ -21,11 +21,14 @@
  *                                                                         *
  ***************************************************************************/
 """
+from __future__ import print_function
+from builtins import str
+from builtins import range
 import os, sys
 
-from PyQt4 import QtGui
+from qgis.PyQt import QtGui
 from PyQt4.Qt import *
-from PyQt4.QtCore import QThread, Qt
+from qgis.PyQt.QtCore import QThread, Qt
 import json, time, math, imghdr, tempfile
 
 from qgis.gui import QgsMessageBar
@@ -82,7 +85,7 @@
 
     def getBucket(self):
 
-        for trial in xrange(3):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/get-pip.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/setup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py

+        for trial in range(3):
             if self.bucket: break
             try:
                 self.bucket = super(S3Manager,self).get_bucket(self.bucket_name)
@@ -112,9 +115,11 @@
 
         """ Testing purpose only """
         if "notify_oam" in self.upload_options:
-            print "notify_oam"
+            # fix_print_with_import
+            print("notify_oam")
         if "trigger_tiling" in self.upload_options:
-            print "trigger_tiling"
+            # fix_print_with_import
+            print("trigger_tiling")
 
         # configure the msg_bar_main (including Cancel button and its container)
         self.msg_bar_main = QgsMessageBar()
@@ -146,7 +151,8 @@
                 self.threads[i].started.connect(self.s3Uploaders[i].run)
                 self.threads[i].start()
 
-                print repr(self.threads[i])
+                # fix_print_with_import
+                print(repr(self.threads[i]))
 
                 # configure the msg_bars for progress bar
                 self.msg_bars.append(QgsMessageBar())
@@ -175,7 +181,7 @@
                 #self.cancel_buttons[i].clicked.connect(self.cancelUpload)
                 """
 
-            except Exception, e:
+            except Exception as e:
                 return repr(e)
 
         #Display upload progress bars in a separate widget
@@ -190,7 +196,8 @@
         return True
 
     def updateProgressBar(self, progress_value, index):
-        print "Progress: " + str(progress_value) + ", index: " + str(index)
+        # fix_print_with_import
+        print("Progress: " + str(progress_value) + ", index: " + str(index))
         if self.progress_bars[index] != None:
             self.progress_bars[index].setValue(progress_value)
 
@@ -211,11 +218,13 @@
                 #self.threads[i] = None
 
         except:
-            print "Error: problem occurred to kill uploaders"
+            # fix_print_with_import
+            print("Error: problem occurred to kill uploaders")
 
     def cancelUpload(self, index):
 
-        print "Cancel button was clicked!"
+        # fix_print_with_import
+        print("Cancel button was clicked!")
 
         """
         try:
@@ -328,7 +337,7 @@
     '''Handle uploads in a separate thread'''
 
     finished = pyqtSignal(bool, int)
-    error = pyqtSignal(Exception, basestring)
+    error = pyqtSignal(Exception, str)
     progress = pyqtSignal(float, int)
 
     def __init__(self, filename, bucket, options, index):
@@ -406,7 +415,7 @@
                 if "trigger_tiling" in self.options:
                     self.triggerTileService()
 
-        except Exception, e:
+        except Exception as e:
             # forward the exception upstream (or try to...)
             # chunk size smaller than 5MB can cause an error, server does not expect it
             self.error.emit(e, traceback.format_exc())
@@ -440,7 +449,7 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
+        if u'id' in list(post_dict.keys()):
             ts_id = post_dict[u'id']
             time = post_dict[u'queued_at']
             QgsMessageLog.logMessage(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py	(refactored)
@@ -22,14 +22,15 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from builtins import str
 
 import os, sys
 import subprocess, time
 
-from PyQt4 import QtCore
+from qgis.PyQt import QtCore
 from PyQt4.QtCore import *
 from PyQt4.QtGui import *
-from PyQt4.QtCore import QThread, pyqtSignal
+from qgis.PyQt.QtCore import QThread, pyqtSignal
 
 
 class CommandWindow(QWidget):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/get-pip.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/get-pip.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import range
 #!/usr/bin/env python
 #
 # Hi There!
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/__init__.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010-2011, Eucalyptus Systems, Inc.
 # Copyright (c) 2011, Nexenta Systems Inc.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py	(refactored)
@@ -25,6 +25,9 @@
 """
 Handles authentication required to AWS and GS
 """
+from past.builtins import cmp
+from builtins import str
+from builtins import object
 
 import base64
 import boto
@@ -230,7 +233,7 @@
         in the StringToSign.
         """
         headers_to_sign = {'Host': self.host}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             if lname.startswith('x-amz'):
                 headers_to_sign[name] = value
@@ -324,7 +327,7 @@
         if http_request.headers.get('Host'):
             host_header_value = http_request.headers['Host']
         headers_to_sign = {'Host': host_header_value}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             if lname.startswith('x-amz'):
                 if isinstance(value, bytes):
@@ -601,7 +604,7 @@
         """
         host_header_value = self.host_header(self.host, http_request)
         headers_to_sign = {'Host': host_header_value}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             # Hooray for the only difference! The main SigV4 signer only does
             # ``Host`` + ``x-amz-*``. But S3 wants pretty much everything
@@ -695,7 +698,7 @@
 
         # ``parse_qs`` will return lists. Don't do that unless there's a real,
         # live list provided.
-        for key, value in existing_qs.items():
+        for key, value in list(existing_qs.items()):
             if isinstance(value, (list, tuple)):
                 if len(value) == 1:
                     existing_qs[key] = value[0]
@@ -852,7 +855,7 @@
         hmac = self._get_hmac()
         s = params['Action'] + params['Timestamp']
         hmac.update(s.encode('utf-8'))
-        keys = params.keys()
+        keys = list(params.keys())
         keys.sort(cmp=lambda x, y: cmp(x.lower(), y.lower()))
         pairs = []
         for key in keys:
@@ -878,7 +881,7 @@
     def _calc_signature(self, params, *args):
         boto.log.debug('using _calc_signature_1')
         hmac = self._get_hmac()
-        keys = params.keys()
+        keys = list(params.keys())
         keys.sort(cmp=lambda x, y: cmp(x.lower(), y.lower()))
         pairs = []
         for key in keys:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/compat.py	(refactored)
@@ -1,3 +1,5 @@
+from future import standard_library
+standard_library.install_aliases()
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -58,10 +60,10 @@
 
 if six.PY3:
     # StandardError was removed, so use the base exception type instead
-    StandardError = Exception
+    Exception = Exception
     long_type = int
     from configparser import ConfigParser
 else:
-    StandardError = StandardErrorRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/handler.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/https_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/jsonresponse.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/plugin.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/provider.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/storage_uri.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py

-    long_type = long
-    from ConfigParser import SafeConfigParser as ConfigParser
+    Exception = Exception
+    long_type = int
+    from configparser import SafeConfigParser as ConfigParser
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py	(refactored)
@@ -42,6 +42,11 @@
 """
 Handles basic connections to AWS
 """
+from __future__ import print_function
+from builtins import zip
+from builtins import str
+from builtins import range
+from builtins import object
 from datetime import datetime
 import errno
 import os
@@ -252,7 +257,7 @@
         """
         Returns the number of connections in the pool.
         """
-        return sum(pool.size() for pool in self.host_to_pool.values())
+        return sum(pool.size() for pool in list(self.host_to_pool.values()))
 
     def get_http_connection(self, host, port, is_secure):
         """
@@ -291,7 +296,7 @@
             now = time.time()
             if self.last_clean_time + self.CLEAN_INTERVAL < now:
                 to_remove = []
-                for (host, pool) in self.host_to_pool.items():
+                for (host, pool) in list(self.host_to_pool.items()):
                     pool.clean()
                     if pool.size() == 0:
                         to_remove.append(host)
@@ -796,7 +801,7 @@
         sock.sendall("CONNECT %s HTTP/1.0\r\n" % host)
         sock.sendall("User-Agent: %s\r\n" % UserAgent)
         if self.proxy_user and self.proxy_pass:
-            for k, v in self.get_proxy_auth_header().items():
+            for k, v in list(self.get_proxy_auth_header().items()):
                 sock.sendall("%s: %s\r\n" % (k, v))
             # See discussion about this config option at
             # https://groups.google.com/forum/?fromgroups#!topic/boto-dev/teenFvOq2Cc
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py	(refactored)
@@ -24,17 +24,18 @@
 """
 Exception classes - Subclassing allows you to check for specific errors
 """
+from builtins import object
 import base64
 import xml.sax
 
 import boto
 
 from boto import handler
-from boto.compat import json, StandardError
+from boto.compat import json, Exception
 from boto.resultset import ResultSet
 
 
-class BotoClientError(StandardError):
+class BotoClientError(Exception):
     """
     General Boto Client error (error accessing AWS)
     """
@@ -49,7 +50,7 @@
         return 'BotoClientError: %s' % self.reason
 
 
-class SDBPersistenceError(StandardError):
+class SDBPersistenceError(Exception):
     pass
 
 
@@ -74,7 +75,7 @@
     pass
 
 
-class BotoServerError(StandardError):
+class BotoServerError(Exception):
     def __init__(self, status, reason, body=None, *args):
         super(BotoServerError, self).__init__(status, reason, body, *args)
         self.status = status
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/handler.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/handler.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/plugin.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/plugin.py	(refactored)
@@ -35,6 +35,7 @@
 
 The actual interface is duck typed.
 """
+from builtins import object
 
 import glob
 import imp
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/provider.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/provider.py	(refactored)
@@ -25,6 +25,8 @@
 """
 This class encapsulates the provider-specific header differences.
 """
+from builtins import str
+from builtins import object
 
 import os
 from boto.compat import six
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 # All rights reserved.
@@ -57,7 +58,7 @@
     # We can't just do an ``defaults.update(...)`` here, as that could
     # *overwrite* regions if present in both.
     # We'll iterate instead, essentially doing a deeper merge.
-    for service, region_info in additions.items():
+    for service, region_info in list(additions.items()):
         # Set the default, if not present, to an empty dict.
         defaults.setdefault(service, {})
         defaults[service].update(region_info)
@@ -134,7 +135,7 @@
 
     region_objs = []
 
-    for region_name, endpoint in endpoints.get(service_name, {}).items():
+    for region_name, endpoint in list(endpoints.get(service_name, {}).items()):
         region_objs.append(
             region_cls(
                 name=region_name,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py	(refactored)
@@ -1,7 +1,9 @@
+from future import standard_library
+standard_library.install_aliases()
 import sys
 from datetime import datetime
 from threading import Thread
-import Queue
+import queue
 
 from boto.utils import RequestHook
 from boto.compat import long_type
@@ -14,7 +16,7 @@
     """
     def __init__(self, filename='/tmp/request_log.csv'):
         self.request_log_file = open(filename, 'w')
-        self.request_log_queue = Queue.Queue(100)
+        self.request_log_queue = queue.Queue(100)
         Thread(target=self._request_log_worker).start()
 
     def handle_request_data(self, request, response, error=False):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -147,7 +148,7 @@
         else:
             return 'False'
 
-    def __nonzero__(self):
+    def __bool__(self):
         return self.status
 
     def startElement(self, name, attrs, connection):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/storage_uri.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/storage_uri.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright 2010 Google Inc.
 # Copyright (c) 2011, Nexenta Systems Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py	(refactored)
@@ -38,6 +38,9 @@
 """
 Some handy utility functions used by several classes.
 """
+from builtins import str
+from builtins import range
+from builtins import object
 
 import subprocess
 import time
@@ -167,7 +170,7 @@
         provider = boto.provider.get_default()
     metadata_prefix = provider.metadata_prefixRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py

     final_headers = headers.copy()
-    for k in metadata.keys():
+    for k in list(metadata.keys()):
         if k.lower() in boto.s3.key.Key.base_user_settable_fields:
             final_headers[k] = metadata[k]
         else:
@@ -181,7 +184,7 @@
         provider = boto.provider.get_default()
     metadata_prefix = provider.metadata_prefix
     metadata = {}
-    for hkey in headers.keys():
+    for hkey in list(headers.keys()):
         if hkey.lower().startswith(metadata_prefix):
             val = urllib.parse.unquote(headers[hkey])
             if isinstance(val, bytes):
@@ -337,11 +340,11 @@
 
     def values(self):
         self._materialize()
-        return super(LazyLoadMetadata, self).values()
+        return list(super(LazyLoadMetadata, self).values())
 
     def items(self):
         self._materialize()
-        return super(LazyLoadMetadata, self).items()
+        return list(super(LazyLoadMetadata, self).items())
 
     def __str__(self):
         self._materialize()
@@ -956,7 +959,7 @@
         '#cloud-boothook': 'text/cloud-boothook'
     }
     rtype = deftype
-    for possible_type, mimetype in starts_with_mappings.items():
+    for possible_type, mimetype in list(starts_with_mappings.items()):
         if content.startswith(possible_type):
             rtype = mimetype
             break
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import zip
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py	(refactored)
@@ -1,4 +1,6 @@
 """Classify responses from layer1 and strict type values."""
+from builtins import str
+from builtins import object
 from datetime import datetime
 from boto.compat import six
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py	(refactored)
@@ -1,4 +1,5 @@
 """Wraps layer1 api methods and converts layer1 dict responses to objects."""
+from builtins import object
 from boto.beanstalk.layer1 import Layer1
 import boto.beanstalk.response
 from boto.exception import BotoServerError
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 from datetime import datetime
 
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 from boto.resultset import ResultSet
 from boto.cloudformation.stack import Capability
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py	(refactored)
@@ -54,7 +54,7 @@
 
     def get_etag(self, response):
         response_headers = response.msg
-        for key in response_headers.keys():
+        for key in list(response_headers.keys()):
             if key.lower() == 'etag':
                 return response_headers[key]
         return None
@@ -90,7 +90,7 @@
             raise CloudFrontServerError(response.status, response.reason, body)
         d = dist_class(connection=self)
         response_headers = response.msg
-        for key in response_headers.keys():
+        for key in list(response_headers.keys()):
             if key.lower() == 'etag':
                 d.etag = response_headers[key]
         h = handler.XmlHandler(d, self)
@@ -316,7 +316,7 @@
             params['MaxItems'] = max_items
         if params:
             uri += '?%s=%s' % params.popitem()
-            for k, v in params.items():
+            for k, v in list(params.items()):
                 uri += '&%s=%s' % (k, v)
         tags=[('InvalidationSummary', InvalidationSummary)]
         rs_class = InvalidationListResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006-2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py

@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
@@ -50,9 +51,9 @@
 
         self.facets = {}
         if 'facets' in attrs:
-            for (facet, values) in attrs['facets'].items():
+            for (facet, values) in list(attrs['facets'].items()):
                 if 'constraints' in values:
-                    self.facets[facet] = dict((k, v) for (k, v) in map(lambda x: (x['value'], x['count']), values['constraints']))
+                    self.facets[facet] = dict((k, v) for (k, v) in [(x['value'], x['count']) for x in values['constraints']])
 
         self.num_pages_needed = ceil(self.hits / self.query.real_size)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 202 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -758,9 +759,9 @@
         :type value: any
         :param value: The value to serialize
         """
-        for k, v in value.items():
+        for k, v in list(value.items()):
             if isinstance(v, dict):
-                for k2, v2 in v.items():
+                for k2, v2 in list(v.items()):
                     self.build_complex_param(params, label + '.' + k, v)
             elif isinstance(v, bool):
                 params['%s.%s' % (label, k)] = v and 'true' or 'false'
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
 #
@@ -47,9 +48,9 @@
 
         self.facets = {}
         if 'facets' in attrs:
-            for (facet, values) in attrs['facets'].items():
+            for (facet, values) in list(attrs['facets'].items()):
                 if 'buckets' in values:
-                    self.facets[facet] = dict((k, v) for (k, v) in map(lambda x: (x['value'], x['count']), values.get('buckets', [])))
+                    self.facets[facet] = dict((k, v) for (k, v) in [(x['value'], x['count']) for x in values.get('buckets', [])])
 
         self.num_pages_needed = ceil(self.hits / self.query.real_size)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py

@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py	(refactored)
@@ -51,7 +51,7 @@
                 range_key = attrs.get(self._range_key_name, None)
             self[self._range_key_name] = range_key
         self._updates = {}
-        for key, value in attrs.items():
+        for key, value in list(attrs.items()):
             if key != self._hash_key_name and key != self._range_key_name:
                 self[key] = value
         self.consumed_units = 0
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py	(refactored)
@@ -24,6 +24,10 @@
 Some utility functions to deal with mapping Amazon DynamoDB types to
 Python types and vice-versa.
 """
+from builtins import bytes
+from builtins import map
+from builtins import str
+from builtins import object
 import base64
 from decimal import (Decimal, DecimalException, Context,
                      Clamped, Overflow, Inexact, Underflow, Rounded)
@@ -63,8 +67,8 @@
 
 if six.PY2:
     def is_str(n):
-        return (isinstance(n, basestring) or
-                isinstance(n, type) and issubclass(n, basestring))
+        return (isinstance(n, str) or
+                isinstance(n, type) and issubclass(n, str))
 
     def is_binary(n):
         return isinstance(n, Binary)
@@ -116,11 +120,11 @@
     elif is_str(val):
         dynamodb_type = 'S'
     elif isinstance(val, (set, frozenset)):
-        if False not in map(is_num, val):
+        if False not in list(map(is_num, val)):
             dynamodb_type = 'NS'
-        elif False not in map(is_str, val):
+        elif False not in list(map(is_str, val)):
             dynamodb_type = 'SS'
-        elif False not in map(is_binary, val):
+        elif False not in list(map(is_binary, val)):
             dynamodb_type = 'BS'
     elif is_binary(val):
         dynamodb_type = 'B'
@@ -211,7 +215,7 @@
     This hook will transform Amazon DynamoDB JSON responses to something
     that maps directly to native Python types.
     """
-    if len(dct.keys()) > 1:
+    if len(list(dct.keys())) > 1:
         return dct
     if 'S' in dct:
         return dct['S']
@@ -286,7 +290,7 @@
                 n = str(float_to_decimal(attr))
             else:
                 n = str(DYNAMODB_CONTEXT.create_decimal(attr))
-            if list(filter(lambda x: x in n, ('Infinity', 'NaN'))):
+            if list([x for x in ('Infinity', 'NaN') if x in n]):
                 raise TypeError('Infinity and NaN not supported')
             return n
         except (TypeError, DecimalException) as e:
@@ -322,7 +326,7 @@
         return attr
 
     def _encode_m(self, attr):
-        return dict([(k, self.encode(v)) for k, v in attr.items()])
+        return dict([(k, self.encode(v)) for k, v in list(attr.items())])
 
     def _encode_l(self, attr):
         return [self.encode(i) for i in attr]RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py

@@ -371,7 +375,7 @@
         return attr
 
     def _decode_m(self, attr):
-        return dict([(k, self.decode(v)) for k, v in attr.items()])
+        return dict([(k, self.decode(v)) for k, v in list(attr.items())])
 
     def _decode_l(self, attr):
         return [self.decode(i) for i in attr]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 from boto.dynamodb2.types import STRING
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 from copy import deepcopy
 
 
@@ -91,13 +92,13 @@
         del self._data[key]
 
     def keys(self):
-        return self._data.keys()
+        return list(self._data.keys())
 
     def values(self):
-        return self._data.values()
+        return list(self._data.values())
 
     def items(self):
-        return self._data.items()
+        return list(self._data.items())
 
     def get(self, key, default=None):
         return self._data.get(key, default)
@@ -217,7 +218,7 @@
         """
         self._data = {}
 
-        for field_name, field_value in data.get('Item', {}).items():
+        for field_name, field_value in list(data.get('Item', {}).items()):
             self[field_name] = self._dynamizer.decode(field_value)
 
         self._loaded = True
@@ -245,7 +246,7 @@
         """
         raw_key_data = {}
 
-        for key, value in self.get_keys().items():
+        for key, value in list(self.get_keys().items()):
             raw_key_data[key] = self._dynamizer.encode(value)
 
         return raw_key_data
@@ -322,7 +323,7 @@
         # and hand-off to the table to handle creation/update.
         final_data = {}
 
-        for key, value in self._data.items():
+        for key, value in list(self._data.items()):
             if not self._is_storable(value):
                 continue
 
@@ -344,14 +345,14 @@
         fields = set()
         alterations = self._determine_alterations()
 
-        for key, value in alterations['adds'].items():
+        for key, value in list(alterations['adds'].items()):
             final_data[key] = {
                 'Action': 'PUT',
                 'Value': self._dynamizer.encode(self._data[key])
             }
             fields.add(key)
 
-        for key, value in alterations['changes'].items():
+        for key, value in list(alterations['changes'].items()):
             final_data[key] = {
                 'Action': 'PUT',
                 'Value': self._dynamizer.encode(self._data[key])
@@ -395,7 +396,7 @@
         # Remove the key(s) from the ``final_data`` if present.
         # They should only be present if this is a new item, in which
         # case we shouldn't be sending as part of the data to update.
-        for fieldname, value in key.items():
+        for fieldname, value in list(key.items()):
             if fieldname in final_data:
                 del final_data[fieldname]
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 class ResultSet(object):
     """
     A class used to lazily handle page-to-page navigation through a set of
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 import boto
 from boto.dynamodb2 import exceptions
 from boto.dynamodb2.fields import (HashKey, RangeKey,
@@ -431,7 +432,7 @@
         if global_indexes:
             gsi_data = []
 
-            for gsi_name, gsi_throughput in global_indexes.items():
+            for gsi_name, gsi_throughput in list(global_indexes.items()):
                 gsi_data.append({
                     "Update": {
                         "IndexName": gsi_name,
@@ -584,7 +585,7 @@
         if global_indexes:
             gsi_data = []
 
-            for gsi_name, gsi_throughput in global_indexes.items():
+            for gsi_name, gsi_throughput in list(global_indexes.items()):
                 gsi_data.append({
                     "Update": {
                         "IndexName": gsi_name,
@@ -646,7 +647,7 @@
         """
         raw_key = {}
 
-        for key, value in keys.items():
+        for key, value in list(keys.items()):
             raw_key[key] = self._dynamizer.encode(value)
 
         return raw_key
@@ -770,7 +771,7 @@
         for x, arg in enumerate(args):
             kwargs[self.schema[x].name] = arg
         ret = self.get_item(**kwargs)
-        if not ret.keys():
+        if not list(ret.keys()):
             return None
         return ret
 
@@ -996,7 +997,7 @@
 
         filters = {}
 
-        for field_and_op, value in filter_kwargs.items():
+        for field_and_op, value in list(filter_kwargs.items()):
             field_bits = field_and_op.split('__')
             fieldname = '__'.join(field_bits[:-1])
 
@@ -1329,7 +1330,7 @@
         if exclusive_start_key:
             kwargs['exclusive_start_key'] = {}
 
-            for key, value in exclusive_start_key.items():
+            for key, value in list(exclusive_start_key.items()):
                 kwargs['exclusive_start_key'][key] = \
                     self._dynamizer.encode(value)
 
@@ -1361,7 +1362,7 @@
         if raw_results.get('LastEvaluatedKey', None):
             last_key = {}
 
-            for key, value in raw_results['LastEvaluatedKey'].items():
+            for key, value in list(raw_results['LastEvaluatedKey'].items()):
                 last_key[key] = self._dynamizer.decode(value)
 
         return {
@@ -1465,7 +1466,7 @@
         if exclusive_start_key:
             kwargs['exclusive_start_key'] = {}
 
-            for key, value in exclusive_start_key.items():
+            for key, value in list(exclusive_start_key.items()):
                 kwargs['exclusive_start_key'][key] = \
                     self._dynamizer.encode(value)
 
@@ -1492,7 +1493,7 @@
         if raw_results.get('LastEvaluatedKey', None):
             last_key = {}
 
-            for key, value in raw_results['LastEvaluatedKey'].items():
+            for key, value in list(raw_results['LastEvaluatedKey'].items()):
                 last_key[key] = self._dynamizer.decode(value)
 
         return {
@@ -1564,7 +1565,7 @@
         for key_data in keys:
             raw_key = {}
 
-            for key, value in key_data.items():
+            for key, value in list(key_data.items()):
                 raw_key[key] = self._dynamizer.encode(value)
 
             items[self.table_name]['Keys'].append(raw_key)
@@ -1585,7 +1586,7 @@
         for raw_key in raw_unproccessed.get('Keys', []):
             py_key = {}
 
-            for key, value in raw_key.items():
+            for key, value in list(raw_key.items()):
                 py_key[key] = self._dynamizer.decode(value)
 
             unprocessed_keys.append(py_key)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/keypair.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotpricehistory.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py	(refactored)
@@ -24,6 +24,9 @@
 """
 Represents a connection to the EC2 service.
 """
+from past.builtins import cmp
+from builtins import str
+from builtins import range
 
 import base64
 import warnings
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Represents an EC2 Object
 """
+from builtins import object
 from boto.ec2.tag import TagSet
 
 
@@ -138,7 +139,7 @@
             tags,
             dry_run=dry_run
         )
-        for key, value in tags.items():
+        for key, value in list(tags.items()):
             if key in self.tags:
                 if value is None or value == self.tags[key]:
                     del self.tags[key]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Represents an EC2 Instance
 """
+from builtins import object
 import boto
 from boto.ec2.ec2object import EC2Object, TaggedEC2Object
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py	(refactored)
@@ -23,6 +23,8 @@
 """
 Represents an EC2 Elastic Network Interface
 """
+from builtins import str
+from builtins import object
 from boto.exception import BotoClientError
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Represents an EC2 Security Group
 """
+from builtins import object
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.exception import BotoClientError
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Represents an EC2 Elastic Block Store Snapshot
 """
+from builtins import object
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.ec2.zone import Zone
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Represents an EC2 Spot Instance Request
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.ec2.launchspecification import LaunchSpecification
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Represents an EC2 Elastic Block Storage Volume
 """
+from builtins import object
 from boto.resultset import ResultSet
 from boto.ec2.tag import Tag
 from boto.ec2.ec2object import TaggedEC2Object
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/activity.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/group.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/instance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/launchconfig.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/limits.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/policy.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/request.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/scheduled.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/tag.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/alarm.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/__init__.py	(refactored)
@@ -26,6 +26,8 @@
 This module provides an interface to the Elastic Compute Cloud (EC2)
 Auto Scaling service.
 """
+from builtins import str
+from builtins import range
 
 import base64
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/activity.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/activity.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2011 Reza Lotun http://reza.lotun.name/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/group.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/group.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2011 Reza Lotun http://reza.lotun.name/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/instance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/instance.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009 Reza Lotun http://reza.lotun.name/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/launchconfig.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/launchconfig.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009 Reza Lotun http://reza.lotun.name/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/limits.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/limits.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/policy.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/policy.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2010 Reza Lotun http://reza.lotun.name/
 # Copyright (c) 2011 Jann Kleen
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/request.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/request.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009 Reza Lotun http://reza.lotun.name/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/scheduled.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/scheduled.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2010 Reza Lotun http://reza.lotun.name/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/tag.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/tag.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py	(refactored)
@@ -23,6 +23,8 @@
 This module provides an interface to the Elastic Compute Cloud (EC2)
 CloudWatch service from AWS.
 """
+from builtins import zip
+from builtins import map
 from boto.compat import json, map, six, zip
 from boto.connection import AWSQueryConnection
 from boto.ec2.cloudwatch.metric import Metric
@@ -136,7 +138,7 @@
     def build_put_params(self, params, name, value=None, timestamp=None,
                          unit=None, dimensions=None, statistics=None):
         args = (name, value, unit, dimensions, statistics, timestamp)
-        length = max(map(lambda a: len(a) if isinstance(a, list) else 1, args))
+        length = max([len(a) if isinstance(a, list) else 1 for a in args])
 
         def aslist(a):
             if isinstance(a, list):
@@ -145,7 +147,7 @@
                 return a
             return [a] * length
 
-        for index, (n, v, u, d, s, t) in enumerate(zip(*map(aslist, args))):
+        for index, (n, v, u, d, s, t) in enumerate(zip(*list(map(aslist, args)))):
             metric_data = {'MetricName': n}
 
             if timestamp:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/alarm.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/alarm.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Reza Lotun http://reza.lotun.name
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Permission is hereby granted, free of charge, to any person obtaining a
 # copy of this software and associated documentation files (the
 # "Software"), to deal in the Software without restriction, including
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/connection.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Reza Lotun http://reza.lotun.name
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Reza Lotun http://reza.lotun.name
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py	(refactored)
@@ -1,3 +1,5 @@
+from future import standard_library
+standard_library.install_aliases()
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -23,7 +25,7 @@
 from boto.connection import AWSQueryConnection, AWSAuthConnection
 from boto.exception import BotoServerError
 import time
-import urllib
+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 from boto.ecs.item import ItemSet
 from boto import handler
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import next
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Spotify AB
 # Copyright (c) 2010 Yelp
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py	(refactored)
@@ -23,6 +23,8 @@
 """
 Represents a connection to the EMR service
 """
+from builtins import str
+from builtins import zip
 import types
 
 import boto
@@ -383,7 +385,7 @@
         if not isinstance(new_sizes, list):
             new_sizes = [new_sizes]
 
-        instance_groups = zip(instance_group_ids, new_sizes)
+        instance_groups = list(zip(instance_group_ids, new_sizes))
 
         params = {}
         for k, ig in enumerate(instance_groups):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py	(refactored)
@@ -24,6 +24,7 @@
 """
 This module contains EMR response objects
 """
+from builtins import object
 
 from boto.resultset import ResultSet
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
 # copy of this software and associated documentation files (the
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Spotify AB
 # Copyright (c) 2010-2011 Yelp
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 # Copyright (c) 2011, Nexenta Systems Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining aRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/utils.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/vault.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/writer.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/acl.py

--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 # Copyright (c) 2011, Nexenta Systems Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py	(refactored)
@@ -1,3 +1,8 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import map
+from builtins import str
+from builtins import filter
 # Copyright (c) 2012 Andy Davidoff http://www.disruptek.com/
 # Copyright (c) 2010 Jason R. Coombs http://www.jaraco.com/
 # Copyright (c) 2008 Chris Moyer http://coredumped.org/
@@ -21,7 +26,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 
-import urllib
+import urllib.request, urllib.parse, urllib.error
 import uuid
 from boto.connection import AWSQueryConnection
 from boto.fps.exception import ResponseErrorFactory
@@ -59,8 +64,8 @@
     def decorator(func):
 
         def wrapper(*args, **kw):
-            hasgroup = lambda x: len(x) == len(filter(kw.has_key, x))
-            if 1 != len(filter(hasgroup, groups)):
+            hasgroup = lambda x: len(x) == len(list(filter(kw.has_key, x)))
+            if 1 != len(list(filter(hasgroup, groups))):
                 message = ' OR '.join(['+'.join(g) for g in groups])
                 message = "{0} requires {1} argument(s)" \
                           "".format(getattr(func, 'action', 'Method'), message)
@@ -86,7 +91,7 @@
 def api_action(*api):
 
     def decorator(func):
-        action = ''.join(api or map(str.capitalize, func.__name__.split('_')))
+        action = ''.join(api or list(map(str.capitalize, func.__name__.split('_'))))
         response = ResponseFactory(action)
         if hasattr(boto.fps.response, action + 'Response'):
             response = getattr(boto.fps.response, action + 'Response')
@@ -212,8 +217,8 @@
         kw.setdefault('callerKey', self.aws_access_key_id)
 
         safestr = lambda x: x is not None and str(x) or ''
-        safequote = lambda x: urllib.quote(safestr(x), safe='~')
-        payload = sorted([(k, safequote(v)) for k, v in kw.items()])
+        safequote = lambda x: urllib.parse.quote(safestr(x), safe='~')
+        payload = sorted([(k, safequote(v)) for k, v in list(kw.items())])
 
         encoded = lambda p: '&'.join([k + '=' + v for k, v in p])
         canonical = '\n'.join(['GET', endpoint, base, encoded(payload)])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py	(refactored)
@@ -1,3 +1,7 @@
+from builtins import str
+from builtins import filter
+from builtins import map
+from builtins import object
 # Copyright (c) 2012 Andy Davidoff http://www.disruptek.com/
 # Copyright (c) 2010 Jason R. Coombs http://www.jaraco.com/
 # Copyright (c) 2008 Chris Moyer http://coredumped.org/
@@ -50,7 +54,7 @@
     def __repr__(self):
         render = lambda pair: '{!s}: {!r}'.format(*pair)
         do_show = lambda pair: not pair[0].startswith('_')
-        attrs = filter(do_show, self.__dict__.items())
+        attrs = list(filter(do_show, list(self.__dict__.items())))
         return '{0}({1})'.format(self.__class__.__name__,
                                ', '.join(map(render, attrs)))
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py	(refactored)
@@ -1,3 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import range
+from builtins import object
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import range
+from builtins import object
 # -*- coding: utf-8 -*-
 # Copyright (c) 2012 Thomas Parslow http://almostobsolete.net/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # -*- coding: utf-8 -*-
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # -*- coding: utf-8 -*-
 # Copyright (c) 2012 Thomas Parslow http://almostobsolete.net/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/utils.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import range
+from builtins import object
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/vault.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/vault.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # -*- coding: utf-8 -*-
 # Copyright (c) 2012 Thomas Parslow http://almostobsolete.net/
 # Copyright (c) 2012 Robie Basak <robie@justgohome.co.uk>
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/writer.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/writer.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # -*- coding: utf-8 -*-
 # Copyright (c) 2012 Thomas Parslow http://almostobsolete.net/
 # Copyright (c) 2012 Robie Basak <robie@justgohome.co.uk>
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/acl.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/acl.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py	(refactored)
@@ -1,3 +1,6 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -20,7 +23,7 @@
 # IN THE SOFTWARE.
 
 import re
-import urllibRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucketlistresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/cors.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/lifecycle.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/user.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/summarymap.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py

+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 
 import boto
@@ -102,7 +105,7 @@
             query_args_l.append('generation=%s' % generation)
         if response_headers:
             for rk, rv in six.iteritems(response_headers):
-                query_args_l.append('%s=%s' % (rk, urllib.quote(rv)))
+                query_args_l.append('%s=%s' % (rk, urllib.parse.quote(rv)))
         try:
             key, resp = self._get_key_internal(key_name, headers,
                                                query_args_l=query_args_l)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucketlistresultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucketlistresultset.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2012 Google Inc.
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/key.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/lifecycle.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/lifecycle.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2013 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py	(refactored)
@@ -1,3 +1,8 @@
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -19,13 +24,13 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 import errno
-import httplib
+import http.client
 import os
 import random
 import re
 import socket
 import time
-import urlparse
+import urllib.parse
 from hashlib import md5
 from boto import config, UserAgent
 from boto.connection import AWSAuthConnection
@@ -54,7 +59,7 @@
 class ResumableUploadHandler(object):
 
     BUFFER_SIZE = 8192
-    RETRYABLE_EXCEPTIONS = (httplib.HTTPException, IOError, socket.error,
+    RETRYABLE_EXCEPTIONS = (http.client.HTTPException, IOError, socket.error,
                             socket.gaierror)
 
     # (start, end) response indicating server has nothing (upload protocol uses
@@ -139,7 +144,7 @@
 
         Raises InvalidUriError if URI is syntactically invalid.
         """
-        parse_result = urlparse.urlparse(uri)
+        parse_result = urllib.parse.urlparse(uri)
         if (parse_result.scheme.lower() not in ['http', 'https'] or
             not parse_result.netloc):
             raise InvalidUriError('Invalid tracker URI (%s)' % uri)
@@ -237,8 +242,8 @@
             # Parse 'bytes=<from>-<to>' range_spec.
             m = re.search('bytes=(\d+)-(\d+)', range_spec)
             if m:
-                server_start = long(m.group(1))
-                server_end = long(m.group(2))
+                server_start = int(m.group(1))
+                server_end = int(m.group(2))
                 got_valid_response = True
         else:
             # No Range header, which means the server does not yet have
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/user.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/user.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2010-2011 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010-2011, Eucalyptus Systems, Inc.
 #
@@ -1110,7 +1111,7 @@
                 return assume_role_policy_document
         else:
 
-            for tld, policy in DEFAULT_POLICY_DOCUMENTS.items():
+            for tld, policy in list(DEFAULT_POLICY_DOCUMENTS.items()):
                 if tld is 'default':
                     # Skip the default. We'll fall back to it if we don't find
                     # anything.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py	(refactored)
@@ -24,6 +24,9 @@
 functions for running commands, managing files, and opening interactive
 shell sessions over those connections.
 """
+from __future__ import print_function
+from builtins import input
+from builtins import object
 from boto.mashups.interactive import interactive_shellRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/task.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/interactive.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py

 import boto
 import os
@@ -89,7 +92,7 @@
             except paramiko.BadHostKeyException:
                 print("%s has an entry in ~/.ssh/known_hosts and it doesn't match" % self.server.hostname)
                 print('Edit that file to remove the entry and then hit return to try again')
-                raw_input('Hit Enter when ready')
+                input('Hit Enter when ready')
                 retry += 1
             except EOFError:
                 print('Unexpected Error from SSH Connection, retry in 5 seconds')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py	(refactored)
@@ -1,3 +1,6 @@
+from __future__ import print_function
+from builtins import input
+from builtins import range
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -38,7 +41,7 @@
                 if isinstance(value, tuple):
                     value = value[0]
                 print('[%d] %s' % (i, value))
-            value = raw_input('%s [%d-%d]: ' % (prompt, min, max))
+            value = input('%s [%d-%d]: ' % (prompt, min, max))
             try:
                 int_value = int(value)
                 value = choices[int_value-1]
@@ -50,7 +53,7 @@
             except IndexError:
                 print('%s is not within the range[%d-%d]' % (min, max))
         else:
-            value = raw_input('%s: ' % prompt)
+            value = input('%s: ' % prompt)
             try:
                 value = prop.validate(value)
                 if prop.empty(value) and prop.required:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py	(refactored)
@@ -22,6 +22,10 @@
 """
 High-level abstraction of an EC2 server
 """
+from __future__ import print_function
+from builtins import str
+from builtins import next
+from builtins import object
 
 import boto.ec2
 from boto.mashups.iobject import IObject
@@ -137,7 +141,7 @@
 
     def get_region(self, params):
         region = params.get('region', None)
-        if isinstance(region, basestring):
+        if isinstance(region, str):
             region = boto.ec2.get_region(region)
             params['region'] = region
         if not region:
@@ -189,7 +193,7 @@
 
     def get_group(self, params):
         group = params.get('group', None)
-        if isinstance(group, basestring):
+        if isinstance(group, str):
             group_list = self.ec2.get_all_security_groups()
             for g in group_list:
                 if g.name == group:
@@ -202,7 +206,7 @@
 
     def get_key(self, params):
         keypair = params.get('keypair', None)
-        if isinstance(keypair, basestring):
+        if isinstance(keypair, str):
             key_list = self.ec2.get_all_key_pairs()
             for k in key_list:
                 if k.name == keypair:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/task.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/task.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py	(refactored)
@@ -1,3 +1,4 @@
+from __future__ import print_function
 from boto.manage.server import Server
 from boto.manage.volume import Volume
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py	(refactored)
@@ -19,6 +19,9 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 from __future__ import print_function
+from past.builtins import cmp
+from builtins import range
+from builtins import object
 
 from boto.sdb.db.model import Model
 from boto.sdb.db.property import StringProperty, IntegerProperty, ListProperty, ReferenceProperty, CalculatedProperty
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py	(refactored)
@@ -1,3 +1,6 @@
+from __future__ import print_function
+from builtins import input
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -39,7 +42,7 @@
             n = 1
             choices = []
             for item in item_list:
-                if isinstance(item, basestring):
+                if isinstance(item, str):
                     print('[%d] %s' % (n, item))
                     choices.append(item)
                     n += 1
@@ -56,7 +59,7 @@
                             choices.append(obj)
                             n += 1
             if choices:
-                val = raw_input('%s[1-%d]: ' % (prompt, len(choices)))
+                val = input('%s[1-%d]: ' % (prompt, len(choices)))
                 if val.startswith('/'):
                     search_str = val[1:]
                 else:
@@ -78,7 +81,7 @@
     def get_string(self, prompt, validation_fn=None):
         okay = False
         while not okay:
-            val = raw_input('%s: ' % prompt)
+            val = input('%s: ' % prompt)
             if validation_fn:
                 okay = validation_fn(val)
                 if not okay:
@@ -91,7 +94,7 @@
         okay = False
         val = ''
         while not okay:
-            val = raw_input('%s: %s' % (prompt, val))
+            val = input('%s: %s' % (prompt, val))
             val = os.path.expanduser(val)
             if os.path.isfile(val):
                 okay = True
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py	(refactored)
@@ -21,6 +21,7 @@
 """
 High-level abstraction of an EC2 order for servers
 """
+from __future__ import print_function
 
 import boto
 import boto.ec2
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py	(refactored)
@@ -21,6 +21,8 @@
 """
 High-level abstraction of an EC2 server
 """
+from __future__ import print_function
+from builtins import str
 
 import boto
 import boto.utils
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py	(refactored)
@@ -1,3 +1,6 @@
+from __future__ import print_function
+from builtins import range
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -322,7 +325,7 @@
         total_records = int(search_rs.TotalNumResults)
         get_page_hits = lambda page: self.search_hits(page_size=page_size, page_number=page)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/layoutparam.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/notification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/price.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/qualification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py

         page_nums = self._get_pages(page_size, total_records)
-        hit_sets = itertools.imap(get_page_hits, page_nums)
+        hit_sets = map(get_page_hits, page_nums)
         return itertools.chain.from_iterable(hit_sets)
 
     def search_hits(self, sort_by='CreationTime', sort_direction='Ascending',
@@ -676,7 +679,7 @@
             params['TestDurationInSeconds'] = test_duration
 
         if answer_key is not None:
-            if isinstance(answer_key, basestring):
+            if isinstance(answer_key, str):
                 params['AnswerKey'] = answer_key  # xml
             else:
                 raise TypeError
@@ -705,7 +708,7 @@
         total_records = int(search_qual.TotalNumResults)
         get_page_quals = lambda page: self.get_qualifications_for_qualification_type(qualification_type_id = qualification_type_id, page_size=page_size, page_number = page)
         page_nums = self._get_pages(page_size, total_records)
-        qual_sets = itertools.imap(get_page_quals, page_nums)
+        qual_sets = map(get_page_quals, page_nums)
         return itertools.chain.from_iterable(qual_sets)
 
     def get_qualifications_for_qualification_type(self, qualification_type_id, page_size=100, page_number = 1):
@@ -744,7 +747,7 @@
             params['TestDurationInSeconds'] = test_duration
 
         if answer_key is not None:
-            if isinstance(answer_key, basestring):
+            if isinstance(answer_key, str):
                 params['AnswerKey'] = answer_key  # xml
             else:
                 raise TypeError
@@ -862,7 +865,7 @@
             keywords = ', '.join(keywords)
         if isinstance(keywords, str):
             final_keywords = keywords
-        elif isinstance(keywords, unicode):
+        elif isinstance(keywords, str):
             final_keywords = keywords.encode('utf-8')
         elif keywords is None:
             final_keywords = ""
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/layoutparam.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/layoutparam.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2008 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/notification.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/notification.py	(refactored)
@@ -23,6 +23,8 @@
 Provides NotificationMessage and Event classes, with utility methods, for
 implementations of the Mechanical Turk Notification API.
 """
+from builtins import str
+from builtins import object
 
 import hmac
 try:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/price.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/price.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/qualification.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/qualification.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2008 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py	(refactored)
@@ -1,3 +1,8 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import zip
+from builtins import str
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -51,8 +56,8 @@
     class ValidatingXML(object):
 
         def validate(self):
-            import urllib2
-            schema_src_file = urllib2.urlopen(self.schema_url)
+            import urllib.request, urllib.error, urllib.parse
+            schema_src_file = urllib.request.urlopen(self.schema_url)
             schema_doc = etree.parse(schema_src_file)
             schema = etree.XMLSchema(schema_doc)
             doc = etree.fromstring(self.get_as_xml())
@@ -128,7 +133,7 @@
     def get_inner_content(self, content):
         content.append_field('Width', self.width)
         content.append_field('Height', self.height)
-        for name, value in self.parameters.items():
+        for name, value in list(self.parameters.items()):
             value = self.parameter_template % vars()
             content.append_field('ApplicationParameter', value)
 
@@ -286,7 +291,7 @@
 
 class Constraint(object):
     def get_attributes(self):
-        pairs = zip(self.attribute_names, self.attribute_values)
+        pairs = list(zip(self.attribute_names, self.attribute_values))
         attrs = ' '.join(
             '%s="%d"' % (name, value)
             for (name, value) in pairs
@@ -323,7 +328,7 @@
         self.attribute_values = pattern, error_text, flags
 
     def get_attributes(self):
-        pairs = zip(self.attribute_names, self.attribute_values)
+        pairs = list(zip(self.attribute_names, self.attribute_values))
         attrs = ' '.join(
             '%s="%s"' % (name, value)
             for (name, value) in pairs
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py	(refactored)
@@ -1,3 +1,7 @@
+from builtins import map
+from builtins import filter
+from builtins import str
+from builtins import range
 # Copyright (c) 2012-2014 Andy Davidoff http://www.disruptek.com/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -134,7 +138,7 @@
 
         def wrapper(*args, **kw):
             members = kwargs.get('members', False)
-            for field in filter(lambda i: i in kw, fields):
+            for field in [i for i in fields if i in kw]:
                 destructure_object(kw.pop(field), kw, field, members=members)
             return func(*args, **kw)
         wrapper.__doc__ = "{0}\nElement|Iter|Map: {1}\n" \
@@ -236,7 +240,7 @@
 
     def decorator(func, quota=int(quota), restore=float(restore)):
         version, accesskey, path = api_version_path[section]
-        action = ''.join(api or map(str.capitalize, func.__name__.split('_')))
+        action = ''.join(api or list(map(str.capitalize, func.__name__.split('_'))))
 
         def wrapper(self, *args, **kw):
             kw.setdefault(accesskey, getattr(self, accesskey, None))
@@ -274,12 +278,12 @@
         super(MWSConnection, self).__init__(*args, **kw)
 
     def _setup_factories(self, extrascopes, **kw):
-        for factory, (scope, Default) in {
+        for factory, (scope, Default) in list({
             'response_factory':
                 (boto.mws.response, self.ResponseFactory),
             'response_error_factory':
                 (boto.mws.exception, self.ResponseErrorFactory),
-        }.items():
+        }.items()):
             if factory in kw:
                 setattr(self, '_' + factory, kw.pop(factory))
             else:
@@ -417,7 +421,7 @@
     def get_service_status(self, **kw):
         """Instruct the user on how to get service status.
         """
-        sections = ', '.join(map(str.lower, api_version_path.keys()))
+        sections = ', '.join(map(str.lower, list(api_version_path.keys())))RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/bootstrap.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/startup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/ebs.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py

         message = "Use {0}.get_(section)_service_status(), " \
                   "where (section) is one of the following: " \
                   "{1}".format(self.__class__.__name__, sections)
@@ -721,10 +725,10 @@
         toggle = set(('FulfillmentChannel.Channel.1',
                       'OrderStatus.Status.1', 'PaymentMethod.1',
                       'LastUpdatedAfter', 'LastUpdatedBefore'))
-        for do, dont in {
+        for do, dont in list({
             'BuyerEmail': toggle.union(['SellerOrderId']),
             'SellerOrderId': toggle.union(['BuyerEmail']),
-        }.items():
+        }.items()):
             if do in kw and any(i in dont for i in kw):
                 message = "Don't include {0} when specifying " \
                           "{1}".format(' or '.join(dont), do)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/exception.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/exception.py	(refactored)
@@ -1,3 +1,4 @@
+from __future__ import print_function
 # Copyright (c) 2012-2014 Andy Davidoff http://www.disruptek.com/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py	(refactored)
@@ -1,3 +1,8 @@
+from builtins import str
+from builtins import filter
+from builtins import hex
+from builtins import map
+from builtins import object
 # Copyright (c) 2012-2014 Andy Davidoff http://www.disruptek.com/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -42,7 +47,7 @@
         self._hint = JITResponse
         self._hint.__name__ = 'JIT_{0}/{1}'.format(self.__class__.__name__,
                                                    hex(id(self._hint))[2:])
-        for name, value in kw.items():
+        for name, value in list(kw.items()):
             setattr(self._hint, name, value)
 
     def __repr__(self):
@@ -202,7 +207,7 @@
         scope = inherit(self.__class__)
         scope.update(self.__dict__)
         declared = lambda attr: isinstance(attr[1], DeclarativeType)
-        for name, node in filter(declared, scope.items()):
+        for name, node in filter(declared, list(scope.items())):
             getattr(node, op)(self, name, parentname=self._name, **kw)
 
     @property
@@ -212,7 +217,7 @@
     def __repr__(self):
         render = lambda pair: '{0!s}: {1!r}'.format(*pair)
         do_show = lambda pair: not pair[0].startswith('_')
-        attrs = filter(do_show, self.__dict__.items())
+        attrs = list(filter(do_show, list(self.__dict__.items())))
         name = self.__class__.__name__
         if name.startswith('JIT_'):
             name = '^{0}^'.format(self._name or '')
@@ -415,7 +420,7 @@
 
     def __repr__(self):
         values = [getattr(self, key, None) for key in self._dimensions]
-        values = filter(None, values)
+        values = [_f for _f in values if _f]
         return 'x'.join(map('{0.Value:0.2f}{0[Units]}'.format, values))
 
     @strip_namespace
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py	(refactored)
@@ -1,3 +1,6 @@
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011 Chris Moyer http://coredumped.org/
 #
@@ -211,11 +214,11 @@
         sdb = boto.connect_sdb()
         domain = sdb.lookup(domain_name)
         item = domain.get_item(item_name)
-        for section in item.keys():
+        for section in list(item.keys()):
             if not self.has_section(section):
                 self.add_section(section)
             d = json.loads(item[section])
-            for attr_name in d.keys():
+            for attr_name in list(d.keys()):
                 attr_value = d[attr_name]
                 if attr_value is None:
                     attr_value = 'None'
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py	(refactored)
@@ -1,3 +1,5 @@
+from future import standard_library
+standard_library.install_aliases()
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -21,7 +23,7 @@
 #
 import boto
 from boto.pyami.scriptbase import ScriptBase
-import os, StringIO
+import os, io
 
 class CopyBot(ScriptBase):
 
@@ -82,7 +84,7 @@
         key.set_contents_from_filename(self.log_path)
 
     def main(self):
-        fp = StringIO.StringIO()
+        fp = io.StringIO()
         boto.config.dump_safe(fp)
         self.notify('%s (%s) Starting' % (self.name, self.instance_id), fp.getvalue())
         if self.src and self.dst:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py	(refactored)
@@ -20,6 +20,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 #
+from __future__ import print_function
 import getopt
 import sys
 import imp
@@ -140,7 +141,7 @@
         params['script_md5'] = key.md5
     # we have everything we need, now build userdata string
     l = []
-    for k, v in params.items():
+    for k, v in list(params.items()):
         if v:
             l.append('%s=%s' % (k, v))
     c = boto.connect_ec2()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 import os
 import sys
 from boto.utils import ShellCommand, get_ts
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/ebs.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/ebs.py	(refactored)
@@ -43,6 +43,7 @@
     mount_point = <directory to mount device, defaults to /ebs>
 
 """
+from builtins import next
 import boto
 from boto.manage.volume import Volume
 from boto.exception import EC2ResponseError
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -43,7 +44,7 @@
             hour = str(random.randrange(24))
         fp = open('/etc/cron.d/%s' % name, "w")
         if env:
-            for key, value in env.items():RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/mysql.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/trac.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbinstance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsecuritygroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsnapshot.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsubnetgroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/event.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/logfile.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/optiongroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/statusinfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/vpcsecuritygroupmembership.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py

+            for key, value in list(env.items()):
                 fp.write('%s=%s\n' % (key, value))
         fp.write('%s %s %s %s %s %s %s\n' % (minute, hour, mday, month, wday, who, command))
         fp.close()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py	(refactored)
@@ -1,3 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
 # Copyright (c) 2009-2012 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -20,7 +24,7 @@
 # IN THE SOFTWARE.
 #
 
-import urllib
+import urllib.request, urllib.parse, urllib.error
 from boto.connection import AWSQueryConnection
 from boto.rds.dbinstance import DBInstance
 from boto.rds.dbsecuritygroup import DBSecurityGroup
@@ -451,7 +455,7 @@
             self.build_list_params(params, l, 'VpcSecurityGroupIds.member')
 
         # Remove any params set to None
-        for k, v in params.items():
+        for k, v in list(params.items()):
           if v is None: del(params[k])
 
         return self.get_object('CreateDBInstance', params, DBInstance)
@@ -990,7 +994,7 @@
         if ec2_security_group_owner_id:
             params['EC2SecurityGroupOwnerId'] = ec2_security_group_owner_id
         if cidr_ip:
-            params['CIDRIP'] = urllib.quote(cidr_ip)
+            params['CIDRIP'] = urllib.parse.quote(cidr_ip)
         return self.get_object('AuthorizeDBSecurityGroupIngress', params,
                                DBSecurityGroup)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbinstance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbinstance.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsecuritygroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsecuritygroup.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents an DBSecurityGroup
 """
+from builtins import object
 from boto.ec2.securitygroup import SecurityGroup
 
 class DBSecurityGroup(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsnapshot.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsnapshot.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsubnetgroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsubnetgroup.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents an DBSubnetGroup
 """
+from builtins import object
 
 class DBSubnetGroup(object):
     """
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/event.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/event.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/logfile.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/logfile.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2014 Jumping Qu http://newrice.blogspot.com/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/optiongroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/optiongroup.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Represents an OptionGroup
 """
+from builtins import object
 
 from boto.rds.dbsecuritygroup import DBSecurityGroup
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -133,7 +134,7 @@
             d[prefix+'ApplyMethod'] = self.apply_method
 
     def _set_string_value(self, value):
-        if not isinstance(value, basestring):
+        if not isinstance(value, str):
             raise ValueError('value must be of type str')
         if self.allowed_values:
             choices = self.allowed_values.split(',')
@@ -142,9 +143,9 @@
         self._value = value
 
     def _set_integer_value(self, value):
-        if isinstance(value, basestring):
+        if isinstance(value, str):
             value = int(value)
-        if isinstance(value, int) or isinstance(value, long):
+        if isinstance(value, int) or isinstance(value, int):
             if self.allowed_values:
                 min, max = self.allowed_values.split('-')
                 if value < int(min) or value > int(max):
@@ -156,7 +157,7 @@
     def _set_boolean_value(self, value):
         if isinstance(value, bool):
             self._value = value
-        elif isinstance(value, basestring):
+        elif isinstance(value, str):
             if value.lower() == 'true':
                 self._value = True
             else:
@@ -180,7 +181,7 @@
         if self.type == 'string':
             return self._value
         elif self.type == 'integer':
-            if not isinstance(self._value, int) and not isinstance(self._value, long):
+            if not isinstance(self._value, int) and not isinstance(self._value, int):
                 self._set_integer_value(self._value)
             return self._value
         elif self.type == 'boolean':
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/statusinfo.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/statusinfo.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/vpcsecuritygroupmembership.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/vpcsecuritygroupmembership.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a VPCSecurityGroupMembership
 """
+from builtins import object
 
 
 class VPCSecurityGroupMembership(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights ReservedRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/acl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py

 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 # Copyright (c) 2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
@@ -482,7 +484,7 @@
                 if isinstance(item, dict):
                     for field_name in item:
                         line.append(item[field_name])
-                elif isinstance(item, basestring):
+                elif isinstance(item, str):
                     line.append(item)
                 line.print_it()
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py	(refactored)
@@ -1,6 +1,8 @@
 from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
 import os
-import urlparse
+import urllib.parse
 import boto
 import boto.connection
 import boto.jsonresponse
@@ -96,7 +98,7 @@
         if not url and self.EnvURL in os.environ:
             url = os.environ[self.EnvURL]
         if url:
-            rslt = urlparse.urlparse(url)
+            rslt = urllib.parse.urlparse(url)
             if 'is_secure' not in self.args:
                 if rslt.scheme == 'https':
                     self.args['is_secure'] = True
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 #
@@ -27,7 +28,7 @@
     @classmethod
     def convert_string(cls, param, value):
         # TODO: could do length validation, etc. here
-        if not isinstance(value, basestring):
+        if not isinstance(value, str):
             raise ValueError
         return value
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 # Copyright (c) 2011 Blue Pines Technologies LLC, Brad Carleton
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py	(refactored)
@@ -45,6 +45,8 @@
    </HealthCheckConfig>
 </CreateHealthCheckRequest>
 """
+from builtins import str
+from builtins import object
 
 
 class HealthCheck(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 # All rights reserved.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Blue Pines Technologies LLC, Brad Carleton
 # www.bluepines.org
 # All rights reserved.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Blue Pines Technologies LLC, Brad Carleton
 # www.bluepines.org
 # Copyright (c) 2012 42 Lines Inc., Jim Browne
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/__init__.py	(refactored)
@@ -60,7 +60,7 @@
 
 def connect_to_region(region_name, **kw_params):
     for region in regions():
-        if 'host' in kw_params.keys():
+        if 'host' in list(kw_params.keys()):
             # Make sure the host specified is not nothing
             if kw_params['host'] not in ['', None]:
                 region.endpoint = kw_params['host']
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/acl.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/acl.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py	(refactored)
@@ -1,3 +1,6 @@
+from builtins import str
+from builtins import next
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
 # All rights reserved.
@@ -369,7 +372,7 @@
         if initial_query_string:
             pairs.append(initial_query_string)
 
-        for key, value in sorted(params.items(), key=lambda x: x[0]):
+        for key, value in sorted(list(params.items()), key=lambda x: x[0]):
             if value is None:
                 continue
             key = key.replace('_', '-')RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlistresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/cors.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/deletemarker.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/lifecycle.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multidelete.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multipart.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/prefix.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/tagging.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/user.py

--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlistresultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlistresultset.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
@@ -395,7 +396,7 @@
         if version_id is not None:
             extra_qp.append("versionId=%s" % version_id)
         if response_headers:
-            for k, v in response_headers.items():
+            for k, v in list(response_headers.items()):
                 extra_qp.append("%s=%s" % (k, urllib.parse.quote(v)))
         if self.provider.security_token:
             headers['x-amz-security-token'] = self.provider.security_token
@@ -414,7 +415,7 @@
             query_part = ''
         if headers:
             hdr_prefix = self.provider.header_prefix
-            for k, v in headers.items():
+            for k, v in list(headers.items()):
                 if k.startswith(hdr_prefix):
                     # headers used for sig generation must be
                     # included in the url also.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/cors.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/cors.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/deletemarker.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/deletemarker.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2010 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011, Nexenta Systems Inc.
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
@@ -304,7 +306,7 @@
             response_headers = self.resp.msg
             self.metadata = boto.utils.get_aws_metadata(response_headers,
                                                         provider)
-            for name, value in response_headers.items():
+            for name, value in list(response_headers.items()):
                 # To get correct size for Range GETs, use Content-Range
                 # header if one was returned. If not, use Content-Length
                 # header.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py	(refactored)
@@ -25,11 +25,12 @@
 Python file interface. The only functions supported are those needed for seeking
 in a Key open for reading.
 """
+from builtins import object
 
 import os
 from boto.exception import StorageResponseError
 
-class KeyFile():
+class KeyFile(object):
 
   def __init__(self, key):
     self.key = key
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/lifecycle.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/lifecycle.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multidelete.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multidelete.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multipart.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multipart.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # Copyright (c) 2010, Eucalyptus Systems, Inc.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/prefix.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/prefix.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py	(refactored)
@@ -1,3 +1,8 @@
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import object
 # Copyright 2010 Google Inc.
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -19,7 +24,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 import errno
-import httplib
+import http.client
 import os
 import re
 import socket
@@ -92,7 +97,7 @@
 
     MIN_ETAG_LEN = 5
 
-    RETRYABLE_EXCEPTIONS = (httplib.HTTPException, IOError, socket.error,
+    RETRYABLE_EXCEPTIONS = (http.client.HTTPException, IOError, socket.error,
                             socket.gaierror)
 
     def __init__(self, tracker_file_name=None, num_retries=None):
@@ -341,7 +346,7 @@
             # which we can safely ignore.
             try:
                 key.close()
-            except httplib.IncompleteRead:
+            except http.client.IncompleteRead:
                 pass
 
             sleep_time_secs = 2**progress_less_iterations
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/tagging.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/tagging.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/website.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/item.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/property.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py

@@ -1,3 +1,4 @@
+from builtins import object
 from boto import handler
 import xml.sax
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/user.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/user.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/website.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/website.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from __future__ import print_function
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -173,14 +174,14 @@
             params['Expected.1.Value'] = expected_value[1]
 
     def _build_batch_list(self, params, items, replace=False):
-        item_names = items.keys()
+        item_names = list(items.keys())
         i = 0
         for item_name in item_names:
             params['Item.%d.ItemName' % i] = item_name
             j = 0
             item = items[item_name]
             if item is not None:
-                attr_names = item.keys()
+                attr_names = list(item.keys())
                 for attr_name in attr_names:
                     value = item[attr_name]
                     if isinstance(value, list):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py	(refactored)
@@ -19,6 +19,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 from __future__ import print_function
+from builtins import object
 
 """
 Represents an SDB Domain
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import next
+from builtins import object
 from boto.compat import six
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py	(refactored)
@@ -1,3 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import next
+from builtins import object
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -31,7 +35,7 @@
 
     @property
     def file(self):
-        from StringIO import StringIO
+        from io import StringIO
         if self._file:
             f = self._file
         else:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/key.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -24,6 +26,7 @@
 from boto.sdb.db.query import Query
 import boto
 from boto.compat import filter
+from future.utils import with_metaclass
 
 class ModelMeta(type):
     "Metaclass for all Models"
@@ -37,12 +40,12 @@
         from boto.sdb.db.manager import get_manager
 
         try:
-            if filter(lambda b: issubclass(b, Model), bases):
+            if [b for b in bases if issubclass(b, Model)]:
                 for base in bases:
                     base.__sub_classes__.append(cls)
                 cls._manager = get_manager(cls)
                 # look for all of the Properties and set their names
-                for key in dict.keys():
+                for key in list(dict.keys()):
                     if isinstance(dict[key], Property):
                         property = dict[key]
                         property.__property_config__(cls, key)
@@ -57,8 +60,7 @@
             # Model class, defined below.
             pass
 
-class Model(object):
-    __metaclass__ = ModelMeta
+class Model(with_metaclass(ModelMeta, object)):
     __consistent__ = False # Consistent is set off by default
     id = None
 
@@ -95,7 +97,7 @@
     @classmethod
     def find(cls, limit=None, next_token=None, **params):
         q = Query(cls, limit=limit, next_token=next_token)
-        for key, value in params.items():
+        for key, value in list(params.items()):
             q.filter('%s =' % key, value)
         return q
 
@@ -111,7 +113,7 @@
     def properties(cls, hidden=True):
         properties = []
         while cls:
-            for key in cls.__dict__.keys():
+            for key in list(cls.__dict__.keys()):
                 prop = cls.__dict__[key]
                 if isinstance(prop, Property):
                     if hidden or not prop.__class__.__name__.startswith('_'):
@@ -126,7 +128,7 @@
     def find_property(cls, prop_name):
         property = None
         while cls:
-            for key in cls.__dict__.keys():
+            for key in list(cls.__dict__.keys()):
                 prop = cls.__dict__[key]
                 if isinstance(prop, Property):
                     if not prop.__class__.__name__.startswith('_') and prop_name == prop.name:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/property.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/property.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import next
+from builtins import object
 from boto.compat import six
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/test_db.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/message.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/service.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/servicedef.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/sonofmmm.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py

@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import object
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/test_db.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/test_db.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 import logging
 import time
 from datetime import datetime
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py	(refactored)
@@ -1,3 +1,9 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import map
+from builtins import str
+from builtins import next
+from builtins import object
 # Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
@@ -71,7 +77,7 @@
                          str: (self.encode_string, self.decode_string),
                       }
         if six.PY2:
-            self.type_map[long] = (self.encode_long, self.decode_long)
+            self.type_map[int] = (self.encode_long, self.decode_long)
 
     def encode(self, item_type, value):
         try:
@@ -108,7 +114,7 @@
         return self.encode_map(prop, values)
 
     def encode_map(self, prop, value):
-        import urllib
+        import urllib.request, urllib.parse, urllib.error
         if value is None:
             return None
         if not isinstance(value, dict):
@@ -120,7 +126,7 @@
                 item_type = self.model_class
             encoded_value = self.encode(item_type, value[key])
             if encoded_value is not None:
-                new_value.append('%s:%s' % (urllib.quote(key), encoded_value))
+                new_value.append('%s:%s' % (urllib.parse.quote(key), encoded_value))
         return new_value
 
     def encode_prop(self, prop, value):
@@ -145,7 +151,7 @@
                     except:
                         k = v
                     dec_val[k] = v
-            value = dec_val.values()
+            value = list(dec_val.values())
         return value
 
     def decode_map(self, prop, value):
@@ -160,11 +166,11 @@
 
     def decode_map_element(self, item_type, value):
         """Decode a single element for a map"""
-        import urllib
+        import urllib.request, urllib.parse, urllib.error
         key = value
         if ":" in value:
             key, value = value.split(':', 1)
-            key = urllib.unquote(key)
+            key = urllib.parse.unquote(key)
         if self.model_class in item_type.mro():
             value = item_type(id=value)
         else:
@@ -316,7 +322,7 @@
             # TODO: Handle tzinfo
             raise TimeDecodeError("Can't handle timezone aware objects: %r" % value)
         tmp = value.split('.')
-        arg = map(int, tmp[0].split(':'))
+        arg = list(map(int, tmp[0].split(':')))
         if len(tmp) == 2:
             arg.append(int(tmp[1]))
         return time(*arg)
@@ -389,7 +395,7 @@
             # systems, however:
             arr = []
             for ch in value:
-                arr.append(six.unichr(ord(ch)))
+                arr.append(six.chr(ord(ch)))
             return u"".join(arr)
 
     def decode_string(self, value):
@@ -623,7 +629,7 @@
 
 
         type_query = "(`__type__` = '%s'" % cls.__name__
-        for subclass in self._get_all_decendents(cls).keys():
+        for subclass in list(self._get_all_decendents(cls).keys()):
             type_query += " or `__type__` = '%s'" % subclass
         type_query += ")"
         query_parts.append(type_query)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py	(refactored)
@@ -1,3 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import object
 # Copyright (c) 2006-2008 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -49,7 +53,7 @@
                           Password : (self.encode_password, self.decode_password),
                           datetime : (self.encode_datetime, self.decode_datetime)}
         if six.PY2:
-            self.type_map[long] = (self.encode_long, self.decode_long)
+            self.type_map[int] = (self.encode_long, self.decode_long)
 
     def get_text_value(self, parent_node):
         value = ''
@@ -116,12 +120,12 @@
         return value
 
     def encode_long(self, value):
-        value = long(value)
+        value = int(value)
         return '%d' % value
 
     def decode_long(self, value):
         value = self.get_text_value(value)
-        return long(value)
+        return int(value)
 
     def encode_bool(self, value):
         if value == True:
@@ -210,9 +214,9 @@
     def _connect(self):
         if self.db_host:
             if self.enable_ssl:
-                from httplib import HTTPSConnection as Connection
+                from http.client import HTTPSConnection as Connection
             else:
-                from httplib import HTTPConnection as Connection
+                from http.client import HTTPConnection as Connection
 
             self.connection = Connection(self.db_host, self.db_port)
 
@@ -348,7 +352,7 @@
         if not self.connection:
             raise NotImplementedError("Can't query without a database connection")
 
-        from urllib import urlencode
+        from urllib.parse import urlencode
 
         query = str(self._build_query(cls, filters, limit, order_by))
         if query:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 #!/usr/bin/env python
 # Copyright (c) 2006-2008 Mitch Garnaat http://garnaat.org/
 #
@@ -64,7 +66,7 @@
 
     def print_command_help(self):
         print('\nCommands:')
-        for key in self.Commands.keys():
+        for key in list(self.Commands.keys()):
             print('  %s\t\t%s' % (key, self.Commands[key]))
 
     def do_reset(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 #!/usr/bin/env python
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py	(refactored)
@@ -1,3 +1,6 @@
+from __future__ import print_function
+from builtins import str
+from builtins import object
 # Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import range
 # Copyright (c) 2010 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011 Harry Marr http://hmarr.com/RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/bigmessage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/jsonmessage.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py

 #
@@ -91,7 +92,7 @@
         params = params or {}
         params['Action'] = action
 
-        for k, v in params.items():
+        for k, v in list(params.items()):
             if isinstance(v, six.text_type):  # UTF-8 encode only if it's Unicode
                 params[k] = v.encode('utf-8')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import zip
+from builtins import range
 # Copyright (c) 2010-2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
@@ -95,7 +97,7 @@
       :param dictionary: dict - value of the serialized parameter
       :param name: name of the serialized parameter
       """
-      items = sorted(dictionary.items(), key=lambda x:x[0])
+      items = sorted(list(dictionary.items()), key=lambda x:x[0])
       for kv, index in zip(items, list(range(1, len(items)+1))):
         key, value = kv
         prefix = '%s.entry.%s' % (name, index)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py	(refactored)
@@ -23,6 +23,7 @@
 """
 A set of results returned by SendMessageBatch.
 """
+from builtins import object
 
 class ResultEntry(dict):
     """
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py	(refactored)
@@ -62,6 +62,7 @@
 The Message class must provide a get_body_encoded method that returns the current body of the message
 in the format in which it would be stored in SQS.
 """
+from builtins import object
 
 import base64
 
@@ -210,7 +211,7 @@
 
     def encode(self, value):
         s = ''
-        for item in value.items():
+        for item in list(value.items()):
             s = s + '%s: %s\n' % (item[0], item[1])
         return s
 
@@ -228,13 +229,13 @@
         self.set_body(self._body)
 
     def keys(self):
-        return self._body.keys()
+        return list(self._body.keys())
 
     def values(self):
-        return self._body.values()
+        return list(self._body.values())
 
     def items(self):
-        return self._body.items()
+        return list(self._body.items())
 
     def has_key(self, key):
         return key in self._body
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py	(refactored)
@@ -22,6 +22,8 @@
 """
 Represents an SQS Queue
 """
+from __future__ import print_function
+from builtins import object
 from boto.compat import urllib
 from boto.sqs.message import Message
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2011 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2011, Eucalyptus Systems, Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py	(refactored)
@@ -1,6 +1,7 @@
 """
 Helper class for creating decision responses.
 """
+from builtins import object
 
 
 class Layer1Decisions(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py	(refactored)
@@ -1,4 +1,6 @@
 """Object-oriented interface to SWF wrapping boto.swf.layer1.Layer1"""
+from builtins import str
+from builtins import object
 
 import time
 from functools import wraps
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py	(refactored)
@@ -1,4 +1,9 @@
 """Utilities for writing code that runs on Python 2 and 3"""
+from future import standard_library
+standard_library.install_aliases()
+from builtins import bytes
+from builtins import str
+from builtins import object
 
 # Copyright (c) 2010-2014 Benjamin Peterson
 #
@@ -42,10 +47,10 @@
 
     MAXSIZE = sys.maxsize
 else:
-    string_types = basestring,
-    integer_types = (int, long)
-    class_types = (type, types.ClassType)
-    text_type = unicode
+    string_types = str,
+    integer_types = (int, int)
+    class_types = (type, type)
+    text_type = str
     binary_type = str
 
     if sys.platform.startswith("java"):
@@ -507,7 +512,7 @@
     Iterator = object
 else:
     def get_unbound_function(unbound):
-        return unbound.im_func
+        return unbound.__func__
 
     def create_bound_method(func, obj):
         return types.MethodType(func, obj, obj.__class__)
@@ -568,7 +573,7 @@
         return s.encode("latin-1")
     def u(s):
         return s
-    unichr = chr
+    chr = chr
     if sys.version_info[1] <= 1:
         def int2byte(i):
             return bytes((i,))
@@ -586,8 +591,8 @@
         return s
     # Workaround for standalone backslash
     def u(s):
-        return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")
-    unichr = unichr
+        return str(s.replace(r'\\', r'\\\\'), "unicode_escape")
+    chr = chr
     int2byte = chr
     def byte2int(bs):
         return ord(bs[0])
@@ -595,8 +600,8 @@
         return ord(buf[i])
     def iterbytes(buf):
         return (ord(byte) for byte in buf)
-    import StringIO
-    StringIO = BytesIO = StringIO.StringIO
+    import io
+    StringIO = BytesIO = io.StringIO
 _add_doc(b, """Byte literal""")
 _add_doc(u, """Text literal""")
 
@@ -637,11 +642,11 @@
         if fp is None:
             return
         def write(data):
-            if not isinstance(data, basestring):
+            if not isinstance(data, str):
                 data = str(data)
             # If the file has an encoding, encode unicode with it.
             if (isinstance(fp, file) and
-                isinstance(data, unicode) and
+                isinstance(data, str) and
                 fp.encoding is not None):
                 errors = getattr(fp, "errors", None)
                 if errors is None:
@@ -651,13 +656,13 @@
         want_unicode = False
         sep = kwargs.pop("sep", None)
         if sep is not None:RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/internetgateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/networkacl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/routetable.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/subnet.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc_peering_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpnconnection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpngateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/compat.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/test.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py

-            if isinstance(sep, unicode):
+            if isinstance(sep, str):
                 want_unicode = True
             elif not isinstance(sep, str):
                 raise TypeError("sep must be None or a string")
         end = kwargs.pop("end", None)
         if end is not None:
-            if isinstance(end, unicode):
+            if isinstance(end, str):
                 want_unicode = True
             elif not isinstance(end, str):
                 raise TypeError("end must be None or a string")
@@ -665,12 +670,12 @@
             raise TypeError("invalid keyword arguments to print()")
         if not want_unicode:
             for arg in args:
-                if isinstance(arg, unicode):
+                if isinstance(arg, str):
                     want_unicode = True
                     break
         if want_unicode:
-            newline = unicode("\n")
-            space = unicode(" ")
+            newline = str("\n")
+            space = str(" ")
         else:
             newline = "\n"
             space = " "
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a connection to the EC2 service.
 """
+from builtins import str
 
 from boto.ec2.connection import EC2Connection
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/internetgateway.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/internetgateway.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents an Internet Gateway
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/networkacl.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/networkacl.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a Network ACL
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/routetable.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/routetable.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a Route Table
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 from boto.resultset import ResultSet
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc_peering_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc_peering_connection.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a VPC Peering Connection.
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpnconnection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpnconnection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2009-2010 Mitch Garnaat http://garnaat.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpngateway.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpngateway.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Represents a Vpn Gateway
 """
+from builtins import object
 
 from boto.ec2.ec2object import TaggedEC2Object
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py	(refactored)
@@ -1,5 +1,6 @@
 # -*- coding: utf-8 -*-
 
+from __future__ import print_function
 import os
 import boto
 import sys
@@ -30,8 +31,10 @@
 
 try:
     release = os.environ.get('SVN_REVISION', 'HEAD')
-    print release
-except Exception, e:
-    print e
+    # fix_print_with_import
+    print(release)
+except Exception as e:
+    # fix_print_with_import
+    print(e)
 
 html_title = "boto v%s" % version
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py	(refactored)
@@ -5,7 +5,10 @@
 (https://bitbucket.org/dhellmann/sphinxcontrib-bitbucket/)
 
 """
-from urlparse import urljoin
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from urllib.parse import urljoin
 
 from docutils import nodes, utils
 from docutils.parsers.rst.roles import set_classes
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -90,7 +92,9 @@
         t.put()
         self.objs.append(t)
         time.sleep(3)
-        print SimpleListModel.all().filter("strs !=", "Fizzle").get_query()
+        # fix_print_with_import
+        print(SimpleListModel.all().filter("strs !=", "Fizzle").get_query())
         for tt in SimpleListModel.all().filter("strs !=", "Fizzle"):
-            print tt.strs
+            # fix_print_with_import
+            print(tt.strs)
             assert("Fizzle" not in tt.strs)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2010 Robert Mela
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import object
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -148,5 +150,6 @@
         """Test with a "like" expression"""
         query = SimpleModel.all()
         query.filter("strs like", "%oo%")
-        print query.get_query()
+        # fix_print_with_import
+        print(query.get_query())
         assert(query.count() == 1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2010 Chris Moyer http://coredumped.org/
 #
 # Permission is hereby granted, free of charge, to any person obtaining aRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/devpay/test_s3.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_layers.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cloudtrail.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/sync/test_cognito_sync.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_table.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py

@@ -60,11 +61,11 @@
         s = Sequence()
         self.sequences.append(s)
         assert(s.val == 0)
-        assert(s.next() == 1)
-        assert(s.next() == 2)
+        assert(next(s) == 1)
+        assert(next(s) == 2)
         s2 = Sequence(s.id)
         assert(s2.val == 2)
-        assert(s.next() == 3)
+        assert(next(s) == 3)
         assert(s.val == 3)
         assert(s2.val == 3)
 
@@ -73,7 +74,7 @@
         s = Sequence(fnc=increment_string)
         self.sequences.append(s)
         assert(s.val == "A")
-        assert(s.next() == "B")
+        assert(next(s) == "B")
 
     def test_fib(self):
         """Test the fibonacci sequence generator"""
@@ -93,7 +94,7 @@
         assert(s.val == 1)
         # Just check the first few numbers in the sequence
         for v in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]:
-            assert(s.next() == v)
+            assert(next(s) == v)
             assert(s.val == v)
             assert(s2.val == v) # it shouldn't matter which reference we use since it's garunteed to be consistent
 
@@ -103,7 +104,7 @@
         s = Sequence(fnc=increment_string)
         self.sequences.append(s)
         assert(s.val == "A")
-        assert(s.next() == "B")
+        assert(next(s) == "B")
         s.val = "Z"
         assert(s.val == "Z")
-        assert(s.next() == "AA")
+        assert(next(s) == "AA")
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/devpay/test_s3.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/devpay/test_s3.py	(refactored)
@@ -24,10 +24,13 @@
 """
 Some unit tests for the S3Connection
 """
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
 
 import time
 import os
-import urllib
+import urllib.request, urllib.parse, urllib.error
 
 from boto.s3.connection import S3Connection
 from boto.exception import S3PermissionsError
@@ -38,7 +41,8 @@
 DEVPAY_HEADERS = { 'x-amz-security-token': AMAZON_USER_TOKEN }
 
 def test():
-    print '--- running S3Connection tests (DevPay) ---'
+    # fix_print_with_import
+    print('--- running S3Connection tests (DevPay) ---')
     c = S3Connection()
     # create a new, empty bucket
     bucket_name = 'test-%d' % int(time.time())
@@ -67,10 +71,10 @@
     fp.close()
     # test generated URLs
     url = k.generate_url(3600, headers=DEVPAY_HEADERS)
-    file = urllib.urlopen(url)
+    file = urllib.request.urlopen(url)
     assert s1 == file.read(), 'invalid URL %s' % url
     url = k.generate_url(3600, force_http=True, headers=DEVPAY_HEADERS)
-    file = urllib.urlopen(url)
+    file = urllib.request.urlopen(url)
     assert s1 == file.read(), 'invalid URL %s' % url
     bucket.delete_key(k, headers=DEVPAY_HEADERS)
     # test a few variations on get_all_keys - first load some data
@@ -175,7 +179,8 @@
 
     c.delete_bucket(bucket, headers=DEVPAY_HEADERS)
 
-    print '--- tests completed ---'
+    # fix_print_with_import
+    print('--- tests completed ---')
 
 if __name__ == '__main__':
     test()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import str
 #!/usr/bin/env python
 
 from tests.unit import unittest
@@ -11,7 +13,8 @@
     devpath = os.path.relpath(os.path.join('..', '..'),
                               start=os.path.dirname(__file__))
     sys.path = [devpath] + sys.path
-    print '>>> advanced FPS tests; using local boto sources'
+    # fix_print_with_import
+    print('>>> advanced FPS tests; using local boto sources')
     advanced = True
 
 from boto.fps.connection import FPSConnection
@@ -63,7 +66,8 @@
             'callerReference':      'foo',
         }
         result = self.fps.cbui_url(**inputs)
-        print "cbui_url() yields {0}".format(result)
+        # fix_print_with_import
+        print("cbui_url() yields {0}".format(result))
 
     @unittest.skipUnless(simple, "skipping simple test")
     def test_get_account_activity(self):
@@ -88,12 +92,14 @@
         try:
             self.fps.write_off_debt(CreditInstrumentId='foo',
                                     AdjustmentAmount=123.45)
-        except Exception, e:
-            print e
+        except Exception as e:
+            # fix_print_with_import
+            print(e)
 
     @unittest.skip('cosmetic')
     def test_repr(self):
-        print self.fps.get_account_balance()
+        # fix_print_with_import
+        print(self.fps.get_account_balance())
 
 
 if __name__ == "__main__":
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Base class to make checking the certs easier.
 """
+from builtins import object
 
 
 # We subclass from ``object`` instead of ``TestCase`` here so that this doesn't
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 import random
 import time
 from functools import partial
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 #!/usr/bin/env python
 import time
 import json
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Tests for Layer1 of DynamoDB
 """
+from __future__ import print_function
 import time
 import base64
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Tests for Layer2 of Amazon DynamoDB
 """
+from __future__ import print_function
 import time
 import uuid
 from decimal import Decimal
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py	(refactored)
@@ -23,6 +23,9 @@
 """
 Tests for DynamoDB v2 high-level abstractions.
 """
+from builtins import next
+from builtins import str
+from builtins import range
 import os
 import time
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Tests for Layer1 of DynamoDB v2
 """
+from builtins import range
 import time
 
 from tests.unit import unittest
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/vpc/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elasticache/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py	(refactored)
@@ -24,6 +24,8 @@
 """
 Some unit tests for the EC2Connection
 """
+from __future__ import print_function
+from builtins import str
 
 import unittest
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Some unit tests for the AutoscaleConnection
 """
+from __future__ import print_function
 
 import time
 from boto.ec2.autoscale import AutoScaleConnection
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Initial, and very limited, unit tests for CloudWatchConnection.
 """
+from builtins import object
 
 import datetime
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Initial, and very limited, unit tests for ELBConnection.
 """
+from builtins import str
 
 import boto
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py	(refactored)
@@ -26,6 +26,7 @@
 as the 'cb' parameter to boto.s3.Key.send_file() and boto.s3.Key.get_file(),
 allowing testing of various file upload/download conditions.
 """
+from builtins import object
 
 import socket
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py	(refactored)
@@ -27,11 +27,13 @@
 """
 Some integration tests for the GSConnection
 """
+from future import standard_library
+standard_library.install_aliases()
 
 import os
 import re
-import StringIO
-import urllib
+import io
+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 
 from boto import handler
@@ -102,14 +104,14 @@
         fp.close()
         # Use generate_url to get the contents
         url = self._conn.generate_url(900, 'GET', bucket=bucket.name, key=key_name)
-        f = urllib.urlopen(url)
+        f = urllib.request.urlopen(url)
         self.assertEqual(s1, f.read())
         f.close()
         # check to make sure set_contents_from_file is working
-        sfp = StringIO.StringIO('foo')
+        sfp = io.StringIO('foo')
         k.set_contents_from_file(sfp)
         self.assertEqual(k.get_contents_as_string(), 'foo')
-        sfp2 = StringIO.StringIO('foo2')
+        sfp2 = io.StringIO('foo2')
         k.set_contents_from_file(sfp2)
         self.assertEqual(k.get_contents_as_string(), 'foo2')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py	(refactored)
@@ -22,8 +22,11 @@
 # IN THE SOFTWARE.
 
 """Integration tests for GS versioning support."""
-
-import StringIO
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+
+import io
 import os
 import tempfile
 from xml import sax
@@ -44,20 +47,20 @@
         b = self._MakeBucket()
         k = b.new_key("foo")
         s1 = "test1"
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_file(fp, if_generation=999)
 
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         k.set_contents_from_file(fp, if_generation=0)
         g1 = k.generation
 
         s2 = "test2"
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_file(fp, if_generation=int(g1)+1)
 
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         k.set_contents_from_file(fp, if_generation=g1)
         self.assertEqual(k.get_contents_as_string(), s2)
 
@@ -156,21 +159,21 @@
         b = self._MakeBucket()
         k = b.new_key("foo")
         s1 = "test1"
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_stream(fp, if_generation=999)
 
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         k.set_contents_from_stream(fp, if_generation=0)
         g1 = k.generation
 
         k = b.get_key("foo")
         s2 = "test2"
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_stream(fp, if_generation=int(g1)+1)
 
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         k.set_contents_from_stream(fp, if_generation=g1)
         self.assertEqual(k.get_contents_as_string(), s2)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py	(refactored)
@@ -22,6 +22,7 @@
 """
 Tests of resumable downloads.
 """
+from __future__ import absolute_import
 
 import errno
 import os
@@ -32,7 +33,7 @@
 from boto.s3.resumable_download_handler import ResumableDownloadHandler
 from boto.exception import ResumableTransferDisposition
 from boto.exception import ResumableDownloadException
-from cb_test_harness import CallbackTestHarness
+from .cb_test_harness import CallbackTestHarness
 from tests.integration.gs.testcase import GSTestCase
 
 
@@ -102,7 +103,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected ResumableDownloadException')
-        except ResumableDownloadException, e:
+        except ResumableDownloadException as e:
             # We'll get a ResumableDownloadException at this point because
             # of CallbackTestHarness (above). Check that the tracker file was
             # created correctly.
@@ -164,7 +165,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected OSError')
-        except OSError, e:
+        except OSError as e:
             # Ensure the error was re-raised.
             self.assertEqual(e.errno, 13)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py

 
@@ -228,7 +229,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected ResumableDownloadException')
-        except ResumableDownloadException, e:
+        except ResumableDownloadException as e:
             self.assertEqual(e.disposition,
                              ResumableTransferDisposition.ABORT_CUR_PROCESS)
             # Ensure a tracker file survived.
@@ -345,7 +346,7 @@
             os.chmod(tmp_dir, 0)
             res_download_handler = ResumableDownloadHandler(
                 tracker_file_name=tracker_file_name)
-        except ResumableDownloadException, e:
+        except ResumableDownloadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('Couldn\'t write URI tracker file'), -1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py	(refactored)
@@ -22,8 +22,13 @@
 """
 Tests of Google Cloud Storage resumable uploads.
 """
-
-import StringIO
+from __future__ import absolute_import
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
+
+import io
 import errno
 import random
 import os
@@ -35,7 +40,7 @@
 from boto.exception import InvalidUriError
 from boto.exception import ResumableTransferDisposition
 from boto.exception import ResumableUploadException
-from cb_test_harness import CallbackTestHarness
+from .cb_test_harness import CallbackTestHarness
 from tests.integration.gs.testcase import GSTestCase
 
 
@@ -57,7 +62,7 @@
         for i in range(size):
             buf.append(str(random.randint(0, 9)))
         file_as_string = ''.join(buf)
-        return (file_as_string, StringIO.StringIO(file_as_string))
+        return (file_as_string, io.StringIO(file_as_string))
 
     def make_small_file(self):
         return self.build_input_file(SMALL_KEY_SIZE)
@@ -120,7 +125,7 @@
                 small_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # We'll get a ResumableUploadException at this point because
             # of CallbackTestHarness (above). Check that the tracker file was
             # created correctly.
@@ -185,7 +190,7 @@
                 small_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected OSError')
-        except OSError, e:
+        except OSError as e:
             # Ensure the error was re-raised.
             self.assertEqual(e.errno, 13)
 
@@ -247,7 +252,7 @@
                 larger_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition,
                              ResumableTransferDisposition.ABORT_CUR_PROCESS)
             # Ensure a tracker file survived.
@@ -296,7 +301,7 @@
         Tests uploading an empty file (exercises boundary conditions).
         """
         res_upload_handler = ResumableUploadHandler()
-        empty_src_file = StringIO.StringIO('')
+        empty_src_file = io.StringIO('')
         empty_src_file.seek(0)
         dst_key = self._MakeKey(set_contents=False)
         dst_key.set_contents_from_file(
@@ -351,7 +356,7 @@
                 larger_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # First abort (from harness-forced failure) should be
             # ABORT_CUR_PROCESS.
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT_CUR_PROCESS)
@@ -368,7 +373,7 @@
             dst_key.set_contents_from_file(
                 largest_src_file, res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # This abort should be a hard abort (file size changing during
             # transfer).
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
@@ -391,7 +396,7 @@
                 test_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('File changed during upload'), -1)
@@ -411,7 +416,7 @@
                     test_file, cb=harness.call,
                     res_upload_handler=res_upload_handler)
                 return False
-            except ResumableUploadException, e:
+            except ResumableUploadException as e:
                 self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
                 # Ensure the file size didn't change.
                 test_file.seek(0, os.SEEK_END)
@@ -422,7 +427,7 @@
                 try:
                     dst_key_uri.get_key()
                     self.fail('Did not get expected InvalidUriError')
-                except InvalidUriError, e:
+                except InvalidUriError as e:
                     pass
             return True
 
@@ -477,7 +482,7 @@
                 small_src_file, res_upload_handler=res_upload_handler,
                 headers={'Content-Length' : SMALL_KEY_SIZE})
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('Attempt to specify Content-Length header'), -1)
@@ -543,7 +548,7 @@
             os.chmod(tmp_dir, 0)
             res_upload_handler = ResumableUploadHandler(
                 tracker_file_name=tracker_file_name)
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('Couldn\'t write URI tracker file'), -1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py	(refactored)
@@ -22,10 +22,14 @@
 # IN THE SOFTWARE.
 
 """Integration tests for StorageUri interface."""
+from future import standard_library
+standard_library.install_aliases()
+from builtins import hex
+from builtins import str
 
 import binascii
 import re
-import StringIO
+import io
 
 from boto import storage_uri
 from boto.exception import BotoClientError
@@ -112,14 +116,14 @@
         self.assertEqual(k.generation, key_uri.generation)
         self.assertEquals(k.get_contents_as_string(), "data1")
 
-        key_uri.set_contents_from_stream(StringIO.StringIO("data2"))
+        key_uri.set_contents_from_stream(io.StringIO("data2"))
         self.assertRegexpMatches(str(key_uri.generation), r"[0-9]+")
         self.assertGreater(key_uri.generation, k.generation)
         k = b.get_key("obj")
         self.assertEqual(k.generation, key_uri.generation)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/testcase.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_password_policy.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_kinesis.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/opsworks/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py

         self.assertEquals(k.get_contents_as_string(), "data2")
 
-        key_uri.set_contents_from_file(StringIO.StringIO("data3"))
+        key_uri.set_contents_from_file(io.StringIO("data3"))
         self.assertRegexpMatches(str(key_uri.generation), r"[0-9]+")
         self.assertGreater(key_uri.generation, k.generation)
         k = b.get_key("obj")
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import str
 # Copyright (c) 2012, Google, Inc.
 # All rights reserved.
 #
@@ -70,12 +72,13 @@
                     return f(*args, **kwargs)
                     try_one_last_time = False
                     break
-                except ExceptionToCheck, e:
+                except ExceptionToCheck as e:
                     msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                     if logger:
                         logger.warning(msg)
                     else:
-                        print msg
+                        # fix_print_with_import
+                        print(msg)
                     time.sleep(mdelay)
                     mtries -= 1
                     mdelay *= backoff
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py	(refactored)
@@ -23,6 +23,8 @@
 """
 Check that db_subnet_groups behave sanely
 """
+from __future__ import print_function
+from builtins import str
 
 import time
 import unittest
@@ -32,15 +34,18 @@
 
 def _is_ok(subnet_group, vpc_id, description, subnets):
     if subnet_group.vpc_id != vpc_id:
-        print 'vpc_id is ',subnet_group.vpc_id, 'but should be ', vpc_id
+        # fix_print_with_import
+        print('vpc_id is ',subnet_group.vpc_id, 'but should be ', vpc_id)
         return 0
     if subnet_group.description != description:
-        print "description is '"+subnet_group.description+"' but should be '"+description+"'"
+        # fix_print_with_import
+        print("description is '"+subnet_group.description+"' but should be '"+description+"'")
         return 0
     if set(subnet_group.subnet_ids) != set(subnets):
         subnets_are = ','.join(subnet_group.subnet_ids)
         should_be   = ','.join(subnets)
-        print "subnets are "+subnets_are+" but should be "+should_be
+        # fix_print_with_import
+        print("subnets are "+subnets_are+" but should be "+should_be)
         return 0
     return 1
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py	(refactored)
@@ -12,6 +12,8 @@
 """
 Check that promotion of read replicas and renaming instances works as expected
 """
+from __future__ import print_function
+from builtins import str
 
 import unittest
 import time
@@ -35,11 +37,13 @@
                     self.conn.delete_dbinstance(db, skip_final_snapshot=True)
 
     def test_promote(self):
-        print '--- running RDS promotion & renaming tests ---'
+        # fix_print_with_import
+        print('--- running RDS promotion & renaming tests ---')
         self.masterDB = self.conn.create_dbinstance(self.masterDB_name, 5, 'db.t1.micro', 'root', 'bototestpw')
         
         # Wait up to 15 minutes for the masterDB to become available
-        print '--- waiting for "%s" to become available  ---' % self.masterDB_name
+        # fix_print_with_import
+        print('--- waiting for "%s" to become available  ---' % self.masterDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
  
@@ -56,7 +60,8 @@
         self.replicaDB = self.conn.create_dbinstance_read_replica(self.replicaDB_name, self.masterDB_name)
 
         # Wait up to 15 minutes for the replicaDB to become available
-        print '--- waiting for "%s" to become available  ---' % self.replicaDB_name
+        # fix_print_with_import
+        print('--- waiting for "%s" to become available  ---' % self.replicaDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
         
@@ -74,7 +79,8 @@
         self.replicaDB = self.conn.promote_read_replica(self.replicaDB_name)
 
         # Wait up to 15 minutes for the replicaDB to become available
-        print '--- waiting for "%s" to be promoted and available  ---' % self.replicaDB_name
+        # fix_print_with_import
+        print('--- waiting for "%s" to be promoted and available  ---' % self.replicaDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
         
@@ -97,12 +103,14 @@
         inst = instances[0]
         self.assertFalse(inst.read_replica_dbinstance_identifiers)
 
-        print '--- renaming "%s" to "%s" ---' % ( self.replicaDB_name, self.renamedDB_name )
+        # fix_print_with_import
+        print('--- renaming "%s" to "%s" ---' % ( self.replicaDB_name, self.renamedDB_name ))
 
         self.renamedDB = self.conn.modify_dbinstance(self.replicaDB_name, new_instance_id=self.renamedDB_name, apply_immediately=True)
 
         # Wait up to 15 minutes for the masterDB to become available
-        print '--- waiting for "%s" to exist  ---' % self.renamedDB_name
+        # fix_print_with_import
+        print('--- waiting for "%s" to exist  ---' % self.renamedDB_name)
 
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
@@ -119,7 +127,8 @@
 
         self.assertTrue(found)
 
-        print '--- waiting for "%s" to become available ---' % self.renamedDB_name
+        # fix_print_with_import
+        print('--- waiting for "%s" to become available ---' % self.renamedDB_name)
 
         instances = self.conn.get_all_dbinstances(self.renamedDB_name)
         inst = instances[0]
@@ -135,4 +144,5 @@
         # Since the replica DB was renamed...
         self.replicaDB = None
 
-        print '--- tests completed ---'
+        # fix_print_with_import
+        print('--- tests completed ---')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
 # Copyright (c) 2014 Tellybug, Matt Millar
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py	(original)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2014 Netflix, Inc. Stefan Praszalowicz
 # Copyright (c) 2014 42Lines, Inc. Jim Browne
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2011 Blue Pines Technologies LLC, Brad Carleton
 # www.bluepines.org
 # Copyright (c) 2012 42 Lines Inc., Jim Browne
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py	(refactored)
@@ -25,6 +25,7 @@
 the interfaces defined in the real boto classes, but don't handle most
 of the optional params (which we indicate with the constant "NOT_IMPL").
 """
+from builtins import object
 
 import copy
 import boto
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py	(refactored)
@@ -23,6 +23,8 @@
 """
 Some unit tests for the S3Connection
 """
+from __future__ import print_function
+from builtins import next
 import unittest
 import time
 import os
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Some integration tests for S3 CORS
 """
+from builtins import zip
 
 import unittest
 import time
@@ -57,16 +58,16 @@
         for i, rule in enumerate(cfg):
             self.assertEqual(rule.id, self.cfg[i].id)
             self.assertEqual(rule.max_age_seconds, self.cfg[i].max_age_seconds)
-            methods = zip(rule.allowed_method, self.cfg[i].allowed_method)
+            methods = list(zip(rule.allowed_method, self.cfg[i].allowed_method))
             for v1, v2 in methods:
                 self.assertEqual(v1, v2)
-            origins = zip(rule.allowed_origin, self.cfg[i].allowed_origin)
+            origins = list(zip(rule.allowed_origin, self.cfg[i].allowed_origin))
             for v1, v2 in origins:
                 self.assertEqual(v1, v2)
-            headers = zip(rule.allowed_header, self.cfg[i].allowed_header)
+            headers = list(zip(rule.allowed_header, self.cfg[i].allowed_header))
             for v1, v2 in headers:
                 self.assertEqual(v1, v2)
-            headers = zip(rule.expose_header, self.cfg[i].expose_header)
+            headers = list(zip(rule.expose_header, self.cfg[i].expose_header))
             for v1, v2 in headers:
                 self.assertEqual(v1, v2)
         self.bucket.delete_cors()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Some unit tests for the S3 Encryption
 """
+from __future__ import print_function
 import unittest
 import time
 from boto.s3.connection import S3Connection
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py	(refactored)
@@ -24,6 +24,8 @@
 """
 Some unit tests for S3 MfaDelete with versioning
 """
+from builtins import input
+from builtins import range
 
 import unittest
 import time
@@ -49,8 +51,8 @@
 
     def test_mfadel(self):
         # Enable Versioning with MfaDelete
-        mfa_sn = raw_input('MFA S/N: ')
-        mfa_code = raw_input('MFA Code: ')
+        mfa_sn = input('MFA S/N: ')
+        mfa_code = input('MFA Code: ')
         self.bucket.configure_versioning(True, mfa_delete=True, mfa_token=(mfa_sn, mfa_code))
 
         # Check enabling mfa worked.
@@ -77,11 +79,11 @@
             pass
 
         # Now try delete again with the MFA token
-        mfa_code = raw_input('MFA Code: ')
+        mfa_code = input('MFA Code: ')
         self.bucket.delete_key('foobar', version_id=v1, mfa_token=(mfa_sn, mfa_code))
 
         # Next suspend versioning and disable MfaDelete on the bucket
-        mfa_code = raw_input('MFA Code: ')
+        mfa_code = input('MFA Code: ')
         self.bucket.configure_versioning(False, mfa_delete=False, mfa_token=(mfa_sn, mfa_code))
 
         # Lastly, check disabling mfa worked.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py	(refactored)
@@ -25,6 +25,7 @@
 """
 Some unit tests for the S3 MultiDelete
 """
+from builtins import range
 
 import unittest
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py	(refactored)
@@ -25,6 +25,7 @@
 """
 Some unit tests for the S3 MultiPartUpload
 """
+from builtins import next
 
 # Note:
 # Multipart uploads require at least one part. If you upload
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py	(refactored)
@@ -24,6 +24,9 @@
 Some multi-threading tests of boto in a greenlet environment.
 """
 from __future__ import print_function
+from builtins import str
+from builtins import range
+from builtins import object
 
 import boto
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Some unit tests for the S3 Versioning.
 """
+from builtins import next
 
 import unittest
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py	(refactored)
@@ -24,6 +24,7 @@
 """
 Some unit tests for the SDBConnectionRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/support/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1_workflow_execution.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py

 """
+from __future__ import print_function
 
 import unittest
 import time
@@ -62,7 +63,7 @@
 
         # try to get the attributes and see if they match
         item = domain.get_attributes(item_1, consistent_read=True)
-        assert len(item.keys()) == len(attrs_1.keys())
+        assert len(list(item.keys())) == len(list(attrs_1.keys()))
         assert item['name1'] == attrs_1['name1']
         assert item['name2'] == attrs_1['name2']
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.
 # All rights reserved.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py	(refactored)
@@ -24,6 +24,8 @@
 """
 Some unit tests for the SQSConnection
 """
+from __future__ import print_function
+from builtins import range
 import time
 from threading import Timer
 from tests.unit import unittest
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py	(refactored)
@@ -23,6 +23,7 @@
 """
 Tests for Session Tokens
 """
+from __future__ import print_function
 
 import unittest
 import os
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1_workflow_execution.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1_workflow_execution.py	(refactored)
@@ -2,6 +2,7 @@
 Tests for Layer1 of Simple Workflow
 
 """
+from builtins import str
 import time
 import uuid
 import json
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import absolute_import
+from past.builtins import execfile
 import os
 import functools
 
@@ -24,5 +26,5 @@
             #  they're set to.
             os.environ.setdefault('AWS_ACCESS_KEY_ID', 'foo')
             os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'bar')
-            from mocks import MTurkConnection
+            from .mocks import MTurkConnection
     SetHostMTurkConnection = functools.partial(MTurkConnection, host=mturk_host)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py	(refactored)
@@ -1,13 +1,14 @@
+from __future__ import absolute_import
 
 import unittest
 import doctest
 from glob import glob
 
-from create_hit_test import *
-from create_hit_with_qualifications import *
-from create_hit_external import *
-from create_hit_with_qualifications import *
-from hit_persistence import *
+from .create_hit_test import *
+from .create_hit_with_qualifications import *
+from .create_hit_external import *
+from .create_hit_with_qualifications import *
+from .hit_persistence import *
 
 doctest_suite = doctest.DocFileSuite(
 	*glob('*.doctest'),
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py	(refactored)
@@ -1,7 +1,11 @@
+from __future__ import print_function
+from __future__ import absolute_import
+from builtins import map
+from builtins import filter
 import itertools
 
-from _init_environment import SetHostMTurkConnection
-from _init_environment import config_environment
+from ._init_environment import SetHostMTurkConnection
+from ._init_environment import config_environment
 
 def description_filter(substring):
 	return lambda hit: substring in hit.Title
@@ -26,22 +30,25 @@
 
 
 	is_boto = description_filter('Boto')
-	print 'getting hits...'
+	# fix_print_with_import
+	print('getting hits...')
 	all_hits = list(conn.get_all_hits())
 	is_reviewable = lambda hit: hit.HITStatus == 'Reviewable'
 	is_not_reviewable = lambda hit: not is_reviewable(hit)
-	hits_to_process = filter(is_boto, all_hits)
-	hits_to_disable = filter(is_not_reviewable, hits_to_process)
-	hits_to_dispose = filter(is_reviewable, hits_to_process)
-	print 'disabling/disposing %d/%d hits' % (len(hits_to_disable), len(hits_to_dispose))
-	map(disable_hit, hits_to_disable)
-	map(dispose_hit, hits_to_dispose)
+	hits_to_process = list(filter(is_boto, all_hits))
+	hits_to_disable = list(filter(is_not_reviewable, hits_to_process))
+	hits_to_dispose = list(filter(is_reviewable, hits_to_process))
+	# fix_print_with_import
+	print('disabling/disposing %d/%d hits' % (len(hits_to_disable), len(hits_to_dispose)))
+	list(map(disable_hit, hits_to_disable))
+	list(map(dispose_hit, hits_to_dispose))
 
 	total_hits = len(all_hits)
 	hits_processed = len(hits_to_process)
 	skipped = total_hits - hits_processed
 	fmt = 'Processed: %(total_hits)d HITs, disabled/disposed: %(hits_processed)d, skipped: %(skipped)d'
-	print fmt % vars()
+	# fix_print_with_import
+	print(fmt % vars())
 
 if __name__ == '__main__':
 	cleanup()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import absolute_import
+from builtins import str
 import unittest
 import uuid
 import datetime
@@ -5,7 +7,7 @@
 from boto.mturk.question import (
         Question, QuestionContent, AnswerSpecification, FreeTextAnswer,
 )
-from _init_environment import SetHostMTurkConnection, config_environment
+from ._init_environment import SetHostMTurkConnection, config_environment
 
 class MTurkCommon(unittest.TestCase):
         def setUp(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py	(refactored)
@@ -1,9 +1,10 @@
+from __future__ import absolute_import
 import unittest
 import uuid
 import datetime
 from boto.mturk.question import ExternalQuestion
 
-from _init_environment import SetHostMTurkConnection, external_url, \
+from ._init_environment import SetHostMTurkConnection, external_url, \
         config_environment
 
 class Test(unittest.TestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py	(refactored)
@@ -1,8 +1,9 @@
+from __future__ import absolute_import
 import unittest
 import os
 from boto.mturk.question import QuestionForm
 
-from common import MTurkCommon
+from .common import MTurkCommon
 
 class TestHITCreation(MTurkCommon):
 	def testCallCreateHitWithOneQuestion(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py	(refactored)
@@ -1,3 +1,4 @@
+from __future__ import print_function
 from boto.mturk.connection import MTurkConnection
 from boto.mturk.question import ExternalQuestion
 from boto.mturk.qualification import Qualifications, PercentAssignmentsApprovedRequirement
@@ -10,7 +11,8 @@
     qualifications.add(PercentAssignmentsApprovedRequirement(comparator="GreaterThan", integer_value="95"))
     create_hit_rs = conn.create_hit(question=q, lifetime=60*65, max_assignments=2, title="Boto External Question Test", keywords=keywords, reward = 0.05, duration=60*6, approval_delay=60*60, annotation='An annotation from boto external question test', qualifications=qualifications)
     assert(create_hit_rs.status == True)
-    print create_hit_rs.HITTypeId
+    # fix_print_with_import
+    print(create_hit_rs.HITTypeId)
 
 if __name__ == "__main__":
     test()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py	(refactored)
@@ -1,7 +1,8 @@
+from __future__ import absolute_import
 import unittest
 import pickle
 
-from common import MTurkCommon
+from .common import MTurkCommon
 
 class TestHITPersistence(MTurkCommon):
 	def create_hit_result(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py	(refactored)
@@ -1,4 +1,6 @@
 from __future__ import absolute_import
+from builtins import str
+from builtins import object
 from boto.mturk.test.support import unittest
 
 sel_args = ('localhost', 4444, '*chrome', 'https://workersandbox.mturk.com')
@@ -6,7 +8,7 @@
 class SeleniumFailed(object):
 	def __init__(self, message):
 		self.message = message
-	def __nonzero__(self):
+	def __bool__(self):
 		return False
 
 def has_selenium():
@@ -17,7 +19,7 @@
 		# a little trick to see if the server is responding
 		try:
 			sel.do_command('shutdown', '')
-		except Exception, e:
+		except Exception as e:
 			if not 'Server Exception' in str(e):
 				raise
 		result = True
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py	(refactored)
@@ -1,6 +1,7 @@
+from __future__ import absolute_import
 from tests.mturk.support import unittest
 
-from common import MTurkCommon
+from .common import MTurkCommon
 from boto.mturk.connection import MTurkRequestError
 
 class TestDisableHITs(MTurkCommon):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright (c) 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # Copyright (c) 2014 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import range
 #!/usr/bin/env python
 import random
 import string
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py	(refactored)
@@ -191,16 +191,16 @@
         policy = self.dist._canned_policy(url, expires)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]
-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(1, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(1, len(list(condition.keys())))
         date_less_than = condition["DateLessThan"]
-        self.assertEqual(1, len(date_less_than.keys()))
+        self.assertEqual(1, len(list(date_less_than.keys())))
         aws_epoch_time = date_less_than["AWS:EpochTime"]
         self.assertEqual(expires, aws_epoch_time)
         
@@ -214,16 +214,16 @@
         policy = self.dist._custom_policy(url, expires=expires)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]
-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(1, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(1, len(list(condition.keys())))
         date_less_than = condition["DateLessThan"]
-        self.assertEqual(1, len(date_less_than.keys()))
+        self.assertEqual(1, len(list(date_less_than.keys())))
         aws_epoch_time = date_less_than["AWS:EpochTime"]
         self.assertEqual(expires, aws_epoch_time)
 
@@ -237,17 +237,17 @@
         policy = self.dist._custom_policy(url, valid_after=valid_after)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py

-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(2, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(2, len(list(condition.keys())))
         date_less_than = condition["DateLessThan"]
         date_greater_than = condition["DateGreaterThan"]
-        self.assertEqual(1, len(date_greater_than.keys()))
+        self.assertEqual(1, len(list(date_greater_than.keys())))
         aws_epoch_time = date_greater_than["AWS:EpochTime"]
         self.assertEqual(valid_after, aws_epoch_time)
 
@@ -261,17 +261,17 @@
         policy = self.dist._custom_policy(url, ip_address=ip_range)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]
-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(2, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(2, len(list(condition.keys())))
         ip_address = condition["IpAddress"]
         self.assertTrue("DateLessThan" in condition)
-        self.assertEqual(1, len(ip_address.keys()))
+        self.assertEqual(1, len(list(ip_address.keys())))
         source_ip = ip_address["AWS:SourceIp"]
         self.assertEqual("%s/32" % ip_range, source_ip)
 
@@ -285,17 +285,17 @@
         policy = self.dist._custom_policy(url, ip_address=ip_range)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]
-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(2, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(2, len(list(condition.keys())))
         self.assertTrue("DateLessThan" in condition)
         ip_address = condition["IpAddress"]
-        self.assertEqual(1, len(ip_address.keys()))
+        self.assertEqual(1, len(list(ip_address.keys())))
         source_ip = ip_address["AWS:SourceIp"]
         self.assertEqual(ip_range, source_ip)
 
@@ -313,27 +313,27 @@
                                           ip_address=ip_range)
         policy = json.loads(policy)
 
-        self.assertEqual(1, len(policy.keys()))
-        statements = policy["Statement"]
-        self.assertEqual(1, len(statements))
-        statement = statements[0]
-        resource = statement["Resource"]
-        self.assertEqual(url, resource)
-        condition = statement["Condition"]
-        self.assertEqual(3, len(condition.keys()))
+        self.assertEqual(1, len(list(policy.keys())))
+        statements = policy["Statement"]
+        self.assertEqual(1, len(statements))
+        statement = statements[0]
+        resource = statement["Resource"]
+        self.assertEqual(url, resource)
+        condition = statement["Condition"]
+        self.assertEqual(3, len(list(condition.keys())))
         #check expires condition
         date_less_than = condition["DateLessThan"]
-        self.assertEqual(1, len(date_less_than.keys()))
+        self.assertEqual(1, len(list(date_less_than.keys())))
         aws_epoch_time = date_less_than["AWS:EpochTime"]
         self.assertEqual(expires, aws_epoch_time)
         #check valid_after condition
         date_greater_than = condition["DateGreaterThan"]
-        self.assertEqual(1, len(date_greater_than.keys()))
+        self.assertEqual(1, len(list(date_greater_than.keys())))
         aws_epoch_time = date_greater_than["AWS:EpochTime"]
         self.assertEqual(valid_after, aws_epoch_time)
         #check source ip address condition
         ip_address = condition["IpAddress"]
-        self.assertEqual(1, len(ip_address.keys()))
+        self.assertEqual(1, len(list(ip_address.keys())))
         source_ip = ip_address["AWS:SourceIp"]
         self.assertEqual(ip_range, source_ip)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py	(refactored)
@@ -128,7 +128,7 @@
         """Check that multiple documents are added correctly to AWS"""
         document = DocumentServiceConnection(
             endpoint="doc-demo-userdomain.us-east-1.cloudsearch.amazonaws.com")
-        for (key, obj) in self.objs.items():
+        for (key, obj) in list(self.objs.items()):
             document.add(key, obj['version'], obj['fields'])
         document.commit()
 
@@ -151,7 +151,7 @@
         """
         document = DocumentServiceConnection(
             endpoint="doc-demo-userdomain.us-east-1.cloudsearch.amazonaws.com")
-        for (key, obj) in self.objs.items():
+        for (key, obj) in list(self.objs.items()):
             document.add(key, obj['version'], obj['fields'])
         doc = document.commit()
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py	(refactored)
@@ -1,3 +1,6 @@
+from builtins import str
+from builtins import next
+from builtins import object
 #!/usr/bin env python
 
 from tests.compat import mock, unittest
@@ -295,7 +298,7 @@
 
         results = search.search(q='Test')
 
-        hits = list(map(lambda x: x['id'], results.docs))
+        hits = list([x['id'] for x in results.docs])
 
         # This relies on the default response which is fed into HTTPretty
         self.assertEqual(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py	(refactored)
@@ -145,7 +145,7 @@
         """Check that multiple documents are added correctly to AWS"""
         document = DocumentServiceConnection(
             endpoint="doc-demo-userdomain.us-east-1.cloudsearch.amazonaws.com")
-        for (key, obj) in self.objs.items():
+        for (key, obj) in list(self.objs.items()):
             document.add(key, obj['fields'])
         document.commit()
 
@@ -167,7 +167,7 @@
         """
         document = DocumentServiceConnection(
             endpoint="doc-demo-userdomain.us-east-1.cloudsearch.amazonaws.com")
-        for (key, obj) in self.objs.items():
+        for (key, obj) in list(self.objs.items()):
             document.add(key, obj['fields'])
         doc = document.commit()
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearchdomain/test_cloudsearchdomain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudtrail/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/directconnect/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_address.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_blockdevicemapping.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancestatus.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancetype.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_securitygroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_snapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_spotinstance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/autoscale/test_group.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_listener.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_loadbalancer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ecs/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_job.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_utils.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kinesis/test_kinesis.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/logs/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/manage/test_ssh.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mturk/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py

@@ -1,3 +1,7 @@
+from __future__ import print_function
+from builtins import str
+from builtins import next
+from builtins import object
 #!/usr/bin env python
 from boto.cloudsearch2.domain import Domain
 from boto.cloudsearch2.layer1 import CloudSearchConnection
@@ -241,7 +245,7 @@
 
         results = search.search(q='Test')
 
-        hits = list(map(lambda x: x['id'], results.docs))
+        hits = list([x['id'] for x in results.docs])
 
         # This relies on the default response which is fed into HTTPretty
         self.assertEqual(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import bytes
 #!/usr/bin/env python
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py	(refactored)
@@ -1,3 +1,6 @@
+from builtins import next
+from builtins import str
+from builtins import range
 from tests.compat import mock, unittest
 from boto.dynamodb2 import exceptions
 from boto.dynamodb2.fields import (HashKey, RangeKey,
@@ -371,14 +374,14 @@
     # ordering everywhere & no erroneous failures.
 
     def test_keys(self):
-        self.assertCountEqual(self.johndoe.keys(), [
+        self.assertCountEqual(list(self.johndoe.keys()), [
             'date_joined',
             'first_name',
             'username',
         ])
 
     def test_values(self):
-        self.assertCountEqual(self.johndoe.values(),
+        self.assertCountEqual(list(self.johndoe.values()),
                               [12345, 'John', 'johndoe'])
 
     def test_contains(self):
@@ -403,7 +406,7 @@
 
     def test_items(self):
         self.assertCountEqual(
-            self.johndoe.items(),
+            list(self.johndoe.items()),
             [
                 ('date_joined', 12345),
                 ('first_name', 'John'),
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py	(refactored)
@@ -1,5 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
 #!/usr/bin/env python
-import httplib
+import http.client
 
 from datetime import datetime, timedelta
 from mock import MagicMock, Mock
@@ -942,12 +944,12 @@
 
 class TestConnectToRegion(unittest.TestCase):
     def setUp(self):
-        self.https_connection = Mock(spec=httplib.HTTPSConnection)
+        self.https_connection = Mock(spec=http.client.HTTPSConnection)
         self.https_connection_factory = (
             Mock(return_value=self.https_connection), ())
 
     def test_aws_region(self):
-        region = boto.ec2.RegionData.keys()[0]
+        region = list(boto.ec2.RegionData.keys())[0]
         self.ec2 = boto.ec2.connect_to_region(
             region,
             https_connection_factory=self.https_connection_factory,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py	(refactored)
@@ -344,7 +344,7 @@
         return rs
 
     def _assert_fields(self, response, **fields):
-        for field, expected in fields.items():
+        for field, expected in list(fields.items()):
             actual = getattr(response, field)
             self.assertEquals(expected, actual,
                               "Field %s: %r != %r" % (field, expected, actual))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py	(refactored)
@@ -1,3 +1,7 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
 #!/usr/bin/env python
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 #!/usr/bin/env python
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import zip
+from builtins import str
 #!/usr/bin/env python
 # Copyright (c) 2012 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
@@ -104,7 +106,7 @@
             self.assertEqual(result, amazon)
 
     def test_decorator_order(self):
-        for action, func in api_call_map.items():
+        for action, func in list(api_call_map.items()):
             func = getattr(self.service_connection, func)
             decs = [func.__name__]
             while func:
@@ -126,7 +128,7 @@
         # It starts empty, but the decorators should add to it as they're
         # applied. As of 2013/10/21, there were 52 calls (with more likely
         # to be added), so let's simply ensure there are enough there.
-        self.assertTrue(len(api_call_map.keys()) > 50)
+        self.assertTrue(len(list(api_call_map.keys())) > 50)
 
     def test_method_for(self):
         # First, ensure that the map is in "right enough" state.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py	(refactored)
@@ -1,3 +1,6 @@
+from builtins import filter
+from builtins import map
+from builtins import range
 #!/usr/bin/env python
 from boto.mws.connection import MWSConnection
 from boto.mws.response import (ResponseFactory, ResponseElement, Element,
@@ -34,10 +37,10 @@
         obj = self.check_issue(Test9Result, text)
         Item = obj._result.Item
         useful = lambda x: not x[0].startswith('_')
-        nest = dict(filter(useful, Item.Nest.__dict__.items()))
+        nest = dict(list(filter(useful, list(Item.Nest.__dict__.items()))))
         self.assertEqual(nest, dict(Zip='Zap', Zam='Zoo'))
         useful = lambda x: not x[0].startswith('_') and not x[0] == 'Nest'
-        item = dict(filter(useful, Item.__dict__.items()))
+        item = dict(list(filter(useful, list(Item.__dict__.items()))))
         self.assertEqual(item, dict(Foo='Bar', Bif='Bam', Zoom=None))
 
     def test_parsing_member_list_specification(self):
@@ -67,7 +70,7 @@
             list(range(4)),
         )
         self.assertSequenceEqual(
-            list(map(lambda x: list(map(int, x.Foo)), obj._result.Extra)),
+            list([list(map(int, x.Foo)) for x in obj._result.Extra]),
             [[4, 5], [], [6, 7]],
         )
 
@@ -121,7 +124,7 @@
         obj = self.check_issue(Test7Result, text)
         item = obj._result.Item
         self.assertEqual(len(item), 3)
-        nests = [z.Nest for z in filter(lambda x: x.Nest, item)]
+        nests = [z.Nest for z in [x for x in item if x.Nest]]RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/provider/test_provider.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_snapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds2/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_zone.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_bucket.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_lifecycle.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_tagging.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_uri.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ses/test_identity.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_actors.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_customergateway.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_dhcpoptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_internetgateway.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_networkacl.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_routetable.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_subnet.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc_peering_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpnconnection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpngateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/filechunkio.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py

         self.assertSequenceEqual(
             [[y.Data for y in nest] for nest in nests],
             [[u'2', u'4', u'6'], [u'1', u'3', u'5']],
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py	(refactored)
@@ -1,3 +1,5 @@
+from __future__ import print_function
+from builtins import str
 #!/usr/bin/env python
 # Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py	(refactored)
@@ -21,6 +21,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 #
+from __future__ import print_function
 from tests.compat import mock, unittest
 from tests.unit import AWSMockServiceTestCase
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 # Copyright 2013 Google Inc.
 # Copyright 2011, Nexenta Systems Inc.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py	(refactored)
@@ -112,7 +112,7 @@
 
         self.service_connection.get_queue('my_queue', '599169622985')
 
-        assert 'QueueOwnerAWSAccountId' in self.actual_request.params.keys()
+        assert 'QueueOwnerAWSAccountId' in list(self.actual_request.params.keys())
         self.assertEquals(self.actual_request.params['QueueOwnerAWSAccountId'], '599169622985')
 
 class SQSProfileName(MockServiceWithConfigTestCase):
@@ -192,7 +192,7 @@
                          '324758f82d026ac6ec5b31a3b192d1e3')
 
         mattributes = message.message_attributes
-        self.assertEqual(len(mattributes.keys()), 2)
+        self.assertEqual(len(list(mattributes.keys())), 2)
         self.assertEqual(mattributes['Count']['data_type'], 'Number')
         self.assertEqual(mattributes['Foo']['string_value'], 'Bar')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 # Copyright (c) 2010 Robert Mela
 #
 # Permission is hereby granted, free of charge, to any person obtaining a
@@ -261,7 +263,7 @@
         self.set_normal_response([key_data, invalid_data, invalid_data])
         response = LazyLoadMetadata(url, num_retries)
         with self.assertRaises(ValueError):
-            response.values()[0]
+            list(response.values())[0]
 
     def test_user_data(self):
         self.set_normal_response(['foo'])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py	(refactored)
@@ -6,7 +6,7 @@
 
 PY3 = sys.version_info[0] == 3
 
-_unicode = str if PY3 else unicode
+_unicode = str if PY3 else str
 
 setup(
     name="filechunkio",
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py	(refactored)
@@ -1,11 +1,13 @@
+from __future__ import absolute_import
+from builtins import next
 import io
 import os
 import tempfile
 import unittest
 
-from filechunkio import FileChunkIO
-from filechunkio import SEEK_CUR
-from filechunkio import SEEK_END
+from .filechunkio import FileChunkIO
+from .filechunkio import SEEK_CUR
+from .filechunkio import SEEK_END
 
 
 class FileChunkIOTest(unittest.TestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py	(refactored)
@@ -1,6 +1,9 @@
 """
 Compatibility...
 """
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
 
 import sys
 
@@ -9,7 +12,7 @@
 if py3k: # pragma: no cover
     string_compare = str
 else: # pragma: no cover
-    string_compare = (str, unicode)
+    string_compare = (str, str)
 
 # Unicode compatibility, borrowed from 'six'
 if py3k: # pragma: no cover
@@ -23,7 +26,7 @@
         """
         Convert to Unicode with unicode escaping
         """
-        return unicode(s.replace(r'\\', r'\\\\'), 'unicode_escape')
+        return str(s.replace(r'\\', r'\\\\'), 'unicode_escape')
 
 if py3k: # pragma: no cover
     from urllib.parse import urlencode, quote # pylint: disable=W0611,F0401,W0611,E0611
@@ -40,17 +43,17 @@
         renaming between Python 2 and 3 versions
         For Python2
         """
-        return iter(d.values())
+        return iter(list(d.values()))
     def iteritems(d):
         """
         Function for iterating on items due to methods
         renaming between Python 2 and 3 versions
         For Python2
         """
-        return iter(d.items())
+        return iter(list(d.items()))
 
 else: # pragma: no cover
-    from urllib import urlencode as original_urlencode, quote # pylint: disable=W0611,F0401,W0611,E0611
+    from urllib.parse import urlencode as original_urlencode, quote # pylint: disable=W0611,F0401,W0611,E0611
     from urllib2 import (Request, HTTPError,   # pylint: disable=W0611,F0401,W0611,E0611
                          ProxyHandler, URLError, urlopen,
                          build_opener, install_opener,
@@ -61,7 +64,7 @@
         """
         Python2-only, ensures that a string is encoding to a str.
         """
-        if isinstance(str_or_unicode, unicode):
+        if isinstance(str_or_unicode, str):
             return str_or_unicode.encode('utf-8')
         else:
             return str_or_unicode
@@ -75,7 +78,7 @@
         Based on the urlencode from django.utils.http
         """
         if hasattr(query, 'items'):
-            query = query.items()
+            query = list(query.items())
         return original_urlencode(
             [(force_str(k),
               [force_str(i) for i in v]
@@ -89,11 +92,11 @@
         renaming between Python 2 and 3 versions
         For Python3
         """
-        return d.itervalues()
+        return iter(d.values())
     def iteritems(d):
         """
         Function for iterating on items due to methods
         renaming between Python 2 and 3 versions
         For Python3
         """
-        return d.iteritems()
+        return iter(d.items())
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py	(refactored)
@@ -70,6 +70,8 @@
 
 """
 from __future__ import division
+from past.builtins import cmp
+from builtins import object
 
 from math import atan, tan, sin, cos, pi, sqrt, atan2, asin
 from geopy.units import radians
@@ -145,7 +147,7 @@
     def __abs__(self):
         return self.__class__(abs(self.kilometers))
 
-    def __nonzero__(self):
+    def __bool__(self):
         return bool(self.kilometers)
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/location.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/units.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/util.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/arcgis.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/baidu.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/base.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/databc.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/dot_us.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geocodefarm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geonames.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/googlev3.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/ignfrance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/navidata.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/opencage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/openmapquest.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py
 
     __bool__ = __nonzero__
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py	(refactored)
@@ -1,17 +1,19 @@
 """
 Formatting...
 """
+from builtins import chr
+from builtins import zip
 
 from geopy import units
 from geopy.compat import py3k
 
 if py3k:
-    unichr = chr # pylint: disable=W0622
+    chr = chr # pylint: disable=W0622
 
 # Unicode characters for symbols that appear in coordinate strings.
-DEGREE = unichr(176)
-PRIME = unichr(8242)
-DOUBLE_PRIME = unichr(8243)
+DEGREE = chr(176)
+PRIME = chr(8242)
+DOUBLE_PRIME = chr(8243)
 ASCII_DEGREE = ''
 ASCII_PRIME = "'"
 ASCII_DOUBLE_PRIME = '"'
@@ -113,7 +115,7 @@
     ('southeast by south', 'SEbS'),
 ]
 
-DIRECTIONS, DIRECTIONS_ABBR = zip(*_DIRECTIONS)
+DIRECTIONS, DIRECTIONS_ABBR = list(zip(*_DIRECTIONS))
 ANGLE_DIRECTIONS = {
     n * 11.25: d
     for n, d
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/location.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/location.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.Location` returns geocoder results.
 """
+from builtins import object
 
 from geopy.point import Point
 from geopy.compat import string_compare, py3k
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py	(refactored)
@@ -2,6 +2,8 @@
 """
 :class:`.Point` data structure.
 """
+from builtins import str
+from builtins import object
 
 import re
 from itertools import islice
@@ -263,7 +265,7 @@
             except KeyError: # pragma: no cover
                 raise NotImplementedError(
                     'Bad distance unit specified, valid are: %r' %
-                    CONVERTERS.keys()
+                    list(CONVERTERS.keys())
                 )
         else:
             return distance
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/util.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/util.py	(refactored)
@@ -1,12 +1,14 @@
 """
 Utils.
 """
+from builtins import str
+from builtins import range
 
 import logging
 from geopy.compat import py3k
 
 if not py3k: # pragma: no cover
-    NUMBER_TYPES = (int, long, float)
+    NUMBER_TYPES = (int, int, float)
 else: # pragma: no cover
     NUMBER_TYPES = (int, float) # long -> int in Py3k
 try:
@@ -44,7 +46,7 @@
         """
         Join with a filter.
         """
-        return sep.join([unicode(i) for i in seq if pred(i)])
+        return sep.join([str(i) for i in seq if pred(i)])
 else:
     def join_filter(sep, seq, pred=bool):
         """
@@ -64,10 +66,10 @@
         if hasattr(page, 'read'): # urllib
             # note getparam in py2
             encoding = page.headers.getparam("charset") or "utf-8"
-            return unicode(page.read(), encoding=encoding)
+            return str(page.read(), encoding=encoding)
         else: # requests?
             encoding = page.headers.get("charset", "utf-8")
-            return unicode(page.content, encoding=encoding)
+            return str(page.content, encoding=encoding)
 else:
     def decode_page(page):
         """
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/__init__.py	(refactored)
@@ -158,6 +158,6 @@
     except KeyError:
         raise GeocoderNotFound(
             "Unknown geocoder '%s'; options are: %s" %
-            (service, SERVICE_TO_GEOCODER.keys())
+            (service, list(SERVICE_TO_GEOCODER.keys()))
         )
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/arcgis.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/arcgis.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.ArcGIS` geocoder.
 """
+from builtins import str
 
 import json
 from time import time
@@ -227,7 +228,7 @@
         token_request_arguments = "&".join([
             "%s=%s" % (key, val)
             for key, val
-            in token_request_arguments.items()
+            in list(token_request_arguments.items())
         ])
         url = "&".join((
             "?".join((self.auth_api, token_request_arguments)),
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/baidu.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/baidu.py	(refactored)
@@ -63,7 +63,7 @@
         """
         return "|".join(
             (":".join(item)
-             for item in components.items()
+             for item in list(components.items())
             )
         )
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/base.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/base.py	(refactored)
@@ -1,6 +1,8 @@
 """
 :class:`.GeoCoder` base object from which other geocoders are templated.
 """
+from builtins import str
+from builtins import object
 
 from ssl import SSLError
 from socket import timeout as SocketTimeout
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.Bing` geocoder.
 """
+from builtins import str
 
 from geopy.compat import urlencode
 from geopy.geocoders.base import Geocoder, DEFAULT_FORMAT_STRING, \
@@ -131,7 +132,7 @@
             params = {
                 key: val
                 for key, val
-                in query.items()
+                in list(query.items())
                 if key in self.structured_query_params
             }
             params['key'] = self.api_key
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/googlev3.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/googlev3.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.GoogleV3` is the Google Maps V3 geocoder.
 """
+from builtins import str
 
 import base64
 import hashlib
@@ -134,7 +135,7 @@
         """
         return "|".join(
             (":".join(item)
-             for item in components.items()
+             for item in list(components.items())
             )
         )
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/navidata.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/navidata.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.NaviData` is the NaviData.pl geocoder.
 """
+from builtins import str
 
 from geopy.compat import urlencode
 from geopy.location import Location
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py	(refactored)
@@ -148,7 +148,7 @@
             params = {
                 key: val
                 for key, val
-                in query.items()RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/photon.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/smartystreets.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/what3words.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/yandex.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/setup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/test_requests.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py

+                in list(query.items())
                 if key in self.structured_query_params
             }
         else:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py	(refactored)
@@ -1,6 +1,7 @@
 """
 :class:`.YahooPlaceFinder` geocoder.
 """
+from builtins import str
 
 from functools import partial
 
@@ -60,12 +61,12 @@
             timeout=timeout, proxies=proxies, user_agent=user_agent
         )
         self.consumer_key = (
-            unicode(consumer_key)
+            str(consumer_key)
             if not py3k
             else str(consumer_key)
         )
         self.consumer_secret = (
-            unicode(consumer_secret)
+            str(consumer_secret)
             if not py3k
             else str(consumer_secret)
         )
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/test_requests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/test_requests.py	(refactored)
@@ -4,6 +4,11 @@
 """Tests for Requests."""
 
 from __future__ import division
+from future import standard_library
+standard_library.install_aliases()
+from builtins import next
+from builtins import str
+from builtins import object
 import json
 import os
 import pickle
@@ -28,7 +33,7 @@
 from requests.hooks import default_hooks
 
 try:
-    import StringIO
+    import io
 except ImportError:
     import io as StringIO
 
@@ -666,8 +671,8 @@
         jar.set(key1, value1)
 
         d1 = dict(jar)
-        d2 = dict(jar.iteritems())
-        d3 = dict(jar.items())
+        d2 = dict(iter(jar.items()))
+        d3 = dict(list(jar.items()))
 
         assert len(jar) == 2
         assert len(d1) == 2
@@ -686,8 +691,8 @@
         jar.set(key1, value1)
 
         d1 = dict(jar)
-        d2 = dict(jar.iteritems())
-        d3 = dict(jar.items())
+        d2 = dict(iter(jar.items()))
+        d3 = dict(list(jar.items()))
 
         assert d1['some_cookie'] == 'some_value'
         assert d2['some_cookie'] == 'some_value'
@@ -704,7 +709,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        keys = jar.keys()
+        keys = list(jar.keys())
         assert keys == list(keys)
         # make sure one can use keys multiple times
         assert list(keys) == list(keys)
@@ -720,7 +725,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        values = jar.values()
+        values = list(jar.values())
         assert values == list(values)
         # make sure one can use values multiple times
         assert list(values) == list(values)
@@ -736,7 +741,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        items = jar.items()
+        items = list(jar.items())
         assert items == list(items)
         # make sure one can use items multiple times
         assert list(items) == list(items)
@@ -750,7 +755,7 @@
 
     def test_response_is_iterable(self):
         r = requests.Response()
-        io = StringIO.StringIO('abc')
+        io = io.StringIO('abc')
         read_ = io.read
 
         def read_mock(amt, decode_content=None):
@@ -924,8 +929,8 @@
 
         # This is testing that they are builtin strings. A bit weird, but there
         # we go.
-        assert 'unicode' in p.headers.keys()
-        assert 'byte' in p.headers.keys()
+        assert 'unicode' in list(p.headers.keys())
+        assert 'byte' in list(p.headers.keys())
 
     def test_can_send_nonstring_objects_with_files(self):
         data = {'a': 0.0}
@@ -1235,8 +1240,8 @@
             'user-Agent': 'requests',
         })
         keyset = frozenset(['Accept', 'user-Agent'])
-        assert frozenset(i[0] for i in cid.items()) == keyset
-        assert frozenset(cid.keys()) == keyset
+        assert frozenset(i[0] for i in list(cid.items())) == keyset
+        assert frozenset(list(cid.keys())) == keyset
         assert frozenset(cid) == keyset
 
     def test_preserve_last_key_case(self):
@@ -1247,8 +1252,8 @@
         cid.update({'ACCEPT': 'application/json'})
         cid['USER-AGENT'] = 'requests'
         keyset = frozenset(['ACCEPT', 'USER-AGENT'])
-        assert frozenset(i[0] for i in cid.items()) == keyset
-        assert frozenset(cid.keys()) == keyset
+        assert frozenset(i[0] for i in list(cid.items())) == keyset
+        assert frozenset(list(cid.keys())) == keyset
         assert frozenset(cid) == keyset
 
 
@@ -1260,21 +1265,21 @@
         from io import BytesIO
         from requests.utils import super_len
 
-        assert super_len(StringIO.StringIO()) == 0
+        assert super_len(io.StringIO()) == 0
         assert super_len(
-            StringIO.StringIO('with so much drama in the LBC')) == 29
+            io.StringIO('with so much drama in the LBC')) == 29
 
         assert super_len(BytesIO()) == 0
         assert super_len(
             BytesIO(b"it's kinda hard bein' snoop d-o-double-g")) == 40
 
         try:
-            import cStringIO
+            import io
         except ImportError:
             pass
         else:
             assert super_len(
-                cStringIO.StringIO('but some how, some way...')) == 25
+                io.StringIO('but some how, some way...')) == 25
 
     def test_get_environ_proxies_ip_ranges(self):
         """Ensures that IP addresses are correctly matches with ranges
@@ -1434,7 +1439,7 @@
             morsel_to_cookie(morsel)
 
 
-class TestTimeout:
+class TestTimeout(object):
     def test_stream_timeout(self):
         try:
             requests.get(httpbin('delay/10'), timeout=2.0)
@@ -1520,12 +1525,12 @@
         return r
 
     def _build_raw(self):
-        string = StringIO.StringIO('')
+        string = io.StringIO('')
         setattr(string, 'release_conn', lambda *args: args)
         return string
 
 
-class TestRedirects:
+class TestRedirects(object):
     default_keyword_args = {
         'stream': False,
         'verify': True,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py	(refactored)
@@ -7,6 +7,8 @@
 This module contains the transport adapters that Requests uses to define
 and maintain connections.
 """
+from builtins import hex
+from builtins import object
 
 import socket
 
@@ -15,7 +17,7 @@
 from .packages.urllib3.response import HTTPResponse
 from .packages.urllib3.util import Timeout as TimeoutSauce
 from .packages.urllib3.util.retry import Retry
-from .compat import urlparse, basestring
+from .compat import urlparse, str
 from .utils import (DEFAULT_CA_BUNDLE_PATH, get_encoding_from_headers,
                     prepend_scheme_if_needed, get_auth_from_url, urldefragauth)
 from .structures import CaseInsensitiveDict
@@ -107,7 +109,7 @@
         self.proxy_manager = {}
         self.config = {}
 
-        for attr, value in state.items():
+        for attr, value in list(state.items()):
             setattr(self, attr, value)
 
         self.init_poolmanager(self._pool_connections, self._pool_maxsize,
@@ -187,7 +189,7 @@
             conn.ca_certs = None
 
         if cert:
-            if not isinstance(cert, basestring):
+            if not isinstance(cert, str):
                 conn.cert_file = cert[0]
                 conn.key_file = cert[1]
             else:
@@ -382,7 +384,7 @@
                                         url,
                                         skip_accept_encoding=True)
 
-                    for header, value in request.headers.items():
+                    for header, value in list(request.headers.items()):
                         low_conn.putheader(header, value)
 
                     low_conn.endheaders()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py	(refactored)
@@ -6,6 +6,8 @@
 
 This module contains the authentication handlers for Requests.
 """
+from builtins import str
+from builtins import object
 
 import os
 import re
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py	(refactored)
@@ -11,6 +11,7 @@
 environment, you can change the definition of where() to return a separately
 packaged CA bundle.
 """
+from __future__ import print_function
 import os.path
 
 try:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py	(refactored)
@@ -3,6 +3,8 @@
 """
 pythoncompat
 """
+from future import standard_library
+standard_library.install_aliases()
 
 from .packages import chardet
 
@@ -33,19 +35,19 @@
 # ---------
 
 if is_py2:
-    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode, getproxies, proxy_bypass
-    from urlparse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
+    from urllib.parse import quote, unquote, quote_plus, unquote_plus, urlencode
+    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
     from urllib2 import parse_http_list
-    import cookielib
-    from Cookie import Morsel
-    from StringIO import StringIO
+    import http.cookiejar
+    from http.cookies import Morsel
+    from io import StringIO
     from .packages.urllib3.packages.ordered_dict import OrderedDict
 
     builtin_str = str
     bytes = str
-    str = unicode
-    basestring = basestring
-    numeric_types = (int, long, float)
+    str = str
+    str = str
+    numeric_types = (int, int, float)
 
 elif is_py3:
     from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag
@@ -58,5 +60,5 @@
     builtin_str = str
     str = str
     bytes = bytes
-    basestring = (str, bytes)
+    str = (str, bytes)
     numeric_types = (int, float)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py	(refactored)
@@ -5,6 +5,9 @@
 
 requests.utils imports from here, so be careful with imports.
 """
+from future import standard_library
+standard_library.install_aliases()
+from builtins import object
 
 import copy
 import time
@@ -210,7 +213,7 @@
     def keys(self):
         """Dict-like keys() that returns a list of names of cookies from the
         jar. See values() and items()."""
-        return list(self.iterkeys())
+        return list(self.keys())
 
     def itervalues(self):
         """Dict-like itervalues() that returns an iterator of values of cookies
@@ -221,7 +224,7 @@
     def values(self):
         """Dict-like values() that returns a list of values of cookies from the
         jar. See keys() and items()."""
-        return list(self.itervalues())
+        return list(self.values())
 
     def iteritems(self):
         """Dict-like iteritems() that returns an iterator of name-value tuples
@@ -234,7 +237,7 @@
         jar. See keys() and values(). Allows client-code to call
         ``dict(RequestsCookieJar)`` and get a vanilla python dict of key value
         pairs."""
-        return list(self.iteritems())
+        return list(self.items())
 
     def list_domains(self):
         """Utility method to list all the domains in the jar."""
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py	(refactored)
@@ -6,6 +6,11 @@
 
 This module contains the primary objects that power Requests.
 """
+from future import standard_library
+standard_library.install_aliases()
+from builtins import bytes
+from builtins import str
+from builtins import object
 
 import collections
 import datetime
@@ -30,7 +35,7 @@
     iter_slices, guess_json_utf, super_len, to_native_string)
 from .compat import (
     cookielib, urlunparse, urlsplit, urlencode, str, bytes, StringIO,
-    is_py2, chardet, json, builtin_str, basestring)
+    is_py2, chardet, json, builtin_str, str)
 from .status_codes import codes
 
 #: The set of HTTP status codes that indicate an automatically
@@ -87,7 +92,7 @@
         elif hasattr(data, '__iter__'):
             result = []
             for k, vs in to_key_val_list(data):
-                if isinstance(vs, basestring) or not hasattr(vs, '__iter__'):
+                if isinstance(vs, str) or not hasattr(vs, '__iter__'):
                     vs = [vs]
                 for v in vs:
                     if v is not None:
@@ -109,7 +114,7 @@
         """
         if (not files):
             raise ValueError("Files must be provided.")
-        elif isinstance(data, basestring):
+        elif isinstance(data, str):
             raise ValueError("Data must not be a string.")
 
         new_fields = []
@@ -117,7 +122,7 @@
         files = to_key_val_list(files or {})
 
         for field, val in fields:
-            if isinstance(val, basestring) or not hasattr(val, '__iter__'):
+            if isinstance(val, str) or not hasattr(val, '__iter__'):
                 val = [val]
             for v in val:
                 if v is not None:
@@ -341,7 +346,7 @@
         if isinstance(url, bytes):
             url = url.decode('utf8')
         else:
-            url = unicode(url) if is_py2 else str(url)
+            url = str(url) if is_py2 else str(url)
 
         # Don't do any URL preparation for non-HTTP schemes like `mailto`,
         # `data` etc to work around exceptions from `url_parse`, which
@@ -408,7 +413,7 @@
         """Prepares the given HTTP headers."""
 
         if headers:
-            self.headers = CaseInsensitiveDict((to_native_string(name), value) for name, value in headers.items())
+            self.headers = CaseInsensitiveDict((to_native_string(name), value) for name, value in list(headers.items()))
         else:
             self.headers = CaseInsensitiveDict()
 
@@ -429,7 +434,7 @@
 
         is_stream = all([
             hasattr(data, '__iter__'),
-            not isinstance(data, (basestring, list, tuple, dict))
+            not isinstance(data, (str, list, tuple, dict))
         ])
 
         try:
@@ -454,7 +459,7 @@
             else:
                 if data and json is None:
                     body = self._encode_params(data)
-                    if isinstance(data, basestring) or hasattr(data, 'read'):
+                    if isinstance(data, str) or hasattr(data, 'read'):
                         content_type = None
                     else:
                         content_type = 'application/x-www-form-urlencoded'
@@ -609,7 +614,7 @@
         )
 
     def __setstate__(self, state):
-        for name, value in state.items():
+        for name, value in list(state.items()):
             setattr(self, name, value)
 
         # pickled objects do not have .raw
@@ -623,7 +628,7 @@
         """Returns true if :attr:`status_code` is 'OK'."""
         return self.ok
 
-    def __nonzero__(self):
+    def __bool__(self):
         """Returns true if :attr:`status_code` is 'OK'."""
         return self.ok
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py	(refactored)
@@ -8,6 +8,9 @@
 requests (cookies, auth, proxies).
 
 """
+from future import standard_library
+standard_library.install_aliases()RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/status_codes.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5freq.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetgroupprober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/constants.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escsm.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py

+from builtins import object
 import os
 from collections import Mapping
 from datetime import datetime
@@ -63,11 +66,11 @@
     merged_setting.update(to_key_val_list(request_setting))
 
     # Remove keys that are set to None.
-    for (k, v) in request_setting.items():
+    for (k, v) in list(request_setting.items()):
         if v is None:
             del merged_setting[k]
 
-    merged_setting = dict((k, v) for (k, v) in merged_setting.items() if v is not None)
+    merged_setting = dict((k, v) for (k, v) in list(merged_setting.items()) if v is not None)
 
     return merged_setting
 
@@ -612,7 +615,7 @@
         if self.trust_env:
             # Set environment's proxies.
             env_proxies = get_environ_proxies(url) or {}
-            for (k, v) in env_proxies.items():
+            for (k, v) in list(env_proxies.items()):
                 proxies.setdefault(k, v)
 
             # Look for requests environment configuration and be compatible
@@ -632,7 +635,7 @@
 
     def get_adapter(self, url):
         """Returns the appropriate connnection adapter for the given URL."""
-        for (prefix, adapter) in self.adapters.items():
+        for (prefix, adapter) in list(self.adapters.items()):
 
             if url.lower().startswith(prefix):
                 return adapter
@@ -642,7 +645,7 @@
 
     def close(self):
         """Closes all adapters and as such the session"""
-        for v in self.adapters.values():
+        for v in list(self.adapters.values()):
             v.close()
 
     def mount(self, prefix, adapter):
@@ -663,11 +666,11 @@
 
     def __setstate__(self, state):
         redirect_cache = state.pop('redirect_cache', {})
-        for attr, value in state.items():
+        for attr, value in list(state.items()):
             setattr(self, attr, value)
 
         self.redirect_cache = RecentlyUsedContainer(REDIRECT_CACHE_SIZE)
-        for redirect, to in redirect_cache.items():
+        for redirect, to in list(redirect_cache.items()):
             self.redirect_cache[redirect] = to
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py	(refactored)
@@ -7,6 +7,7 @@
 Data structures that power Requests.
 
 """
+from builtins import str
 
 import collections
 
@@ -57,7 +58,7 @@
         del self._store[key.lower()]
 
     def __iter__(self):
-        return (casedkey for casedkey, mappedvalue in self._store.values())
+        return (casedkey for casedkey, mappedvalue in list(self._store.values()))
 
     def __len__(self):
         return len(self._store)
@@ -67,7 +68,7 @@
         return (
             (lowerkey, keyval[1])
             for (lowerkey, keyval)
-            in self._store.items()
+            in list(self._store.items())
         )
 
     def __eq__(self, other):
@@ -80,10 +81,10 @@
 
     # Copy is required
     def copy(self):
-        return CaseInsensitiveDict(self._store.values())
+        return CaseInsensitiveDict(list(self._store.values()))
 
     def __repr__(self):
-        return str(dict(self.items()))
+        return str(dict(list(self.items())))
 
 class LookupDict(dict):
     """Dictionary lookup object."""
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py	(refactored)
@@ -8,6 +8,9 @@
 that are also useful for external consumption.
 
 """
+from builtins import str
+from builtins import chr
+from builtins import range
 
 import cgi
 import codecs
@@ -26,7 +29,7 @@
 from .compat import parse_http_list as _parse_list_header
 from .compat import (quote, urlparse, bytes, str, OrderedDict, unquote, is_py2,
                      builtin_str, getproxies, proxy_bypass, urlunparse,
-                     basestring)
+                     str)
 from .cookies import RequestsCookieJar, cookiejar_from_dict
 from .structures import CaseInsensitiveDict
 from .exceptions import InvalidURL
@@ -42,7 +45,7 @@
     """Returns an internal sequence dictionary update."""
 
     if hasattr(d, 'items'):
-        d = d.items()
+        d = list(d.items())
 
     return d
 
@@ -116,7 +119,7 @@
 def guess_filename(obj):
     """Tries to guess the filename of the given object."""
     name = getattr(obj, 'name', None)
-    if (name and isinstance(name, basestring) and name[0] != '<' and
+    if (name and isinstance(name, str) and name[0] != '<' and
             name[-1] != '>'):
         return os.path.basename(name)
 
@@ -164,7 +167,7 @@
         raise ValueError('cannot encode objects that are not 2-tuples')
 
     if isinstance(value, collections.Mapping):
-        value = value.items()
+        value = list(value.items())
 
     return list(value)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py	(refactored)
@@ -20,7 +20,7 @@
 
 
 def detect(aBuf):
-    if ((version_info < (3, 0) and isinstance(aBuf, unicode)) or
+    if ((version_info < (3, 0) and isinstance(aBuf, str)) or
             (version_info >= (3, 0) and not isinstance(aBuf, bytes))):
         raise ValueError('Expected a bytes object, not a unicode object')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is Mozilla Communicator client code.
 #
@@ -43,7 +44,7 @@
 MINIMUM_DATA_THRESHOLD = 3
 
 
-class CharDistributionAnalysis:
+class CharDistributionAnalysis(object):
     def __init__(self):
         # Mapping table to get frequency order from char order (get from
         # GetOrder())
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is Mozilla Universal charset detector code.
 #
@@ -30,7 +31,7 @@
 import re
 
 
-class CharSetProber:
+class CharSetProber(object):
     def __init__(self):
         pass
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is mozilla.org code.
 #
@@ -29,7 +30,7 @@
 from .compat import wrap_ord
 
 
-class CodingStateMachine:
+class CodingStateMachine(object):
     def __init__(self, sm):
         self._mModel = sm
         self._mCurrentBytePos = 0
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py	(refactored)
@@ -22,7 +22,7 @@
 
 
 if sys.version_info < (3, 0):
-    base_str = (str, unicode)
+    base_str = (str, str)
 else:
     base_str = (bytes, str)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py	(original)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrfreq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwfreq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312freq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/hebrewprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jisfreq.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jpcntx.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langbulgarianmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langcyrillicmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langgreekmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhebrewmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhungarianmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langthaimodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/latin1prober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcharsetprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcssm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sbcharsetprober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sjisprober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/universaldetector.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/utf8prober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is mozilla.org code.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jpcntx.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jpcntx.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is Mozilla Communicator client code.
 #
@@ -120,7 +121,7 @@
 (0,4,0,3,0,3,0,3,0,3,5,5,3,3,3,3,4,3,4,3,3,3,4,4,4,3,3,3,3,4,3,5,3,3,1,3,2,4,5,5,5,5,4,3,4,5,5,3,2,2,3,3,3,3,2,3,3,1,2,3,2,4,3,3,3,4,0,4,0,2,0,4,3,2,2,1,2,0,3,0,0,4,1),
 )
 
-class JapaneseContextAnalysis:
+class JapaneseContextAnalysis(object):
     def __init__(self):
         self.reset()
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcharsetprober.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcharsetprober.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is Mozilla Universal charset detector code.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sjisprober.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sjisprober.py	(refactored)
@@ -1,3 +1,5 @@
+from builtins import str
+from builtins import range
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is mozilla.org code.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/universaldetector.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/universaldetector.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is Mozilla Universal charset detector code.
 #
@@ -41,7 +42,7 @@
 eHighbyte = 2
 
 
-class UniversalDetector:
+class UniversalDetector(object):
     def __init__(self):
         self._highBitDetector = re.compile(b'[\x80-\xFF]')
         self._escDetector = re.compile(b'(\033|~{)')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/utf8prober.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/utf8prober.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import range
 ######################## BEGIN LICENSE BLOCK ########################
 # The Original Code is mozilla.org code.
 #
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py	(refactored)
@@ -1,8 +1,9 @@
+from builtins import object
 from collections import Mapping, MutableMapping
 try:
     from threading import RLock
 except ImportError:  # Platform-specific: No threads available
-    class RLock:
+    class RLock(object):
         def __enter__(self):
             pass
 
@@ -238,19 +239,19 @@
         other = args[0] if len(args) >= 1 else ()
         
         if isinstance(other, HTTPHeaderDict):
-            for key, val in other.iteritems():
+            for key, val in other.items():
                 self.add(key, val)
         elif isinstance(other, Mapping):
             for key in other:
                 self.add(key, other[key])
         elif hasattr(other, "keys"):
-            for key in other.keys():
+            for key in list(other.keys()):
                 self.add(key, other[key])
         else:
             for key, value in other:
                 self.add(key, value)
 
-        for key, value in kwargs.items():
+        for key, value in list(kwargs.items()):
             self.add(key, value)
 
     def getlist(self, key):
@@ -301,7 +302,7 @@
             yield val[0], ', '.join(val[1:])
 
     def items(self):
-        return list(self.iteritems())
+        return list(self.items())
 
     @classmethod
     def from_httplib(cls, message): # Python 2
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py	(refactored)
@@ -1,3 +1,6 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import object
 import datetime
 import sys
 import socket
@@ -8,7 +11,7 @@
 try:  # Python 3
     from http.client import HTTPConnection as _HTTPConnection, HTTPException
 except ImportError:
-    from httplib import HTTPConnection as _HTTPConnection, HTTPException
+    from http.client import HTTPConnection as _HTTPConnection, HTTPException
 
 
 class DummyConnection(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py	(refactored)
@@ -1,3 +1,8 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
+from builtins import object
 import errno
 import logging
 import sys
@@ -9,8 +14,8 @@
 try:  # Python 3
     from queue import LifoQueue, Empty, Full
 except ImportError:
-    from Queue import LifoQueue, Empty, Full
-    import Queue as _  # Platform-specific: Windows
+    from queue import LifoQueue, Empty, Full
+    import queue as _  # Platform-specific: Windows
 
 
 from .exceptions import (
@@ -180,7 +185,7 @@
         self.proxy_headers = _proxy_headers or {}
 
         # Fill the queue up so that doing get() on it will block properly
-        for _ in xrange(maxsize):
+        for _ in range(maxsize):
             self.pool.put(None)
 
         # These are mostly for testing and debugging purposes.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 import email.utils
 import mimetypes
 
@@ -126,7 +127,7 @@
         parts = []
         iterable = header_parts
         if isinstance(header_parts, dict):
-            iterable = header_parts.items()
+            iterable = list(header_parts.items())
 
         for name, value in iterable:
             if value:
@@ -145,7 +146,7 @@
             if self.headers.get(sort_key, False):
                 lines.append('%s: %s' % (sort_key, self.headers[sort_key]))
 
-        for header_name, header_value in self.headers.items():
+        for header_name, header_value in list(self.headers.items()):
             if header_name not in sort_keys:
                 if header_value:
                     lines.append('%s: %s' % (header_name, header_value))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 import codecs
 
 from uuid import uuid4
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py	(refactored)
@@ -1,9 +1,11 @@
+from future import standard_library
+standard_library.install_aliases()
 import logging
 
 try:  # Python 3
     from urllib.parse import urljoin
 except ImportError:
-    from urlparse import urljoin
+    from urllib.parse import urljoin
 
 from ._collections import RecentlyUsedContainer
 from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py	(refactored)
@@ -1,7 +1,10 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import object
 try:
     from urllib.parse import urlencode
 except ImportError:
-    from urllib import urlencode
+    from urllib.parse import urlencode
 
 from .filepost import encode_multipart_formdata
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py	(refactored)
@@ -1,7 +1,11 @@
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import object
 try:
     import http.client as httplib
 except ImportError:
-    import httplib
+    import http.client
 import zlib
 import io
 from socket import timeout as SocketTimeout
@@ -10,7 +14,7 @@
 from .exceptions import (
     ProtocolError, DecodeError, ReadTimeoutError, ResponseNotChunked
 )
-from .packages.six import string_types as basestring, binary_type, PY3
+from .packages.six import string_types as str, binary_type, PY3
 from .connection import HTTPException, BaseSSLError
 from .util.response import is_fp_closed
 
@@ -114,7 +118,7 @@
         self._original_response = original_response
         self._fp_bytes_read = 0
 
-        if body and isinstance(body, (basestring, binary_type)):
+        if body and isinstance(body, (str, binary_type)):
             self._body = body
 
         self._pool = pool
@@ -321,7 +325,7 @@
         headers = r.msg
         if not isinstance(headers, HTTPHeaderDict):
             if PY3: # Python 3
-                headers = HTTPHeaderDict(headers.items())
+                headers = HTTPHeaderDict(list(headers.items()))
             else: # Python 2
                 headers = HTTPHeaderDict.from_httplib(headers)
 
@@ -398,7 +402,7 @@
         except ValueError:
             # Invalid chunked protocol response, abort.
             self.close()
-            raise httplib.IncompleteRead(line)
+            raise http.client.IncompleteRead(line)
 
     def _handle_chunk(self, amt):
         returned_chunk = None
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py	(refactored)
@@ -3,11 +3,13 @@
 
 Issue #10, see: http://code.google.com/p/urllib3/issues/detail?id=10
 """
+from future import standard_library
+standard_library.install_aliases()
 
 try:
     from http.client import HTTPSConnection
 except ImportError:
-    from httplib import HTTPSConnection
+    from http.client import HTTPSConnection
 from logging import getLogger
 from ntlm import ntlm
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py	(refactored)
@@ -43,6 +43,9 @@
 .. _crime attack: https://en.wikipedia.org/wiki/CRIME_(security_exploit)
 
 '''
+from builtins import str
+from builtins import range
+from builtins import object
 
 try:
     from ndg.httpsclient.ssl_peer_verification import SUBJ_ALT_NAME_SUPPORT
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py	(refactored)
@@ -1,11 +1,13 @@
+from future import standard_library
+standard_library.install_aliases()
 # Backport of OrderedDict() class that runs on Python 2.4, 2.5, 2.6, 2.7 and pypy.
 # Passes Python2.7's test suite and incorporates all the latest updates.
 # Copyright 2009 Raymond Hettinger, released under the MIT License.
 # http://code.activestate.com/recipes/576693/
 try:
-    from thread import get_ident as _get_ident
+    from _thread import get_ident as _get_ident
 except ImportError:
-    from dummy_thread import get_ident as _get_ident
+    from _dummy_thread import get_ident as _get_ident
 
 try:
     from _abcoll import KeysView, ValuesView, ItemsView
@@ -79,7 +81,7 @@
     def clear(self):
         'od.clear() -> None.  Remove all items from od.'
         try:
-            for node in self.__map.itervalues():
+            for node in self.__map.values():
                 del node[:]
             root = self.__root
             root[:] = [root, root, None]
@@ -162,12 +164,12 @@
             for key in other:
                 self[key] = other[key]
         elif hasattr(other, 'keys'):
-            for key in other.keys():
+            for key in list(other.keys()):
                 self[key] = other[key]
         else:
             for key, value in other:
                 self[key] = value
-        for key, value in kwds.items():
+        for key, value in list(kwds.items()):
             self[key] = value
 
     __update = update  # let subclasses override update without breaking __init__
@@ -203,7 +205,7 @@
         try:
             if not self:
                 return '%s()' % (self.__class__.__name__,)
-            return '%s(%r)' % (self.__class__.__name__, self.items())
+            return '%s(%r)' % (self.__class__.__name__, list(self.items()))
         finally:
             del _repr_running[call_key]
 
@@ -238,7 +240,7 @@
 
         '''
         if isinstance(other, OrderedDict):
-            return len(self)==len(other) and self.items() == other.items()
+            return len(self)==len(other) and list(self.items()) == list(other.items())
         return dict.__eq__(self, other)
 
     def __ne__(self, other):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py	(refactored)
@@ -1,4 +1,9 @@
 """Utilities for writing code that runs on Python 2 and 3"""
+from future import standard_library
+standard_library.install_aliases()
+from builtins import bytes
+from builtins import str
+from builtins import object
 
 #Copyright (c) 2010-2011 Benjamin Peterson
 
@@ -39,10 +44,10 @@
 
     MAXSIZE = sys.maxsize
 else:
-    string_types = basestring,
-    integer_types = (int, long)
-    class_types = (type, types.ClassType)
-    text_type = unicode
+    string_types = str,
+    integer_types = (int, int)
+    class_types = (type, type)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/ssl_.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/timeout.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/url.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py

+    text_type = str
     binary_type = str
 
     if sys.platform.startswith("java"):
@@ -242,7 +247,7 @@
         return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)
 else:
     def get_unbound_function(unbound):
-        return unbound.im_func
+        return unbound.__func__
 
     class Iterator(object):
 
@@ -291,10 +296,10 @@
     def b(s):
         return s
     def u(s):
-        return unicode(s, "unicode_escape")
+        return str(s, "unicode_escape")
     int2byte = chr
-    import StringIO
-    StringIO = BytesIO = StringIO.StringIO
+    import io
+    StringIO = BytesIO = io.StringIO
 _add_doc(b, """Byte literal""")
 _add_doc(u, """Text literal""")
 
@@ -338,19 +343,19 @@
         if fp is None:
             return
         def write(data):
-            if not isinstance(data, basestring):
+            if not isinstance(data, str):
                 data = str(data)
             fp.write(data)
         want_unicode = False
         sep = kwargs.pop("sep", None)
         if sep is not None:
-            if isinstance(sep, unicode):
+            if isinstance(sep, str):
                 want_unicode = True
             elif not isinstance(sep, str):
                 raise TypeError("sep must be None or a string")
         end = kwargs.pop("end", None)
         if end is not None:
-            if isinstance(end, unicode):
+            if isinstance(end, str):
                 want_unicode = True
             elif not isinstance(end, str):
                 raise TypeError("end must be None or a string")
@@ -358,12 +363,12 @@
             raise TypeError("invalid keyword arguments to print()")
         if not want_unicode:
             for arg in args:
-                if isinstance(arg, unicode):
+                if isinstance(arg, str):
                     want_unicode = True
                     break
         if want_unicode:
-            newline = unicode("\n")
-            space = unicode(" ")
+            newline = str("\n")
+            space = str(" ")
         else:
             newline = "\n"
             space = " "
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py	(refactored)
@@ -1,4 +1,5 @@
 """The match_hostname() function from Python 3.3.3, essential when using SSL."""
+from builtins import map
 
 # Note: This file is under the PSF license as the code comes from the python
 # stdlib.   http://docs.python.org/3/license.html
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 import time
 import logging
 
@@ -200,7 +201,7 @@
     def is_exhausted(self):
         """ Are we out of retries? """
         retry_counts = (self.total, self.connect, self.read, self.redirect)
-        retry_counts = list(filter(None, retry_counts))
+        retry_counts = list([_f for _f in retry_counts if _f])
         if not retry_counts:
             return False
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/ssl_.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/ssl_.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 from binascii import hexlify, unhexlify
 from hashlib import md5, sha1, sha256
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/timeout.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/timeout.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import object
 # The default socket timeout, used by httplib to indicate that no timeout was
 # specified by the user
 from socket import _GLOBAL_DEFAULT_TIMEOUT
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/url.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/url.py	(refactored)
@@ -1,3 +1,4 @@
+from builtins import str
 from collections import namedtuple
 
 from ..exceptions import LocationParseError
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py	(refactored)
@@ -22,14 +22,15 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from builtins import str
 
 import os, sys
 import json
 from datetime import datetime
 from dateutil import parser
 
-from PyQt4 import QtGui, uic
-from PyQt4 import QtCore
+from qgis.PyQt import QtGui, uic
+from qgis.PyQt import QtCore
 from PyQt4.Qt import *
 # from PyQt4.Qt import QGraphicsScene, QPixmap
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py	(refactored)
@@ -22,16 +22,19 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from __future__ import absolute_import
+from builtins import str
 
 import os, sys
 import json
 
-from PyQt4 import QtGui, uic
-from PyQt4 import QtCore
+from qgis.PyQt import QtGui, uic
+from qgis.PyQt import QtCore
 from PyQt4.Qt import *
 from qgis.gui import QgsMessageBar
 
-from img_browser import ImgBrowser
+from .img_browser import ImgBrowser
 from module.module_access_oam_catalog import OAMCatalogAccess
 from module.module_geocoding import nominatim_search
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py	(refactored)
@@ -22,10 +22,14 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from __future__ import absolute_import
+from builtins import str
+from builtins import range
 
 import os, sys
 
-from PyQt4 import QtGui, uic
+from qgis.PyQt import QtGui, uic
 from PyQt4.Qt import *
 
 from qgis.gui import QgsMessageBar
@@ -35,7 +39,7 @@
 import traceback
 
 from module.module_handle_metadata import ImgMetadataHandler
-from upload_progress_window import UploadProgressWindow
+from .upload_progress_window import UploadProgressWindow
 from module.module_gdal_utilities import ReprojectionCmdWindow
 from module.module_validate_files import validate_layer, validate_file
 from module.module_img_utilities import ThumbnailCreation
@@ -194,7 +198,7 @@
                     # print(item.data(Qt.UserRole))
 
     def selectFile(self):
-        selected_file = QFileDialog.getOpenFileName(
+        selected_file, __ = QFileDialog.getOpenFileName(
             self,
             'Select imagery file',
             os.path.expanduser("~"))
@@ -570,7 +574,7 @@
         imgMetaHdlr = ImgMetadataHandler(file_abspath)
         imgMetaHdlr.extractMetaInImagery()
         metaForUpload = dict(
-            imgMetaHdlr.getMetaInImagery().items() + metaInputInDict.items())
+            list(imgMetaHdlr.getMetaInImagery().items()) + list(metaInputInDict.items()))RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/setting_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/help/source/conf.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_gdal_utilities.py

         strMetaForUpload = str(json.dumps(metaForUpload))
 
         json_file_abspath = file_abspath + '_meta.json'
@@ -747,7 +751,7 @@
 
     def loadMetadataReviewBox(self):
         json_file_abspaths = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             file_abspath = str(
                 self.sources_list_widget.item(index).data(Qt.UserRole))
             json_file_abspath = ''
@@ -787,7 +791,7 @@
                 'Please check the lisence term.',
                 level=QgsMessageBar.WARNING)
         else:
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 upload_file_abspath = str(
                     self.added_sources_list_widget.item(index).data(Qt.UserRole))
                 # create thumbnail
@@ -862,7 +866,7 @@
         # print('fileAbsPath: ' + fileAbsPath)
 
         # print(str(self.added_sources_list_widget.count()))
-        for index in xrange(0, self.added_sources_list_widget.count()):
+        for index in range(0, self.added_sources_list_widget.count()):
             refFileAbsPath = str(
                 self.added_sources_list_widget.item(index).data(Qt.UserRole))
             # print('refFileAbsPath: ' + refFileAbsPath)
@@ -871,7 +875,7 @@
                 break
 
         # print(str(self.sources_list_widget.count()))
-        for index in xrange(0, self.sources_list_widget.count()):
+        for index in range(0, self.sources_list_widget.count()):
             refFileAbsPath = str(
                 self.sources_list_widget.item(index).data(Qt.UserRole))
             # print('refFileAbsPath: ' + refFileAbsPath)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/setting_dialog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/setting_dialog.py	(refactored)
@@ -22,10 +22,11 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from builtins import str
 
 import os, sys
 
-from PyQt4 import QtGui, uic
+from qgis.PyQt import QtGui, uic
 from PyQt4.Qt import *
 
 from qgis.core import QgsMessageLog
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py	(refactored)
@@ -22,15 +22,18 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from builtins import str
+from builtins import range
 
 import sys, os, time, math
 # import imghdr, tempfile, requests, json
 # import traceback
 # from ast import literal_eval
 
-from PyQt4 import QtCore
+from qgis.PyQt import QtCore
 from PyQt4.QtGui import *      # modify this part?
-from PyQt4.QtCore import QThread, pyqtSignal
+from qgis.PyQt.QtCore import QThread, pyqtSignal
 from PyQt4.Qt import *
 
 from module.module_access_s3 import S3UploadWorker
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py	(refactored)
@@ -22,16 +22,21 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import object
 
 import os, sys
 # import pycurl
 # import urllib2
 import requests
 import json
-from StringIO import StringIO
+from io import StringIO
 
 
-class OAMCatalogAccess:
+class OAMCatalogAccess(object):
 
     def __init__(self, hostUrl, action=None, dictQueries=None, parent=None):
         # probably need to make a textbox for editing hostUrl later
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py	(refactored)
@@ -28,9 +28,9 @@
 # import traceback
 # from ast import literal_eval
 
-from PyQt4 import QtCore
+from qgis.PyQt import QtCore
 from PyQt4.QtGui import *      # modify this part?
-from PyQt4.QtCore import QThread, pyqtSignal
+from qgis.PyQt.QtCore import QThread, pyqtSignal
 
 #import boto
 #from boto.s3.connection import S3Connection, S3ResponseError
@@ -148,7 +148,7 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
+        if u'id' in list(post_dict.keys()):
             ts_id = post_dict[u'id']
             time = post_dict[u'queued_at']
             QgsMessageLog.logMessage(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py	(refactored)
@@ -1,10 +1,11 @@
+from builtins import str
 import os, sys
 import time
 
-from PyQt4 import QtCore
+from qgis.PyQt import QtCore
 from PyQt4.QtCore import *
 from PyQt4.QtGui import *
-from PyQt4.QtCore import QThread, pyqtSignal
+from qgis.PyQt.QtCore import QThread, pyqtSignal
 
 
 class CommandWindow(QWidget):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py	(refactored)
@@ -22,13 +22,19 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from future import standard_library
+standard_library.install_aliases()
+from builtins import str
+from builtins import range
+from builtins import object
 
 import sys, os, time
-import urllib2
+import urllib.request, urllib.error, urllib.parse
 import json
-from PyQt4 import QtCore
+from qgis.PyQt import QtCore
 from PyQt4.QtGui import *
-from PyQt4.QtCore import QThread, pyqtSignal, QObject
+from qgis.PyQt.QtCore import QThread, pyqtSignal, QObject
 from PyQt4.Qt import *
 
 class ThumbnailManager(QObject):
@@ -51,7 +57,7 @@
         # print(imgAbspath)
         if not os.path.exists(imgAbspath):
             try:
-                response = urllib2.urlopen(urlThumbnail)
+                response = urllib.request.urlopen(urlThumbnail)
                 chunkSize = 1024 * 16
                 f = open(imgAbspath, 'wb')
                 while True:
@@ -67,7 +73,7 @@
         return imgAbspath
 
 
-class ImgMetaDownloader:
+class ImgMetaDownloader(object):
     def __init__(self, parent=None):
         pass
 
@@ -75,7 +81,7 @@
     def downloadImgMeta(urlImgMeta, imgMetaAbsPath):
         try:
             f = open(imgMetaAbsPath, 'w')
-            f.write(urllib2.urlopen(urlImgMeta).read())
+            f.write(urllib.request.urlopen(urlImgMeta).read())
             f.close()
         except Exception as e:
             print(str(e))
@@ -333,7 +339,7 @@
     def run(self):
         try:
             self.started.emit(True, self.index)
-            u = urllib2.urlopen(self.url)
+            u = urllib.request.urlopen(self.url)
             f = open(self.fileAbsPath, 'wb')
             meta = u.info()
             fileSize = int(meta.getheaders("Content-Length")[0])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_gdal_utilities.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_gdal_utilities.py	(refactored)
@@ -22,6 +22,8 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_geocoding.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_validate_files.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/qgis_interface.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_oam_client_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_resources.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_s3_uploader.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py

 """
+from __future__ import print_function
+from builtins import str
 
 import os, sys
 from osgeo import gdal, osr, ogr
@@ -120,8 +122,9 @@
                   adfGeoTransform[4] * x +
                   adfGeoTransform[5] * y)
     else:
-        print "BBOX might be wrong. Transformation coefficient " + \
-            "could not be fetched from raster"
+        # fix_print_with_import
+        print("BBOX might be wrong. Transformation coefficient " + \
+            "could not be fetched from raster")
         return (x, y)
 
     # Report the georeferenced coordinates
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py	(refactored)
@@ -22,13 +22,16 @@
  ***************************************************************************/
  This script initializes the plugin, making it known to QGIS.
 """
+from __future__ import print_function
+from builtins import str
+from builtins import object
 
 import os, sys
 from osgeo import gdal, osr, ogr
 from ast import literal_eval
 
 
-class ImgMetadataHandler:
+class ImgMetadataHandler(object):
 
     def __init__(self, imgFileAbspath):
         self.imgFileAbspath = imgFileAbspath
@@ -63,7 +66,8 @@
             self.extractGsd()
             return True
         else:
-            print "Error: could not open the gdaldataset."
+            # fix_print_with_import
+            print("Error: could not open the gdaldataset.")
             return False
 
     def extractProjName(self):
@@ -140,8 +144,9 @@
             geoX = geoTransform[0] + geoTransform[1] * x + geoTransform[2] * y
             geoY = geoTransform[3] + geoTransform[4] * x + geoTransform[5] * y
         else:
-            print "BBOX might be wrong. Transformation coefficient " + \
-                "could not be fetched from raster"
+            # fix_print_with_import
+            print("BBOX might be wrong. Transformation coefficient " + \
+                "could not be fetched from raster")
             return (x, y)
 
         # Report the georeferenced coordinates
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py	(refactored)
@@ -1,6 +1,8 @@
+from __future__ import print_function
+from builtins import object
 from PIL import Image
 
-class ThumbnailCreation:
+class ThumbnailCreation(object):
 
     def __init__(self):
         pass
@@ -24,6 +26,7 @@
                 im = im.resize(size)
                 im.save(outfile, "PNG")
             except Exception as e:
-                print(e, infile)
+                # fix_print_with_import
+                print((e, infile))
 
         return outfile
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/qgis_interface.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/qgis_interface.py	(refactored)
@@ -24,7 +24,7 @@
 )
 
 import logging
-from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal
+from qgis.PyQt.QtCore import QObject, pyqtSlot, pyqtSignal
 from qgis.core import QgsMapLayerRegistry
 from qgis.gui import QgsMapCanvasLayer
 LOGGER = logging.getLogger('QGIS')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py	(refactored)
@@ -1,5 +1,7 @@
 # coding=utf-8
 """Tests QGIS plugin init."""
+from future import standard_library
+standard_library.install_aliases()
 
 __author__ = 'Tim Sutton <tim@linfiniti.com>'
 __revision__ = '$Format:%H$'
@@ -11,7 +13,7 @@
 import os
 import unittest
 import logging
-import ConfigParser
+import configparser
 
 LOGGER = logging.getLogger('QGIS')
 
@@ -47,7 +49,7 @@
             'metadata.txt'))
         LOGGER.info(file_path)
         metadata = []
-        parser = ConfigParser.ConfigParser()
+        parser = configparser.ConfigParser()
         parser.optionxform = str
         parser.read(file_path)
         message = 'Cannot find a section named "general" in %s' % file_path
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_oam_client_dialog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_oam_client_dialog.py	(refactored)
@@ -7,6 +7,7 @@
      (at your option) any later version.
 
 """
+from __future__ import absolute_import
 
 __author__ = 'tassia@acaia.ca'
 __date__ = '2015-07-01'
@@ -14,11 +15,11 @@
 
 import unittest
 
-from PyQt4.QtGui import QDialogButtonBox, QDialog
+from qgis.PyQt.QtWidgets import QDialogButtonBox, QDialog
 
 from oam_client_dialog import OpenAerialMapDialog
 
-from utilities import get_qgis_app
+from .utilities import get_qgis_app
 QGIS_APP = get_qgis_app()
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py	(refactored)
@@ -8,6 +8,7 @@
      (at your option) any later version.
 
 """
+from __future__ import absolute_import
 __author__ = 'tim@linfiniti.com'
 __date__ = '20/01/2011'
 __copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
@@ -20,7 +21,7 @@
     QgsCoordinateReferenceSystem,
     QgsRasterLayer)
 
-from utilities import get_qgis_app
+from .utilities import get_qgis_app
 QGIS_APP = get_qgis_app()
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_resources.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_resources.py	(refactored)
@@ -14,7 +14,7 @@
 
 import unittest
 
-from PyQt4.QtGui import QIcon
+from qgis.PyQt.QtGui import QIcon
 
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_s3_uploader.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_s3_uploader.py	(refactored)
@@ -1,4 +1,4 @@
 import unittest
 import os
 
-from PyQt4.QtCore import QCoreApplication
+from qgis.PyQt.QtCore import QCoreApplication
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py	(refactored)
@@ -7,7 +7,8 @@
      (at your option) any later version.
 
 """
-from utilities import get_qgis_app
+from __future__ import absolute_import
+from .utilities import get_qgis_app
 
 __author__ = 'ismailsunni@yahoo.co.id'
 __date__ = '12/10/2011'
@@ -16,7 +17,7 @@
 import unittest
 import os
 
-from PyQt4.QtCore import QCoreApplication, QTranslator
+from qgis.PyQt.QtCore import QCoreApplication, QTranslator
 
 QGIS_APP = get_qgis_app()
 
@@ -26,12 +27,12 @@
 
     def setUp(self):
         """Runs before each test."""
-        if 'LANG' in os.environ.iterkeys():
+        if 'LANG' in iter(os.environ.keys()):
             os.environ.__delitem__('LANG')
 
     def tearDown(self):
         """Runs after each test."""
-        if 'LANG' in os.environ.iterkeys():
+        if 'LANG' in iter(os.environ.keys()):
             os.environ.__delitem__('LANG')
 
     def test_qgis_translations(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py	(refactored)
@@ -1,5 +1,6 @@
 # coding=utf-8
 """Common functionality used by regression tests."""
+from __future__ import absolute_import
 
 import sys
 import logging
@@ -23,10 +24,10 @@
     """
 
     try:
-        from PyQt4 import QtGui, QtCore
+        from qgis.PyQt import QtGui, QtCore
         from qgis.core import QgsApplication
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py
RefactoringTool: Files that were modified:
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/make_package.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_search_dialog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/get-pip.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/setup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/handler.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/https_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/jsonresponse.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/plugin.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/provider.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/storage_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/keypair.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotpricehistory.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/activity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/instance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/launchconfig.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/limits.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/policy.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/request.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/scheduled.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/tag.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/alarm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/vault.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/writer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/acl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucketlistresultset.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/cors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/lifecycle.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/user.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/summarymap.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/task.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/interactive.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/layoutparam.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/notification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/price.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/qualification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/bootstrap.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/startup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/ebs.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/mysql.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/trac.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsecuritygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsnapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsubnetgroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/event.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/logfile.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/optiongroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/statusinfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/vpcsecuritygroupmembership.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/acl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlistresultset.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/cors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/deletemarker.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/lifecycle.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multidelete.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multipart.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/prefix.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/tagging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/user.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/website.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/item.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/property.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/test_db.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/message.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/service.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/servicedef.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/sonofmmm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/bigmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/jsonmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/internetgateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/networkacl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/routetable.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/subnet.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc_peering_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpnconnection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpngateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/test.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/devpay/test_s3.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_layers.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cloudtrail.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/sync/test_cognito_sync.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/vpc/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elasticache/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/testcase.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_password_policy.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_kinesis.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/opsworks/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/support/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1_workflow_execution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearchdomain/test_cloudsearchdomain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudtrail/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/directconnect/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_address.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_blockdevicemapping.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancetype.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_snapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_spotinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/autoscale/test_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_listener.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_loadbalancer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ecs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_job.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kinesis/test_kinesis.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/logs/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/manage/test_ssh.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mturk/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/provider/test_provider.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_snapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_zone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_lifecycle.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_tagging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ses/test_identity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_actors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_customergateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_dhcpoptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_internetgateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_networkacl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_routetable.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_subnet.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc_peering_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpnconnection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpngateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/filechunkio.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/location.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/units.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/util.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/arcgis.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/baidu.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/base.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/databc.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/dot_us.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geocodefarm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geonames.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/googlev3.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/ignfrance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/navidata.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/opencage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/openmapquest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/photon.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/smartystreets.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/what3words.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/yandex.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/setup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/test_requests.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/status_codes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5freq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetgroupprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/constants.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escsm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrfreq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwfreq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312freq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/hebrewprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jisfreq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jpcntx.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langbulgarianmodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langcyrillicmodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langgreekmodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhebrewmodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhungarianmodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langthaimodel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/latin1prober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcharsetprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcssm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sbcharsetprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sjisprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/universaldetector.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/utf8prober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/ssl_.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/timeout.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/url.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/setting_dialog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/help/source/conf.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_gdal_utilities.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_geocoding.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_validate_files.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/qgis_interface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_oam_client_dialog.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_resources.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_s3_uploader.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py
RefactoringTool: Warnings/messages while refactoring:
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py ###
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 31: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py ###
RefactoringTool: Line 491: Calls to builtin next() possibly shadowed by global binding
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py ###
RefactoringTool: Line 37: You should use a for loop here
RefactoringTool: Line 38: You should use a for loop here
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py ###
RefactoringTool: Line 232: Calls to builtin next() possibly shadowed by global binding
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py ###
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py ###
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 32: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py ###
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 5: could not convert: from PyQt4.QtCore import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 6: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py ###
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
RefactoringTool: Line 30: could not convert: from PyQt4.QtGui import *
RefactoringTool: Cannot handle star imports.
         from qgis.gui import QgsMapCanvas
-        from qgis_interface import QgisInterface
+        from .qgis_interface import QgisInterface
     except ImportError:
         return None, None, None, None
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py	(refactored)
@@ -5,8 +5,8 @@
 """
 
 import sys, os, time
-from PyQt4 import QtCore
-from PyQt4.QtCore import QThread, pyqtSignal
+from qgis.PyQt import QtCore
+from qgis.PyQt.QtCore import QThread, pyqtSignal
 
 class S3UploadWorker(QThread):
 

Process finished with exit code 0
```
