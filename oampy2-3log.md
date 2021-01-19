```sh
/usr/bin/2to3 /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap
RefactoringTool: Skipping optional fixer: buffer
RefactoringTool: Skipping optional fixer: idioms
RefactoringTool: Skipping optional fixer: set_literal
RefactoringTool: Skipping optional fixer: ws_comma
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/make_package.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/oam_main.py	(refactored)
@@ -38,12 +38,12 @@
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
@@ -217,9 +217,9 @@
 
         """Create the menu and toolbar inside the QGIS GUI."""
 
-        self.menu = self.tr(u'&Open Aerial Map (OAM)')
-        self.toolbar = self.iface.addToolBar(u'OpenAerialMap')
-        self.toolbar.setObjectName(u'OpenAerialMap')
+        self.menu = self.tr('&Open Aerial Map (OAM)')
+        self.toolbar = self.iface.addToolBar('OpenAerialMap')
+        self.toolbar.setObjectName('OpenAerialMap')
 
         """Create the menu entries and toolbar icons inside the QGIS GUI."""
 
@@ -230,25 +230,25 @@
 
         self.add_action(
             icon_path_img_wizard,
-            text=self.tr(u'Upload Imagery'),
+            text=self.tr('Upload Imagery'),
             callback=self.displayImgUploaderWizard,
             parent=self.iface.mainWindow())
 
         self.add_action(
             icon_path_search_tool,
-            text=self.tr(u'Search Imagery'),
+            text=self.tr('Search Imagery'),
             callback=self.displaySearchTool,
             parent=self.iface.mainWindow())
 
         self.add_action(
             icon_path_setting_dialog,
-            text=self.tr(u'Edit Default Settings'),
+            text=self.tr('Edit Default Settings'),
             callback=self.displaySettingDialog,
             parent=self.iface.mainWindow())
 
         self.add_action(
             icon_path_help,
-            text=self.tr(u'OAM Help'),
+            text=self.tr('OAM Help'),
             callback=self.displayHelp,
             parent=self.iface.mainWindow())
 
@@ -256,7 +256,7 @@
         """Removes the plugin menu item and icon from QGIS GUI."""
         for action in self.actions:
             self.iface.removePluginMenu(
-                self.tr(u'&Open Aerial Map (OAM)'), action)
+                self.tr('&Open Aerial Map (OAM)'), action)
             self.iface.removeToolBarIcon(action)
         del self.toolbar
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/plugin_upload.py	(refactored)
@@ -7,7 +7,7 @@
 
 import sys
 import getpass
-import xmlrpclib
+import xmlrpc.client
 from optparse import OptionParser
 
 # Configuration
@@ -31,25 +31,25 @@
         parameters.server,
         parameters.port,
         ENDPOINT)
-    print "Connecting to: %s" % hide_password(address)
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
+        print("Plugin ID: %s" % plugin_id)
+        print("Version ID: %s" % version_id)
+    except xmlrpc.client.ProtocolError as err:
+        print("A protocol error occurred")
+        print("URL: %s" % hide_password(err.url, 0))
+        print("HTTP/HTTPS headers: %s" % err.headers)
+        print("Error code: %d" % err.errcode)
+        print("Error message: %s" % err.errmsg)
+    except xmlrpc.client.Fault as err:
+        print("A fault occurred")
+        print("Fault code: %d" % err.faultCode)
+        print("Fault string: %s" % err.faultString)
 
 
 def hide_password(url, start=6):
@@ -85,7 +85,7 @@
         help="Specify server name", metavar="plugins.qgis.org")
     options, args = parser.parse_args()
     if len(args) != 1:
-        print "Please specify zip file.\n"
+        print("Please specify zip file.\n")
         parser.print_help()
         sys.exit(1)
     if not options.server:
@@ -95,8 +95,8 @@
     if not options.username:
         # interactive mode
         username = getpass.getuser()
-        print "Please enter user name [%s] :" % username,
-        res = raw_input()
+        print("Please enter user name [%s] :" % username, end=' ')
+        res = input()
         if res != "":
             options.username = res
         else:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/set_env.py	(refactored)
@@ -60,15 +60,15 @@
 
             # QgsApplication.prefixPath() contains the path to qgis executable (i.e. .../Qgis.app/MacOS)
             # get the path to Qgis application folder
-            qgis_app = u"%s/.." % QgsApplication.prefixPath()
+            qgis_app = "%s/.." % QgsApplication.prefixPath()
             qgis_app = QDir(qgis_app).absolutePath()
 
             # get the path to the GDAL framework within the Qgis application folder (Qgis standalone only)
-            qgis_standalone_gdal_path = u"%s/Frameworks/GDAL.framework" % qgis_app
+            qgis_standalone_gdal_path = "%s/Frameworks/GDAL.framework" % qgis_app
 
             # get the path to the GDAL framework when installed as external framework
-            gdal_versionsplit = unicode(Version(gdal.VersionInfo("RELEASE_NAME"))).split('.')
-            gdal_base_path = u"/Library/Frameworks/GDAL.framework/Versions/%s.%s/Programs" % (gdal_versionsplit[0], gdal_versionsplit[1])
+            gdal_versionsplit = str(Version(gdal.VersionInfo("RELEASE_NAME"))).split('.')
+            gdal_base_path = "/Library/Frameworks/GDAL.framework/Versions/%s.%s/Programs" % (gdal_versionsplit[0], gdal_versionsplit[1])
 
             if os.path.exists(qgis_standalone_gdal_path):  # qgis standalone
                 os.environ['PATH'] = os.environ['PATH'] + ':' +  qgis_standalone_gdal_path
@@ -91,7 +91,7 @@
         if isinstance(ver, Version):
             self.vers = ver.vers
         elif isinstance(ver, tuple) or isinstance(ver, list):
-            self.vers = map(str, ver)
+            self.vers = list(map(str, ver))
         elif isinstance(ver, str):
             self.vers = self.string2vers(ver)
 
@@ -99,7 +99,7 @@
     def string2vers(string):
         vers = ['0', '0', '0']
 
-        nums = unicode(string).split(".")
+        nums = str(string).split(".")
 
         if len(nums) > 0:
             vers[0] = nums[0]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py	(refactored)
@@ -301,7 +301,7 @@
                     if not "EPSG3857" in filename:
                         json_filename = os.path.splitext(filename)[0]+'_EPSG3857.json'
                 json_file = open(json_filename, 'w')
-                print >> json_file, json_string
+                print(json_string, file=json_file)
                 json_file.close()
 
             self.loadMetadataReviewBox()
@@ -495,9 +495,9 @@
                     point.Transform(transform)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_backup_img_uploader_wizard.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_search_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py

                     lower_right = json.loads(point.ExportToJson())['coordinates']
             except (RuntimeError, TypeError, NameError) as error:
-                print error
+                print(error)
             except:
-                print "Unexpected error:", sys.exc_info()[0]
+                print("Unexpected error:", sys.exc_info()[0])
 
             self.metadata[filename]['BBOX'] = (upper_left,lower_left,upper_right,lower_right)
 
@@ -563,7 +563,7 @@
 
     def loadMetadataReviewBox(self):
         json_filenames = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             if filename not in self.reprojected:
                 f = os.path.splitext(filename)[0]+'.json'
@@ -600,7 +600,7 @@
         bucket_secret = str(self.secret_key_edit.text())
 
         self.bucket = None
-        for trial in xrange(3):
+        for trial in range(3):
             if self.bucket: break
             try:
                 connection = S3Connection(bucket_key,bucket_secret)
@@ -647,7 +647,7 @@
             self.upload_options.append("trigger_tiling")
 
         if self.startConnection():
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 filename = str(self.sources_list_widget.item(index).data(Qt.UserRole))
 
                 self.bar2.clearWidgets()
@@ -768,7 +768,7 @@
     '''Handle uploads in a separate thread'''
 
     finished = pyqtSignal(bool)
-    error = pyqtSignal(Exception, basestring)
+    error = pyqtSignal(Exception, str)
     progress = pyqtSignal(float)
 
     def __init__(self,filename,bucket,options):
@@ -817,9 +817,9 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
-            ts_id = post_dict[u'id']
-            time = post_dict[u'queued_at']
+        if 'id' in list(post_dict.keys()):
+            ts_id = post_dict['id']
+            time = post_dict['queued_at']
             QgsMessageLog.logMessage(
                 'Tile service #%s triggered on %s\n' % (ts_id,time),
                 'OAM',
@@ -874,7 +874,7 @@
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
@@ -114,7 +114,7 @@
             self.startSearch()
 
     def test(self, *argv):
-        print(str(argv))
+        print((str(argv)))
 
     def createQueriesSettings(self):
         self.settings.setValue('CHECKBOX_LOCATION', True)
@@ -242,7 +242,7 @@
 
         for singleMetaInDict in metadataInList:
             item = QListWidgetItem()
-            item.setText(singleMetaInDict[u'title'])
+            item.setText(singleMetaInDict['title'])
             item.setData(Qt.UserRole, singleMetaInDict)
             self.listWidget.addItem(item)
 
@@ -294,7 +294,7 @@
             elif self.comboBoxOrderBy.currentText() == 'GSD':
                 dictQueries['order_by'] = "gsd"
 
-            print(self.comboBoxOrderBy.currentText())
+            print((self.comboBoxOrderBy.currentText()))
 
 
             if self.radioButtonAsc.isChecked():
@@ -309,7 +309,7 @@
             self.refreshListWidget(metadataInList)
 
         except Exception as e:
-            print(repr(e))
+            print((repr(e)))
             qMsgBox = QMessageBox()
             qMsgBox.setWindowTitle('Message')
             qMsgBox.setText("Please make sure if you entered valid data" +
@@ -372,8 +372,8 @@
                     self.displayThumnailDownloadError)
 
                 pos = self.pos()
-                print(pos.x())
-                print(pos.y())
+                print((pos.x()))
+                print((pos.y()))
                 pos.setX(pos.x() + 400)
                 pos.setY(pos.y() + 20)
                 self.imgBrowser.move(pos)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_img_uploader_wizard.py	(refactored)
@@ -388,7 +388,7 @@
                              % (str(count+1), str(num_selected_layers)),
                             level=QgsMessageBar.INFO)
                         # Isn't it better to use thread?
-                        print('Reprojecting {0}'.format(str(os.path.basename(file_abspath))))
+                        print(('Reprojecting {0}'.format(str(os.path.basename(file_abspath)))))
 
                         """ probably, it is better to create a class for reprojection """
                         file_abspath = reproject(file_abspath)
@@ -435,7 +435,7 @@
                     # extract metadata from GeoTiff, and merge with the metadata from textbox
                     imgMetaHdlr = ImgMetadataHandler(file_abspath)
                     imgMetaHdlr.extractMetaInImagery()
-                    metaForUpload = dict(imgMetaHdlr.getMetaInImagery().items() + metaInputInDict.items())
+                    metaForUpload = dict(list(imgMetaHdlr.getMetaInImagery().items()) + list(metaInputInDict.items()))
                     strMetaForUpload = str(json.dumps(metaForUpload))
 
                     #json_file_abspath = os.path.splitext(file_abspath)[0] + '.tif_meta.json'
@@ -535,7 +535,7 @@
 
     def loadMetadataReviewBox(self):
         json_file_abspaths = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             file_abspath = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             json_file_abspath = ''
             #if self.reproject_check_box.isChecked():
@@ -584,7 +584,7 @@
                 'Please check the lisence term.',
                 level=QgsMessageBar.WARNING)
         else:
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 upload_file_abspath = str(self.added_sources_list_widget.item(index).data(Qt.UserRole))
                 upload_file_abspaths.append(upload_file_abspath)
 
@@ -643,7 +643,7 @@
         #print('fileAbsPath: ' + fileAbsPath)
 
         #print(str(self.added_sources_list_widget.count()))
-        for index in xrange(0, self.added_sources_list_widget.count()):
+        for index in range(0, self.added_sources_list_widget.count()):
             refFileAbsPath = str(self.added_sources_list_widget.item(index).data(Qt.UserRole))
             #print('refFileAbsPath: ' + refFileAbsPath)
             if fileAbsPath == refFileAbsPath:
@@ -651,7 +651,7 @@
                 break
 
         #print(str(self.sources_list_widget.count()))
-        for index in xrange(0, self.sources_list_widget.count()):
+        for index in range(0, self.sources_list_widget.count()):
             refFileAbsPath = str(self.sources_list_widget.item(index).data(Qt.UserRole))
             #print('refFileAbsPath: ' + refFileAbsPath)
             if fileAbsPath == refFileAbsPath:
@@ -674,6 +674,6 @@
         # Probably, it is better to change this part into log file.
         print('')
         print('------------------------------------------------')
-        print('Success:{0} Cancel:{1} Fail:{2}'.format(numSuccess, numCancelled, numFailed))
+        print(('Success:{0} Cancel:{1} Fail:{2}'.format(numSuccess, numCancelled, numFailed)))
         print('------------------------------------------------')
         print('')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py	(original)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_command_window.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/get-pip.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/setup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth_handler.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/backup_files/backup_module_access_s3.py	(refactored)
@@ -82,7 +82,7 @@
 
     def getBucket(self):
 
-        for trial in xrange(3):
+        for trial in range(3):
             if self.bucket: break
             try:
                 self.bucket = super(S3Manager,self).get_bucket(self.bucket_name)
@@ -112,9 +112,9 @@
 
         """ Testing purpose only """
         if "notify_oam" in self.upload_options:
-            print "notify_oam"
+            print("notify_oam")
         if "trigger_tiling" in self.upload_options:
-            print "trigger_tiling"
+            print("trigger_tiling")
 
         # configure the msg_bar_main (including Cancel button and its container)
         self.msg_bar_main = QgsMessageBar()
@@ -146,7 +146,7 @@
                 self.threads[i].started.connect(self.s3Uploaders[i].run)
                 self.threads[i].start()
 
-                print repr(self.threads[i])
+                print(repr(self.threads[i]))
 
                 # configure the msg_bars for progress bar
                 self.msg_bars.append(QgsMessageBar())
@@ -175,7 +175,7 @@
                 #self.cancel_buttons[i].clicked.connect(self.cancelUpload)
                 """
 
-            except Exception, e:
+            except Exception as e:
                 return repr(e)
 
         #Display upload progress bars in a separate widget
@@ -190,7 +190,7 @@
         return True
 
     def updateProgressBar(self, progress_value, index):
-        print "Progress: " + str(progress_value) + ", index: " + str(index)
+        print("Progress: " + str(progress_value) + ", index: " + str(index))
         if self.progress_bars[index] != None:
             self.progress_bars[index].setValue(progress_value)
 
@@ -211,11 +211,11 @@
                 #self.threads[i] = None
 
         except:
-            print "Error: problem occurred to kill uploaders"
+            print("Error: problem occurred to kill uploaders")
 
     def cancelUpload(self, index):
 
-        print "Cancel button was clicked!"
+        print("Cancel button was clicked!")
 
         """
         try:
@@ -328,7 +328,7 @@
     '''Handle uploads in a separate thread'''
 
     finished = pyqtSignal(bool, int)
-    error = pyqtSignal(Exception, basestring)
+    error = pyqtSignal(Exception, str)
     progress = pyqtSignal(float, int)
 
     def __init__(self, filename, bucket, options, index):
@@ -406,7 +406,7 @@
                 if "trigger_tiling" in self.options:
                     self.triggerTileService()
 
-        except Exception, e:
+        except Exception as e:
             # forward the exception upstream (or try to...)
             # chunk size smaller than 5MB can cause an error, server does not expect it
             self.error.emit(e, traceback.format_exc())
@@ -440,9 +440,9 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
-            ts_id = post_dict[u'id']
-            time = post_dict[u'queued_at']
+        if 'id' in list(post_dict.keys()):
+            ts_id = post_dict['id']
+            time = post_dict['queued_at']
             QgsMessageLog.logMessage(
                 'Tile service #%s triggered on %s\n' % (ts_id,time),
                 'OAM',
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/setup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/setup.py	(refactored)
@@ -23,7 +23,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 
-from __future__ import print_function
+
 
 try:
     from setuptools import setup
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth.py	(refactored)
@@ -230,7 +230,7 @@
         in the StringToSign.
         """
         headers_to_sign = {'Host': self.host}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             if lname.startswith('x-amz'):
                 headers_to_sign[name] = value
@@ -324,7 +324,7 @@
         if http_request.headers.get('Host'):
             host_header_value = http_request.headers['Host']
         headers_to_sign = {'Host': host_header_value}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             if lname.startswith('x-amz'):
                 if isinstance(value, bytes):
@@ -601,7 +601,7 @@
         """
         host_header_value = self.host_header(self.host, http_request)
         headers_to_sign = {'Host': host_header_value}
-        for name, value in http_request.headers.items():
+        for name, value in list(http_request.headers.items()):
             lname = name.lower()
             # Hooray for the only difference! The main SigV4 signer only does
             # ``Host`` + ``x-amz-*``. But S3 wants pretty much everything
@@ -695,7 +695,7 @@
 
         # ``parse_qs`` will return lists. Don't do that unless there's a real,
         # live list provided.
-        for key, value in existing_qs.items():
+        for key, value in list(existing_qs.items()):
             if isinstance(value, (list, tuple)):
                 if len(value) == 1:
                     existing_qs[key] = value[0]
@@ -852,7 +852,7 @@
         hmac = self._get_hmac()
         s = params['Action'] + params['Timestamp']
         hmac.update(s.encode('utf-8'))
-        keys = params.keys()
+        keys = list(params.keys())
         keys.sort(cmp=lambda x, y: cmp(x.lower(), y.lower()))
         pairs = []
         for key in keys:
@@ -878,7 +878,7 @@
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
@@ -58,10 +58,10 @@
 
 if six.PY3:
     # StandardError was removed, so use the base exception type instead
-    StandardError = Exception
+    Exception = Exception
     long_type = int
     from configparser import ConfigParser
 else:
-    StandardError = StandardError
-    long_type = long
-    from ConfigParser import SafeConfigParser as ConfigParser
+    Exception = Exception
+    long_type = int
+    from configparser import SafeConfigParser as ConfigParser
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/connection.py	(refactored)
@@ -252,7 +252,7 @@
         """
         Returns the number of connections in the pool.
         """
-        return sum(pool.size() for pool in self.host_to_pool.values())
+        return sum(pool.size() for pool in list(self.host_to_pool.values()))
 
     def get_http_connection(self, host, port, is_secure):
         """
@@ -291,7 +291,7 @@
             now = time.time()
             if self.last_clean_time + self.CLEAN_INTERVAL < now:
                 to_remove = []
-                for (host, pool) in self.host_to_pool.items():
+                for (host, pool) in list(self.host_to_pool.items()):
                     pool.clean()
                     if pool.size() == 0:
                         to_remove.append(host)
@@ -796,7 +796,7 @@
         sock.sendall("CONNECT %s HTTP/1.0\r\n" % host)
         sock.sendall("User-Agent: %s\r\n" % UserAgent)
         if self.proxy_user and self.proxy_pass:RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/handler.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/https_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/jsonresponse.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/plugin.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/provider.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/storage_uri.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/exception.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/object.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/optionstatus.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/__init__.py

-            for k, v in self.get_proxy_auth_header().items():
+            for k, v in list(self.get_proxy_auth_header().items()):
                 sock.sendall("%s: %s\r\n" % (k, v))
             # See discussion about this config option at
             # https://groups.google.com/forum/?fromgroups#!topic/boto-dev/teenFvOq2Cc
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/exception.py	(refactored)
@@ -30,11 +30,11 @@
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
@@ -49,7 +49,7 @@
         return 'BotoClientError: %s' % self.reason
 
 
-class SDBPersistenceError(StandardError):
+class SDBPersistenceError(Exception):
     pass
 
 
@@ -74,7 +74,7 @@
     pass
 
 
-class BotoServerError(StandardError):
+class BotoServerError(Exception):
     def __init__(self, status, reason, body=None, *args):
         super(BotoServerError, self).__init__(status, reason, body, *args)
         self.status = status
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/regioninfo.py	(refactored)
@@ -57,7 +57,7 @@
     # We can't just do an ``defaults.update(...)`` here, as that could
     # *overwrite* regions if present in both.
     # We'll iterate instead, essentially doing a deeper merge.
-    for service, region_info in additions.items():
+    for service, region_info in list(additions.items()):
         # Set the default, if not present, to an empty dict.
         defaults.setdefault(service, {})
         defaults[service].update(region_info)
@@ -134,7 +134,7 @@
 
     region_objs = []
 
-    for region_name, endpoint in endpoints.get(service_name, {}).items():
+    for region_name, endpoint in list(endpoints.get(service_name, {}).items()):
         region_objs.append(
             region_cls(
                 name=region_name,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/requestlog.py	(refactored)
@@ -1,7 +1,7 @@
 import sys
 from datetime import datetime
 from threading import Thread
-import Queue
+import queue
 
 from boto.utils import RequestHook
 from boto.compat import long_type
@@ -14,7 +14,7 @@
     """
     def __init__(self, filename='/tmp/request_log.csv'):
         self.request_log_file = open(filename, 'w')
-        self.request_log_queue = Queue.Queue(100)
+        self.request_log_queue = queue.Queue(100)
         Thread(target=self._request_log_worker).start()
 
     def handle_request_data(self, request, response, error=False):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/resultset.py	(refactored)
@@ -147,7 +147,7 @@
         else:
             return 'False'
 
-    def __nonzero__(self):
+    def __bool__(self):
         return self.status
 
     def startElement(self, name, attrs, connection):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/utils.py	(refactored)
@@ -167,7 +167,7 @@
         provider = boto.provider.get_default()
     metadata_prefix = provider.metadata_prefix
     final_headers = headers.copy()
-    for k in metadata.keys():
+    for k in list(metadata.keys()):
         if k.lower() in boto.s3.key.Key.base_user_settable_fields:
             final_headers[k] = metadata[k]
         else:
@@ -181,7 +181,7 @@
         provider = boto.provider.get_default()
     metadata_prefix = provider.metadata_prefix
     metadata = {}
-    for hkey in headers.keys():
+    for hkey in list(headers.keys()):
         if hkey.lower().startswith(metadata_prefix):
             val = urllib.parse.unquote(headers[hkey])
             if isinstance(val, bytes):
@@ -337,11 +337,11 @@
 
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
@@ -677,7 +677,7 @@
 
     class _Item(object):
         def __init__(self, key, value):
-            self.previous = self.next = None
+            self.previous = self.__next__ = None
             self.key = key
             self.value = value
 
@@ -697,7 +697,7 @@
         cur = self.head
         while cur:
             yield cur.key
-            cur = cur.next
+            cur = cur.__next__
 
     def __len__(self):
         return len(self._dict)
@@ -745,8 +745,8 @@
             return
 
         previous = item.previous
-        previous.next = item.next
-        if item.next is not None:
+        previous.next = item.__next__
+        if item.__next__ is not None:
             item.next.previous = previous
         else:
             self.tail = previous
@@ -956,7 +956,7 @@
         '#cloud-boothook': 'text/cloud-boothook'
     }
     rtype = deftype
-    for possible_type, mimetype in starts_with_mappings.items():
+    for possible_type, mimetype in list(starts_with_mappings.items()):
         if content.startswith(possible_type):
             rtype = mimetype
             break
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py	(refactored)
@@ -50,9 +50,9 @@
 
         self.facets = {}
         if 'facets' in attrs:
-            for (facet, values) in attrs['facets'].items():
+            for (facet, values) in list(attrs['facets'].items()):
                 if 'constraints' in values:
-                    self.facets[facet] = dict((k, v) for (k, v) in map(lambda x: (x['value'], x['count']), values['constraints']))RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/optionstatus.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/exceptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/contrib/ymlmessage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py

+                    self.facets[facet] = dict((k, v) for (k, v) in [(x['value'], x['count']) for x in values['constraints']])
 
         self.num_pages_needed = ceil(self.hits / self.query.real_size)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py	(refactored)
@@ -758,9 +758,9 @@
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py	(refactored)
@@ -47,9 +47,9 @@
 
         self.facets = {}
         if 'facets' in attrs:
-            for (facet, values) in attrs['facets'].items():
+            for (facet, values) in list(attrs['facets'].items()):
                 if 'buckets' in values:
-                    self.facets[facet] = dict((k, v) for (k, v) in map(lambda x: (x['value'], x['count']), values.get('buckets', [])))
+                    self.facets[facet] = dict((k, v) for (k, v) in [(x['value'], x['count']) for x in values.get('buckets', [])])
 
         self.num_pages_needed = ceil(self.hits / self.query.real_size)
 
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py	(refactored)
@@ -47,16 +47,16 @@
         self.consistent_read = consistent_read
 
     def _queue_unprocessed(self, res):
-        if u'UnprocessedKeys' not in res:
+        if 'UnprocessedKeys' not in res:
             return
-        if self.table.name not in res[u'UnprocessedKeys']:
+        if self.table.name not in res['UnprocessedKeys']:
             return
 
-        keys = res[u'UnprocessedKeys'][self.table.name][u'Keys']
+        keys = res['UnprocessedKeys'][self.table.name]['Keys']
 
         for key in keys:
-            h = key[u'HashKeyElement']
-            r = key[u'RangeKeyElement'] if u'RangeKeyElement' in key else None
+            h = key['HashKeyElement']
+            r = key['RangeKeyElement'] if 'RangeKeyElement' in key else None
             self.keys.append((h, r))
 
     def __iter__(self):
@@ -68,10 +68,10 @@
             res = batch.submit()
 
             # parse the results
-            if self.table.name not in res[u'Responses']:
+            if self.table.name not in res['Responses']:
                 continue
-            self.consumed_units += res[u'Responses'][self.table.name][u'ConsumedCapacityUnits']
-            for elem in res[u'Responses'][self.table.name][u'Items']:
+            self.consumed_units += res['Responses'][self.table.name]['ConsumedCapacityUnits']
+            for elem in res['Responses'][self.table.name]['Items']:
                 yield elem
 
             # re-queue un processed keys
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py	(refactored)
@@ -63,8 +63,8 @@
 
 if six.PY2:
     def is_str(n):
-        return (isinstance(n, basestring) or
-                isinstance(n, type) and issubclass(n, basestring))
+        return (isinstance(n, str) or
+                isinstance(n, type) and issubclass(n, str))
 
     def is_binary(n):
         return isinstance(n, Binary)
@@ -116,11 +116,11 @@
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
@@ -211,7 +211,7 @@
     This hook will transform Amazon DynamoDB JSON responses to something
     that maps directly to native Python types.
     """
-    if len(dct.keys()) > 1:
+    if len(list(dct.keys())) > 1:
         return dct
     if 'S' in dct:
         return dct['S']
@@ -286,7 +286,7 @@
                 n = str(float_to_decimal(attr))
             else:
                 n = str(DYNAMODB_CONTEXT.create_decimal(attr))
-            if list(filter(lambda x: x in n, ('Infinity', 'NaN'))):
+            if list([x for x in ('Infinity', 'NaN') if x in n]):
                 raise TypeError('Infinity and NaN not supported')
             return n
         except (TypeError, DecimalException) as e:
@@ -322,7 +322,7 @@
         return attr
 
     def _encode_m(self, attr):
-        return dict([(k, self.encode(v)) for k, v in attr.items()])
+        return dict([(k, self.encode(v)) for k, v in list(attr.items())])
 
     def _encode_l(self, attr):
         return [self.encode(i) for i in attr]
@@ -371,7 +371,7 @@
         return attr
 
     def _decode_m(self, attr):
-        return dict([(k, self.decode(v)) for k, v in attr.items()])
+        return dict([(k, self.decode(v)) for k, v in list(attr.items())])
 
     def _decode_l(self, attr):
         return [self.decode(i) for i in attr]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py	(refactored)
@@ -91,13 +91,13 @@
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
@@ -217,7 +217,7 @@
         """
         self._data = {}
 
-        for field_name, field_value in data.get('Item', {}).items():
+        for field_name, field_value in list(data.get('Item', {}).items()):
             self[field_name] = self._dynamizer.decode(field_value)
 
         self._loaded = True
@@ -245,7 +245,7 @@
         """
         raw_key_data = {}
 
-        for key, value in self.get_keys().items():
+        for key, value in list(self.get_keys().items()):
             raw_key_data[key] = self._dynamizer.encode(value)
 
         return raw_key_data
@@ -322,7 +322,7 @@
         # and hand-off to the table to handle creation/update.
         final_data = {}
 
-        for key, value in self._data.items():RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/types.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/address.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/bundleinstance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancetype.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/keypair.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/launchspecification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/placementgroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/regioninfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotdatafeedsubscription.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotpricehistory.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/zone.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/activity.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/group.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/instance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/launchconfig.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/limits.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/policy.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/request.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/scheduled.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/autoscale/tag.py

+        for key, value in list(self._data.items()):
             if not self._is_storable(value):
                 continue
 
@@ -344,14 +344,14 @@
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
@@ -395,7 +395,7 @@
         # Remove the key(s) from the ``final_data`` if present.
         # They should only be present if this is a new item, in which
         # case we shouldn't be sending as part of the data to update.
-        for fieldname, value in key.items():
+        for fieldname, value in list(key.items()):
             if fieldname in final_data:
                 del final_data[fieldname]
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py	(refactored)
@@ -431,7 +431,7 @@
         if global_indexes:
             gsi_data = []
 
-            for gsi_name, gsi_throughput in global_indexes.items():
+            for gsi_name, gsi_throughput in list(global_indexes.items()):
                 gsi_data.append({
                     "Update": {
                         "IndexName": gsi_name,
@@ -584,7 +584,7 @@
         if global_indexes:
             gsi_data = []
 
-            for gsi_name, gsi_throughput in global_indexes.items():
+            for gsi_name, gsi_throughput in list(global_indexes.items()):
                 gsi_data.append({
                     "Update": {
                         "IndexName": gsi_name,
@@ -646,7 +646,7 @@
         """
         raw_key = {}
 
-        for key, value in keys.items():
+        for key, value in list(keys.items()):
             raw_key[key] = self._dynamizer.encode(value)
 
         return raw_key
@@ -770,7 +770,7 @@
         for x, arg in enumerate(args):
             kwargs[self.schema[x].name] = arg
         ret = self.get_item(**kwargs)
-        if not ret.keys():
+        if not list(ret.keys()):
             return None
         return ret
 
@@ -996,7 +996,7 @@
 
         filters = {}
 
-        for field_and_op, value in filter_kwargs.items():
+        for field_and_op, value in list(filter_kwargs.items()):
             field_bits = field_and_op.split('__')
             fieldname = '__'.join(field_bits[:-1])
 
@@ -1329,7 +1329,7 @@
         if exclusive_start_key:
             kwargs['exclusive_start_key'] = {}
 
-            for key, value in exclusive_start_key.items():
+            for key, value in list(exclusive_start_key.items()):
                 kwargs['exclusive_start_key'][key] = \
                     self._dynamizer.encode(value)
 
@@ -1361,7 +1361,7 @@
         if raw_results.get('LastEvaluatedKey', None):
             last_key = {}
 
-            for key, value in raw_results['LastEvaluatedKey'].items():
+            for key, value in list(raw_results['LastEvaluatedKey'].items()):
                 last_key[key] = self._dynamizer.decode(value)
 
         return {
@@ -1465,7 +1465,7 @@
         if exclusive_start_key:
             kwargs['exclusive_start_key'] = {}
 
-            for key, value in exclusive_start_key.items():
+            for key, value in list(exclusive_start_key.items()):
                 kwargs['exclusive_start_key'][key] = \
                     self._dynamizer.encode(value)
 
@@ -1492,7 +1492,7 @@
         if raw_results.get('LastEvaluatedKey', None):
             last_key = {}
 
-            for key, value in raw_results['LastEvaluatedKey'].items():
+            for key, value in list(raw_results['LastEvaluatedKey'].items()):
                 last_key[key] = self._dynamizer.decode(value)
 
         return {
@@ -1564,7 +1564,7 @@
         for key_data in keys:
             raw_key = {}
 
-            for key, value in key_data.items():
+            for key, value in list(key_data.items()):
                 raw_key[key] = self._dynamizer.encode(value)
 
             items[self.table_name]['Keys'].append(raw_key)
@@ -1585,7 +1585,7 @@
         for raw_key in raw_unproccessed.get('Keys', []):
             py_key = {}
 
-            for key, value in raw_key.items():
+            for key, value in list(raw_key.items()):
                 py_key[key] = self._dynamizer.decode(value)
 
             unprocessed_keys.append(py_key)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py	(refactored)
@@ -77,7 +77,7 @@
     offering.describe()
     unit_price = float(offering.fixed_price)
     total_price = unit_price * params['quantity']
-    print('!!! You are about to purchase %d of these offerings for a total of $%.2f !!!' % (params['quantity'], total_price))
+    print(('!!! You are about to purchase %d of these offerings for a total of $%.2f !!!' % (params['quantity'], total_price)))
     answer = six.moves.input('Are you sure you want to do this?  If so, enter YES: ')
     if answer.strip().lower() == 'yes':
         offering.purchase(params['quantity'])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py	(refactored)
@@ -138,7 +138,7 @@
             tags,
             dry_run=dry_run
         )
-        for key, value in tags.items():
+        for key, value in list(tags.items()):
             if key in self.tags:
                 if value is None or value == self.tags[key]:
                     del self.tags[key]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py	(refactored)
@@ -81,13 +81,13 @@
             self.marketplace = True if value == 'true' else False
 
     def describe(self):
-        print('ID=%s' % self.id)
-        print('\tInstance Type=%s' % self.instance_type)
-        print('\tZone=%s' % self.availability_zone)
-        print('\tDuration=%s' % self.duration)
-        print('\tFixed Price=%s' % self.fixed_price)
-        print('\tUsage Price=%s' % self.usage_price)
-        print('\tDescription=%s' % self.description)
+        print(('ID=%s' % self.id))
+        print(('\tInstance Type=%s' % self.instance_type))
+        print(('\tZone=%s' % self.availability_zone))
+        print(('\tDuration=%s' % self.duration))
+        print(('\tFixed Price=%s' % self.fixed_price))
+        print(('\tUsage Price=%s' % self.usage_price))
+        print(('\tDescription=%s' % self.description))
 
     def purchase(self, instance_count=1, dry_run=False):
         return self.connection.purchase_reserved_instance_offering(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py	(refactored)
@@ -136,7 +136,7 @@
     def build_put_params(self, params, name, value=None, timestamp=None,
                          unit=None, dimensions=None, statistics=None):
         args = (name, value, unit, dimensions, statistics, timestamp)
-        length = max(map(lambda a: len(a) if isinstance(a, list) else 1, args))RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/alarm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/datapoint.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/dimension.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/listelement.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listelement.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/simpleresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/exceptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/response.py

+        length = max([len(a) if isinstance(a, list) else 1 for a in args])
 
         def aslist(a):
             if isinstance(a, list):
@@ -145,7 +145,7 @@
                 return a
             return [a] * length
 
-        for index, (n, v, u, d, s, t) in enumerate(zip(*map(aslist, args))):
+        for index, (n, v, u, d, s, t) in enumerate(zip(*list(map(aslist, args)))):
             metric_data = {'MetricName': n}
 
             if timestamp:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py	(refactored)
@@ -23,7 +23,7 @@
 from boto.connection import AWSQueryConnection, AWSAuthConnection
 from boto.exception import BotoServerError
 import time
-import urllib
+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 from boto.ecs.item import ItemSet
 from boto import handler
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py	(refactored)
@@ -383,7 +383,7 @@
         if not isinstance(new_sizes, list):
             new_sizes = [new_sizes]
 
-        instance_groups = zip(instance_group_ids, new_sizes)
+        instance_groups = list(zip(instance_group_ids, new_sizes))
 
         params = {}
         for k, ig in enumerate(instance_groups):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py	(refactored)
@@ -21,7 +21,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 
-import urllib
+import urllib.request, urllib.parse, urllib.error
 import uuid
 from boto.connection import AWSQueryConnection
 from boto.fps.exception import ResponseErrorFactory
@@ -59,8 +59,8 @@
     def decorator(func):
 
         def wrapper(*args, **kw):
-            hasgroup = lambda x: len(x) == len(filter(kw.has_key, x))
-            if 1 != len(filter(hasgroup, groups)):
+            hasgroup = lambda x: len(x) == len(list(filter(kw.has_key, x)))
+            if 1 != len(list(filter(hasgroup, groups))):
                 message = ' OR '.join(['+'.join(g) for g in groups])
                 message = "{0} requires {1} argument(s)" \
                           "".format(getattr(func, 'action', 'Method'), message)
@@ -86,7 +86,7 @@
 def api_action(*api):
 
     def decorator(func):
-        action = ''.join(api or map(str.capitalize, func.__name__.split('_')))
+        action = ''.join(api or list(map(str.capitalize, func.__name__.split('_'))))
         response = ResponseFactory(action)
         if hasattr(boto.fps.response, action + 'Response'):
             response = getattr(boto.fps.response, action + 'Response')
@@ -212,8 +212,8 @@
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
@@ -50,7 +50,7 @@
     def __repr__(self):
         render = lambda pair: '{!s}: {!r}'.format(*pair)
         do_show = lambda pair: not pair[0].startswith('_')
-        attrs = filter(do_show, self.__dict__.items())
+        attrs = list(filter(do_show, list(self.__dict__.items())))
         return '{0}({1})'.format(self.__class__.__name__,
                                ', '.join(map(render, attrs)))
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py	(refactored)
@@ -651,8 +651,8 @@
 
         """
         uri = 'vaults/%s/jobs' % vault_name
-        response_headers = [('x-amz-job-id', u'JobId'),
-                            ('Location', u'Location')]
+        response_headers = [('x-amz-job-id', 'JobId'),
+                            ('Location', 'Location')]
         json_job_data = json.dumps(job_data)
         return self.make_request('POST', uri, data=json_job_data,
                                  ok_responses=(202,),
@@ -728,9 +728,9 @@
             "Range: bytes=0-1048575". By default, this operation downloads the
             entire output.
         """
-        response_headers = [('x-amz-sha256-tree-hash', u'TreeHash'),
-                            ('Content-Range', u'ContentRange'),
-                            ('Content-Type', u'ContentType')]
+        response_headers = [('x-amz-sha256-tree-hash', 'TreeHash'),
+                            ('Content-Range', 'ContentRange'),
+                            ('Content-Type', 'ContentType')]
         headers = None
         if byte_range:
             headers = {'Range': 'bytes=%d-%d' % byte_range}
@@ -807,9 +807,9 @@
         :param description: The optional description of the archive you
             are uploading.
         """
-        response_headers = [('x-amz-archive-id', u'ArchiveId'),
-                            ('Location', u'Location'),
-                            ('x-amz-sha256-tree-hash', u'TreeHash')]
+        response_headers = [('x-amz-archive-id', 'ArchiveId'),
+                            ('Location', 'Location'),
+                            ('x-amz-sha256-tree-hash', 'TreeHash')]
         uri = 'vaults/%s/archives' % vault_name
         try:
             content_length = str(len(archive))
@@ -938,8 +938,8 @@
         :param part_size: The size of each part except the last, in bytes. The
             last part can be smaller than this part size.
         """
-        response_headers = [('x-amz-multipart-upload-id', u'UploadId'),
-                            ('Location', u'Location')]
+        response_headers = [('x-amz-multipart-upload-id', 'UploadId'),
+                            ('Location', 'Location')]
         headers = {'x-amz-part-size': str(part_size)}
         if description:
             headers['x-amz-archive-description'] = description
@@ -1029,8 +1029,8 @@
             archive. This value should be the sum of all the sizes of
             the individual parts that you uploaded.
         """
-        response_headers = [('x-amz-archive-id', u'ArchiveId'),
-                            ('Location', u'Location')]
+        response_headers = [('x-amz-archive-id', 'ArchiveId'),
+                            ('Location', 'Location')]
         headers = {'x-amz-sha256-tree-hash': sha256_treehash,
                    'x-amz-archive-size': str(archive_size)}
         uri = 'vaults/%s/multipart-uploads/%s' % (vault_name, upload_id)
@@ -1272,7 +1272,7 @@
         headers = {'x-amz-content-sha256': linear_hash,
                    'x-amz-sha256-tree-hash': tree_hash,
                    'Content-Range': 'bytes %d-%d/*' % byte_range}
-        response_headers = [('x-amz-sha256-tree-hash', u'TreeHash')]
+        response_headers = [('x-amz-sha256-tree-hash', 'TreeHash')]
         uri = 'vaults/%s/multipart-uploads/%s' % (vault_name, upload_id)
         return self.make_request('PUT', uri, headers=headers,
                                  data=part_data, ok_responses=(204,),
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/response.py	(original)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/utils.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/vault.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/writer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/acl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucketlistresultset.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/cors.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/key.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/lifecycle.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/user.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/summarymap.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/__init__.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/response.py	(refactored)
@@ -32,7 +32,7 @@
     def __init__(self, http_response, response_headers):
         self.http_response = http_response
         self.status = http_response.status
-        self[u'RequestId'] = http_response.getheader('x-amzn-requestid')
+        self['RequestId'] = http_response.getheader('x-amzn-requestid')
         if response_headers:
             for header_name, item_name in response_headers:
                 self[item_name] = http_response.getheader(header_name)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/bucket.py	(refactored)
@@ -20,7 +20,7 @@
 # IN THE SOFTWARE.
 
 import re
-import urllib
+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 
 import boto
@@ -102,7 +102,7 @@
             query_args_l.append('generation=%s' % generation)
         if response_headers:
             for rk, rv in six.iteritems(response_headers):
-                query_args_l.append('%s=%s' % (rk, urllib.quote(rv)))
+                query_args_l.append('%s=%s' % (rk, urllib.parse.quote(rv)))
         try:
             key, resp = self._get_key_internal(key_name, headers,
                                                query_args_l=query_args_l)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/gs/resumable_upload_handler.py	(refactored)
@@ -19,13 +19,13 @@
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
@@ -54,7 +54,7 @@
 class ResumableUploadHandler(object):
 
     BUFFER_SIZE = 8192
-    RETRYABLE_EXCEPTIONS = (httplib.HTTPException, IOError, socket.error,
+    RETRYABLE_EXCEPTIONS = (http.client.HTTPException, IOError, socket.error,
                             socket.gaierror)
 
     # (start, end) response indicating server has nothing (upload protocol uses
@@ -99,15 +99,15 @@
             # is attempted on a file), but warn user for other errors.
             if e.errno != errno.ENOENT:
                 # Will restart because self.tracker_uri is None.
-                print('Couldn\'t read URI tracker file (%s): %s. Restarting '
+                print(('Couldn\'t read URI tracker file (%s): %s. Restarting '
                       'upload from scratch.' %
-                      (self.tracker_file_name, e.strerror))
+                      (self.tracker_file_name, e.strerror)))
         except InvalidUriError as e:
             # Warn user, but proceed (will restart because
             # self.tracker_uri is None).
-            print('Invalid tracker URI (%s) found in URI tracker file '
+            print(('Invalid tracker URI (%s) found in URI tracker file '
                   '(%s). Restarting upload from scratch.' %
-                  (uri, self.tracker_file_name))
+                  (uri, self.tracker_file_name)))
         finally:
             if f:
                 f.close()
@@ -139,7 +139,7 @@
 
         Raises InvalidUriError if URI is syntactically invalid.
         """
-        parse_result = urlparse.urlparse(uri)
+        parse_result = urllib.parse.urlparse(uri)
         if (parse_result.scheme.lower() not in ['http', 'https'] or
             not parse_result.netloc):
             raise InvalidUriError('Invalid tracker URI (%s)' % uri)
@@ -237,8 +237,8 @@
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
@@ -252,7 +252,7 @@
                 'Couldn\'t parse upload server state query response (%s)' %
                 str(resp.getheaders()), ResumableTransferDisposition.START_OVER)
         if conn.debug >= 1:
-            print('Server has: Range: %d - %d.' % (server_start, server_end))
+            print(('Server has: Range: %d - %d.' % (server_start, server_end)))
         return (server_start, server_end)
 
     def _start_new_resumable_upload(self, key, headers=None):
@@ -452,7 +452,7 @@
                     print('Resuming transfer.')
             except ResumableUploadException as e:
                 if conn.debug >= 1:
-                    print('Unable to resume transfer (%s).' % e.message)
+                    print(('Unable to resume transfer (%s).' % e.message))
                 self._start_new_resumable_upload(key, headers)
         else:
             self._start_new_resumable_upload(key, headers)
@@ -527,19 +527,19 @@
     def handle_resumable_upload_exception(self, e, debug):
         if (e.disposition == ResumableTransferDisposition.ABORT_CUR_PROCESS):
             if debug >= 1:
-                print('Caught non-retryable ResumableUploadException (%s); '
-                      'aborting but retaining tracker file' % e.message)
+                print(('Caught non-retryable ResumableUploadException (%s); '
+                      'aborting but retaining tracker file' % e.message))
             raise
         elif (e.disposition == ResumableTransferDisposition.ABORT):
             if debug >= 1:
-                print('Caught non-retryable ResumableUploadException (%s); '
-                      'aborting and removing tracker file' % e.message)
+                print(('Caught non-retryable ResumableUploadException (%s); '
+                      'aborting and removing tracker file' % e.message))
             self._remove_tracker_file()
             raise
         else:
             if debug >= 1:
-                print('Caught ResumableUploadException (%s) - will retry' %
-                      e.message)
+                print(('Caught ResumableUploadException (%s) - will retry' %
+                      e.message))
 
     def track_progress_less_iterations(self, server_had_bytes_before_attempt,
                                        roll_back_md5=True, debug=0):
@@ -563,9 +563,9 @@
         # Use binary exponential backoff to desynchronize client requests.
         sleep_time_secs = random.random() * (2**self.progress_less_iterations)
         if debug >= 1:
-            print('Got retryable failure (%d progress-less in a row).\n'
+            print(('Got retryable failure (%d progress-less in a row).\n'
                    'Sleeping %3.1f seconds before re-trying' %
-                   (self.progress_less_iterations, sleep_time_secs))
+                   (self.progress_less_iterations, sleep_time_secs)))
         time.sleep(sleep_time_secs)
 
     def send_file(self, key, fp, headers, cb=None, num_cb=10, hash_algs=None):
@@ -664,7 +664,7 @@
                 return
             except self.RETRYABLE_EXCEPTIONS as e:
                 if debug >= 1:
-                    print('Caught exception (%s)' % e.__repr__())
+                    print(('Caught exception (%s)' % e.__repr__()))
                 if isinstance(e, IOError) and e.errno == errno.EPIPE:
                     # Broken pipe error causes httplib to immediately
                     # close the socket (http://bugs.python.org/issue5542),
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py	(refactored)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/task.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/interactive.py

@@ -1110,7 +1110,7 @@
                 return assume_role_policy_document
         else:
 
-            for tld, policy in DEFAULT_POLICY_DOCUMENTS.items():
+            for tld, policy in list(DEFAULT_POLICY_DOCUMENTS.items()):
                 if tld is 'default':
                     # Skip the default. We'll fall back to it if we don't find
                     # anything.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/cmdshell.py	(refactored)
@@ -87,9 +87,9 @@
                 else:
                     raise
             except paramiko.BadHostKeyException:
-                print("%s has an entry in ~/.ssh/known_hosts and it doesn't match" % self.server.hostname)
+                print(("%s has an entry in ~/.ssh/known_hosts and it doesn't match" % self.server.hostname))
                 print('Edit that file to remove the entry and then hit return to try again')
-                raw_input('Hit Enter when ready')
+                input('Hit Enter when ready')
                 retry += 1
             except EOFError:
                 print('Unexpected Error from SSH Connection, retry in 5 seconds')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/propget.py	(refactored)
@@ -37,8 +37,8 @@
                 value = choices[i-1]
                 if isinstance(value, tuple):
                     value = value[0]
-                print('[%d] %s' % (i, value))
-            value = raw_input('%s [%d-%d]: ' % (prompt, min, max))
+                print(('[%d] %s' % (i, value)))
+            value = input('%s [%d-%d]: ' % (prompt, min, max))
             try:
                 int_value = int(value)
                 value = choices[int_value-1]
@@ -46,11 +46,11 @@
                     value = value[1]
                 valid = True
             except ValueError:
-                print('%s is not a valid choice' % value)
+                print(('%s is not a valid choice' % value))
             except IndexError:
-                print('%s is not within the range[%d-%d]' % (min, max))
+                print(('%s is not within the range[%d-%d]' % (min, max)))
         else:
-            value = raw_input('%s: ' % prompt)
+            value = input('%s: ' % prompt)
             try:
                 value = prop.validate(value)
                 if prop.empty(value) and prop.required:
@@ -58,6 +58,6 @@
                 else:
                     valid = True
             except:
-                print('Invalid value: %s' % value)
+                print(('Invalid value: %s' % value))
     return value
         
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/server.py	(refactored)
@@ -118,8 +118,8 @@
         print('running the following command on the remote server:')
         print(command)
         t = self.ssh_client.run(command)
-        print('\t%s' % t[0])
-        print('\t%s' % t[1])
+        print(('\t%s' % t[0]))
+        print(('\t%s' % t[1]))
         print('...complete!')
         print('registering image...')
         self.image_id = self.server.ec2.register_image(name=prefix, image_location='%s/%s.manifest.xml' % (bucket, prefix))
@@ -137,7 +137,7 @@
 
     def get_region(self, params):
         region = params.get('region', None)
-        if isinstance(region, basestring):
+        if isinstance(region, str):
             region = boto.ec2.get_region(region)
             params['region'] = region
         if not region:
@@ -189,7 +189,7 @@
 
     def get_group(self, params):
         group = params.get('group', None)
-        if isinstance(group, basestring):
+        if isinstance(group, str):
             group_list = self.ec2.get_all_security_groups()
             for g in group_list:
                 if g.name == group:
@@ -202,7 +202,7 @@
 
     def get_key(self, params):
         keypair = params.get('keypair', None)
-        if isinstance(keypair, basestring):
+        if isinstance(keypair, str):
             key_list = self.ec2.get_all_key_pairs()
             for k in key_list:
                 if k.name == keypair:
@@ -332,7 +332,7 @@
             while instance.update() != 'running':
                 time.sleep(1)
             instance.use_ip(elastic_ip)
-            print('set the elastic IP of the first instance to %s' % elastic_ip)
+            print(('set the elastic IP of the first instance to %s' % elastic_ip))
         for instance in instances:
             s = cls()
             s.ec2 = ec2
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/test_manage.py	(refactored)
@@ -19,16 +19,16 @@
 
 print('--> Run "df -k" on Server')
 status = server.run('df -k')
-print(status[1])
+print((status[1]))
 
 print('--> Now run volume.make_ready to make the volume ready to use on server')
 volume.make_ready(server)
 
 print('--> Run "df -k" on Server')
 status = server.run('df -k')
-print(status[1])
+print((status[1]))
 
 print('--> Do an "ls -al" on the new filesystem')
 status = server.run('ls -al %s' % volume.mount_point)
-print(status[1])
+print((status[1]))
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/manage/volume.py	(refactored)
@@ -18,7 +18,7 @@
 # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
-from __future__ import print_function
+
 
 from boto.sdb.db.model import Model
 from boto.sdb.db.property import StringProperty, IntegerProperty, ListProperty, ReferenceProperty, CalculatedProperty
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/interactive.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/interactive.py	(refactored)
@@ -15,7 +15,7 @@
 # You should have received a copy of the GNU Lesser General Public License
 # along with Paramiko; if not, write to the Free Software Foundation, Inc.,
 # 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.
-from __future__ import print_function
+
 
 import socket
 import sys
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py	(refactored)
@@ -39,24 +39,24 @@
             n = 1
             choices = []
             for item in item_list:
-                if isinstance(item, basestring):
-                    print('[%d] %s' % (n, item))
+                if isinstance(item, str):
+                    print(('[%d] %s' % (n, item)))
                     choices.append(item)
                     n += 1
                 else:
                     obj, id, desc = item
                     if desc:
                         if desc.find(search_str) >= 0:
-                            print('[%d] %s - %s' % (n, id, desc))
+                            print(('[%d] %s - %s' % (n, id, desc)))
                             choices.append(obj)
                             n += 1
                     else:
                         if id.find(search_str) >= 0:
-                            print('[%d] %s' % (n, id))RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/iobject.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/layoutparam.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/notification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/price.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/qualification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py

+                            print(('[%d] %s' % (n, id)))
                             choices.append(obj)
                             n += 1
             if choices:
-                val = raw_input('%s[1-%d]: ' % (prompt, len(choices)))
+                val = input('%s[1-%d]: ' % (prompt, len(choices)))
                 if val.startswith('/'):
                     search_str = val[1:]
                 else:
@@ -66,10 +66,10 @@
                             return None
                         choice = choices[int_val-1]
                     except ValueError:
-                        print('%s is not a valid choice' % val)
+                        print(('%s is not a valid choice' % val))
                     except IndexError:
-                        print('%s is not within the range[1-%d]' % (val,
-                                                                    len(choices)))
+                        print(('%s is not within the range[1-%d]' % (val,
+                                                                    len(choices))))
             else:
                 print("No objects matched your pattern")
                 search_str = ''
@@ -78,11 +78,11 @@
     def get_string(self, prompt, validation_fn=None):
         okay = False
         while not okay:
-            val = raw_input('%s: ' % prompt)
+            val = input('%s: ' % prompt)
             if validation_fn:
                 okay = validation_fn(val)
                 if not okay:
-                    print('Invalid value: %s' % val)
+                    print(('Invalid value: %s' % val))
             else:
                 okay = True
         return val
@@ -91,7 +91,7 @@
         okay = False
         val = ''
         while not okay:
-            val = raw_input('%s: %s' % (prompt, val))
+            val = input('%s: %s' % (prompt, val))
             val = os.path.expanduser(val)
             if os.path.isfile(val):
                 okay = True
@@ -104,7 +104,7 @@
                 else:
                     val = ''
             else:
-                print('Invalid value: %s' % val)
+                print(('Invalid value: %s' % val))
                 val = ''
         return val
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/order.py	(refactored)
@@ -175,8 +175,8 @@
         print() 
         print('QTY\tNAME\tTYPE\nAMI\t\tGroups\t\t\tKeyPair')
         for item in self.items:
-            print('%s\t%s\t%s\t%s\t%s\t%s' % (item.quantity, item.name, item.instance_type,
-                                              item.ami.id, item.groups, item.key.name))
+            print(('%s\t%s\t%s\t%s\t%s\t%s' % (item.quantity, item.name, item.instance_type,
+                                              item.ami.id, item.groups, item.key.name)))
 
     def place(self, block=True):
         if get_domain() is None:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mashups/server.py	(refactored)
@@ -298,7 +298,7 @@
         path, name = os.path.split(cert_file)
         remote_cert_file = '/mnt/%s' % name
         self.put_file(cert_file, remote_cert_file)
-        print('\tdeleting %s' % BotoConfigPath)
+        print(('\tdeleting %s' % BotoConfigPath))
         # delete the metadata.ini file if it exists
         try:
             sftp_client.remove(BotoConfigPath)
@@ -314,11 +314,11 @@
             command += '-r i386'
         else:
             command += '-r x86_64'
-        print('\t%s' % command)
+        print(('\t%s' % command))
         t = ssh_client.exec_command(command)
         response = t[1].read()
-        print('\t%s' % response)
-        print('\t%s' % t[2].read())
+        print(('\t%s' % response))
+        print(('\t%s' % t[2].read()))
         print('...complete!')
 
     def upload_bundle(self, bucket, prefix):
@@ -328,12 +328,12 @@
         command += '-b %s ' % bucket
         command += '-a %s ' % self.ec2.aws_access_key_id
         command += '-s %s ' % self.ec2.aws_secret_access_key
-        print('\t%s' % command)
+        print(('\t%s' % command))
         ssh_client = self.get_ssh_client()
         t = ssh_client.exec_command(command)
         response = t[1].read()
-        print('\t%s' % response)
-        print('\t%s' % t[2].read())
+        print(('\t%s' % response))
+        print(('\t%s' % t[2].read()))
         print('...complete!')
 
     def create_image(self, bucket=None, prefix=None, key_file=None, cert_file=None, size=None):
@@ -384,12 +384,12 @@
         return self.ec2.detach_volume(volume_id=volume_id, instance_id=self.instance_id)
 
     def install_package(self, package_name):
-        print('installing %s...' % package_name)
+        print(('installing %s...' % package_name))
         command = 'yum -y install %s' % package_name
-        print('\t%s' % command)
+        print(('\t%s' % command))
         ssh_client = self.get_ssh_client()
         t = ssh_client.exec_command(command)
         response = t[1].read()
-        print('\t%s' % response)
-        print('\t%s' % t[2].read())
+        print(('\t%s' % response))
+        print(('\t%s' % t[2].read()))
         print('...complete!')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/connection.py	(refactored)
@@ -322,7 +322,7 @@
         total_records = int(search_rs.TotalNumResults)
         get_page_hits = lambda page: self.search_hits(page_size=page_size, page_number=page)
         page_nums = self._get_pages(page_size, total_records)
-        hit_sets = itertools.imap(get_page_hits, page_nums)
+        hit_sets = map(get_page_hits, page_nums)
         return itertools.chain.from_iterable(hit_sets)
 
     def search_hits(self, sort_by='CreationTime', sort_direction='Ascending',
@@ -676,7 +676,7 @@
             params['TestDurationInSeconds'] = test_duration
 
         if answer_key is not None:
-            if isinstance(answer_key, basestring):
+            if isinstance(answer_key, str):
                 params['AnswerKey'] = answer_key  # xml
             else:
                 raise TypeError
@@ -705,7 +705,7 @@
         total_records = int(search_qual.TotalNumResults)
         get_page_quals = lambda page: self.get_qualifications_for_qualification_type(qualification_type_id = qualification_type_id, page_size=page_size, page_number = page)
         page_nums = self._get_pages(page_size, total_records)
-        qual_sets = itertools.imap(get_page_quals, page_nums)
+        qual_sets = map(get_page_quals, page_nums)
         return itertools.chain.from_iterable(qual_sets)
 
     def get_qualifications_for_qualification_type(self, qualification_type_id, page_size=100, page_number = 1):
@@ -744,7 +744,7 @@
             params['TestDurationInSeconds'] = test_duration
 
         if answer_key is not None:
-            if isinstance(answer_key, basestring):
+            if isinstance(answer_key, str):
                 params['AnswerKey'] = answer_key  # xml
             else:
                 raise TypeError
@@ -862,7 +862,7 @@
             keywords = ', '.join(keywords)
         if isinstance(keywords, str):
             final_keywords = keywords
-        elif isinstance(keywords, unicode):
+        elif isinstance(keywords, str):
             final_keywords = keywords.encode('utf-8')
         elif keywords is None:
             final_keywords = ""
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mturk/question.py	(refactored)
@@ -51,8 +51,8 @@
     class ValidatingXML(object):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/bootstrap.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/helloworld.py

 
         def validate(self):
-            import urllib2
-            schema_src_file = urllib2.urlopen(self.schema_url)
+            import urllib.request, urllib.error, urllib.parse
+            schema_src_file = urllib.request.urlopen(self.schema_url)
             schema_doc = etree.parse(schema_src_file)
             schema = etree.XMLSchema(schema_doc)
             doc = etree.fromstring(self.get_as_xml())
@@ -128,7 +128,7 @@
     def get_inner_content(self, content):
         content.append_field('Width', self.width)
         content.append_field('Height', self.height)
-        for name, value in self.parameters.items():
+        for name, value in list(self.parameters.items()):
             value = self.parameter_template % vars()
             content.append_field('ApplicationParameter', value)
 
@@ -286,7 +286,7 @@
 
 class Constraint(object):
     def get_attributes(self):
-        pairs = zip(self.attribute_names, self.attribute_values)
+        pairs = list(zip(self.attribute_names, self.attribute_values))
         attrs = ' '.join(
             '%s="%d"' % (name, value)
             for (name, value) in pairs
@@ -323,7 +323,7 @@
         self.attribute_values = pattern, error_text, flags
 
     def get_attributes(self):
-        pairs = zip(self.attribute_names, self.attribute_values)
+        pairs = list(zip(self.attribute_names, self.attribute_values))
         attrs = ' '.join(
             '%s="%s"' % (name, value)
             for (name, value) in pairs
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/connection.py	(refactored)
@@ -134,7 +134,7 @@
 
         def wrapper(*args, **kw):
             members = kwargs.get('members', False)
-            for field in filter(lambda i: i in kw, fields):
+            for field in [i for i in fields if i in kw]:
                 destructure_object(kw.pop(field), kw, field, members=members)
             return func(*args, **kw)
         wrapper.__doc__ = "{0}\nElement|Iter|Map: {1}\n" \
@@ -236,7 +236,7 @@
 
     def decorator(func, quota=int(quota), restore=float(restore)):
         version, accesskey, path = api_version_path[section]
-        action = ''.join(api or map(str.capitalize, func.__name__.split('_')))
+        action = ''.join(api or list(map(str.capitalize, func.__name__.split('_'))))
 
         def wrapper(self, *args, **kw):
             kw.setdefault(accesskey, getattr(self, accesskey, None))
@@ -274,12 +274,12 @@
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
@@ -417,7 +417,7 @@
     def get_service_status(self, **kw):
         """Instruct the user on how to get service status.
         """
-        sections = ', '.join(map(str.lower, api_version_path.keys()))
+        sections = ', '.join(map(str.lower, list(api_version_path.keys())))
         message = "Use {0}.get_(section)_service_status(), " \
                   "where (section) is one of the following: " \
                   "{1}".format(self.__class__.__name__, sections)
@@ -721,10 +721,10 @@
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
@@ -27,7 +27,7 @@
     def __call__(self, status, reason, body=None):
         server = BotoServerError(status, reason, body=body)
         supplied = self.find_element(server.error_code, '', ResponseError)
-        print(supplied.__name__)
+        print((supplied.__name__))
         return supplied(status, reason, body=body)
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/mws/response.py	(refactored)
@@ -42,7 +42,7 @@
         self._hint = JITResponse
         self._hint.__name__ = 'JIT_{0}/{1}'.format(self.__class__.__name__,
                                                    hex(id(self._hint))[2:])
-        for name, value in kw.items():
+        for name, value in list(kw.items()):
             setattr(self._hint, name, value)
 
     def __repr__(self):
@@ -202,7 +202,7 @@
         scope = inherit(self.__class__)
         scope.update(self.__dict__)
         declared = lambda attr: isinstance(attr[1], DeclarativeType)
-        for name, node in filter(declared, scope.items()):
+        for name, node in filter(declared, list(scope.items())):
             getattr(node, op)(self, name, parentname=self._name, **kw)
 
     @property
@@ -212,7 +212,7 @@
     def __repr__(self):
         render = lambda pair: '{0!s}: {1!r}'.format(*pair)
         do_show = lambda pair: not pair[0].startswith('_')
-        attrs = filter(do_show, self.__dict__.items())
+        attrs = list(filter(do_show, list(self.__dict__.items())))
         name = self.__class__.__name__
         if name.startswith('JIT_'):
             name = '^{0}^'.format(self._name or '')
@@ -415,7 +415,7 @@
 
     def __repr__(self):
         values = [getattr(self, key, None) for key in self._dimensions]
-        values = filter(None, values)
+        values = [_f for _f in values if _f]
         return 'x'.join(map('{0.Value:0.2f}{0[Units]}'.format, values))
 
     @strip_namespace
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py	(refactored)
@@ -178,7 +178,7 @@
     def dump(self):
         s = StringIO()
         self.write(s)
-        print(s.getvalue())
+        print((s.getvalue()))
 
     def dump_safe(self, fp=None):
         if not fp:
@@ -211,11 +211,11 @@
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
@@ -21,7 +21,7 @@
 #
 import boto
 from boto.pyami.scriptbase import ScriptBase
-import os, StringIO
+import os, io
 
 class CopyBot(ScriptBase):
 
@@ -82,7 +82,7 @@
         key.set_contents_from_filename(self.log_path)
 
     def main(self):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/startup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/apache.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/ebs.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/mysql.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/trac.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbinstance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsecuritygroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsnapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/dbsubnetgroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/event.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/logfile.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/optiongroup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/statusinfo.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/vpcsecuritygroupmembership.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py

-        fp = StringIO.StringIO()
+        fp = io.StringIO()
         boto.config.dump_safe(fp)
         self.notify('%s (%s) Starting' % (self.name, self.instance_id), fp.getvalue())
         if self.src and self.dst:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py	(refactored)
@@ -124,14 +124,14 @@
     required = ['ami']
     for pname in required:
         if not params.get(pname, None):
-            print('%s is required' % pname)
+            print(('%s is required' % pname))
             usage()
     if params['script_name']:
         # first copy the desired module file to S3 bucket
         if reload:
-            print('Reloading module %s to S3' % params['script_name'])
+            print(('Reloading module %s to S3' % params['script_name']))
         else:
-            print('Copying module %s to S3' % params['script_name'])
+            print(('Copying module %s to S3' % params['script_name']))
         l = imp.find_module(params['script_name'])
         c = boto.connect_s3()
         bucket = c.get_bucket(params['script_bucket'])
@@ -140,7 +140,7 @@
         params['script_md5'] = key.md5
     # we have everything we need, now build userdata string
     l = []
-    for k, v in params.items():
+    for k, v in list(params.items()):
         if v:
             l.append('%s=%s' % (k, v))
     c = boto.connect_ec2()
@@ -155,10 +155,10 @@
         r = img.run(user_data=s, key_name=params['keypair'],
                     security_groups=[params['group']],
                     max_count=params.get('num_instances', 1))
-        print('AMI: %s - %s (Started)' % (params['ami'], img.location))
-        print('Reservation %s contains the following instances:' % r.id)
+        print(('AMI: %s - %s (Started)' % (params['ami'], img.location)))
+        print(('Reservation %s contains the following instances:' % r.id))
         for i in r.instances:
-            print('\t%s' % i.id)
+            print(('\t%s' % i.id))
         if wait:
             running = False
             while not running:
@@ -169,9 +169,9 @@
                 if status.count('running') == len(r.instances):
                     running = True
             for i in r.instances:
-                print('Instance: %s' % i.ami_launch_index)
-                print('Public DNS Name: %s' % i.public_dns_name)
-                print('Private DNS Name: %s' % i.private_dns_name)
+                print(('Instance: %s' % i.ami_launch_index))
+                print(('Public DNS Name: %s' % i.public_dns_name))
+                print(('Private DNS Name: %s' % i.private_dns_name))
 
 if __name__ == "__main__":
     main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/installer.py	(refactored)
@@ -43,7 +43,7 @@
             hour = str(random.randrange(24))
         fp = open('/etc/cron.d/%s' % name, "w")
         if env:
-            for key, value in env.items():
+            for key, value in list(env.items()):
                 fp.write('%s=%s\n' % (key, value))
         fp.write('%s %s %s %s %s %s %s\n' % (minute, hour, mday, month, wday, who, command))
         fp.close()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/__init__.py	(refactored)
@@ -20,7 +20,7 @@
 # IN THE SOFTWARE.
 #
 
-import urllib
+import urllib.request, urllib.parse, urllib.error
 from boto.connection import AWSQueryConnection
 from boto.rds.dbinstance import DBInstance
 from boto.rds.dbsecuritygroup import DBSecurityGroup
@@ -451,7 +451,7 @@
             self.build_list_params(params, l, 'VpcSecurityGroupIds.member')
 
         # Remove any params set to None
-        for k, v in params.items():
+        for k, v in list(params.items()):
           if v is None: del(params[k])
 
         return self.get_object('CreateDBInstance', params, DBInstance)
@@ -990,7 +990,7 @@
         if ec2_security_group_owner_id:
             params['EC2SecurityGroupOwnerId'] = ec2_security_group_owner_id
         if cidr_ip:
-            params['CIDRIP'] = urllib.quote(cidr_ip)
+            params['CIDRIP'] = urllib.parse.quote(cidr_ip)
         return self.get_object('AuthorizeDBSecurityGroupIngress', params,
                                DBSecurityGroup)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds/parametergroup.py	(refactored)
@@ -133,7 +133,7 @@
             d[prefix+'ApplyMethod'] = self.apply_method
 
     def _set_string_value(self, value):
-        if not isinstance(value, basestring):
+        if not isinstance(value, str):
             raise ValueError('value must be of type str')
         if self.allowed_values:
             choices = self.allowed_values.split(',')
@@ -142,9 +142,9 @@
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
@@ -156,7 +156,7 @@
     def _set_boolean_value(self, value):
         if isinstance(value, bool):
             self._value = value
-        elif isinstance(value, basestring):
+        elif isinstance(value, str):
             if value.lower() == 'true':
                 self._value = True
             else:
@@ -180,7 +180,7 @@
         if self.type == 'string':
             return self._value
         elif self.type == 'integer':
-            if not isinstance(self._value, int) and not isinstance(self._value, long):
+            if not isinstance(self._value, int) and not isinstance(self._value, int):
                 self._set_integer_value(self._value)
             return self._value
         elif self.type == 'boolean':
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py	(refactored)
@@ -46,7 +46,7 @@
             else:
                 debugger.post_mortem(tb)
         elif debug_flag:
-            print(traceback.print_tb(tb))
+            print((traceback.print_tb(tb)))
             sys.exit(1)
         else:
             print(value)
@@ -68,7 +68,7 @@
 
     def print_it(self):
         if not self.printed:
-            print(self.line)
+            print((self.line))
             self.printed = True
 
 class RequiredParamError(boto.exception.BotoClientError):
@@ -343,7 +343,7 @@
         if hasattr(options, 'help_filters') and options.help_filters:
             print('Available filters:')
             for filter in self.Filters:
-                print('%s\t%s' % (filter.name, filter.doc))
+                print(('%s\t%s' % (filter.name, filter.doc)))
             sys.exit(0)
         if options.debug:
             self.args['debug'] = 2
@@ -455,7 +455,7 @@
             print(e)
             sys.exit(1)
         except self.ServiceClass.ResponseError as err:
-            print('Error(%s): %s' % (err.error_code, err.error_message))
+            print(('Error(%s): %s' % (err.error_code, err.error_message)))
             sys.exit(1)
         except boto.roboto.awsqueryservice.NoCredentialsError as err:RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/acl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlistresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/cors.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/deletemarker.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py

             print('Unable to find credentials.')
@@ -482,7 +482,7 @@
                 if isinstance(item, dict):
                     for field_name in item:
                         line.append(item[field_name])
-                elif isinstance(item, basestring):
+                elif isinstance(item, str):
                     line.append(item)
                 line.print_it()
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py	(refactored)
@@ -1,6 +1,6 @@
-from __future__ import print_function
+
 import os
-import urlparse
+import urllib.parse
 import boto
 import boto.connection
 import boto.jsonresponse
@@ -96,7 +96,7 @@
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
@@ -27,7 +27,7 @@
     @classmethod
     def convert_string(cls, param, value):
         # TODO: could do length validation, etc. here
-        if not isinstance(value, basestring):
+        if not isinstance(value, str):
             raise ValueError
         return value
 
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucket.py	(refactored)
@@ -369,7 +369,7 @@
         if initial_query_string:
             pairs.append(initial_query_string)
 
-        for key, value in sorted(params.items(), key=lambda x: x[0]):
+        for key, value in sorted(list(params.items()), key=lambda x: x[0]):
             if value is None:
                 continue
             key = key.replace('_', '-')
@@ -380,7 +380,7 @@
             if not isinstance(value, six.binary_type):
                 value = value.encode('utf-8')
             if value:
-                pairs.append(u'%s=%s' % (
+                pairs.append('%s=%s' % (
                     urllib.parse.quote(key),
                     urllib.parse.quote(value)
                 ))
@@ -664,10 +664,10 @@
 
         def delete_keys2(hdrs):
             hdrs = hdrs or {}
-            data = u"""<?xml version="1.0" encoding="UTF-8"?>"""
-            data += u"<Delete>"
+            data = """<?xml version="1.0" encoding="UTF-8"?>"""
+            data += "<Delete>"
             if quiet:
-                data += u"<Quiet>true</Quiet>"
+                data += "<Quiet>true</Quiet>"
             count = 0
             while count < 1000:
                 try:
@@ -694,11 +694,11 @@
                     result.errors.append(error)
                     continue
                 count += 1
-                data += u"<Object><Key>%s</Key>" % xml.sax.saxutils.escape(key_name)
+                data += "<Object><Key>%s</Key>" % xml.sax.saxutils.escape(key_name)
                 if version_id:
-                    data += u"<VersionId>%s</VersionId>" % version_id
-                data += u"</Object>"
-            data += u"</Delete>"
+                    data += "<VersionId>%s</VersionId>" % version_id
+                data += "</Object>"
+            data += "</Delete>"
             if count <= 0:
                 return False  # no more
             data = data.encode('utf-8')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/bucketlogging.py	(refactored)
@@ -66,18 +66,18 @@
 
     def to_xml(self):
         # caller is responsible to encode to utf-8
-        s = u'<?xml version="1.0" encoding="UTF-8"?>'
-        s += u'<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">'
+        s = '<?xml version="1.0" encoding="UTF-8"?>'
+        s += '<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">'
         if self.target is not None:
-            s += u'<LoggingEnabled>'
-            s += u'<TargetBucket>%s</TargetBucket>' % self.target
+            s += '<LoggingEnabled>'
+            s += '<TargetBucket>%s</TargetBucket>' % self.target
             prefix = self.prefix or ''
-            s += u'<TargetPrefix>%s</TargetPrefix>' % xml.sax.saxutils.escape(prefix)
+            s += '<TargetPrefix>%s</TargetPrefix>' % xml.sax.saxutils.escape(prefix)
             if self.grants:
                 s += '<TargetGrants>'
                 for grant in self.grants:
                     s += grant.to_xml()
                 s += '</TargetGrants>'
-            s += u'</LoggingEnabled>'
-        s += u'</BucketLoggingStatus>'
+            s += '</LoggingEnabled>'
+        s += '</BucketLoggingStatus>'
         return s
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/connection.py	(refactored)
@@ -395,7 +395,7 @@
         if version_id is not None:
             extra_qp.append("versionId=%s" % version_id)
         if response_headers:
-            for k, v in response_headers.items():
+            for k, v in list(response_headers.items()):
                 extra_qp.append("%s=%s" % (k, urllib.parse.quote(v)))
         if self.provider.security_token:
             headers['x-amz-security-token'] = self.provider.security_token
@@ -414,7 +414,7 @@
             query_part = ''
         if headers:
             hdr_prefix = self.provider.header_prefix
-            for k, v in headers.items():
+            for k, v in list(headers.items()):
                 if k.startswith(hdr_prefix):
                     # headers used for sig generation must be
                     # included in the url also.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/key.py	(refactored)
@@ -136,9 +136,9 @@
 
     def __repr__(self):
         if self.bucket:
-            name = u'<Key: %s,%s>' % (self.bucket.name, self.name)
+            name = '<Key: %s,%s>' % (self.bucket.name, self.name)
         else:
-            name = u'<Key: None,%s>' % self.name
+            name = '<Key: None,%s>' % self.name
 
         # Encode to bytes for Python 2 to prevent display decoding issues
         if not isinstance(name, str):
@@ -304,7 +304,7 @@
             response_headers = self.resp.msg
             self.metadata = boto.utils.get_aws_metadata(response_headers,
                                                         provider)
-            for name, value in response_headers.items():
+            for name, value in list(response_headers.items()):
                 # To get correct size for Range GETs, use Content-RangeRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/lifecycle.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multidelete.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/multipart.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/prefix.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/tagging.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/user.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/website.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/item.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/key.py

                 # header if one was returned. If not, use Content-Length
                 # header.
@@ -372,7 +372,7 @@
         self.mode = None
         self.closed = True
 
-    def next(self):
+    def __next__(self):
         """
         By providing a next method, the key object supports use as an iterator.
         For example, you can now say:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/keyfile.py	(refactored)
@@ -112,7 +112,7 @@
   def flush(self):
     raise NotImplementedError('flush not implemented in KeyFile')
 
-  def next(self):
+  def __next__(self):
     raise NotImplementedError('next not implemented in KeyFile')
 
   def readinto(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/s3/resumable_download_handler.py	(refactored)
@@ -19,7 +19,7 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 import errno
-import httplib
+import http.client
 import os
 import re
 import socket
@@ -92,7 +92,7 @@
 
     MIN_ETAG_LEN = 5
 
-    RETRYABLE_EXCEPTIONS = (httplib.HTTPException, IOError, socket.error,
+    RETRYABLE_EXCEPTIONS = (http.client.HTTPException, IOError, socket.error,
                             socket.gaierror)
 
     def __init__(self, tracker_file_name=None, num_retries=None):
@@ -132,17 +132,17 @@
             # read correctly. Since ETags need not be MD5s, we now do a simple
             # length sanity check instead.
             if len(self.etag_value_for_current_download) < self.MIN_ETAG_LEN:
-                print('Couldn\'t read etag in tracker file (%s). Restarting '
-                      'download from scratch.' % self.tracker_file_name)
+                print(('Couldn\'t read etag in tracker file (%s). Restarting '
+                      'download from scratch.' % self.tracker_file_name))
         except IOError as e:
             # Ignore non-existent file (happens first time a download
             # is attempted on an object), but warn user for other errors.
             if e.errno != errno.ENOENT:
                 # Will restart because
                 # self.etag_value_for_current_download is None.
-                print('Couldn\'t read URI tracker file (%s): %s. Restarting '
+                print(('Couldn\'t read URI tracker file (%s): %s. Restarting '
                       'download from scratch.' %
-                      (self.tracker_file_name, e.strerror))
+                      (self.tracker_file_name, e.strerror)))
         finally:
             if f:
                 f.close()
@@ -288,7 +288,7 @@
                 return
             except self.RETRYABLE_EXCEPTIONS as e:
                 if debug >= 1:
-                    print('Caught exception (%s)' % e.__repr__())
+                    print(('Caught exception (%s)' % e.__repr__()))
                 if isinstance(e, IOError) and e.errno == errno.EPIPE:
                     # Broken pipe error causes httplib to immediately
                     # close the socket (http://bugs.python.org/issue5542),
@@ -304,21 +304,21 @@
                 if (e.disposition ==
                     ResumableTransferDisposition.ABORT_CUR_PROCESS):
                     if debug >= 1:
-                        print('Caught non-retryable ResumableDownloadException '
-                              '(%s)' % e.message)
+                        print(('Caught non-retryable ResumableDownloadException '
+                              '(%s)' % e.message))
                     raise
                 elif (e.disposition ==
                     ResumableTransferDisposition.ABORT):
                     if debug >= 1:
-                        print('Caught non-retryable ResumableDownloadException '
+                        print(('Caught non-retryable ResumableDownloadException '
                               '(%s); aborting and removing tracker file' %
-                              e.message)
+                              e.message))
                     self._remove_tracker_file()
                     raise
                 else:
                     if debug >= 1:
-                        print('Caught ResumableDownloadException (%s) - will '
-                              'retry' % e.message)
+                        print(('Caught ResumableDownloadException (%s) - will '
+                              'retry' % e.message))
 
             # At this point we had a re-tryable failure; see if made progress.
             if get_cur_file_size(fp) > had_file_bytes_before_attempt:
@@ -341,12 +341,12 @@
             # which we can safely ignore.
             try:
                 key.close()
-            except httplib.IncompleteRead:
+            except http.client.IncompleteRead:
                 pass
 
             sleep_time_secs = 2**progress_less_iterations
             if debug >= 1:
-                print('Got retryable failure (%d progress-less in a row).\n'
+                print(('Got retryable failure (%d progress-less in a row).\n'
                       'Sleeping %d seconds before re-trying' %
-                      (progress_less_iterations, sleep_time_secs))
+                      (progress_less_iterations, sleep_time_secs)))
             time.sleep(sleep_time_secs)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/connection.py	(refactored)
@@ -173,14 +173,14 @@
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
@@ -234,9 +234,9 @@
             requests made on this specific connection instance. It is by
             no means an account-wide estimate.
         """
-        print('Total Usage: %f compute seconds' % self.box_usage)
+        print(('Total Usage: %f compute seconds' % self.box_usage))
         cost = self.box_usage * 0.14
-        print('Approximate Cost: $%f' % cost)
+        print(('Approximate Cost: $%f' % cost))
 
     def get_domain(self, domain_name, validate=True):
         """
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/domain.py	(refactored)
@@ -18,7 +18,7 @@
 # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
-from __future__ import print_function
+
 
 """
 Represents an SDB Domain
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/queryresultset.py	(refactored)
@@ -89,5 +89,5 @@
                 raise StopIteration
             more_results = self.next_token is not None
 
-    def next(self):
+    def __next__(self):
         return next(self.__iter__())
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/blob.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/property.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/test_db.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py

@@ -31,7 +31,7 @@
 
     @property
     def file(self):
-        from StringIO import StringIO
+        from io import StringIO
         if self._file:
             f = self._file
         else:
@@ -60,7 +60,7 @@
     def readline(self):
         return self.file.readline()
 
-    def next(self):
+    def __next__(self):
         return next(self.file)
 
     def __iter__(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/model.py	(refactored)
@@ -37,12 +37,12 @@
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
@@ -57,8 +57,7 @@
             # Model class, defined below.
             pass
 
-class Model(object):
-    __metaclass__ = ModelMeta
+class Model(object, metaclass=ModelMeta):
     __consistent__ = False # Consistent is set off by default
     id = None
 
@@ -95,7 +94,7 @@
     @classmethod
     def find(cls, limit=None, next_token=None, **params):
         q = Query(cls, limit=limit, next_token=next_token)
-        for key, value in params.items():
+        for key, value in list(params.items()):
             q.filter('%s =' % key, value)
         return q
 
@@ -111,7 +110,7 @@
     def properties(cls, hidden=True):
         properties = []
         while cls:
-            for key in cls.__dict__.keys():
+            for key in list(cls.__dict__.keys()):
                 prop = cls.__dict__[key]
                 if isinstance(prop, Property):
                     if hidden or not prop.__class__.__name__.startswith('_'):
@@ -126,7 +125,7 @@
     def find_property(cls, prop_name):
         property = None
         while cls:
-            for key in cls.__dict__.keys():
+            for key in list(cls.__dict__.keys()):
                 prop = cls.__dict__[key]
                 if isinstance(prop, Property):
                     if not prop.__class__.__name__.startswith('_') and prop_name == prop.name:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/query.py	(refactored)
@@ -39,7 +39,7 @@
     def __iter__(self):
         return iter(self.manager.query(self))
 
-    def next(self):
+    def __next__(self):
         if self.__local_iter__ is None:
             self.__local_iter__ = self.__iter__()
         return next(self.__local_iter__)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/sequence.py	(refactored)
@@ -215,7 +215,7 @@
 
     db = property(_connect)
 
-    def next(self):
+    def __next__(self):
         self.val = self.fnc(self.val, self.last_value)
         return self.val
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/sdbmanager.py	(refactored)
@@ -71,7 +71,7 @@
                          str: (self.encode_string, self.decode_string),
                       }
         if six.PY2:
-            self.type_map[long] = (self.encode_long, self.decode_long)
+            self.type_map[int] = (self.encode_long, self.decode_long)
 
     def encode(self, item_type, value):
         try:
@@ -108,7 +108,7 @@
         return self.encode_map(prop, values)
 
     def encode_map(self, prop, value):
-        import urllib
+        import urllib.request, urllib.parse, urllib.error
         if value is None:
             return None
         if not isinstance(value, dict):
@@ -120,7 +120,7 @@
                 item_type = self.model_class
             encoded_value = self.encode(item_type, value[key])
             if encoded_value is not None:
-                new_value.append('%s:%s' % (urllib.quote(key), encoded_value))
+                new_value.append('%s:%s' % (urllib.parse.quote(key), encoded_value))
         return new_value
 
     def encode_prop(self, prop, value):
@@ -145,7 +145,7 @@
                     except:
                         k = v
                     dec_val[k] = v
-            value = dec_val.values()
+            value = list(dec_val.values())
         return value
 
     def decode_map(self, prop, value):
@@ -160,11 +160,11 @@
 
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
@@ -316,7 +316,7 @@
             # TODO: Handle tzinfo
             raise TimeDecodeError("Can't handle timezone aware objects: %r" % value)
         tmp = value.split('.')
-        arg = map(int, tmp[0].split(':'))
+        arg = list(map(int, tmp[0].split(':')))
         if len(tmp) == 2:
             arg.append(int(tmp[1]))
         return time(*arg)
@@ -389,8 +389,8 @@
             # systems, however:
             arr = []
             for ch in value:
-                arr.append(six.unichr(ord(ch)))
-            return u"".join(arr)
+                arr.append(six.chr(ord(ch)))
+            return "".join(arr)
 
     def decode_string(self, value):
         """Decoding a string is really nothing, just
@@ -623,7 +623,7 @@
 
 
         type_query = "(`__type__` = '%s'" % cls.__name__
-        for subclass in self._get_all_decendents(cls).keys():
+        for subclass in list(self._get_all_decendents(cls).keys()):
             type_query += " or `__type__` = '%s'" % subclass
         type_query += ")"
         query_parts.append(type_query)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/db/manager/xmlmanager.py	(refactored)
@@ -49,7 +49,7 @@
                           Password : (self.encode_password, self.decode_password),
                           datetime : (self.encode_datetime, self.decode_datetime)}
         if six.PY2:
-            self.type_map[long] = (self.encode_long, self.decode_long)
+            self.type_map[int] = (self.encode_long, self.decode_long)
 
     def get_text_value(self, parent_node):
         value = ''
@@ -116,12 +116,12 @@
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
@@ -210,9 +210,9 @@
     def _connect(self):
         if self.db_host:
             if self.enable_ssl:
-                from httplib import HTTPSConnection as Connection
+                from http.client import HTTPSConnection as Connection
             else:
-                from httplib import HTTPConnection as ConnectionRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/message.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/service.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/servicedef.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/sonofmmm.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/exceptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/__init__.py

+                from http.client import HTTPConnection as Connection
 
             self.connection = Connection(self.db_host, self.db_port)
 
@@ -348,7 +348,7 @@
         if not self.connection:
             raise NotImplementedError("Can't query without a database connection")
 
-        from urllib import urlencode
+        from urllib.parse import urlencode
 
         query = str(self._build_query(cls, filters, limit, order_by))
         if query:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/bs.py	(refactored)
@@ -64,8 +64,8 @@
 
     def print_command_help(self):
         print('\nCommands:')
-        for key in self.Commands.keys():
-            print('  %s\t\t%s' % (key, self.Commands[key]))
+        for key in list(self.Commands.keys()):
+            print(('  %s\t\t%s' % (key, self.Commands[key])))
 
     def do_reset(self):
         iq = self.sd.get_obj('input_queue')
@@ -77,7 +77,7 @@
                 i += 1
                 iq.delete_message(m)
                 m = iq.read()
-            print('deleted %d messages' % i)
+            print(('deleted %d messages' % i))
         ob = self.sd.get_obj('output_bucket')
         ib = self.sd.get_obj('input_bucket')
         if ob:
@@ -88,7 +88,7 @@
             for k in ob:
                 i += 1
                 k.delete()
-            print('deleted %d keys' % i)
+            print(('deleted %d keys' % i))
 
     def do_submit(self):
         if not self.options.path:
@@ -98,8 +98,8 @@
         s = Submitter(self.sd)
         t = s.submit_path(self.options.path, None, self.options.ignore, None,
                           None, True, self.options.path)
-        print('A total of %d files were submitted' % t[1])
-        print('Batch Identifier: %s' % t[0])
+        print(('A total of %d files were submitted' % t[1]))
+        print(('Batch Identifier: %s' % t[0]))
 
     def do_start(self):
         ami_id = self.sd.get('ami_id')
@@ -120,15 +120,15 @@
                     max_count=self.options.num_instances,
                     instance_type=instance_type,
                     security_groups=[security_group])
-        print('Starting AMI: %s' % ami_id)
-        print('Reservation %s contains the following instances:' % r.id)
+        print(('Starting AMI: %s' % ami_id))
+        print(('Reservation %s contains the following instances:' % r.id))
         for i in r.instances:
-            print('\t%s' % i.id)
+            print(('\t%s' % i.id))
 
     def do_status(self):
         iq = self.sd.get_obj('input_queue')
         if iq:
-            print('The input_queue (%s) contains approximately %s messages' % (iq.id, iq.count()))
+            print(('The input_queue (%s) contains approximately %s messages' % (iq.id, iq.count())))
         ob = self.sd.get_obj('output_bucket')
         ib = self.sd.get_obj('input_bucket')
         if ob:
@@ -137,7 +137,7 @@
             total = 0
             for k in ob:
                 total += 1
-            print('The output_bucket (%s) contains %d keys' % (ob.name, total))
+            print(('The output_bucket (%s) contains %d keys' % (ob.name, total)))
 
     def do_retrieve(self):
         if not self.options.path:
@@ -155,7 +155,7 @@
             print('Available Batches:')
             rs = d.query("['type'='Batch']")
             for item in rs:
-                print('  %s' % item.name)
+                print(('  %s' % item.name))
         else:
             self.parser.error('No output_domain specified for service')
             
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/result.py	(refactored)
@@ -83,7 +83,7 @@
                 key_name = output.split(';')[0]
                 key = bucket.lookup(key_name)
                 file_name = os.path.join(path, key_name)
-                print('retrieving file: %s to %s' % (key_name, file_name))
+                print(('retrieving file: %s to %s' % (key_name, file_name)))
                 key.get_contents_to_filename(file_name)
             self.num_files += 1
 
@@ -107,7 +107,7 @@
             print('No output queue or domain, just retrieving files from output_bucket')
             for key in bucket:
                 file_name = os.path.join(path, key)
-                print('retrieving file: %s to %s' % (key, file_name))
+                print(('retrieving file: %s to %s' % (key, file_name)))
                 key.get_contents_to_filename(file_name)
                 self.num_files + 1
 
@@ -122,14 +122,14 @@
             self.get_results_from_bucket(path)
         if self.log_fp:
             self.log_fp.close()
-        print('%d results successfully retrieved.' % self.num_files)
+        print(('%d results successfully retrieved.' % self.num_files))
         if self.num_files > 0:
             self.avg_time = float(self.total_time)/self.num_files
-            print('Minimum Processing Time: %d' % self.min_time.seconds)
-            print('Maximum Processing Time: %d' % self.max_time.seconds)
-            print('Average Processing Time: %f' % self.avg_time)
+            print(('Minimum Processing Time: %d' % self.min_time.seconds))
+            print(('Maximum Processing Time: %d' % self.max_time.seconds))
+            print(('Average Processing Time: %f' % self.avg_time))
             self.elapsed_time = self.latest_time-self.earliest_time
-            print('Elapsed Time: %d' % self.elapsed_time.seconds)
+            print(('Elapsed Time: %d' % self.elapsed_time.seconds))
             tput = 1.0 / ((self.elapsed_time.seconds/60.0) / self.num_files)
-            print('Throughput: %f transactions / minute' % tput)
+            print(('Throughput: %f transactions / minute' % tput))
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/services/submit.py	(refactored)
@@ -76,12 +76,12 @@
                 for file in files:
                     fullpath = os.path.join(root, file)
                     if status:
-                        print('Submitting %s' % fullpath)
+                        print(('Submitting %s' % fullpath))
                     self.submit_file(fullpath, metadata, cb, num_cb, prefix)
                     total += 1
         elif os.path.isfile(path):
             self.submit_file(path, metadata, cb, num_cb)
             total += 1
         else:
-            print('problem with %s' % path)
+            print(('problem with %s' % path))
         return (metadata['Batch'], total)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py	(refactored)
@@ -91,7 +91,7 @@
         params = params or {}
         params['Action'] = action
 
-        for k, v in params.items():
+        for k, v in list(params.items()):
             if isinstance(v, six.text_type):  # UTF-8 encode only if it's Unicode
                 params[k] = v.encode('utf-8')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py	(refactored)
@@ -95,7 +95,7 @@
       :param dictionary: dict - value of the serialized parameter
       :param name: name of the serialized parameter
       """
-      items = sorted(dictionary.items(), key=lambda x:x[0])
+      items = sorted(list(dictionary.items()), key=lambda x:x[0])
       for kv, index in zip(items, list(range(1, len(items)+1))):
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/attributes.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/bigmessage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/jsonmessage.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/messageattributes.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/exceptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/customergateway.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/dhcpoptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/internetgateway.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/networkacl.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/routetable.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/subnet.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpc_peering_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpnconnection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/vpngateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/test.py
         key, value = kv
         prefix = '%s.entry.%s' % (name, index)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py	(refactored)
@@ -210,7 +210,7 @@
 
     def encode(self, value):
         s = ''
-        for item in value.items():
+        for item in list(value.items()):
             s = s + '%s: %s\n' % (item[0], item[1])
         return s
 
@@ -228,13 +228,13 @@
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
@@ -473,7 +473,7 @@
                 m = Message(self, body)
                 self.write(m)
                 n += 1
-                print('writing message %d' % n)
+                print(('writing message %d' % n))
                 body = ''
             else:
                 body = body + l
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py	(refactored)
@@ -42,10 +42,10 @@
 
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
@@ -487,7 +487,7 @@
     advance_iterator = next
 except NameError:
     def advance_iterator(it):
-        return it.next()
+        return it.__next__()
 next = advance_iterator
 
 
@@ -507,14 +507,14 @@
     Iterator = object
 else:
     def get_unbound_function(unbound):
-        return unbound.im_func
+        return unbound.__func__
 
     def create_bound_method(func, obj):
         return types.MethodType(func, obj, obj.__class__)
 
     class Iterator(object):
 
-        def next(self):
+        def __next__(self):
             return type(self).__next__(self)
 
     callable = callable
@@ -568,7 +568,7 @@
         return s.encode("latin-1")
     def u(s):
         return s
-    unichr = chr
+    chr = chr
     if sys.version_info[1] <= 1:
         def int2byte(i):
             return bytes((i,))
@@ -586,8 +586,8 @@
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
@@ -595,8 +595,8 @@
         return ord(buf[i])
     def iterbytes(buf):
         return (ord(byte) for byte in buf)
-    import StringIO
-    StringIO = BytesIO = StringIO.StringIO
+    import io
+    StringIO = BytesIO = io.StringIO
 _add_doc(b, """Byte literal""")
 _add_doc(u, """Text literal""")
 
@@ -637,11 +637,11 @@
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
@@ -651,13 +651,13 @@
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
@@ -665,12 +665,12 @@
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/conf.py	(refactored)
@@ -12,8 +12,8 @@
 templates_path = ['_templates']
 source_suffix = '.rst'
 master_doc = 'index'
-project = u'boto'
-copyright = u'2009,2010, Mitch Garnaat'
+project = 'boto'
+copyright = '2009,2010, Mitch Garnaat'
 version = boto.__version__
 exclude_trees = []
 pygments_style = 'sphinx'
@@ -22,16 +22,16 @@
 html_static_path = ['_static']
 htmlhelp_basename = 'botodoc'
 latex_documents = [
-  ('index', 'boto.tex', u'boto Documentation',
-   u'Mitch Garnaat', 'manual'),
+  ('index', 'boto.tex', 'boto Documentation',
+   'Mitch Garnaat', 'manual'),
 ]
 intersphinx_mapping = {'http://docs.python.org/': None}
 github_project_url = 'https://github.com/boto/boto/'
 
 try:
     release = os.environ.get('SVN_REVISION', 'HEAD')
-    print release
-except Exception, e:
-    print e
+    print(release)
+except Exception as e:
+    print(e)
 
 html_title = "boto v%s" % version
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/docs/source/extensions/githublinks/__init__.py	(refactored)
@@ -5,7 +5,7 @@
 (https://bitbucket.org/dhellmann/sphinxcontrib-bitbucket/)
 
 """
-from urlparse import urljoin
+from urllib.parse import urljoin
 
 from docutils import nodes, utils
 from docutils.parsers.rst.roles import set_classes
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/test.py	(refactored)
@@ -19,7 +19,7 @@
 # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
-from __future__ import print_function
+
 
 import argparse
 import os
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py	(refactored)
@@ -90,7 +90,7 @@
         t.put()
         self.objs.append(t)
         time.sleep(3)
-        print SimpleListModel.all().filter("strs !=", "Fizzle").get_query()
+        print(SimpleListModel.all().filter("strs !=", "Fizzle").get_query())
         for tt in SimpleListModel.all().filter("strs !=", "Fizzle"):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_lists.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/devpay/test_s3.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test_verify_signature.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/awslambda/test_awslambda.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudhsm/test_cloudhsm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_layers.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch2/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch2/test_layers.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cloudtrail.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/codedeploy/test_codedeploy.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/identity/test_cognito_identity.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/sync/test_cognito_sync.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/configservice/test_configservice.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/directconnect/test_directconnect.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_table.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_cert_verification.py

-            print tt.strs
+            print(tt.strs)
             assert("Fizzle" not in tt.strs)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_password.py	(refactored)
@@ -81,8 +81,8 @@
         id= obj.id
         time.sleep(5)
         obj = MyModel.get_by_id(id)
-        self.assertEquals(obj.password, 'bar')
-        self.assertEquals(str(obj.password), expected)
+        self.assertEqual(obj.password, 'bar')
+        self.assertEqual(str(obj.password), expected)
                           #hmac.new('mysecret','bar').hexdigest())
  
         
@@ -90,11 +90,11 @@
         cls = self.test_model()
         obj = cls(id='passwordtest')
         obj.password = 'foo'
-        self.assertEquals('foo', obj.password)
+        self.assertEqual('foo', obj.password)
         obj.save()
         time.sleep(5)
         obj = cls.get_by_id('passwordtest')
-        self.assertEquals('foo', obj.password)
+        self.assertEqual('foo', obj.password)
 
     def test_password_constructor_hashfunc(self):
         import hmac
@@ -103,8 +103,8 @@
         obj = cls()
         obj.password='hello'
         expected = myhashfunc('hello').hexdigest()
-        self.assertEquals(obj.password, 'hello')
-        self.assertEquals(str(obj.password), expected)
+        self.assertEqual(obj.password, 'hello')
+        self.assertEqual(str(obj.password), expected)
         obj.save()
         id = obj.id
         time.sleep(5)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_query.py	(refactored)
@@ -148,5 +148,5 @@
         """Test with a "like" expression"""
         query = SimpleModel.all()
         query.filter("strs like", "%oo%")
-        print query.get_query()
+        print(query.get_query())
         assert(query.count() == 1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/db/test_sequence.py	(refactored)
@@ -60,11 +60,11 @@
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
 
@@ -73,7 +73,7 @@
         s = Sequence(fnc=increment_string)
         self.sequences.append(s)
         assert(s.val == "A")
-        assert(s.next() == "B")
+        assert(next(s) == "B")
 
     def test_fib(self):
         """Test the fibonacci sequence generator"""
@@ -93,7 +93,7 @@
         assert(s.val == 1)
         # Just check the first few numbers in the sequence
         for v in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]:
-            assert(s.next() == v)
+            assert(next(s) == v)
             assert(s.val == v)
             assert(s2.val == v) # it shouldn't matter which reference we use since it's garunteed to be consistent
 
@@ -103,7 +103,7 @@
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
@@ -27,7 +27,7 @@
 
 import time
 import os
-import urllib
+import urllib.request, urllib.parse, urllib.error
 
 from boto.s3.connection import S3Connection
 from boto.exception import S3PermissionsError
@@ -38,7 +38,7 @@
 DEVPAY_HEADERS = { 'x-amz-security-token': AMAZON_USER_TOKEN }
 
 def test():
-    print '--- running S3Connection tests (DevPay) ---'
+    print('--- running S3Connection tests (DevPay) ---')
     c = S3Connection()
     # create a new, empty bucket
     bucket_name = 'test-%d' % int(time.time())
@@ -67,10 +67,10 @@
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
@@ -175,7 +175,7 @@
 
     c.delete_bucket(bucket, headers=DEVPAY_HEADERS)
 
-    print '--- tests completed ---'
+    print('--- tests completed ---')
 
 if __name__ == '__main__':
     test()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test.py	(refactored)
@@ -11,7 +11,7 @@
     devpath = os.path.relpath(os.path.join('..', '..'),
                               start=os.path.dirname(__file__))
     sys.path = [devpath] + sys.path
-    print '>>> advanced FPS tests; using local boto sources'
+    print('>>> advanced FPS tests; using local boto sources')
     advanced = True
 
 from boto.fps.connection import FPSConnection
@@ -63,7 +63,7 @@
             'callerReference':      'foo',
         }
         result = self.fps.cbui_url(**inputs)
-        print "cbui_url() yields {0}".format(result)
+        print("cbui_url() yields {0}".format(result))
 
     @unittest.skipUnless(simple, "skipping simple test")
     def test_get_account_activity(self):
@@ -88,12 +88,12 @@
         try:
             self.fps.write_off_debt(CreditInstrumentId='foo',
                                     AdjustmentAmount=123.45)
-        except Exception, e:
-            print e
+        except Exception as e:
+            print(e)
 
     @unittest.skip('cosmetic')
     def test_repr(self):
-        print self.fps.get_account_balance()
+        print(self.fps.get_account_balance())
 
 
 if __name__ == "__main__":
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py	(refactored)
@@ -136,7 +136,7 @@
         self.assertEqual(self.stack_name, stack.stack_name)
         
         params = [(p.key, p.value) for p in stack.parameters]
-        self.assertEquals([('Parameter1', 'initial_value'),
+        self.assertEqual([('Parameter1', 'initial_value'),
                            ('Parameter2', 'initial_value')], params)
         
         for _ in range(30):
@@ -154,7 +154,7 @@
         stacks = self.connection.describe_stacks(self.stack_name)
         stack = stacks[0]
         params = [(p.key, p.value) for p in stacks[0].parameters]
-        self.assertEquals([('Parameter1', 'initial_value'),
+        self.assertEqual([('Parameter1', 'initial_value'),
                            ('Parameter2', 'updated_value')], params)
 
         # Waiting for the update to complete to unblock the delete_stack in the
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/vpc/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2containerservice/test_ec2containerservice.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elasticache/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/emr/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer2.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py

@@ -127,7 +127,7 @@
         reservation = image.run(security_groups=[group.name])
         instance = reservation.instances[0]
         while instance.state != 'running':
-            print('\tinstance is %s' % instance.state)
+            print(('\tinstance is %s' % instance.state))
             time.sleep(30)
             instance.update()
         # instance in now running, try to telnet to port 80
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py	(refactored)
@@ -46,7 +46,7 @@
         # have any autoscale groups to introspect. It's useful, however, to
         # catch simple errors
 
-        print('--- running %s tests ---' % self.__class__.__name__)
+        print(('--- running %s tests ---' % self.__class__.__name__))
         c = AutoScaleConnection()
 
         self.assertTrue(repr(c).startswith('AutoScaleConnection'))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py	(refactored)
@@ -261,13 +261,13 @@
 
         c.make_request = make_request
         alarms = c.describe_alarms()
-        self.assertEquals(alarms.next_token, 'mynexttoken')
-        self.assertEquals(alarms[0].name, 'FancyAlarm')
-        self.assertEquals(alarms[0].comparison, '<')
-        self.assertEquals(alarms[0].dimensions, {u'Job': [u'ANiceCronJob']})
-        self.assertEquals(alarms[1].name, 'SuperFancyAlarm')
-        self.assertEquals(alarms[1].comparison, '>')
-        self.assertEquals(alarms[1].dimensions, {u'Job': [u'ABadCronJob']})
+        self.assertEqual(alarms.next_token, 'mynexttoken')
+        self.assertEqual(alarms[0].name, 'FancyAlarm')
+        self.assertEqual(alarms[0].comparison, '<')
+        self.assertEqual(alarms[0].dimensions, {'Job': ['ANiceCronJob']})
+        self.assertEqual(alarms[1].name, 'SuperFancyAlarm')
+        self.assertEqual(alarms[1].comparison, '>')
+        self.assertEqual(alarms[1].dimensions, {'Job': ['ABadCronJob']})
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py	(refactored)
@@ -30,8 +30,8 @@
 
 import os
 import re
-import StringIO
-import urllib
+import io
+import urllib.request, urllib.parse, urllib.error
 import xml.sax
 
 from boto import handler
@@ -102,14 +102,14 @@
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
 
@@ -195,7 +195,7 @@
         k.set_metadata(mdkey2, mdval2)
 
         # Test unicode character.
-        mdval3 = u'föö'
+        mdval3 = 'föö'
         mdkey3 = 'meta3'
         k.set_metadata(mdkey3, mdval3)
         k.set_contents_from_string(s1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py	(refactored)
@@ -23,7 +23,7 @@
 
 """Integration tests for GS versioning support."""
 
-import StringIO
+import io
 import os
 import tempfile
 from xml import sax
@@ -44,20 +44,20 @@
         b = self._MakeBucket()
         k = b.new_key("foo")
         s1 = "test1"
-        fp = StringIO.StringIO(s1)
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        fp = io.StringIO(s1)
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_file(fp, if_generation=999)
 
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         k.set_contents_from_file(fp, if_generation=0)
         g1 = k.generation
 
         s2 = "test2"
-        fp = StringIO.StringIO(s2)
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        fp = io.StringIO(s2)
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_file(fp, if_generation=int(g1)+1)
 
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         k.set_contents_from_file(fp, if_generation=g1)
         self.assertEqual(k.get_contents_as_string(), s2)
 
@@ -65,14 +65,14 @@
         b = self._MakeBucket()
         k = b.new_key("foo")
         s1 = "test1"
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_string(s1, if_generation=999)
 
         k.set_contents_from_string(s1, if_generation=0)
         g1 = k.generation
 
         s2 = "test2"
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_string(s2, if_generation=int(g1)+1)
 
         k.set_contents_from_string(s2, if_generation=g1)
@@ -94,13 +94,13 @@
             b = self._MakeBucket()
             k = b.new_key("foo")
 
-            with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+            with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
                 k.set_contents_from_filename(fname1, if_generation=999)
 
             k.set_contents_from_filename(fname1, if_generation=0)
             g1 = k.generation
 
-            with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+            with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
                 k.set_contents_from_filename(fname2, if_generation=int(g1)+1)
 
             k.set_contents_from_filename(fname2, if_generation=g1)
@@ -127,17 +127,17 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             b.set_acl("bucket-owner-full-control", key_name="foo",
                       if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_acl("bucket-owner-full-control", key_name="foo",
                       if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_acl("bucket-owner-full-control", key_name="foo",
                       if_generation=g2, if_metageneration=int(mg2) + 1)
 
@@ -156,21 +156,21 @@
         b = self._MakeBucket()
         k = b.new_key("foo")
         s1 = "test1"
-        fp = StringIO.StringIO(s1)
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        fp = io.StringIO(s1)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py

+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_stream(fp, if_generation=999)
 
-        fp = StringIO.StringIO(s1)
+        fp = io.StringIO(s1)
         k.set_contents_from_stream(fp, if_generation=0)
         g1 = k.generation
 
         k = b.get_key("foo")
         s2 = "test2"
-        fp = StringIO.StringIO(s2)
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        fp = io.StringIO(s2)
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_contents_from_stream(fp, if_generation=int(g1)+1)
 
-        fp = StringIO.StringIO(s2)
+        fp = io.StringIO(s2)
         k.set_contents_from_stream(fp, if_generation=g1)
         self.assertEqual(k.get_contents_as_string(), s2)
 
@@ -192,17 +192,17 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             b.set_canned_acl("bucket-owner-full-control", key_name="foo",
                       if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_canned_acl("bucket-owner-full-control", key_name="foo",
                       if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_canned_acl("bucket-owner-full-control", key_name="foo",
                       if_generation=g2, if_metageneration=int(mg2) + 1)
 
@@ -246,15 +246,15 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             b.set_xml_acl(acl, key_name="foo", if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_xml_acl(acl, key_name="foo", if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             b.set_xml_acl(acl, key_name="foo", if_generation=g2,
                           if_metageneration=int(mg2) + 1)
 
@@ -286,15 +286,15 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             k.set_acl("bucket-owner-full-control", if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_acl("bucket-owner-full-control", if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_acl("bucket-owner-full-control", if_generation=g2,
                       if_metageneration=int(mg2) + 1)
 
@@ -325,17 +325,17 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             k.set_canned_acl("bucket-owner-full-control",
                              if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_canned_acl("bucket-owner-full-control",
                              if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_canned_acl("bucket-owner-full-control", if_generation=g2,
                       if_metageneration=int(mg2) + 1)
 
@@ -377,15 +377,15 @@
         self.assertEqual(g2, g1)
         self.assertGreater(mg2, mg1)
 
-        with self.assertRaisesRegexp(ValueError, ("Received if_metageneration "
+        with self.assertRaisesRegex(ValueError, ("Received if_metageneration "
                                                   "argument with no "
                                                   "if_generation argument")):
             k.set_xml_acl(acl, if_metageneration=123)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_xml_acl(acl, if_generation=int(g2) + 1)
 
-        with self.assertRaisesRegexp(GSResponseError, VERSION_MISMATCH):
+        with self.assertRaisesRegex(GSResponseError, VERSION_MISMATCH):
             k.set_xml_acl(acl, if_generation=g2, if_metageneration=int(mg2) + 1)
 
         k.set_xml_acl(acl, if_generation=g2)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py	(refactored)
@@ -32,7 +32,7 @@
 from boto.s3.resumable_download_handler import ResumableDownloadHandler
 from boto.exception import ResumableTransferDisposition
 from boto.exception import ResumableDownloadException
-from cb_test_harness import CallbackTestHarness
+from .cb_test_harness import CallbackTestHarness
 from tests.integration.gs.testcase import GSTestCase
 
 
@@ -102,7 +102,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected ResumableDownloadException')
-        except ResumableDownloadException, e:
+        except ResumableDownloadException as e:
             # We'll get a ResumableDownloadException at this point because
             # of CallbackTestHarness (above). Check that the tracker file was
             # created correctly.
@@ -111,7 +111,7 @@
             self.assertTrue(os.path.exists(tracker_file_name))
             f = open(tracker_file_name)
             etag_line = f.readline()
-            self.assertEquals(etag_line.rstrip('\n'), small_src_key.etag.strip('"\''))
+            self.assertEqual(etag_line.rstrip('\n'), small_src_key.etag.strip('"\''))
 
     def test_retryable_exception_recovery(self):
         """
@@ -164,7 +164,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected OSError')
-        except OSError, e:
+        except OSError as e:
             # Ensure the error was re-raised.
             self.assertEqual(e.errno, 13)
 
@@ -228,7 +228,7 @@
                 dst_fp, cb=harness.call,
                 res_download_handler=res_download_handler)
             self.fail('Did not get expected ResumableDownloadException')
-        except ResumableDownloadException, e:
+        except ResumableDownloadException as e:
             self.assertEqual(e.disposition,
                              ResumableTransferDisposition.ABORT_CUR_PROCESS)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py

             # Ensure a tracker file survived.
@@ -345,7 +345,7 @@
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
@@ -23,7 +23,7 @@
 Tests of Google Cloud Storage resumable uploads.
 """
 
-import StringIO
+import io
 import errno
 import random
 import os
@@ -35,7 +35,7 @@
 from boto.exception import InvalidUriError
 from boto.exception import ResumableTransferDisposition
 from boto.exception import ResumableUploadException
-from cb_test_harness import CallbackTestHarness
+from .cb_test_harness import CallbackTestHarness
 from tests.integration.gs.testcase import GSTestCase
 
 
@@ -57,7 +57,7 @@
         for i in range(size):
             buf.append(str(random.randint(0, 9)))
         file_as_string = ''.join(buf)
-        return (file_as_string, StringIO.StringIO(file_as_string))
+        return (file_as_string, io.StringIO(file_as_string))
 
     def make_small_file(self):
         return self.build_input_file(SMALL_KEY_SIZE)
@@ -120,7 +120,7 @@
                 small_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # We'll get a ResumableUploadException at this point because
             # of CallbackTestHarness (above). Check that the tracker file was
             # created correctly.
@@ -185,7 +185,7 @@
                 small_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected OSError')
-        except OSError, e:
+        except OSError as e:
             # Ensure the error was re-raised.
             self.assertEqual(e.errno, 13)
 
@@ -247,7 +247,7 @@
                 larger_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition,
                              ResumableTransferDisposition.ABORT_CUR_PROCESS)
             # Ensure a tracker file survived.
@@ -296,7 +296,7 @@
         Tests uploading an empty file (exercises boundary conditions).
         """
         res_upload_handler = ResumableUploadHandler()
-        empty_src_file = StringIO.StringIO('')
+        empty_src_file = io.StringIO('')
         empty_src_file.seek(0)
         dst_key = self._MakeKey(set_contents=False)
         dst_key.set_contents_from_file(
@@ -351,7 +351,7 @@
                 larger_src_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # First abort (from harness-forced failure) should be
             # ABORT_CUR_PROCESS.
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT_CUR_PROCESS)
@@ -368,7 +368,7 @@
             dst_key.set_contents_from_file(
                 largest_src_file, res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             # This abort should be a hard abort (file size changing during
             # transfer).
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
@@ -391,7 +391,7 @@
                 test_file, cb=harness.call,
                 res_upload_handler=res_upload_handler)
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('File changed during upload'), -1)
@@ -411,7 +411,7 @@
                     test_file, cb=harness.call,
                     res_upload_handler=res_upload_handler)
                 return False
-            except ResumableUploadException, e:
+            except ResumableUploadException as e:
                 self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
                 # Ensure the file size didn't change.
                 test_file.seek(0, os.SEEK_END)
@@ -422,7 +422,7 @@
                 try:
                     dst_key_uri.get_key()
                     self.fail('Did not get expected InvalidUriError')
-                except InvalidUriError, e:
+                except InvalidUriError as e:
                     pass
             return True
 
@@ -477,7 +477,7 @@
                 small_src_file, res_upload_handler=res_upload_handler,
                 headers={'Content-Length' : SMALL_KEY_SIZE})
             self.fail('Did not get expected ResumableUploadException')
-        except ResumableUploadException, e:
+        except ResumableUploadException as e:
             self.assertEqual(e.disposition, ResumableTransferDisposition.ABORT)
             self.assertNotEqual(
                 e.message.find('Attempt to specify Content-Length header'), -1)
@@ -543,7 +543,7 @@
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
@@ -25,7 +25,7 @@
 
 import binascii
 import re
-import StringIO
+import io
 
 from boto import storage_uri
 from boto.exception import BotoClientError
@@ -62,7 +62,7 @@
 
         uri = orig_uri.clone_replace_key(k)
         self.assertTrue(uri.has_version())
-        self.assertRegexpMatches(str(uri.generation), r"[0-9]+")
+        self.assertRegex(str(uri.generation), r"[0-9]+")
 
     def testSetAclXml(self):
         """Ensures that calls to the set_xml_acl functions succeed."""
@@ -97,9 +97,9 @@
         new_obj_acl_string = k.get_acl().to_xml()
         new_bucket_acl_string = bucket_uri.get_acl().to_xml()
         new_bucket_def_acl_string = bucket_uri.get_def_acl().to_xml()
-        self.assertRegexpMatches(new_obj_acl_string, r"AllUsers")
-        self.assertRegexpMatches(new_bucket_acl_string, r"AllUsers")
-        self.assertRegexpMatches(new_bucket_def_acl_string, r"AllUsers")
+        self.assertRegex(new_obj_acl_string, r"AllUsers")
+        self.assertRegex(new_bucket_acl_string, r"AllUsers")
+        self.assertRegex(new_bucket_def_acl_string, r"AllUsers")
 
     def testPropertiesUpdated(self):
         b = self._MakeBucket()
@@ -107,24 +107,24 @@
         key_uri = bucket_uri.clone_replace_name("obj")
         key_uri.set_contents_from_string("data1")
 
-        self.assertRegexpMatches(str(key_uri.generation), r"[0-9]+")
+        self.assertRegex(str(key_uri.generation), r"[0-9]+")
         k = b.get_key("obj")RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/testcase.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_password_policy.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_kinesis.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kms/test_kms.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/logs/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/logs/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/opsworks/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py

         self.assertEqual(k.generation, key_uri.generation)
-        self.assertEquals(k.get_contents_as_string(), "data1")
+        self.assertEqual(k.get_contents_as_string(), "data1")
 
-        key_uri.set_contents_from_stream(StringIO.StringIO("data2"))
-        self.assertRegexpMatches(str(key_uri.generation), r"[0-9]+")
+        key_uri.set_contents_from_stream(io.StringIO("data2"))
+        self.assertRegex(str(key_uri.generation), r"[0-9]+")
         self.assertGreater(key_uri.generation, k.generation)
         k = b.get_key("obj")
         self.assertEqual(k.generation, key_uri.generation)
-        self.assertEquals(k.get_contents_as_string(), "data2")
+        self.assertEqual(k.get_contents_as_string(), "data2")
 
-        key_uri.set_contents_from_file(StringIO.StringIO("data3"))
-        self.assertRegexpMatches(str(key_uri.generation), r"[0-9]+")
+        key_uri.set_contents_from_file(io.StringIO("data3"))
+        self.assertRegex(str(key_uri.generation), r"[0-9]+")
         self.assertGreater(key_uri.generation, k.generation)
         k = b.get_key("obj")
         self.assertEqual(k.generation, key_uri.generation)
-        self.assertEquals(k.get_contents_as_string(), "data3")
+        self.assertEqual(k.get_contents_as_string(), "data3")
 
     def testCompose(self):
         data1 = 'hello '
@@ -142,13 +142,13 @@
         key_uri_composite = bucket_uri.clone_replace_name("composite")
         components = [key_uri1, key_uri2]
         key_uri_composite.compose(components, content_type='text/plain')
-        self.assertEquals(key_uri_composite.get_contents_as_string(),
+        self.assertEqual(key_uri_composite.get_contents_as_string(),
                           data1 + data2)
         composite_key = key_uri_composite.get_key()
         cloud_crc32c = binascii.hexlify(
             composite_key.cloud_hashes['crc32c'])
-        self.assertEquals(cloud_crc32c, hex(expected_crc)[2:])
-        self.assertEquals(composite_key.content_type, 'text/plain')
+        self.assertEqual(cloud_crc32c, hex(expected_crc)[2:])
+        self.assertEqual(composite_key.content_type, 'text/plain')
 
         # Compose disallowed between buckets.
         key_uri1.bucket_name += '2'
@@ -156,6 +156,6 @@
             key_uri_composite.compose(components)
             self.fail('Composing between buckets didn\'t fail as expected.')
         except BotoClientError as err:
-            self.assertEquals(
+            self.assertEqual(
                 err.reason, 'GCS does not support inter-bucket composing')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py	(refactored)
@@ -257,11 +257,11 @@
         self.assertIsNone(k.generation)
         k.set_contents_from_string("test1")
         g1 = k.generation
-        self.assertRegexpMatches(g1, r'[0-9]+')
+        self.assertRegex(g1, r'[0-9]+')
         self.assertEqual(k.metageneration, '1')
         k.set_contents_from_string("test2")
         g2 = k.generation
         self.assertNotEqual(g1, g2)
-        self.assertRegexpMatches(g2, r'[0-9]+')
+        self.assertRegex(g2, r'[0-9]+')
         self.assertGreater(int(g2), int(g1))
         self.assertEqual(k.metageneration, '1')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py	(refactored)
@@ -70,12 +70,12 @@
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
+                        print(msg)
                     time.sleep(mdelay)
                     mtries -= 1
                     mdelay *= backoff
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py	(refactored)
@@ -1,5 +1,5 @@
 #!/usr/bin/env python
-from __future__ import print_function
+
 import sys
 import os
 import os.path
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py	(refactored)
@@ -32,15 +32,15 @@
 
 def _is_ok(subnet_group, vpc_id, description, subnets):
     if subnet_group.vpc_id != vpc_id:
-        print 'vpc_id is ',subnet_group.vpc_id, 'but should be ', vpc_id
+        print('vpc_id is ',subnet_group.vpc_id, 'but should be ', vpc_id)
         return 0
     if subnet_group.description != description:
-        print "description is '"+subnet_group.description+"' but should be '"+description+"'"
+        print("description is '"+subnet_group.description+"' but should be '"+description+"'")
         return 0
     if set(subnet_group.subnet_ids) != set(subnets):
         subnets_are = ','.join(subnet_group.subnet_ids)
         should_be   = ','.join(subnets)
-        print "subnets are "+subnets_are+" but should be "+should_be
+        print("subnets are "+subnets_are+" but should be "+should_be)
         return 0
     return 1
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py	(refactored)
@@ -35,11 +35,11 @@
                     self.conn.delete_dbinstance(db, skip_final_snapshot=True)
 
     def test_promote(self):
-        print '--- running RDS promotion & renaming tests ---'
+        print('--- running RDS promotion & renaming tests ---')
         self.masterDB = self.conn.create_dbinstance(self.masterDB_name, 5, 'db.t1.micro', 'root', 'bototestpw')
         
         # Wait up to 15 minutes for the masterDB to become available
-        print '--- waiting for "%s" to become available  ---' % self.masterDB_name
+        print('--- waiting for "%s" to become available  ---' % self.masterDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
  
@@ -56,7 +56,7 @@
         self.replicaDB = self.conn.create_dbinstance_read_replica(self.replicaDB_name, self.masterDB_name)
 
         # Wait up to 15 minutes for the replicaDB to become available
-        print '--- waiting for "%s" to become available  ---' % self.replicaDB_name
+        print('--- waiting for "%s" to become available  ---' % self.replicaDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
         
@@ -74,7 +74,7 @@
         self.replicaDB = self.conn.promote_read_replica(self.replicaDB_name)
 
         # Wait up to 15 minutes for the replicaDB to become available
-        print '--- waiting for "%s" to be promoted and available  ---' % self.replicaDB_name
+        print('--- waiting for "%s" to be promoted and available  ---' % self.replicaDB_name)
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
         
@@ -97,12 +97,12 @@
         inst = instances[0]
         self.assertFalse(inst.read_replica_dbinstance_identifiers)
 
-        print '--- renaming "%s" to "%s" ---' % ( self.replicaDB_name, self.renamedDB_name )
+        print('--- renaming "%s" to "%s" ---' % ( self.replicaDB_name, self.renamedDB_name ))
 
         self.renamedDB = self.conn.modify_dbinstance(self.replicaDB_name, new_instance_id=self.renamedDB_name, apply_immediately=True)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py

 
         # Wait up to 15 minutes for the masterDB to become available
-        print '--- waiting for "%s" to exist  ---' % self.renamedDB_name
+        print('--- waiting for "%s" to exist  ---' % self.renamedDB_name)
 
         wait_timeout = time.time() + (15 * 60)
         time.sleep(60)
@@ -119,7 +119,7 @@
 
         self.assertTrue(found)
 
-        print '--- waiting for "%s" to become available ---' % self.renamedDB_name
+        print('--- waiting for "%s" to become available ---' % self.renamedDB_name)
 
         instances = self.conn.get_all_dbinstances(self.renamedDB_name)
         inst = instances[0]
@@ -135,4 +135,4 @@
         # Since the replica DB was renamed...
         self.replicaDB = None
 
-        print '--- tests completed ---'
+        print('--- tests completed ---')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py	(refactored)
@@ -31,36 +31,36 @@
     def test_create_health_check(self):
         hc = HealthCheck(ip_addr="54.217.7.118", port=80, hc_type="HTTP", resource_path="/testing")
         result = self.conn.create_health_check(hc)
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Type'], 'HTTP')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'IPAddress'], '54.217.7.118')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Port'], '80')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'ResourcePath'], '/testing')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Type'], 'HTTP')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['IPAddress'], '54.217.7.118')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Port'], '80')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['ResourcePath'], '/testing')
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
     def test_create_https_health_check(self):
         hc = HealthCheck(ip_addr="54.217.7.118", port=443, hc_type="HTTPS", resource_path="/testing")
         result = self.conn.create_health_check(hc)
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Type'], 'HTTPS')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'IPAddress'], '54.217.7.118')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Port'], '443')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'ResourcePath'], '/testing')
-        self.assertFalse('FullyQualifiedDomainName' in result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'])
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Type'], 'HTTPS')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['IPAddress'], '54.217.7.118')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Port'], '443')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['ResourcePath'], '/testing')
+        self.assertFalse('FullyQualifiedDomainName' in result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig'])
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
     def test_create_https_health_check_fqdn(self):
         hc = HealthCheck(ip_addr=None, port=443, hc_type="HTTPS", resource_path="/", fqdn="google.com")
         result = self.conn.create_health_check(hc)
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Type'], 'HTTPS')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'FullyQualifiedDomainName'], 'google.com')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Port'], '443')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'ResourcePath'], '/')
-        self.assertFalse('IPAddress' in result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'])
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Type'], 'HTTPS')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['FullyQualifiedDomainName'], 'google.com')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Port'], '443')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['ResourcePath'], '/')
+        self.assertFalse('IPAddress' in result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig'])
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
     def test_create_and_list_health_check(self):
@@ -92,25 +92,25 @@
     def test_create_health_check_string_match(self):
         hc = HealthCheck(ip_addr="54.217.7.118", port=80, hc_type="HTTP_STR_MATCH", resource_path="/testing", string_match="test")
         result = self.conn.create_health_check(hc)
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Type'], 'HTTP_STR_MATCH')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'IPAddress'], '54.217.7.118')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Port'], '80')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'ResourcePath'], '/testing')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'SearchString'], 'test')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Type'], 'HTTP_STR_MATCH')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['IPAddress'], '54.217.7.118')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Port'], '80')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['ResourcePath'], '/testing')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['SearchString'], 'test')
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
     def test_create_health_check_https_string_match(self):
         hc = HealthCheck(ip_addr="54.217.7.118", port=80, hc_type="HTTPS_STR_MATCH", resource_path="/testing", string_match="test")
         result = self.conn.create_health_check(hc)
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Type'], 'HTTPS_STR_MATCH')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'IPAddress'], '54.217.7.118')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'Port'], '80')RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/domains/test_route53domains.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connect_to_region.py

-        self.assertEquals(result[u'CreateHealthCheckResponse'][
-                          u'HealthCheck'][u'HealthCheckConfig'][u'ResourcePath'], '/testing')
-        self.assertEquals(result[u'CreateHealthCheckResponse'][u'HealthCheck'][u'HealthCheckConfig'][u'SearchString'], 'test')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Type'], 'HTTPS_STR_MATCH')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['IPAddress'], '54.217.7.118')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['Port'], '80')
+        self.assertEqual(result['CreateHealthCheckResponse'][
+                          'HealthCheck']['HealthCheckConfig']['ResourcePath'], '/testing')
+        self.assertEqual(result['CreateHealthCheckResponse']['HealthCheck']['HealthCheckConfig']['SearchString'], 'test')
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
     def test_create_resource_record_set(self):
@@ -148,9 +148,9 @@
         hc_params = self.health_check_params(request_interval=10)
         hc = HealthCheck(**hc_params)
         result = self.conn.create_health_check(hc)
-        hc_config = (result[u'CreateHealthCheckResponse']
-                     [u'HealthCheck'][u'HealthCheckConfig'])
-        self.assertEquals(hc_config[u'RequestInterval'],
+        hc_config = (result['CreateHealthCheckResponse']
+                     ['HealthCheck']['HealthCheckConfig'])
+        self.assertEqual(hc_config['RequestInterval'],
                           six.text_type(hc_params['request_interval']))
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
@@ -158,9 +158,9 @@
         hc_params = self.health_check_params(failure_threshold=1)
         hc = HealthCheck(**hc_params)
         result = self.conn.create_health_check(hc)
-        hc_config = (result[u'CreateHealthCheckResponse']
-                     [u'HealthCheck'][u'HealthCheckConfig'])
-        self.assertEquals(hc_config[u'FailureThreshold'],
+        hc_config = (result['CreateHealthCheckResponse']
+                     ['HealthCheck']['HealthCheckConfig'])
+        self.assertEqual(hc_config['FailureThreshold'],
                           six.text_type(hc_params['failure_threshold']))
         self.conn.delete_health_check(result['CreateHealthCheckResponse']['HealthCheck']['Id'])
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py	(refactored)
@@ -47,14 +47,14 @@
     def test_a(self):
         self.zone.add_a(self.base_domain, '102.11.23.1', 80)
         record = self.zone.get_a(self.base_domain)
-        self.assertEquals(record.name, u'%s.' % self.base_domain)
-        self.assertEquals(record.resource_records, [u'102.11.23.1'])
-        self.assertEquals(record.ttl, u'80')
+        self.assertEqual(record.name, '%s.' % self.base_domain)
+        self.assertEqual(record.resource_records, ['102.11.23.1'])
+        self.assertEqual(record.ttl, '80')
         self.zone.update_a(self.base_domain, '186.143.32.2', '800')
         record = self.zone.get_a(self.base_domain)
-        self.assertEquals(record.name, u'%s.' % self.base_domain)
-        self.assertEquals(record.resource_records, [u'186.143.32.2'])
-        self.assertEquals(record.ttl, u'800')
+        self.assertEqual(record.name, '%s.' % self.base_domain)
+        self.assertEqual(record.resource_records, ['186.143.32.2'])
+        self.assertEqual(record.ttl, '800')
 
     def test_cname(self):
         self.zone.add_cname(
@@ -63,22 +63,22 @@
             200
         )
         record = self.zone.get_cname('www.%s' % self.base_domain)
-        self.assertEquals(record.name, u'www.%s.' % self.base_domain)
-        self.assertEquals(record.resource_records, [
-            u'webserver.%s.' % self.base_domain
+        self.assertEqual(record.name, 'www.%s.' % self.base_domain)
+        self.assertEqual(record.resource_records, [
+            'webserver.%s.' % self.base_domain
         ])
-        self.assertEquals(record.ttl, u'200')
+        self.assertEqual(record.ttl, '200')
         self.zone.update_cname(
             'www.%s' % self.base_domain,
             'web.%s' % self.base_domain,
             45
         )
         record = self.zone.get_cname('www.%s' % self.base_domain)
-        self.assertEquals(record.name, u'www.%s.' % self.base_domain)
-        self.assertEquals(record.resource_records, [
-            u'web.%s.' % self.base_domain
+        self.assertEqual(record.name, 'www.%s.' % self.base_domain)
+        self.assertEqual(record.resource_records, [
+            'web.%s.' % self.base_domain
         ])
-        self.assertEquals(record.ttl, u'45')
+        self.assertEqual(record.ttl, '45')
 
     def test_mx(self):
         self.zone.add_mx(
@@ -90,10 +90,10 @@
             1000
         )
         record = self.zone.get_mx(self.base_domain)
-        self.assertEquals(set(record.resource_records),
-                          set([u'10 mx1.%s.' % self.base_domain,
-                               u'20 mx2.%s.' % self.base_domain]))
-        self.assertEquals(record.ttl, u'1000')
+        self.assertEqual(set(record.resource_records),
+                          set(['10 mx1.%s.' % self.base_domain,
+                               '20 mx2.%s.' % self.base_domain]))
+        self.assertEqual(record.ttl, '1000')
         self.zone.update_mx(
             self.base_domain,
             [
@@ -103,10 +103,10 @@
             50
         )
         record = self.zone.get_mx(self.base_domain)
-        self.assertEquals(set(record.resource_records),
-                          set([u'10 mail1.%s.' % self.base_domain,
+        self.assertEqual(set(record.resource_records),
+                          set(['10 mail1.%s.' % self.base_domain,
                                '20 mail2.%s.' % self.base_domain]))
-        self.assertEquals(record.ttl, u'50')
+        self.assertEqual(record.ttl, '50')
 
     def test_get_records(self):
         self.zone.get_records()
@@ -128,7 +128,7 @@
             'A',
             all=True
         )
-        self.assertEquals(len(wrrs), 2)
+        self.assertEqual(len(wrrs), 2)
         self.zone.delete_a('wrr.%s' % self.base_domain, all=True)
 
     def test_identifiers_lbrs(self):
@@ -141,7 +141,7 @@
             'A',
             all=True
         )
-        self.assertEquals(len(lbrs), 2)
+        self.assertEqual(len(lbrs), 2)
         self.zone.delete_a('lbr.%s' % self.base_domain,
                            identifier=('bam', 'us-west-1'))
         self.zone.delete_a('lbr.%s' % self.base_domain,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py	(refactored)
@@ -115,7 +115,7 @@
         # grant log write perms to target bucket using canned-acl
         self.bucket.set_acl("log-delivery-write")
         target_bucket = self.bucket_name
-        target_prefix = u"jp/ログ/"
+        target_prefix = "jp/ログ/"
         # Check existing status is disabled
         bls = sb.get_logging_status()
         self.assertEqual(bls.target, None)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connect_to_region.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connect_to_region.py	(refactored)
@@ -37,36 +37,36 @@
     def testWithNonAWSHost(self):
         connect_args = dict({'host':'www.not-a-website.com'})
         connection = connect_to_region('us-east-1', **connect_args)
-        self.assertEquals('www.not-a-website.com', connection.host)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_https_cert_validation.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py

+        self.assertEqual('www.not-a-website.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
     def testSuccessWithHostOverrideRegion(self):
         connect_args = dict({'host':'s3.amazonaws.com'})
         connection = connect_to_region('us-west-2', **connect_args)
-        self.assertEquals('s3.amazonaws.com', connection.host)
+        self.assertEqual('s3.amazonaws.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
 
     def testSuccessWithDefaultUSWest1(self):
         connection = connect_to_region('us-west-2')
-        self.assertEquals('s3-us-west-2.amazonaws.com', connection.host)
+        self.assertEqual('s3-us-west-2.amazonaws.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
     def testSuccessWithDefaultUSEast1(self):
         connection = connect_to_region('us-east-1')
-        self.assertEquals('s3.amazonaws.com', connection.host)
+        self.assertEqual('s3.amazonaws.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
     def testDefaultWithInvalidHost(self):
         connect_args = dict({'host':''})
         connection = connect_to_region('us-west-2', **connect_args)
-        self.assertEquals('s3-us-west-2.amazonaws.com', connection.host)
+        self.assertEqual('s3-us-west-2.amazonaws.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
     def testDefaultWithInvalidHostNone(self):
         connect_args = dict({'host':None})
         connection = connect_to_region('us-east-1', **connect_args)
-        self.assertEquals('s3.amazonaws.com', connection.host)
+        self.assertEqual('s3.amazonaws.com', connection.host)
         self.assertIsInstance(connection, S3Connection)
 
     def tearDown(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py	(refactored)
@@ -135,7 +135,7 @@
         mdval2 = 'This is the second metadata value'
         k.set_metadata(mdkey2, mdval2)
         # try a unicode metadata value
-        mdval3 = u'föö'
+        mdval3 = 'föö'
         mdkey3 = 'meta3'
         k.set_metadata(mdkey3, mdval3)
         k.set_contents_from_string(s1)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py	(refactored)
@@ -57,16 +57,16 @@
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py	(refactored)
@@ -384,7 +384,7 @@
         key.set_contents_from_string('Some text here.')
 
         check = self.bucket.get_key('test_date')
-        self.assertEqual(check.get_metadata('date'), u'20130524T155935Z')
+        self.assertEqual(check.get_metadata('date'), '20130524T155935Z')
         self.assertTrue('x-amz-meta-date' in check._get_remote_metadata())
 
     def test_header_casing(self):
@@ -401,15 +401,15 @@
     def test_header_encoding(self):
         key = self.bucket.new_key('test_header_encoding')
 
-        key.set_metadata('Cache-control', u'public, max-age=500')
-        key.set_metadata('Test-Plus', u'A plus (+)')
-        key.set_metadata('Content-disposition', u'filename=Schöne Zeit.txt')
+        key.set_metadata('Cache-control', 'public, max-age=500')
+        key.set_metadata('Test-Plus', 'A plus (+)')
+        key.set_metadata('Content-disposition', 'filename=Schöne Zeit.txt')
         key.set_metadata('Content-Encoding', 'gzip')
         key.set_metadata('Content-Language', 'de')
         key.set_metadata('Content-Type', 'application/pdf')
         self.assertEqual(key.content_type, 'application/pdf')
         key.set_metadata('X-Robots-Tag', 'all')
-        key.set_metadata('Expires', u'Thu, 01 Dec 1994 16:00:00 GMT')
+        key.set_metadata('Expires', 'Thu, 01 Dec 1994 16:00:00 GMT')
         key.set_contents_from_string('foo')
 
         check = self.bucket.get_key('test_header_encoding')
@@ -432,7 +432,7 @@
         self.assertEqual(check.expires, 'Thu,%2001%20Dec%201994%2016:00:00%20GMT')
         self.assertEqual(remote_metadata['expires'], 'Thu,%2001%20Dec%201994%2016:00:00%20GMT')
 
-        expected = u'filename=Schöne Zeit.txt'
+        expected = 'filename=Schöne Zeit.txt'
         if six.PY2:
             # Newer versions of python default to unicode strings, but python 2
             # requires encoding to UTF-8 to compare the two properly
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py	(refactored)
@@ -49,8 +49,8 @@
 
     def test_mfadel(self):
         # Enable Versioning with MfaDelete
-        mfa_sn = raw_input('MFA S/N: ')
-        mfa_code = raw_input('MFA Code: ')
+        mfa_sn = input('MFA S/N: ')
+        mfa_code = input('MFA Code: ')
         self.bucket.configure_versioning(True, mfa_delete=True, mfa_token=(mfa_sn, mfa_code))
 
         # Check enabling mfa worked.
@@ -77,11 +77,11 @@
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
@@ -86,7 +86,7 @@
         self.assertEqual(len(result.errors), 1)
 
     def test_delete_kanji(self):
-        result = self.bucket.delete_keys([u"漢字", Key(name=u"日本語")])
+        result = self.bucket.delete_keys(["漢字", Key(name="日本語")])
         self.assertEqual(len(result.deleted), 2)
         self.assertEqual(len(result.errors), 0)
 
@@ -96,7 +96,7 @@
         self.assertEqual(len(result.errors), 0)
 
     def test_delete_kanji_by_list(self):
-        for key_name in [u"漢字", u"日本語", u"テスト"]:RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_cert_verification.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ses/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ses/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_sns_sqs_subscription.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_bigmessage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/storage_uri/test_storage_uri.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/support/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_cert_verification.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_layer1_workflow_execution.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py

+        for key_name in ["漢字", "日本語", "テスト"]:
             key = self.bucket.new_key(key_name)
             key.set_contents_from_string('this is a test')
         result = self.bucket.delete_keys(self.bucket.list())
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py	(refactored)
@@ -57,7 +57,7 @@
         self.bucket.delete()
 
     def test_abort(self):
-        key_name = u"テスト"
+        key_name = "テスト"
         mpu = self.bucket.initiate_multipart_upload(key_name)
         mpu.cancel_upload()
 
@@ -72,7 +72,7 @@
         self.assertNotEqual(cmpu.etag, None)
 
     def test_complete_japanese(self):
-        key_name = u"テスト"
+        key_name = "テスト"
         mpu = self.bucket.initiate_multipart_upload(key_name)
         fp = StringIO("small file")
         mpu.upload_part_from_file(fp, part_num=1)
@@ -82,7 +82,7 @@
         self.assertNotEqual(cmpu.etag, None)
 
     def test_list_japanese(self):
-        key_name = u"テスト"
+        key_name = "テスト"
         mpu = self.bucket.initiate_multipart_upload(key_name)
         rs = self.bucket.list_multipart_uploads()
         # New bucket, so only one upload expected
@@ -93,7 +93,7 @@
         lmpu.cancel_upload()
 
     def test_list_multipart_uploads(self):
-        key_name = u"テスト"
+        key_name = "テスト"
         mpus = []
         mpus.append(self.bucket.initiate_multipart_upload(key_name))
         mpus.append(self.bucket.initiate_multipart_upload(key_name))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py	(refactored)
@@ -23,7 +23,7 @@
 """
 Some multi-threading tests of boto in a greenlet environment.
 """
-from __future__ import print_function
+
 
 import boto
 import time
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py	(refactored)
@@ -62,7 +62,7 @@
 
         # try to get the attributes and see if they match
         item = domain.get_attributes(item_1, consistent_read=True)
-        assert len(item.keys()) == len(attrs_1.keys())
+        assert len(list(item.keys())) == len(list(attrs_1.keys()))
         assert item['name1'] == attrs_1['name1']
         assert item['name2'] == attrs_1['name2']
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/_init_environment.py	(refactored)
@@ -12,7 +12,7 @@
     global SetHostMTurkConnection
     try:
             local = os.path.join(os.path.dirname(__file__), 'local.py')
-            execfile(local)
+            exec(compile(open(local, "rb").read(), local, 'exec'))
     except:
             pass
 
@@ -24,5 +24,5 @@
             #  they're set to.
             os.environ.setdefault('AWS_ACCESS_KEY_ID', 'foo')
             os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'bar')
-            from mocks import MTurkConnection
+            from .mocks import MTurkConnection
     SetHostMTurkConnection = functools.partial(MTurkConnection, host=mturk_host)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/all_tests.py	(refactored)
@@ -3,11 +3,11 @@
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
@@ -1,7 +1,7 @@
 import itertools
 
-from _init_environment import SetHostMTurkConnection
-from _init_environment import config_environment
+from ._init_environment import SetHostMTurkConnection
+from ._init_environment import config_environment
 
 def description_filter(substring):
 	return lambda hit: substring in hit.Title
@@ -26,22 +26,22 @@
 
 
 	is_boto = description_filter('Boto')
-	print 'getting hits...'
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
+	print('disabling/disposing %d/%d hits' % (len(hits_to_disable), len(hits_to_dispose)))
+	list(map(disable_hit, hits_to_disable))
+	list(map(dispose_hit, hits_to_dispose))
 
 	total_hits = len(all_hits)
 	hits_processed = len(hits_to_process)
 	skipped = total_hits - hits_processed
 	fmt = 'Processed: %(total_hits)d HITs, disabled/disposed: %(hits_processed)d, skipped: %(skipped)d'
-	print fmt % vars()
+	print(fmt % vars())
 
 if __name__ == '__main__':
 	cleanup()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/common.py	(refactored)
@@ -5,7 +5,7 @@
 from boto.mturk.question import (
         Question, QuestionContent, AnswerSpecification, FreeTextAnswer,
 )
-from _init_environment import SetHostMTurkConnection, config_environment
+from ._init_environment import SetHostMTurkConnection, config_environment
 
 class MTurkCommon(unittest.TestCase):
         def setUp(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_external.py	(refactored)
@@ -3,7 +3,7 @@
 import datetime
 from boto.mturk.question import ExternalQuestion
 
-from _init_environment import SetHostMTurkConnection, external_url, \
+from ._init_environment import SetHostMTurkConnection, external_url, \
         config_environment
 
 class Test(unittest.TestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_test.py	(refactored)
@@ -2,7 +2,7 @@
 import os
 from boto.mturk.question import QuestionForm
 
-from common import MTurkCommon
+from .common import MTurkCommon
 
 class TestHITCreation(MTurkCommon):
 	def testCallCreateHitWithOneQuestion(self):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/mocks.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/run-doctest.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_exception.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_stsanon.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py

--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/create_hit_with_qualifications.py	(refactored)
@@ -10,7 +10,7 @@
     qualifications.add(PercentAssignmentsApprovedRequirement(comparator="GreaterThan", integer_value="95"))
     create_hit_rs = conn.create_hit(question=q, lifetime=60*65, max_assignments=2, title="Boto External Question Test", keywords=keywords, reward = 0.05, duration=60*6, approval_delay=60*60, annotation='An annotation from boto external question test', qualifications=qualifications)
     assert(create_hit_rs.status == True)
-    print create_hit_rs.HITTypeId
+    print(create_hit_rs.HITTypeId)
 
 if __name__ == "__main__":
     test()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/hit_persistence.py	(refactored)
@@ -1,7 +1,7 @@
 import unittest
 import pickle
 
-from common import MTurkCommon
+from .common import MTurkCommon
 
 class TestHITPersistence(MTurkCommon):
 	def create_hit_result(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py	(refactored)
@@ -1,4 +1,4 @@
-from __future__ import absolute_import
+
 from boto.mturk.test.support import unittest
 
 sel_args = ('localhost', 4444, '*chrome', 'https://workersandbox.mturk.com')
@@ -6,7 +6,7 @@
 class SeleniumFailed(object):
 	def __init__(self, message):
 		self.message = message
-	def __nonzero__(self):
+	def __bool__(self):
 		return False
 
 def has_selenium():
@@ -17,7 +17,7 @@
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
@@ -1,6 +1,6 @@
 from tests.mturk.support import unittest
 
-from common import MTurkCommon
+from .common import MTurkCommon
 from boto.mturk.connection import MTurkRequestError
 
 class TestDisableHITs(MTurkCommon):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py	(refactored)
@@ -504,7 +504,7 @@
 
 class TestHTTPRequest(unittest.TestCase):
     def test_user_agent_not_url_encoded(self):
-        headers = {'Some-Header': u'should be url encoded',
+        headers = {'Some-Header': 'should be url encoded',
                    'User-Agent': UserAgent}
         request = HTTPRequest('PUT', 'https', 'amazon.com', 443, None,
                               None, {}, headers, 'Body')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py	(refactored)
@@ -84,7 +84,7 @@
         auth = HmacAuthV4Handler('sns.us-east-1.amazonaws.com',
                                  mock.Mock(), self.provider)
         params = {
-            'Message': u'We \u2665 utf-8'.encode('utf-8'),
+            'Message': 'We \u2665 utf-8'.encode('utf-8'),
         }
         request = HTTPRequest(
             'POST', 'https', 'sns.us-east-1.amazonaws.com', 443,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_layer1.py	(refactored)
@@ -16,16 +16,16 @@
 
     def default_body(self):
         return json.dumps(
-            {u'ListAvailableSolutionStacksResponse':
-               {u'ListAvailableSolutionStacksResult':
-                  {u'SolutionStackDetails': [
-                      {u'PermittedFileTypes': [u'war', u'zip'],
-                       u'SolutionStackName': u'32bit Amazon Linux running Tomcat 7'},
-                      {u'PermittedFileTypes': [u'zip'],
-                       u'SolutionStackName': u'32bit Amazon Linux running PHP 5.3'}],
-                      u'SolutionStacks': [u'32bit Amazon Linux running Tomcat 7',
-                                          u'32bit Amazon Linux running PHP 5.3']},
-                u'ResponseMetadata': {u'RequestId': u'request_id'}}}).encode('utf-8')
+            {'ListAvailableSolutionStacksResponse':
+               {'ListAvailableSolutionStacksResult':
+                  {'SolutionStackDetails': [
+                      {'PermittedFileTypes': ['war', 'zip'],
+                       'SolutionStackName': '32bit Amazon Linux running Tomcat 7'},
+                      {'PermittedFileTypes': ['zip'],
+                       'SolutionStackName': '32bit Amazon Linux running PHP 5.3'}],
+                      'SolutionStacks': ['32bit Amazon Linux running Tomcat 7',
+                                          '32bit Amazon Linux running PHP 5.3']},
+                'ResponseMetadata': {'RequestId': 'request_id'}}}).encode('utf-8')
 
     def test_list_available_solution_stacks(self):
         self.set_http_response(status_code=200)
@@ -37,8 +37,8 @@
                                       ['ListAvailableSolutionStacksResult']\
                                       ['SolutionStacks']
         self.assertEqual(solution_stacks,
-                        [u'32bit Amazon Linux running Tomcat 7',
-                         u'32bit Amazon Linux running PHP 5.3'])
+                        ['32bit Amazon Linux running Tomcat 7',
+                         '32bit Amazon Linux running PHP 5.3'])
         # These are the parameters that are actually sent to the CloudFormation
         # service.
         self.assert_request_parameters({
@@ -54,15 +54,15 @@
     def default_body(self):
         return json.dumps({
             'CreateApplicationVersionResponse':
-              {u'CreateApplicationVersionResult':
-                 {u'ApplicationVersion':
-                    {u'ApplicationName': u'application1',
-                     u'DateCreated': 1343067094.342,
-                     u'DateUpdated': 1343067094.342,
-                     u'Description': None,
-                     u'SourceBundle': {u'S3Bucket': u'elasticbeanstalk-us-east-1',
-                     u'S3Key': u'resources/elasticbeanstalk-sampleapp.war'},
-                     u'VersionLabel': u'version1'}}}}).encode('utf-8')
+              {'CreateApplicationVersionResult':
+                 {'ApplicationVersion':
+                    {'ApplicationName': 'application1',
+                     'DateCreated': 1343067094.342,
+                     'DateUpdated': 1343067094.342,
+                     'Description': None,
+                     'SourceBundle': {'S3Bucket': 'elasticbeanstalk-us-east-1',
+                     'S3Key': 'resources/elasticbeanstalk-sampleapp.war'},
+                     'VersionLabel': 'version1'}}}}).encode('utf-8')
 
     def test_create_application_version(self):
         self.set_http_response(status_code=200)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_distribution.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py

@@ -41,15 +41,15 @@
 
     def setUp(self):
         super(CloudFormationConnectionBase, self).setUp()
-        self.stack_id = u'arn:aws:cloudformation:us-east-1:18:stack/Name/id'
+        self.stack_id = 'arn:aws:cloudformation:us-east-1:18:stack/Name/id'
 
 
 class TestCloudFormationCreateStack(CloudFormationConnectionBase):
     def default_body(self):
         return json.dumps(
-            {u'CreateStackResponse':
-                 {u'CreateStackResult': {u'StackId': self.stack_id},
-                  u'ResponseMetadata': {u'RequestId': u'1'}}}).encode('utf-8')
+            {'CreateStackResponse':
+                 {'CreateStackResult': {'StackId': self.stack_id},
+                  'ResponseMetadata': {'RequestId': '1'}}}).encode('utf-8')
 
     def test_create_stack_has_correct_request_params(self):
         self.set_http_response(status_code=200)
@@ -104,7 +104,7 @@
     def test_create_stack_fails(self):
         self.set_http_response(status_code=400, reason='Bad Request',
             body=b'{"Error": {"Code": 1, "Message": "Invalid arg."}}')
-        with self.assertRaisesRegexp(self.service_connection.ResponseError,
+        with self.assertRaisesRegex(self.service_connection.ResponseError,
             'Invalid arg.'):
             api_response = self.service_connection.create_stack(
                 'stack_name', template_body=SAMPLE_TEMPLATE,
@@ -125,9 +125,9 @@
 class TestCloudFormationUpdateStack(CloudFormationConnectionBase):
     def default_body(self):
         return json.dumps(
-            {u'UpdateStackResponse':
-                 {u'UpdateStackResult': {u'StackId': self.stack_id},
-                  u'ResponseMetadata': {u'RequestId': u'1'}}}).encode('utf-8')
+            {'UpdateStackResponse':
+                 {'UpdateStackResult': {'StackId': self.stack_id},
+                  'ResponseMetadata': {'RequestId': '1'}}}).encode('utf-8')
 
     def test_update_stack_all_args(self):
         self.set_http_response(status_code=200)
@@ -193,8 +193,8 @@
 class TestCloudFormationDeleteStack(CloudFormationConnectionBase):
     def default_body(self):
         return json.dumps(
-            {u'DeleteStackResponse':
-                 {u'ResponseMetadata': {u'RequestId': u'1'}}}).encode('utf-8')
+            {'DeleteStackResponse':
+                 {'ResponseMetadata': {'RequestId': '1'}}}).encode('utf-8')
 
     def test_delete_stack(self):
         self.set_http_response(status_code=200)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py	(refactored)
@@ -143,7 +143,7 @@
         h = boto.handler.XmlHandler(rs, None)
         xml.sax.parseString(SAMPLE_XML, h)
         tags = rs[0].tags
-        self.assertEqual(tags, {u'key0': u'value0', u'key1': u'value1'})
+        self.assertEqual(tags, {'key0': 'value0', 'key1': 'value1'})
 
     def test_event_creation_time_with_millis(self):
         millis_xml = SAMPLE_XML.replace(
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
         policy = json.loads(policy)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py

 
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
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py	(refactored)
@@ -24,7 +24,7 @@
         with mock.patch.object(json, 'loads', fake_loads_value_error):
             search = SearchConnection(endpoint=HOSTNAME)
 
-            with self.assertRaisesRegexp(SearchServiceException, 'non-json'):
+            with self.assertRaisesRegex(SearchServiceException, 'non-json'):
                 search.search(q='test')
 
     @unittest.skipUnless(hasattr(json, 'JSONDecodeError'),
@@ -33,5 +33,5 @@
         with mock.patch.object(json, 'loads', fake_loads_json_error):
             search = SearchConnection(endpoint=HOSTNAME)
 
-            with self.assertRaisesRegexp(SearchServiceException, 'non-json'):
+            with self.assertRaisesRegex(SearchServiceException, 'non-json'):
                 search.search(q='test')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py	(refactored)
@@ -295,7 +295,7 @@
 
         results = search.search(q='Test')
 
-        hits = list(map(lambda x: x['id'], results.docs))
+        hits = list([x['id'] for x in results.docs])
 
         # This relies on the default response which is fed into HTTPretty
         self.assertEqual(
@@ -361,7 +361,7 @@
         results = search.search(q='Test', facet=['tags'])
 
         self.assertTrue('tags' not in results.facets)
-        self.assertEqual(results.facets['animals'], {u'lions': u'1', u'fish': u'2'})
+        self.assertEqual(results.facets['animals'], {'lions': '1', 'fish': '2'})
 
 
 class CloudSearchNonJsonTest(CloudSearchSearchBaseTest):
@@ -384,7 +384,7 @@
     def test_response(self):
         search = SearchConnection(endpoint=HOSTNAME)
 
-        with self.assertRaisesRegexp(SearchServiceException, 'foo bar baz'):
+        with self.assertRaisesRegex(SearchServiceException, 'foo bar baz'):
             search.search(q='Test')
 
 
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
 
@@ -343,4 +343,4 @@
         except CommitMismatchError as e:
             self.assertTrue(hasattr(e, 'errors'))
             self.assertIsInstance(e.errors, list)
-            self.assertEquals(e.errors[0], self.response['errors'][0].get('message'))
+            self.assertEqual(e.errors[0], self.response['errors'][0].get('message'))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py	(refactored)
@@ -24,7 +24,7 @@
         with mock.patch.object(json, 'loads', fake_loads_value_error):
             search = SearchConnection(endpoint=HOSTNAME)
 
-            with self.assertRaisesRegexp(SearchServiceException, 'non-json'):
+            with self.assertRaisesRegex(SearchServiceException, 'non-json'):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearchdomain/test_cloudsearchdomain.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudtrail/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/directconnect/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_batch.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py

                 search.search(q='test')
 
     @unittest.skipUnless(hasattr(json, 'JSONDecodeError'),
@@ -33,5 +33,5 @@
         with mock.patch.object(json, 'loads', fake_loads_json_error):
             search = SearchConnection(endpoint=HOSTNAME)
 
-            with self.assertRaisesRegexp(SearchServiceException, 'non-json'):
+            with self.assertRaisesRegex(SearchServiceException, 'non-json'):
                 search.search(q='test')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py	(refactored)
@@ -241,7 +241,7 @@
 
         results = search.search(q='Test')
 
-        hits = list(map(lambda x: x['id'], results.docs))
+        hits = list([x['id'] for x in results.docs])
 
         # This relies on the default response which is fed into HTTPretty
         self.assertEqual(
@@ -307,7 +307,7 @@
         results = search.search(q='Test', facet={'tags': {}})
 
         self.assertTrue('tags' not in results.facets)
-        self.assertEqual(results.facets['animals'], {u'lions': u'1', u'fish': u'2'})
+        self.assertEqual(results.facets['animals'], {'lions': '1', 'fish': '2'})
 
 
 class CloudSearchNonJsonTest(CloudSearchSearchBaseTest):
@@ -330,7 +330,7 @@
     def test_response(self):
         search = SearchConnection(endpoint=HOSTNAME)
 
-        with self.assertRaisesRegexp(SearchServiceException, 'foo bar baz'):
+        with self.assertRaisesRegex(SearchServiceException, 'foo bar baz'):
             search.search(q='Test')
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_batch.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_batch.py	(refactored)
@@ -32,8 +32,8 @@
     'Table': {
         'CreationDateTime': 1349910554.478,
         'ItemCount': 1,
-        'KeySchema': {'HashKeyElement': {'AttributeName': u'foo',
-                                         'AttributeType': u'S'}},
+        'KeySchema': {'HashKeyElement': {'AttributeName': 'foo',
+                                         'AttributeType': 'S'}},
         'ProvisionedThroughput': {'ReadCapacityUnits': 10,
                                   'WriteCapacityUnits': 10},
         'TableName': 'testtable',
@@ -45,8 +45,8 @@
     'Table': {
         'CreationDateTime': 1349910554.478,
         'ItemCount': 1,
-        'KeySchema': {'HashKeyElement': {'AttributeName': u'baz',
-                                         'AttributeType': u'S'},
+        'KeySchema': {'HashKeyElement': {'AttributeName': 'baz',
+                                         'AttributeType': 'S'},
                       'RangeKeyElement': {'AttributeName': 'myrange',
                                           'AttributeType': 'N'}},
         'ProvisionedThroughput': {'ReadCapacityUnits': 10,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py	(refactored)
@@ -122,13 +122,13 @@
     @unittest.skipUnless(six.PY2, "Python 2 only")
     def test_unicode_py2(self):
         # It's dirty. But remains for backward compatibility.
-        data = types.Binary(u'\x01')
+        data = types.Binary('\x01')
         self.assertEqual(data, b'\x01')
         self.assertEqual(bytes(data), b'\x01')
 
         # Delegate to built-in b'\x01' == u'\x01'
         # In Python 2.x these are considered equal
-        self.assertEqual(data, u'\x01')
+        self.assertEqual(data, '\x01')
 
         # Check that the value field is of type bytes
         self.assertEqual(type(data.value), bytes)
@@ -136,7 +136,7 @@
     @unittest.skipUnless(six.PY3, "Python 3 only")
     def test_unicode_py3(self):
         with self.assertRaises(TypeError):
-            types.Binary(u'\x01')
+            types.Binary('\x01')
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py	(refactored)
@@ -371,14 +371,14 @@
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
@@ -403,7 +403,7 @@
 
     def test_items(self):
         self.assertCountEqual(
-            self.johndoe.items(),
+            list(self.johndoe.items()),
             [
                 ('date_joined', 12345),
                 ('first_name', 'John'),
@@ -956,7 +956,7 @@
         self.assertEqual(next(self.results), 'Hello john #10')
         self.assertEqual(next(self.results), 'Hello john #11')
         self.assertEqual(next(self.results), 'Hello john #12')
-        self.assertRaises(StopIteration, self.results.next)
+        self.assertRaises(StopIteration, self.results.__next__)
         self.assertEqual(self.results._limit, 7)
 
     def test_limit_smaller_than_first_page(self):
@@ -964,7 +964,7 @@
         results.to_call(fake_results, 'john', greeting='Hello', limit=2)
         self.assertEqual(next(results), 'Hello john #0')
         self.assertEqual(next(results), 'Hello john #1')
-        self.assertRaises(StopIteration, results.next)
+        self.assertRaises(StopIteration, results.__next__)
 
     def test_limit_equals_page(self):
         results = ResultSet()
@@ -975,7 +975,7 @@
         self.assertEqual(next(results), 'Hello john #2')
         self.assertEqual(next(results), 'Hello john #3')
         self.assertEqual(next(results), 'Hello john #4')
-        self.assertRaises(StopIteration, results.next)
+        self.assertRaises(StopIteration, results.__next__)
 
     def test_limit_greater_than_page(self):
         results = ResultSet()
@@ -988,7 +988,7 @@
         self.assertEqual(next(results), 'Hello john #4')
         # Second page
         self.assertEqual(next(results), 'Hello john #5')
-        self.assertRaises(StopIteration, results.next)
+        self.assertRaises(StopIteration, results.__next__)
 
     def test_iteration_noresults(self):
         def none(limit=10):
@@ -998,7 +998,7 @@
 
         results = ResultSet()
         results.to_call(none, limit=20)
-        self.assertRaises(StopIteration, results.next)
+        self.assertRaises(StopIteration, results.__next__)
 
     def test_iteration_sporadic_pages(self):
         # Some pages have no/incomplete results but have a ``LastEvaluatedKey``
@@ -1052,7 +1052,7 @@
         self.assertEqual(next(results), 'Result #4')
         self.assertEqual(next(results), 'Result #5')
         self.assertEqual(next(results), 'Result #6')
-        self.assertRaises(StopIteration, results.next)
+        self.assertRaises(StopIteration, results.__next__)
 
     def test_list(self):
         self.assertEqual(list(self.results), [
@@ -1135,7 +1135,7 @@
 
         self.results.fetch_more()
         self.assertEqual(self.results._results, [])
-        self.assertRaises(StopIteration, self.results.next)
+        self.assertRaises(StopIteration, self.results.__next__)
 
     def test_iteration(self):
         # First page.
@@ -1143,7 +1143,7 @@
         self.assertEqual(next(self.results), 'hello bob')
         self.assertEqual(next(self.results), 'hello jane')
         self.assertEqual(next(self.results), 'hello johndoe')RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_address.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_blockdevicemapping.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_ec2object.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancestatus.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancetype.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_securitygroup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_snapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_spotinstance.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_volume.py

-        self.assertRaises(StopIteration, self.results.next)
+        self.assertRaises(StopIteration, self.results.__next__)
 
 
 class TableTestCase(unittest.TestCase):
@@ -2606,7 +2606,7 @@
             self.assertEqual(len(results._results), 1)
             self.assertEqual(res_3['username'], 'foodoe')
 
-            self.assertRaises(StopIteration, results.next)
+            self.assertRaises(StopIteration, results.__next__)
 
         self.assertEqual(mock_query_2.call_count, 1)
 
@@ -2697,7 +2697,7 @@
             self.assertEqual(len(results._results), 1)
             self.assertEqual(res_3['username'], 'zoeydoe')
 
-            self.assertRaises(StopIteration, results.next)
+            self.assertRaises(StopIteration, results.__next__)
 
         self.assertEqual(mock_scan_2.call_count, 1)
 
@@ -3060,7 +3060,7 @@
             self.assertEqual(len(results._results), 1)
             self.assertEqual(res_3['username'], 'zoeydoe')
 
-            self.assertRaises(StopIteration, results.next)
+            self.assertRaises(StopIteration, results.__next__)
 
         self.assertEqual(mock_batch_get_2.call_count, 1)
         self.assertEqual(results._keys_left, [])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py	(refactored)
@@ -1,5 +1,5 @@
 #!/usr/bin/env python
-import httplib
+import http.client
 
 from datetime import datetime, timedelta
 from mock import MagicMock, Mock
@@ -785,33 +785,33 @@
     def test_get_all_images(self):
         self.set_http_response(status_code=200)
         parsed = self.ec2.get_all_images()
-        self.assertEquals(1, len(parsed))
-        self.assertEquals("ami-abcd1234", parsed[0].id)
-        self.assertEquals("111111111111/windows2008r2-hvm-i386-20130702", parsed[0].location)
-        self.assertEquals("available", parsed[0].state)
-        self.assertEquals("111111111111", parsed[0].ownerId)
-        self.assertEquals("111111111111", parsed[0].owner_id)
-        self.assertEquals(False, parsed[0].is_public)
-        self.assertEquals("i386", parsed[0].architecture)
-        self.assertEquals("machine", parsed[0].type)
-        self.assertEquals(None, parsed[0].kernel_id)
-        self.assertEquals(None, parsed[0].ramdisk_id)
-        self.assertEquals(None, parsed[0].owner_alias)
-        self.assertEquals("windows", parsed[0].platform)
-        self.assertEquals("Windows Test", parsed[0].name)
-        self.assertEquals("Windows Test Description", parsed[0].description)
-        self.assertEquals("ebs", parsed[0].root_device_type)
-        self.assertEquals("/dev/sda1", parsed[0].root_device_name)
-        self.assertEquals("hvm", parsed[0].virtualization_type)
-        self.assertEquals("xen", parsed[0].hypervisor)
-        self.assertEquals(None, parsed[0].instance_lifecycle)
+        self.assertEqual(1, len(parsed))
+        self.assertEqual("ami-abcd1234", parsed[0].id)
+        self.assertEqual("111111111111/windows2008r2-hvm-i386-20130702", parsed[0].location)
+        self.assertEqual("available", parsed[0].state)
+        self.assertEqual("111111111111", parsed[0].ownerId)
+        self.assertEqual("111111111111", parsed[0].owner_id)
+        self.assertEqual(False, parsed[0].is_public)
+        self.assertEqual("i386", parsed[0].architecture)
+        self.assertEqual("machine", parsed[0].type)
+        self.assertEqual(None, parsed[0].kernel_id)
+        self.assertEqual(None, parsed[0].ramdisk_id)
+        self.assertEqual(None, parsed[0].owner_alias)
+        self.assertEqual("windows", parsed[0].platform)
+        self.assertEqual("Windows Test", parsed[0].name)
+        self.assertEqual("Windows Test Description", parsed[0].description)
+        self.assertEqual("ebs", parsed[0].root_device_type)
+        self.assertEqual("/dev/sda1", parsed[0].root_device_name)
+        self.assertEqual("hvm", parsed[0].virtualization_type)
+        self.assertEqual("xen", parsed[0].hypervisor)
+        self.assertEqual(None, parsed[0].instance_lifecycle)
 
         # 1 billing product parsed into a list
-        self.assertEquals(1, len(parsed[0].billing_products))
-        self.assertEquals("bp-6ba54002", parsed[0].billing_products[0])
+        self.assertEqual(1, len(parsed[0].billing_products))
+        self.assertEqual("bp-6ba54002", parsed[0].billing_products[0])
 
         # Just verify length, there is already a block_device_mapping test
-        self.assertEquals(5, len(parsed[0].block_device_mapping))
+        self.assertEqual(5, len(parsed[0].block_device_mapping))
 
         # TODO: No tests for product codes?
 
@@ -929,25 +929,25 @@
     def test_modify_group_set_invalid(self):
         self.set_http_response(status_code=200)
 
-        with self.assertRaisesRegexp(TypeError, 'iterable'):
+        with self.assertRaisesRegex(TypeError, 'iterable'):
             self.ec2.modify_network_interface_attribute('id', 'groupSet',
                                                         False)
 
     def test_modify_attr_invalid(self):
         self.set_http_response(status_code=200)
 
-        with self.assertRaisesRegexp(ValueError, 'Unknown attribute'):
+        with self.assertRaisesRegex(ValueError, 'Unknown attribute'):
             self.ec2.modify_network_interface_attribute('id', 'invalid', 0)
 
 
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py	(refactored)
@@ -53,7 +53,7 @@
     def test_update_with_validate_true_raises_value_error(self):
         self.eni_one.connection = mock.Mock()
         self.eni_one.connection.get_all_network_interfaces.return_value = []
-        with self.assertRaisesRegexp(ValueError, "^eni-1 is not a valid ENI ID$"):
+        with self.assertRaisesRegex(ValueError, "^eni-1 is not a valid ENI ID$"):
             self.eni_one.update(True)
 
     def test_update_with_result_set_greater_than_0_updates_dict(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py	(refactored)
@@ -38,7 +38,7 @@
 
         self.assertEqual(len(response), 1)
         self.assertTrue(isinstance(response[0], ReservedInstance))
-        self.assertEquals(response[0].id, 'ididididid')
-        self.assertEquals(response[0].instance_count, 5)
-        self.assertEquals(response[0].start, '2014-05-03T14:10:10.944Z')
-        self.assertEquals(response[0].end, '2014-05-03T14:10:11.000Z')
+        self.assertEqual(response[0].id, 'ididididid')
+        self.assertEqual(response[0].instance_count, 5)
+        self.assertEqual(response[0].start, '2014-05-03T14:10:10.944Z')
+        self.assertEqual(response[0].end, '2014-05-03T14:10:11.000Z')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_volume.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_volume.py	(refactored)
@@ -113,7 +113,7 @@
     def test_update_with_validate_true_raises_value_error(self):RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/autoscale/test_group.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/cloudwatch/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_attribute.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_listener.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_loadbalancer.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ecs/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/elasticache/test_api_interface.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_instance_group_args.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_job.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer1.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_response.py

         self.volume_one.connection = mock.Mock()
         self.volume_one.connection.get_all_volumes.return_value = []
-        with self.assertRaisesRegexp(ValueError, "^1 is not a valid Volume ID$"):
+        with self.assertRaisesRegex(ValueError, "^1 is not a valid Volume ID$"):
             self.volume_one.update(True)
 
     def test_update_returns_status(self):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py	(refactored)
@@ -344,9 +344,9 @@
         return rs
 
     def _assert_fields(self, response, **fields):
-        for field, expected in fields.items():
+        for field, expected in list(fields.items()):
             actual = getattr(response, field)
-            self.assertEquals(expected, actual,
+            self.assertEqual(expected, actual,
                               "Field %s: %r != %r" % (field, expected, actual))
 
     def test_JobFlows_example(self):
@@ -383,6 +383,6 @@
                             masterinstancetype='m1.large',
                             ec2keyname='myubersecurekey',
                             keepjobflowalivewhennosteps='false')
-        self.assertEquals(6, len(jobflow.steps))
-        self.assertEquals(2, len(jobflow.instancegroups))
-
+        self.assertEqual(6, len(jobflow.steps))
+        self.assertEqual(2, len(jobflow.instancegroups))
+
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_instance_group_args.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_instance_group_args.py	(refactored)
@@ -17,7 +17,7 @@
         Test InstanceGroup init raises ValueError when market==spot and
         bidprice is not specified.
         """
-        with self.assertRaisesRegexp(ValueError, 'bidprice must be specified'):
+        with self.assertRaisesRegex(ValueError, 'bidprice must be specified'):
             InstanceGroup(1, 'MASTER', 'm1.small',
                           'SPOT', 'master')
 
@@ -35,7 +35,7 @@
         """
         instance_group = InstanceGroup(1, 'MASTER', 'm1.small',
                                        'SPOT', 'master', bidprice=Decimal(1.10))
-        self.assertEquals('1.10', instance_group.bidprice[:4])
+        self.assertEqual('1.10', instance_group.bidprice[:4])
 
     def test_bidprice_float(self):
         """
@@ -43,7 +43,7 @@
         """
         instance_group = InstanceGroup(1, 'MASTER', 'm1.small',
                                        'SPOT', 'master', bidprice=1.1)
-        self.assertEquals('1.1', instance_group.bidprice)
+        self.assertEqual('1.1', instance_group.bidprice)
 
     def test_bidprice_string(self):
         """
@@ -51,7 +51,7 @@
         """
         instance_group = InstanceGroup(1, 'MASTER', 'm1.small',
                                        'SPOT', 'master', bidprice='1.1')
-        self.assertEquals('1.1', instance_group.bidprice)
+        self.assertEqual('1.1', instance_group.bidprice)
 
 if __name__ == "__main__":
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer1.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer1.py	(refactored)
@@ -12,15 +12,15 @@
     def setUp(self):
         super(GlacierLayer1ConnectionBase, self).setUp()
         self.json_header = [('Content-Type', 'application/json')]
-        self.vault_name = u'examplevault'
+        self.vault_name = 'examplevault'
         self.vault_arn = 'arn:aws:glacier:us-east-1:012345678901:vaults/' + \
                           self.vault_name
-        self.vault_info = {u'CreationDate': u'2012-03-16T22:22:47.214Z',
-                           u'LastInventoryDate': u'2012-03-21T22:06:51.218Z',
-                           u'NumberOfArchives': 2,
-                           u'SizeInBytes': 12334,
-                           u'VaultARN': self.vault_arn,
-                           u'VaultName': self.vault_name}
+        self.vault_info = {'CreationDate': '2012-03-16T22:22:47.214Z',
+                           'LastInventoryDate': '2012-03-21T22:06:51.218Z',
+                           'NumberOfArchives': 2,
+                           'SizeInBytes': 12334,
+                           'VaultARN': self.vault_arn,
+                           'VaultName': self.vault_name}
 
 
 class GlacierVaultsOperations(GlacierLayer1ConnectionBase):
@@ -30,9 +30,9 @@
         self.service_connection.create_vault(self.vault_name)
 
     def test_list_vaults(self):
-        content = {u'Marker': None,
-                   u'RequestId': None,
-                   u'VaultList': [self.vault_info]}
+        content = {'Marker': None,
+                   'RequestId': None,
+                   'VaultList': [self.vault_info]}
         self.set_http_response(status_code=200, header=self.json_header,
                                body=json.dumps(content).encode('utf-8'))
         api_response = self.service_connection.list_vaults()
@@ -40,7 +40,7 @@
 
     def test_describe_vaults(self):
         content = copy.copy(self.vault_info)
-        content[u'RequestId'] = None
+        content['RequestId'] = None
         self.set_http_response(status_code=200, header=self.json_header,
                                body=json.dumps(content).encode('utf-8'))
         api_response = self.service_connection.describe_vault(self.vault_name)
@@ -58,13 +58,13 @@
         self.job_content = 'abc' * 1024
 
     def test_initiate_archive_job(self):
-        content = {u'Type': u'archive-retrieval',
-                   u'ArchiveId': u'AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q',
-                   u'Description': u'Test Archive',
-                   u'SNSTopic': u'Topic',
-                   u'JobId': None,
-                   u'Location': None,
-                   u'RequestId': None}
+        content = {'Type': 'archive-retrieval',
+                   'ArchiveId': 'AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q',
+                   'Description': 'Test Archive',
+                   'SNSTopic': 'Topic',
+                   'JobId': None,
+                   'Location': None,
+                   'RequestId': None}
         self.set_http_response(status_code=202, header=self.json_header,
                                body=json.dumps(content).encode('utf-8'))
         api_response = self.service_connection.initiate_job(self.vault_name,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py	(refactored)
@@ -257,8 +257,8 @@
             dict(EXAMPLE_PART_LIST_COMPLETE)) # take a copy
         parts_result = self.vault.list_all_parts(sentinel.upload_id)
         expected = [call('examplevault', sentinel.upload_id)]
-        self.assertEquals(expected, self.mock_layer1.list_parts.call_args_list)
-        self.assertEquals(EXAMPLE_PART_LIST_COMPLETE, parts_result)
+        self.assertEqual(expected, self.mock_layer1.list_parts.call_args_list)
+        self.assertEqual(EXAMPLE_PART_LIST_COMPLETE, parts_result)
 
     def test_list_all_parts_two_pages(self):
         self.mock_layer1.list_parts.side_effect = [
@@ -270,8 +270,8 @@
         expected = [call('examplevault', sentinel.upload_id),
                     call('examplevault', sentinel.upload_id,
                          marker=EXAMPLE_PART_LIST_RESULT_PAGE_1['Marker'])]
-        self.assertEquals(expected, self.mock_layer1.list_parts.call_args_list)
-        self.assertEquals(EXAMPLE_PART_LIST_COMPLETE, parts_result)
+        self.assertEqual(expected, self.mock_layer1.list_parts.call_args_list)
+        self.assertEqual(EXAMPLE_PART_LIST_COMPLETE, parts_result)RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_utils.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/iam/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kinesis/test_kinesis.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kms/test_kms.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/logs/test_layer1.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/machinelearning/test_machinelearning.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/manage/test_ssh.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mturk/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py

 
     @patch('boto.glacier.vault.resume_file_upload')
     def test_resume_archive_from_file(self, mock_resume_file_upload):
@@ -313,7 +313,7 @@
 
 class TestRangeStringParsing(unittest.TestCase):
     def test_simple_range(self):
-        self.assertEquals(
+        self.assertEqual(
             Vault._range_string_to_part_index('0-3', 4), 0)
 
     def test_range_one_too_big(self):
@@ -321,7 +321,7 @@
         # See: https://forums.aws.amazon.com/thread.jspa?threadID=106866&tstart=0
         # Workaround is to assume that if a (start, end] range appears to be
         # returned then that is what it is.
-        self.assertEquals(
+        self.assertEqual(
             Vault._range_string_to_part_index('0-4', 4), 0)
 
     def test_range_too_big(self):
@@ -334,5 +334,5 @@
 
     def test_range_end_mismatch(self):
         # End mismatch is OK, since the last part might be short
-        self.assertEquals(
+        self.assertEqual(
             Vault._range_string_to_part_index('0-2', 4), 0)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_response.py	(refactored)
@@ -29,7 +29,7 @@
     def test_204_body_isnt_passed_to_json(self):
         response = self.create_response(status_code=204,header=[('Content-Type','application/json')])
         result = GlacierResponse(response,response.getheaders())
-        self.assertEquals(result.status, response.status)
+        self.assertEqual(result.status, response.status)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py	(refactored)
@@ -130,7 +130,7 @@
     def test_returns_archive_id(self):
         self.writer.write(b'1')
         self.writer.close()
-        self.assertEquals(sentinel.archive_id, self.writer.get_archive_id())
+        self.assertEqual(sentinel.archive_id, self.writer.get_archive_id())
 
     def test_current_tree_hash(self):
         self.writer.write(b'1234')
@@ -178,7 +178,7 @@
         self.assertEqual(final_size, self.writer.current_uploaded_size)
 
     def test_upload_id(self):
-        self.assertEquals(sentinel.upload_id, self.writer.upload_id)
+        self.assertEqual(sentinel.upload_id, self.writer.upload_id)
 
 
 class TestResume(unittest.TestCase):
@@ -226,4 +226,4 @@
         archive_id = resume_file_upload(
             self.vault, sentinel.upload_id, self.part_size, StringIO('1'), {},
             self.chunk_size)
-        self.assertEquals(sentinel.archive_id, archive_id)
+        self.assertEqual(sentinel.archive_id, archive_id)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/iam/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/iam/test_connection.py	(refactored)
@@ -332,7 +332,7 @@
     def test_generate_credential_report(self):
         self.set_http_response(status_code=200)
         response = self.service_connection.generate_credential_report()
-        self.assertEquals(response['generate_credential_report_response']
+        self.assertEqual(response['generate_credential_report_response']
                                   ['generate_credential_report_result']
                                   ['state'], 'COMPLETE')
 
@@ -389,7 +389,7 @@
              'VirtualMFADeviceName': 'ExampleName',
              'Action': 'CreateVirtualMFADevice'},
             ignore_params_values=['Version'])
-        self.assertEquals(response['create_virtual_mfa_device_response']
+        self.assertEqual(response['create_virtual_mfa_device_response']
                                   ['create_virtual_mfa_device_result']
                                   ['virtual_mfa_device']
                                   ['serial_number'], 'arn:aws:iam::123456789012:mfa/ExampleName')
@@ -429,7 +429,7 @@
                 'Action': 'GetAccountPasswordPolicy',
             },
             ignore_params_values=['Version'])
-        self.assertEquals(response['get_account_password_policy_response']
+        self.assertEqual(response['get_account_password_policy_response']
                           ['get_account_password_policy_result']['password_policy']
                           ['minimum_password_length'], '12')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kms/test_kms.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kms/test_kms.py	(refactored)
@@ -47,7 +47,7 @@
         This test ensures that only binary is used for blob type parameters.
         """ 
         self.set_http_response(status_code=200)
-        data = u'\u00e9'
+        data = '\u00e9'
         with self.assertRaises(TypeError):
             self.service_connection.encrypt(key_id='foo', plaintext=data)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mturk/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mturk/test_connection.py	(refactored)
@@ -23,6 +23,6 @@
     def test_get_file_upload_url_success(self):
         self.set_http_response(status_code=200, body=GET_FILE_UPLOAD_URL)
         rset = self.service_connection.get_file_upload_url('aid', 'qid')
-        self.assertEquals(len(rset), 1)
-        self.assertEquals(rset[0].FileUploadURL,
+        self.assertEqual(len(rset), 1)
+        self.assertEqual(rset[0].FileUploadURL,
                           'http://s3.amazonaws.com/myawsbucket/puppy.jpg')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_connection.py	(refactored)
@@ -104,7 +104,7 @@
             self.assertEqual(result, amazon)
 
     def test_decorator_order(self):
-        for action, func in api_call_map.items():
+        for action, func in list(api_call_map.items()):
             func = getattr(self.service_connection, func)
             decs = [func.__name__]
             while func:
@@ -126,7 +126,7 @@
         # It starts empty, but the decorators should add to it as they're
         # applied. As of 2013/10/21, there were 52 calls (with more likely
         # to be added), so let's simply ensure there are enough there.
-        self.assertTrue(len(api_call_map.keys()) > 50)
+        self.assertTrue(len(list(api_call_map.keys())) > 50)
 
     def test_method_for(self):
         # First, ensure that the map is in "right enough" state.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py	(refactored)
@@ -34,10 +34,10 @@
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
 
     def test_parsing_member_list_specification(self):RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/mws/test_response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/provider/test_provider.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_snapshot.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds2/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_zone.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_bucket.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_cors_configuration.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_lifecycle.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_tagging.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_uri.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_website.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ses/test_identity.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py

@@ -67,7 +67,7 @@
             list(range(4)),
         )
         self.assertSequenceEqual(
-            list(map(lambda x: list(map(int, x.Foo)), obj._result.Extra)),
+            list([list(map(int, x.Foo)) for x in obj._result.Extra]),
             [[4, 5], [], [6, 7]],
         )
 
@@ -121,14 +121,14 @@
         obj = self.check_issue(Test7Result, text)
         item = obj._result.Item
         self.assertEqual(len(item), 3)
-        nests = [z.Nest for z in filter(lambda x: x.Nest, item)]
+        nests = [z.Nest for z in [x for x in item if x.Nest]]
         self.assertSequenceEqual(
             [[y.Data for y in nest] for nest in nests],
-            [[u'2', u'4', u'6'], [u'1', u'3', u'5']],
+            [['2', '4', '6'], ['1', '3', '5']],
         )
         self.assertSequenceEqual(
             [element.Simple for element in item[1].List],
-            [[u'4', u'5', u'6'], [u'7', u'8', u'9']],
+            [['4', '5', '6'], ['7', '8', '9']],
         )
         self.assertSequenceEqual(
             item[-1].List[0].Simple,
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/provider/test_provider.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/provider/test_provider.py	(refactored)
@@ -10,13 +10,13 @@
 
 INSTANCE_CONFIG = {
     'allowall': {
-        u'AccessKeyId': u'iam_access_key',
-        u'Code': u'Success',
-        u'Expiration': u'2012-09-01T03:57:34Z',
-        u'LastUpdated': u'2012-08-31T21:43:40Z',
-        u'SecretAccessKey': u'iam_secret_key',
-        u'Token': u'iam_token',
-        u'Type': u'AWS-HMAC'
+        'AccessKeyId': 'iam_access_key',
+        'Code': 'Success',
+        'Expiration': '2012-09-01T03:57:34Z',
+        'LastUpdated': '2012-08-31T21:43:40Z',
+        'SecretAccessKey': 'iam_secret_key',
+        'Token': 'iam_token',
+        'Type': 'AWS-HMAC'
     }
 }
 
@@ -348,13 +348,13 @@
         first_expiration = (now + timedelta(seconds=10)).strftime(
             "%Y-%m-%dT%H:%M:%SZ")
         credentials = {
-            u'AccessKeyId': u'first_access_key',
-            u'Code': u'Success',
-            u'Expiration': first_expiration,
-            u'LastUpdated': u'2012-08-31T21:43:40Z',
-            u'SecretAccessKey': u'first_secret_key',
-            u'Token': u'first_token',
-            u'Type': u'AWS-HMAC'
+            'AccessKeyId': 'first_access_key',
+            'Code': 'Success',
+            'Expiration': first_expiration,
+            'LastUpdated': '2012-08-31T21:43:40Z',
+            'SecretAccessKey': 'first_secret_key',
+            'Token': 'first_token',
+            'Type': 'AWS-HMAC'
         }
         instance_config = {'allowall': credentials}
         self.get_instance_metadata.return_value = instance_config
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/rds/test_connection.py	(refactored)
@@ -148,7 +148,7 @@
         self.assertEqual(db.allocated_storage, 200)
         self.assertEqual(
             db.endpoint,
-            (u'mydbinstance2.c0hjqouvn9mf.us-west-2.rds.amazonaws.com', 3306))
+            ('mydbinstance2.c0hjqouvn9mf.us-west-2.rds.amazonaws.com', 3306))
         self.assertEqual(db.instance_class, 'db.m1.large')
         self.assertEqual(db.master_username, 'awsuser')
         self.assertEqual(db.availability_zone, 'us-west-2b')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/route53/test_connection.py	(refactored)
@@ -171,7 +171,7 @@
 
         self.assertEqual(response['CreateHostedZoneResponse']
                                  ['HostedZone']['Config']['PrivateZone'],
-                         u'false')
+                         'false')
 
 
 @attr(route53=True)
@@ -223,11 +223,11 @@
                                                        )
 
         self.assertEqual(r['CreateHostedZoneResponse']['HostedZone']
-                          ['Config']['PrivateZone'], u'true')
+                          ['Config']['PrivateZone'], 'true')
         self.assertEqual(r['CreateHostedZoneResponse']['HostedZone']
-                          ['VPC']['VPCId'], u'vpc-1a2b3c4d')
+                          ['VPC']['VPCId'], 'vpc-1a2b3c4d')
         self.assertEqual(r['CreateHostedZoneResponse']['HostedZone']
-                          ['VPC']['VPCRegion'], u'us-east-1')
+                          ['VPC']['VPCRegion'], 'us-east-1')
 
 
 @attr(route53=True)
@@ -273,9 +273,9 @@
         response = self.service_connection.get_all_hosted_zones()
 
         domains = ['example2.com.', 'example1.com.', 'example.com.']
-        print(response['ListHostedZonesResponse']['HostedZones'][0])
+        print((response['ListHostedZonesResponse']['HostedZones'][0]))
         for d in response['ListHostedZonesResponse']['HostedZones']:
-            print("Removing: %s" % d['Name'])
+            print(("Removing: %s" % d['Name']))
             domains.remove(d['Name'])
 
         self.assertEqual(domains, [])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_bucket.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_bucket.py	(refactored)
@@ -93,7 +93,7 @@
             # Ensure Unicode chars get encoded.
             'bar': '☃',
             # Ensure unicode strings with non-ascii characters get encoded
-            'baz': u'χ',
+            'baz': 'χ',
             # Underscores are bad, m'kay?
             'some_other': 'thing',
             # Change the variant of ``max-keys``.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_connection.py	(refactored)
@@ -179,7 +179,7 @@
 </ListAllMyBucketsResult>"""
 
     def create_service_connection(self, **kwargs):
-        kwargs['calling_format'] = u'boto.s3.connection.OrdinaryCallingFormat'
+        kwargs['calling_format'] = 'boto.s3.connection.OrdinaryCallingFormat'
         return super(TestUnicodeCallingFormat,
                      self).create_service_connection(**kwargs)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py	(refactored)
@@ -42,8 +42,8 @@
 
     def test_unicode_name(self):
         k = Key()
-        k.name = u'Österreich'
-        print(repr(k))
+        k.name = 'Österreich'
+        print((repr(k)))
 
     def test_when_no_restore_header_present(self):
         self.set_http_response(status_code=200)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py	(refactored)
@@ -28,8 +28,8 @@
 from boto.sns.connection import SNSConnection
 
 QUEUE_POLICY = {
-    u'Policy':
-        (u'{"Version":"2008-10-17","Id":"arn:aws:sqs:us-east-1:'
+    'Policy':
+        ('{"Version":"2008-10-17","Id":"arn:aws:sqs:us-east-1:'
          'idnum:testqueuepolicy/SQSDefaultPolicy","Statement":'
          '[{"Sid":"sidnum","Effect":"Allow","Principal":{"AWS":"*"},'
          '"Action":"SQS:GetQueueUrl","Resource":'
@@ -229,7 +229,7 @@
 
     def test_publish_with_utf8_message(self):
         self.set_http_response(status_code=200)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_queue.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sts/test_connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sts/test_credentials.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer1_decisions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_actors.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_base.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_domain.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_types.py

-        subject = message = u'We \u2665 utf-8'.encode('utf-8')
+        subject = message = 'We \u2665 utf-8'.encode('utf-8')
         self.service_connection.publish('topic', message, subject)
         self.assert_request_parameters({
             'Action': 'Publish',
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py	(refactored)
@@ -112,8 +112,8 @@
 
         self.service_connection.get_queue('my_queue', '599169622985')
 
-        assert 'QueueOwnerAWSAccountId' in self.actual_request.params.keys()
-        self.assertEquals(self.actual_request.params['QueueOwnerAWSAccountId'], '599169622985')
+        assert 'QueueOwnerAWSAccountId' in list(self.actual_request.params.keys())
+        self.assertEqual(self.actual_request.params['QueueOwnerAWSAccountId'], '599169622985')
 
 class SQSProfileName(MockServiceWithConfigTestCase):
     connection_class = SQSConnection
@@ -140,7 +140,7 @@
         self.initialize_service_connection()
         self.set_http_response(status_code=200)
 
-        self.assertEquals(self.service_connection.profile_name, self.profile_name)
+        self.assertEqual(self.service_connection.profile_name, self.profile_name)
 
 class SQSMessageAttributesParsing(AWSMockServiceTestCase):
     connection_class = SQSConnection
@@ -192,7 +192,7 @@
                          '324758f82d026ac6ec5b31a3b192d1e3')
 
         mattributes = message.message_attributes
-        self.assertEqual(len(mattributes.keys()), 2)
+        self.assertEqual(len(list(mattributes.keys())), 2)
         self.assertEqual(mattributes['Count']['data_type'], 'Number')
         self.assertEqual(mattributes['Foo']['string_value'], 'Bar')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py	(refactored)
@@ -67,8 +67,8 @@
         with self.assertRaises(SQSDecodeError) as context:
             xml.sax.parseString(body.encode('utf-8'), h)
         message = context.exception.message
-        self.assertEquals(message.id, sample_value)
-        self.assertEquals(message.receipt_handle, sample_value)
+        self.assertEqual(message.id, sample_value)
+        self.assertEqual(message.receipt_handle, sample_value)
 
     @attr(sqs=True)
     def test_encode_bytes_message(self):
@@ -92,20 +92,20 @@
         msg = BigMessage()
         # Try just a bucket name
         bucket, key = msg._get_bucket_key('s3://foo')
-        self.assertEquals(bucket, 'foo')
-        self.assertEquals(key, None)
+        self.assertEqual(bucket, 'foo')
+        self.assertEqual(key, None)
         # Try just a bucket name with trailing "/"
         bucket, key = msg._get_bucket_key('s3://foo/')
-        self.assertEquals(bucket, 'foo')
-        self.assertEquals(key, None)
+        self.assertEqual(bucket, 'foo')
+        self.assertEqual(key, None)
         # Try a bucket and a key
         bucket, key = msg._get_bucket_key('s3://foo/bar')
-        self.assertEquals(bucket, 'foo')
-        self.assertEquals(key, 'bar')
+        self.assertEqual(bucket, 'foo')
+        self.assertEqual(key, 'bar')
         # Try a bucket and a key with "/"
         bucket, key = msg._get_bucket_key('s3://foo/bar/fie/baz')
-        self.assertEquals(bucket, 'foo')
-        self.assertEquals(key, 'bar/fie/baz')
+        self.assertEqual(bucket, 'foo')
+        self.assertEqual(key, 'bar/fie/baz')
         # Try it with no s3:// prefix
         with self.assertRaises(SQSDecodeError) as context:
             bucket, key = msg._get_bucket_key('foo/bar')
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer1_decisions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer1_decisions.py	(refactored)
@@ -9,7 +9,7 @@
         self.decisions = boto.swf.layer1_decisions.Layer1Decisions()
 
     def assert_data(self, *data):
-        self.assertEquals(self.decisions._data, list(data))
+        self.assertEqual(self.decisions._data, list(data))
 
     def test_continue_as_new_workflow_execution(self):
         self.decisions.continue_as_new_workflow_execution(
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_base.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_base.py	(refactored)
@@ -22,10 +22,10 @@
         )
 
     def test_instantiation(self):
-        self.assertEquals(MOCK_DOMAIN, self.swf_base.domain)
-        self.assertEquals(MOCK_ACCESS_KEY, self.swf_base.aws_access_key_id)
-        self.assertEquals(MOCK_SECRET_KEY,
+        self.assertEqual(MOCK_DOMAIN, self.swf_base.domain)
+        self.assertEqual(MOCK_ACCESS_KEY, self.swf_base.aws_access_key_id)
+        self.assertEqual(MOCK_SECRET_KEY,
                           self.swf_base.aws_secret_access_key)
-        self.assertEquals(MOCK_REGION, self.swf_base.region)
+        self.assertEqual(MOCK_REGION, self.swf_base.region)
         boto.swf.layer2.Layer1.assert_called_with(
             MOCK_ACCESS_KEY, MOCK_SECRET_KEY, region=MOCK_REGION)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_domain.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_domain.py	(refactored)
@@ -14,8 +14,8 @@
         self.domain.region = 'test-region'
 
     def test_domain_instantiation(self):
-        self.assertEquals('test-domain', self.domain.name)
-        self.assertEquals('My test domain', self.domain.description)
+        self.assertEqual('test-domain', self.domain.name)
+        self.assertEqual('My test domain', self.domain.description)
 
     def test_domain_list_activities(self):
         self.domain._swf.list_activity_types.return_value = {
@@ -44,11 +44,11 @@
                           'S3Upload', 'SepiaTransform', 'DoUpdate')
 
         activity_types = self.domain.activities()
-        self.assertEquals(6, len(activity_types))
+        self.assertEqual(6, len(activity_types))
         for activity_type in activity_types:
             self.assertIsInstance(activity_type, ActivityType)
             self.assertTrue(activity_type.name in expected_names)
-            self.assertEquals(self.domain.region, activity_type.region)
+            self.assertEqual(self.domain.region, activity_type.region)
 
     def test_domain_list_workflows(self):
         self.domain._swf.list_workflow_types.return_value = {
@@ -63,14 +63,14 @@
         expected_names = ('ProcessFile', 'test_workflow_name') 
         
         workflow_types = self.domain.workflows()
-        self.assertEquals(2, len(workflow_types))
+        self.assertEqual(2, len(workflow_types))
         for workflow_type in workflow_types:
             self.assertIsInstance(workflow_type, WorkflowType)
             self.assertTrue(workflow_type.name in expected_names)
-            self.assertEquals(self.domain.aws_access_key_id, workflow_type.aws_access_key_id)
-            self.assertEquals(self.domain.aws_secret_access_key, workflow_type.aws_secret_access_key)
-            self.assertEquals(self.domain.name, workflow_type.domain)
-            self.assertEquals(self.domain.region, workflow_type.region)
+            self.assertEqual(self.domain.aws_access_key_id, workflow_type.aws_access_key_id)
+            self.assertEqual(self.domain.aws_secret_access_key, workflow_type.aws_secret_access_key)
+            self.assertEqual(self.domain.name, workflow_type.domain)
+            self.assertEqual(self.domain.region, workflow_type.region)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_customergateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_dhcpoptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_internetgateway.py

 
     def test_domain_list_executions(self):
         self.domain._swf.list_open_workflow_executions.return_value = {
@@ -104,13 +104,13 @@
                                       'version': '1.0'}}]}
 
         executions = self.domain.executions()
-        self.assertEquals(4, len(executions))
+        self.assertEqual(4, len(executions))
         for wf_execution in executions:
             self.assertIsInstance(wf_execution, WorkflowExecution)
-            self.assertEquals(self.domain.aws_access_key_id, wf_execution.aws_access_key_id)
-            self.assertEquals(self.domain.aws_secret_access_key, wf_execution.aws_secret_access_key)
-            self.assertEquals(self.domain.name, wf_execution.domain)
-            self.assertEquals(self.domain.region, wf_execution.region)
+            self.assertEqual(self.domain.aws_access_key_id, wf_execution.aws_access_key_id)
+            self.assertEqual(self.domain.aws_secret_access_key, wf_execution.aws_secret_access_key)
+            self.assertEqual(self.domain.name, wf_execution.domain)
+            self.assertEqual(self.domain.region, wf_execution.region)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_types.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_types.py	(refactored)
@@ -38,9 +38,9 @@
         execution = wf_type.start(task_list='hello_world')
 
         self.assertIsInstance(execution, WorkflowExecution)
-        self.assertEquals(wf_type.name, execution.name)
-        self.assertEquals(wf_type.version, execution.version)
-        self.assertEquals(run_id, execution.runId)
+        self.assertEqual(wf_type.name, execution.name)
+        self.assertEqual(wf_type.version, execution.version)
+        self.assertEqual(run_id, execution.runId)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py	(refactored)
@@ -58,17 +58,17 @@
     def clstest(self, cls):
         """Insure that password.__eq__ hashes test value before compare."""
         password = cls('foo')
-        self.assertNotEquals(password, 'foo')
+        self.assertNotEqual(password, 'foo')
 
         password.set('foo')
         hashed = str(password)
-        self.assertEquals(password, 'foo')
-        self.assertEquals(password.str, hashed)
+        self.assertEqual(password, 'foo')
+        self.assertEqual(password.str, hashed)
 
         password = cls(hashed)
-        self.assertNotEquals(password.str, 'foo')
-        self.assertEquals(password, 'foo')
-        self.assertEquals(password.str, hashed)
+        self.assertNotEqual(password.str, 'foo')
+        self.assertEqual(password, 'foo')
+        self.assertEqual(password.str, hashed)
 
     def test_aaa_version_1_9_default_behavior(self):
         self.clstest(Password)
@@ -79,7 +79,7 @@
 
         password = SHA224Password()
         password.set('foo')
-        self.assertEquals(hashlib.sha224(b'foo').hexdigest(), str(password))
+        self.assertEqual(hashlib.sha224(b'foo').hexdigest(), str(password))
 
     def test_hmac(self):
         def hmac_hashfunc(cls, msg):
@@ -94,7 +94,7 @@
         password = HMACPassword()
         password.set('foo')
 
-        self.assertEquals(str(password),
+        self.assertEqual(str(password),
                           hmac.new(b'mysecretkey', b'foo').hexdigest())
 
     def test_constructor(self):
@@ -102,7 +102,7 @@
 
         password = Password(hashfunc=hmac_hashfunc)
         password.set('foo')
-        self.assertEquals(password.str,
+        self.assertEqual(password.str,
                           hmac.new(b'mysecretkey', b'foo').hexdigest())
 
 
@@ -261,7 +261,7 @@
         self.set_normal_response([key_data, invalid_data, invalid_data])
         response = LazyLoadMetadata(url, num_retries)
         with self.assertRaises(ValueError):
-            response.values()[0]
+            list(response.values())[0]
 
     def test_user_data(self):
         self.set_normal_response(['foo'])
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_customergateway.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_customergateway.py	(refactored)
@@ -43,7 +43,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(len(api_response), 1)
+        self.assertEqual(len(api_response), 1)
         self.assertIsInstance(api_response[0], CustomerGateway)
         self.assertEqual(api_response[0].id, 'cgw-b4dc3961')
 
@@ -80,11 +80,11 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, CustomerGateway)
-        self.assertEquals(api_response.id, 'cgw-b4dc3961')
-        self.assertEquals(api_response.state, 'pending')
-        self.assertEquals(api_response.type, 'ipsec.1')
-        self.assertEquals(api_response.ip_address, '12.1.2.3')
-        self.assertEquals(api_response.bgp_asn, 65534)
+        self.assertEqual(api_response.id, 'cgw-b4dc3961')
+        self.assertEqual(api_response.state, 'pending')
+        self.assertEqual(api_response.type, 'ipsec.1')
+        self.assertEqual(api_response.ip_address, '12.1.2.3')
+        self.assertEqual(api_response.bgp_asn, 65534)
 
 
 class TestDeleteCustomerGateway(AWSMockServiceTestCase):
@@ -108,7 +108,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 if __name__ == '__main__':
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_dhcpoptions.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_dhcpoptions.py	(refactored)
@@ -59,11 +59,11 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(len(api_response), 1)
+        self.assertEqual(len(api_response), 1)
         self.assertIsInstance(api_response[0], DhcpOptions)
-        self.assertEquals(api_response[0].id, 'dopt-7a8b9c2d')
-        self.assertEquals(api_response[0].options['domain-name'], ['example.com'])
-        self.assertEquals(api_response[0].options['domain-name-servers'], ['10.2.5.1', '10.2.5.2'])
+        self.assertEqual(api_response[0].id, 'dopt-7a8b9c2d')
+        self.assertEqual(api_response[0].options['domain-name'], ['example.com'])
+        self.assertEqual(api_response[0].options['domain-name-servers'], ['10.2.5.1', '10.2.5.2'])
 
 
 class TestCreateDhcpOptions(AWSMockServiceTestCase):
@@ -154,12 +154,12 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, DhcpOptions)
-        self.assertEquals(api_response.id, 'dopt-7a8b9c2d')
-        self.assertEquals(api_response.options['domain-name'], ['example.com'])
-        self.assertEquals(api_response.options['domain-name-servers'], ['10.2.5.1', '10.2.5.2'])
-        self.assertEquals(api_response.options['ntp-servers'], ['10.12.12.1', '10.12.12.2'])
-        self.assertEquals(api_response.options['netbios-name-servers'], ['10.20.20.1'])
-        self.assertEquals(api_response.options['netbios-node-type'], ['2'])RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_networkacl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_routetable.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_subnet.py

+        self.assertEqual(api_response.id, 'dopt-7a8b9c2d')
+        self.assertEqual(api_response.options['domain-name'], ['example.com'])
+        self.assertEqual(api_response.options['domain-name-servers'], ['10.2.5.1', '10.2.5.2'])
+        self.assertEqual(api_response.options['ntp-servers'], ['10.12.12.1', '10.12.12.2'])
+        self.assertEqual(api_response.options['netbios-name-servers'], ['10.20.20.1'])
+        self.assertEqual(api_response.options['netbios-node-type'], ['2'])
 
 
 class TestDeleteDhcpOptions(AWSMockServiceTestCase):
@@ -183,7 +183,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestAssociateDhcpOptions(AWSMockServiceTestCase):
@@ -209,7 +209,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_internetgateway.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_internetgateway.py	(refactored)
@@ -40,7 +40,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(len(api_response), 1)
+        self.assertEqual(len(api_response), 1)
         self.assertIsInstance(api_response[0], InternetGateway)
         self.assertEqual(api_response[0].id, 'igw-eaad4883EXAMPLE')
 
@@ -94,7 +94,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestAttachInternetGateway(AWSMockServiceTestCase):
@@ -120,7 +120,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestDetachInternetGateway(AWSMockServiceTestCase):
@@ -146,7 +146,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_routetable.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_routetable.py	(refactored)
@@ -87,37 +87,37 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(len(api_response), 2)
+        self.assertEqual(len(api_response), 2)
         self.assertIsInstance(api_response[0], RouteTable)
-        self.assertEquals(api_response[0].id, 'rtb-13ad487a')
-        self.assertEquals(len(api_response[0].routes), 1)
-        self.assertEquals(api_response[0].routes[0].destination_cidr_block, '10.0.0.0/22')
-        self.assertEquals(api_response[0].routes[0].gateway_id, 'local')
-        self.assertEquals(api_response[0].routes[0].state, 'active')
-        self.assertEquals(len(api_response[0].associations), 1)
-        self.assertEquals(api_response[0].associations[0].id, 'rtbassoc-12ad487b')
-        self.assertEquals(api_response[0].associations[0].route_table_id, 'rtb-13ad487a')
+        self.assertEqual(api_response[0].id, 'rtb-13ad487a')
+        self.assertEqual(len(api_response[0].routes), 1)
+        self.assertEqual(api_response[0].routes[0].destination_cidr_block, '10.0.0.0/22')
+        self.assertEqual(api_response[0].routes[0].gateway_id, 'local')
+        self.assertEqual(api_response[0].routes[0].state, 'active')
+        self.assertEqual(len(api_response[0].associations), 1)
+        self.assertEqual(api_response[0].associations[0].id, 'rtbassoc-12ad487b')
+        self.assertEqual(api_response[0].associations[0].route_table_id, 'rtb-13ad487a')
         self.assertIsNone(api_response[0].associations[0].subnet_id)
-        self.assertEquals(api_response[0].associations[0].main, True)
-        self.assertEquals(api_response[1].id, 'rtb-f9ad4890')
-        self.assertEquals(len(api_response[1].routes), 4)
-        self.assertEquals(api_response[1].routes[0].destination_cidr_block, '10.0.0.0/22')
-        self.assertEquals(api_response[1].routes[0].gateway_id, 'local')
-        self.assertEquals(api_response[1].routes[0].state, 'active')
-        self.assertEquals(api_response[1].routes[1].destination_cidr_block, '0.0.0.0/0')
-        self.assertEquals(api_response[1].routes[1].gateway_id, 'igw-eaad4883')
-        self.assertEquals(api_response[1].routes[1].state, 'active')
-        self.assertEquals(api_response[1].routes[2].destination_cidr_block, '10.0.0.0/21')
-        self.assertEquals(api_response[1].routes[2].interface_id, 'eni-884ec1d1')
-        self.assertEquals(api_response[1].routes[2].state, 'blackhole')
-        self.assertEquals(api_response[1].routes[3].destination_cidr_block, '11.0.0.0/22')
-        self.assertEquals(api_response[1].routes[3].vpc_peering_connection_id, 'pcx-efc52b86')
-        self.assertEquals(api_response[1].routes[3].state, 'blackhole')
-        self.assertEquals(len(api_response[1].associations), 1)
-        self.assertEquals(api_response[1].associations[0].id, 'rtbassoc-faad4893')
-        self.assertEquals(api_response[1].associations[0].route_table_id, 'rtb-f9ad4890')
-        self.assertEquals(api_response[1].associations[0].subnet_id, 'subnet-15ad487c')
-        self.assertEquals(api_response[1].associations[0].main, False)
+        self.assertEqual(api_response[0].associations[0].main, True)
+        self.assertEqual(api_response[1].id, 'rtb-f9ad4890')
+        self.assertEqual(len(api_response[1].routes), 4)
+        self.assertEqual(api_response[1].routes[0].destination_cidr_block, '10.0.0.0/22')
+        self.assertEqual(api_response[1].routes[0].gateway_id, 'local')
+        self.assertEqual(api_response[1].routes[0].state, 'active')
+        self.assertEqual(api_response[1].routes[1].destination_cidr_block, '0.0.0.0/0')
+        self.assertEqual(api_response[1].routes[1].gateway_id, 'igw-eaad4883')
+        self.assertEqual(api_response[1].routes[1].state, 'active')
+        self.assertEqual(api_response[1].routes[2].destination_cidr_block, '10.0.0.0/21')
+        self.assertEqual(api_response[1].routes[2].interface_id, 'eni-884ec1d1')
+        self.assertEqual(api_response[1].routes[2].state, 'blackhole')
+        self.assertEqual(api_response[1].routes[3].destination_cidr_block, '11.0.0.0/22')
+        self.assertEqual(api_response[1].routes[3].vpc_peering_connection_id, 'pcx-efc52b86')
+        self.assertEqual(api_response[1].routes[3].state, 'blackhole')
+        self.assertEqual(len(api_response[1].associations), 1)
+        self.assertEqual(api_response[1].associations[0].id, 'rtbassoc-faad4893')
+        self.assertEqual(api_response[1].associations[0].route_table_id, 'rtb-f9ad4890')
+        self.assertEqual(api_response[1].associations[0].subnet_id, 'subnet-15ad487c')
+        self.assertEqual(api_response[1].associations[0].main, False)
 
 
 class TestAssociateRouteTable(AWSMockServiceTestCase):
@@ -143,7 +143,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, 'rtbassoc-f8ad4891')
+        self.assertEqual(api_response, 'rtbassoc-f8ad4891')
 
 
 class TestDisassociateRouteTable(AWSMockServiceTestCase):
@@ -167,7 +167,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestCreateRouteTable(AWSMockServiceTestCase):
@@ -204,11 +204,11 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, RouteTable)
-        self.assertEquals(api_response.id, 'rtb-f9ad4890')
-        self.assertEquals(len(api_response.routes), 1)
-        self.assertEquals(api_response.routes[0].destination_cidr_block, '10.0.0.0/22')
-        self.assertEquals(api_response.routes[0].gateway_id, 'local')
-        self.assertEquals(api_response.routes[0].state, 'active')
+        self.assertEqual(api_response.id, 'rtb-f9ad4890')
+        self.assertEqual(len(api_response.routes), 1)
+        self.assertEqual(api_response.routes[0].destination_cidr_block, '10.0.0.0/22')
+        self.assertEqual(api_response.routes[0].gateway_id, 'local')
+        self.assertEqual(api_response.routes[0].state, 'active')
 
 
 class TestDeleteRouteTable(AWSMockServiceTestCase):
@@ -232,7 +232,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestReplaceRouteTableAssociation(AWSMockServiceTestCase):
@@ -258,7 +258,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_replace_route_table_association_with_assoc(self):
         self.set_http_response(status_code=200)
@@ -271,7 +271,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, 'rtbassoc-faad4893')
+        self.assertEqual(api_response, 'rtbassoc-faad4893')
 
 
 class TestCreateRoute(AWSMockServiceTestCase):
@@ -298,7 +298,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_create_route_instance(self):
         self.set_http_response(status_code=200)
@@ -312,7 +312,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_create_route_interface(self):
         self.set_http_response(status_code=200)
@@ -326,7 +326,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_create_route_vpc_peering_connection(self):
         self.set_http_response(status_code=200)
@@ -340,7 +340,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestReplaceRoute(AWSMockServiceTestCase):
@@ -367,7 +367,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_replace_route_instance(self):
         self.set_http_response(status_code=200)
@@ -381,7 +381,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_replace_route_interface(self):
         self.set_http_response(status_code=200)
@@ -395,7 +395,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_replace_route_vpc_peering_connection(self):
         self.set_http_response(status_code=200)
@@ -409,7 +409,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestDeleteRoute(AWSMockServiceTestCase):
@@ -434,7 +434,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_subnet.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_subnet.py	(refactored)
@@ -58,7 +58,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(len(api_response), 2)
+        self.assertEqual(len(api_response), 2)
         self.assertIsInstance(api_response[0], Subnet)
         self.assertEqual(api_response[0].id, 'subnet-9d4a7b6c')
         self.assertEqual(api_response[1].id, 'subnet-6e7f829e')
@@ -97,12 +97,12 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, Subnet)
-        self.assertEquals(api_response.id, 'subnet-9d4a7b6c')
-        self.assertEquals(api_response.state, 'pending')
-        self.assertEquals(api_response.vpc_id, 'vpc-1a2b3c4d')
-        self.assertEquals(api_response.cidr_block, '10.0.1.0/24')
-        self.assertEquals(api_response.available_ip_address_count, 251)
-        self.assertEquals(api_response.availability_zone, 'us-east-1a')
+        self.assertEqual(api_response.id, 'subnet-9d4a7b6c')
+        self.assertEqual(api_response.state, 'pending')
+        self.assertEqual(api_response.vpc_id, 'vpc-1a2b3c4d')
+        self.assertEqual(api_response.cidr_block, '10.0.1.0/24')
+        self.assertEqual(api_response.available_ip_address_count, 251)
+        self.assertEqual(api_response.availability_zone, 'us-east-1a')
 
 
 class TestDeleteSubnet(AWSMockServiceTestCase):
@@ -126,7 +126,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc_peering_connection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpnconnection.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpngateway.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/filechunkio.py

                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 if __name__ == '__main__':
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc.py	(refactored)
@@ -70,11 +70,11 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, VPC)
-        self.assertEquals(api_response.id, 'vpc-1a2b3c4d')
-        self.assertEquals(api_response.state, 'pending')
-        self.assertEquals(api_response.cidr_block, '10.0.0.0/16')
-        self.assertEquals(api_response.dhcp_options_id, 'dopt-1a2b3c4d2')
-        self.assertEquals(api_response.instance_tenancy, 'default')
+        self.assertEqual(api_response.id, 'vpc-1a2b3c4d')
+        self.assertEqual(api_response.state, 'pending')
+        self.assertEqual(api_response.cidr_block, '10.0.0.0/16')
+        self.assertEqual(api_response.dhcp_options_id, 'dopt-1a2b3c4d2')
+        self.assertEqual(api_response.instance_tenancy, 'default')
 
 
 class TestDeleteVpc(AWSMockServiceTestCase):
@@ -98,7 +98,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestModifyVpcAttribute(AWSMockServiceTestCase):
@@ -124,7 +124,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
     def test_modify_vpc_attribute_dns_hostnames(self):
         self.set_http_response(status_code=200)
@@ -137,7 +137,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestGetAllClassicLinkVpc(AWSMockServiceTestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc_peering_connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpc_peering_connection.py	(refactored)
@@ -157,7 +157,7 @@
 
     def test_delete_vpc_peering_connection(self):
         self.set_http_response(status_code=200)
-        self.assertEquals(self.service_connection.delete_vpc_peering_connection('pcx-12345678'), True)
+        self.assertEqual(self.service_connection.delete_vpc_peering_connection('pcx-12345678'), True)
 
 class TestDeleteVpcPeeringConnectionShortForm(unittest.TestCase):
     DESCRIBE_VPC_PEERING_CONNECTIONS= b"""<?xml version="1.0" encoding="UTF-8"?>
@@ -199,14 +199,14 @@
         vpc_conn.make_request = mock.Mock(return_value=mock_response)
         vpc_peering_connections = vpc_conn.get_all_vpc_peering_connections()
 
-        self.assertEquals(1, len(vpc_peering_connections))
+        self.assertEqual(1, len(vpc_peering_connections))
         vpc_peering_connection = vpc_peering_connections[0]
 
         mock_response = mock.Mock()
         mock_response.read.return_value = self.DELETE_VPC_PEERING_CONNECTION
         mock_response.status = 200
         vpc_conn.make_request = mock.Mock(return_value=mock_response)
-        self.assertEquals(True, vpc_peering_connection.delete())
+        self.assertEqual(True, vpc_peering_connection.delete())
 
         self.assertIn('DeleteVpcPeeringConnection', vpc_conn.make_request.call_args_list[0][0])
         self.assertNotIn('DeleteVpc', vpc_conn.make_request.call_args_list[0][0])
@@ -224,7 +224,7 @@
 
     def test_reject_vpc_peering_connection(self):
         self.set_http_response(status_code=200)
-        self.assertEquals(self.service_connection.reject_vpc_peering_connection('pcx-12345678'), True)
+        self.assertEqual(self.service_connection.reject_vpc_peering_connection('pcx-12345678'), True)
 
 
 class TestAcceptVpcPeeringConnection(AWSMockServiceTestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpnconnection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpnconnection.py	(refactored)
@@ -170,9 +170,9 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, VpnConnection)
-        self.assertEquals(api_response.id, 'vpn-83ad48ea')
-        self.assertEquals(api_response.customer_gateway_id, 'cgw-b4dc3961')
-        self.assertEquals(api_response.options.static_routes_only, True)
+        self.assertEqual(api_response.id, 'vpn-83ad48ea')
+        self.assertEqual(api_response.customer_gateway_id, 'cgw-b4dc3961')
+        self.assertEqual(api_response.options.static_routes_only, True)
 
 
 class TestDeleteVPNConnection(AWSMockServiceTestCase):
@@ -196,7 +196,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestCreateVPNConnectionRoute(AWSMockServiceTestCase):
@@ -222,7 +222,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 
 class TestDeleteVPNConnectionRoute(AWSMockServiceTestCase):
@@ -248,7 +248,7 @@
             ignore_params_values=['AWSAccessKeyId', 'SignatureMethod',
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
-        self.assertEquals(api_response, True)
+        self.assertEqual(api_response, True)
 
 if __name__ == '__main__':
     unittest.main()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpngateway.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/test_vpngateway.py	(refactored)
@@ -83,7 +83,7 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, VpnGateway)
-        self.assertEquals(api_response.id, 'vgw-8db04f81')
+        self.assertEqual(api_response.id, 'vgw-8db04f81')
 
 
 class TestDeleteVpnGateway(AWSMockServiceTestCase):
@@ -136,8 +136,8 @@
                                   'SignatureVersion', 'Timestamp',
                                   'Version'])
         self.assertIsInstance(api_response, Attachment)
-        self.assertEquals(api_response.vpc_id, 'vpc-1a2b3c4d')
-        self.assertEquals(api_response.state, 'attaching')
+        self.assertEqual(api_response.vpc_id, 'vpc-1a2b3c4d')
+        self.assertEqual(api_response.state, 'attaching')
 
 
 class TestDetachVpnGateway(AWSMockServiceTestCase):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/setup.py	(refactored)
@@ -6,7 +6,7 @@
 
 PY3 = sys.version_info[0] == 3
 
-_unicode = str if PY3 else unicodeRefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/setup.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/exc.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/location.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/units.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/util.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/__init__.py

+_unicode = str if PY3 else str
 
 setup(
     name="filechunkio",
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/__init__.py	(refactored)
@@ -1,4 +1,4 @@
-from __future__ import absolute_import
+
 
 from .filechunkio import FileChunkIO
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py	(refactored)
@@ -3,9 +3,9 @@
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
@@ -9,7 +9,7 @@
 if py3k: # pragma: no cover
     string_compare = str
 else: # pragma: no cover
-    string_compare = (str, unicode)
+    string_compare = (str, str)
 
 # Unicode compatibility, borrowed from 'six'
 if py3k: # pragma: no cover
@@ -23,7 +23,7 @@
         """
         Convert to Unicode with unicode escaping
         """
-        return unicode(s.replace(r'\\', r'\\\\'), 'unicode_escape')
+        return str(s.replace(r'\\', r'\\\\'), 'unicode_escape')
 
 if py3k: # pragma: no cover
     from urllib.parse import urlencode, quote # pylint: disable=W0611,F0401,W0611,E0611
@@ -40,17 +40,17 @@
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
@@ -61,7 +61,7 @@
         """
         Python2-only, ensures that a string is encoding to a str.
         """
-        if isinstance(str_or_unicode, unicode):
+        if isinstance(str_or_unicode, str):
             return str_or_unicode.encode('utf-8')
         else:
             return str_or_unicode
@@ -75,7 +75,7 @@
         Based on the urlencode from django.utils.http
         """
         if hasattr(query, 'items'):
-            query = query.items()
+            query = list(query.items())
         return original_urlencode(
             [(force_str(k),
               [force_str(i) for i in v]
@@ -89,11 +89,11 @@
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
@@ -69,7 +69,7 @@
     3276.157156868931
 
 """
-from __future__ import division
+
 
 from math import atan, tan, sin, cos, pi, sqrt, atan2, asin
 from geopy.units import radians
@@ -145,7 +145,7 @@
     def __abs__(self):
         return self.__class__(abs(self.kilometers))
 
-    def __nonzero__(self):
+    def __bool__(self):
         return bool(self.kilometers)
 
     __bool__ = __nonzero__
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/format.py	(refactored)
@@ -6,12 +6,12 @@
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
@@ -113,7 +113,7 @@
     ('southeast by south', 'SEbS'),
 ]
 
-DIRECTIONS, DIRECTIONS_ABBR = zip(*_DIRECTIONS)
+DIRECTIONS, DIRECTIONS_ABBR = list(zip(*_DIRECTIONS))
 ANGLE_DIRECTIONS = {
     n * 11.25: d
     for n, d
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/point.py	(refactored)
@@ -263,7 +263,7 @@
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
@@ -6,7 +6,7 @@
 from geopy.compat import py3k
 
 if not py3k: # pragma: no cover
-    NUMBER_TYPES = (int, long, float)
+    NUMBER_TYPES = (int, int, float)
 else: # pragma: no cover
     NUMBER_TYPES = (int, float) # long -> int in Py3k
 try:
@@ -44,7 +44,7 @@
         """
         Join with a filter.
         """
-        return sep.join([unicode(i) for i in seq if pred(i)])
+        return sep.join([str(i) for i in seq if pred(i)])
 else:
     def join_filter(sep, seq, pred=bool):
         """
@@ -64,10 +64,10 @@
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
@@ -227,7 +227,7 @@
         token_request_arguments = "&".join([
             "%s=%s" % (key, val)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/arcgis.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/baidu.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/base.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/databc.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/dot_us.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geocodefarm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/geonames.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/googlev3.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/ignfrance.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/navidata.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/opencage.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/openmapquest.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/photon.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/smartystreets.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/what3words.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/yandex.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/setup.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/test_requests.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/api.py

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
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/bing.py	(refactored)
@@ -131,7 +131,7 @@
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
@@ -134,7 +134,7 @@
         """
         return "|".join(
             (":".join(item)
-             for item in components.items()
+             for item in list(components.items())
             )
         )
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/osm.py	(refactored)
@@ -148,7 +148,7 @@
             params = {
                 key: val
                 for key, val
-                in query.items()
+                in list(query.items())
                 if key in self.structured_query_params
             }
         else:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/geocoders/placefinder.py	(refactored)
@@ -60,12 +60,12 @@
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
@@ -3,7 +3,7 @@
 
 """Tests for Requests."""
 
-from __future__ import division
+
 import json
 import os
 import pickle
@@ -28,7 +28,7 @@
 from requests.hooks import default_hooks
 
 try:
-    import StringIO
+    import io
 except ImportError:
     import io as StringIO
 
@@ -666,8 +666,8 @@
         jar.set(key1, value1)
 
         d1 = dict(jar)
-        d2 = dict(jar.iteritems())
-        d3 = dict(jar.items())
+        d2 = dict(iter(jar.items()))
+        d3 = dict(list(jar.items()))
 
         assert len(jar) == 2
         assert len(d1) == 2
@@ -686,8 +686,8 @@
         jar.set(key1, value1)
 
         d1 = dict(jar)
-        d2 = dict(jar.iteritems())
-        d3 = dict(jar.items())
+        d2 = dict(iter(jar.items()))
+        d3 = dict(list(jar.items()))
 
         assert d1['some_cookie'] == 'some_value'
         assert d2['some_cookie'] == 'some_value'
@@ -704,7 +704,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        keys = jar.keys()
+        keys = list(jar.keys())
         assert keys == list(keys)
         # make sure one can use keys multiple times
         assert list(keys) == list(keys)
@@ -720,7 +720,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        values = jar.values()
+        values = list(jar.values())
         assert values == list(values)
         # make sure one can use values multiple times
         assert list(values) == list(values)
@@ -736,7 +736,7 @@
         jar.set(key, value)
         jar.set(key1, value1)
 
-        items = jar.items()
+        items = list(jar.items())
         assert items == list(items)
         # make sure one can use items multiple times
         assert list(items) == list(items)
@@ -750,7 +750,7 @@
 
     def test_response_is_iterable(self):
         r = requests.Response()
-        io = StringIO.StringIO('abc')
+        io = io.StringIO('abc')
         read_ = io.read
 
         def read_mock(amt, decode_content=None):
@@ -924,8 +924,8 @@
 
         # This is testing that they are builtin strings. A bit weird, but there
         # we go.
-        assert 'unicode' in p.headers.keys()
-        assert 'byte' in p.headers.keys()
+        assert 'unicode' in list(p.headers.keys())
+        assert 'byte' in list(p.headers.keys())
 
     def test_can_send_nonstring_objects_with_files(self):
         data = {'a': 0.0}
@@ -1235,8 +1235,8 @@
             'user-Agent': 'requests',
         })
         keyset = frozenset(['Accept', 'user-Agent'])
-        assert frozenset(i[0] for i in cid.items()) == keyset
-        assert frozenset(cid.keys()) == keyset
+        assert frozenset(i[0] for i in list(cid.items())) == keyset
+        assert frozenset(list(cid.keys())) == keyset
         assert frozenset(cid) == keyset
 
     def test_preserve_last_key_case(self):
@@ -1247,8 +1247,8 @@
         cid.update({'ACCEPT': 'application/json'})
         cid['USER-AGENT'] = 'requests'
         keyset = frozenset(['ACCEPT', 'USER-AGENT'])
-        assert frozenset(i[0] for i in cid.items()) == keyset
-        assert frozenset(cid.keys()) == keyset
+        assert frozenset(i[0] for i in list(cid.items())) == keyset
+        assert frozenset(list(cid.keys())) == keyset
         assert frozenset(cid) == keyset
 
 
@@ -1260,21 +1260,21 @@
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
@@ -1520,7 +1520,7 @@
         return r
 
     def _build_raw(self):
-        string = StringIO.StringIO('')
+        string = io.StringIO('')
         setattr(string, 'release_conn', lambda *args: args)
         return string
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/adapters.py	(refactored)
@@ -15,7 +15,7 @@
 from .packages.urllib3.response import HTTPResponse
 from .packages.urllib3.util import Timeout as TimeoutSauceRefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/exceptions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/hooks.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/status_codes.py

 from .packages.urllib3.util.retry import Retry
-from .compat import urlparse, basestring
+from .compat import urlparse, str
 from .utils import (DEFAULT_CA_BUNDLE_PATH, get_encoding_from_headers,
                     prepend_scheme_if_needed, get_auth_from_url, urldefragauth)
 from .structures import CaseInsensitiveDict
@@ -107,7 +107,7 @@
         self.proxy_manager = {}
         self.config = {}
 
-        for attr, value in state.items():
+        for attr, value in list(state.items()):
             setattr(self, attr, value)
 
         self.init_poolmanager(self._pool_connections, self._pool_maxsize,
@@ -187,7 +187,7 @@
             conn.ca_certs = None
 
         if cert:
-            if not isinstance(cert, basestring):
+            if not isinstance(cert, str):
                 conn.cert_file = cert[0]
                 conn.key_file = cert[1]
             else:
@@ -382,7 +382,7 @@
                                         url,
                                         skip_accept_encoding=True)
 
-                    for header, value in request.headers.items():
+                    for header, value in list(request.headers.items()):
                         low_conn.putheader(header, value)
 
                     low_conn.endheaders()
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py	(refactored)
@@ -22,4 +22,4 @@
         return os.path.join(os.path.dirname(__file__), 'cacert.pem')
 
 if __name__ == '__main__':
-    print(where())
+    print((where()))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py	(refactored)
@@ -33,19 +33,19 @@
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
@@ -58,5 +58,5 @@
     builtin_str = str
     str = str
     bytes = bytes
-    basestring = (str, bytes)
+    str = (str, bytes)
     numeric_types = (int, float)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py	(refactored)
@@ -210,7 +210,7 @@
     def keys(self):
         """Dict-like keys() that returns a list of names of cookies from the
         jar. See values() and items()."""
-        return list(self.iterkeys())
+        return list(self.keys())
 
     def itervalues(self):
         """Dict-like itervalues() that returns an iterator of values of cookies
@@ -221,7 +221,7 @@
     def values(self):
         """Dict-like values() that returns a list of values of cookies from the
         jar. See keys() and items()."""
-        return list(self.itervalues())
+        return list(self.values())
 
     def iteritems(self):
         """Dict-like iteritems() that returns an iterator of name-value tuples
@@ -234,7 +234,7 @@
         jar. See keys() and values(). Allows client-code to call
         ``dict(RequestsCookieJar)`` and get a vanilla python dict of key value
         pairs."""
-        return list(self.iteritems())
+        return list(self.items())
 
     def list_domains(self):
         """Utility method to list all the domains in the jar."""
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py	(refactored)
@@ -30,7 +30,7 @@
     iter_slices, guess_json_utf, super_len, to_native_string)
 from .compat import (
     cookielib, urlunparse, urlsplit, urlencode, str, bytes, StringIO,
-    is_py2, chardet, json, builtin_str, basestring)
+    is_py2, chardet, json, builtin_str, str)
 from .status_codes import codes
 
 #: The set of HTTP status codes that indicate an automatically
@@ -87,7 +87,7 @@
         elif hasattr(data, '__iter__'):
             result = []
             for k, vs in to_key_val_list(data):
-                if isinstance(vs, basestring) or not hasattr(vs, '__iter__'):
+                if isinstance(vs, str) or not hasattr(vs, '__iter__'):
                     vs = [vs]
                 for v in vs:
                     if v is not None:
@@ -109,7 +109,7 @@
         """
         if (not files):
             raise ValueError("Files must be provided.")
-        elif isinstance(data, basestring):
+        elif isinstance(data, str):
             raise ValueError("Data must not be a string.")
 
         new_fields = []
@@ -117,7 +117,7 @@
         files = to_key_val_list(files or {})
 
         for field, val in fields:
-            if isinstance(val, basestring) or not hasattr(val, '__iter__'):
+            if isinstance(val, str) or not hasattr(val, '__iter__'):
                 val = [val]
             for v in val:
                 if v is not None:
@@ -341,7 +341,7 @@
         if isinstance(url, bytes):
             url = url.decode('utf8')
         else:
-            url = unicode(url) if is_py2 else str(url)
+            url = str(url) if is_py2 else str(url)
 
         # Don't do any URL preparation for non-HTTP schemes like `mailto`,
         # `data` etc to work around exceptions from `url_parse`, which
@@ -408,7 +408,7 @@
         """Prepares the given HTTP headers."""
 
         if headers:
-            self.headers = CaseInsensitiveDict((to_native_string(name), value) for name, value in headers.items())
+            self.headers = CaseInsensitiveDict((to_native_string(name), value) for name, value in list(headers.items()))
         else:
             self.headers = CaseInsensitiveDict()
 
@@ -429,7 +429,7 @@
 
         is_stream = all([
             hasattr(data, '__iter__'),
-            not isinstance(data, (basestring, list, tuple, dict))
+            not isinstance(data, (str, list, tuple, dict))
         ])
 
         try:
@@ -454,7 +454,7 @@
             else:
                 if data and json is None:
                     body = self._encode_params(data)
-                    if isinstance(data, basestring) or hasattr(data, 'read'):
+                    if isinstance(data, str) or hasattr(data, 'read'):
                         content_type = None
                     else:
                         content_type = 'application/x-www-form-urlencoded'
@@ -609,7 +609,7 @@
         )
 
     def __setstate__(self, state):
-        for name, value in state.items():
+        for name, value in list(state.items()):
             setattr(self, name, value)
 
         # pickled objects do not have .raw
@@ -623,7 +623,7 @@
         """Returns true if :attr:`status_code` is 'OK'."""
         return self.ok
 
-    def __nonzero__(self):
+    def __bool__(self):
         """Returns true if :attr:`status_code` is 'OK'."""
         return self.ok
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5freq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5prober.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardetect.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetgroupprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/constants.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/cp949prober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escsm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrfreq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwfreq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312freq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312prober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/hebrewprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jisfreq.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/jpcntx.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langbulgarianmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langcyrillicmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langgreekmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhebrewmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langhungarianmodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/langthaimodel.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/latin1prober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcharsetprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/mbcssm.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sbcharsetprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/sjisprober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/universaldetector.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/utf8prober.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/__init__.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py	(refactored)
@@ -63,11 +63,11 @@
     merged_setting.update(to_key_val_list(request_setting))
 
     # Remove keys that are set to None.
-    for (k, v) in request_setting.items():
+    for (k, v) in list(request_setting.items()):
         if v is None:
             del merged_setting[k]
 
-    merged_setting = dict((k, v) for (k, v) in merged_setting.items() if v is not None)
+    merged_setting = dict((k, v) for (k, v) in list(merged_setting.items()) if v is not None)
 
     return merged_setting
 
@@ -612,7 +612,7 @@
         if self.trust_env:
             # Set environment's proxies.
             env_proxies = get_environ_proxies(url) or {}
-            for (k, v) in env_proxies.items():
+            for (k, v) in list(env_proxies.items()):
                 proxies.setdefault(k, v)
 
             # Look for requests environment configuration and be compatible
@@ -632,7 +632,7 @@
 
     def get_adapter(self, url):
         """Returns the appropriate connnection adapter for the given URL."""
-        for (prefix, adapter) in self.adapters.items():
+        for (prefix, adapter) in list(self.adapters.items()):
 
             if url.lower().startswith(prefix):
                 return adapter
@@ -642,7 +642,7 @@
 
     def close(self):
         """Closes all adapters and as such the session"""
-        for v in self.adapters.values():
+        for v in list(self.adapters.values()):
             v.close()
 
     def mount(self, prefix, adapter):
@@ -663,11 +663,11 @@
 
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
@@ -57,7 +57,7 @@
         del self._store[key.lower()]
 
     def __iter__(self):
-        return (casedkey for casedkey, mappedvalue in self._store.values())
+        return (casedkey for casedkey, mappedvalue in list(self._store.values()))
 
     def __len__(self):
         return len(self._store)
@@ -67,7 +67,7 @@
         return (
             (lowerkey, keyval[1])
             for (lowerkey, keyval)
-            in self._store.items()
+            in list(self._store.items())
         )
 
     def __eq__(self, other):
@@ -80,10 +80,10 @@
 
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
@@ -26,7 +26,7 @@
 from .compat import parse_http_list as _parse_list_header
 from .compat import (quote, urlparse, bytes, str, OrderedDict, unquote, is_py2,
                      builtin_str, getproxies, proxy_bypass, urlunparse,
-                     basestring)
+                     str)
 from .cookies import RequestsCookieJar, cookiejar_from_dict
 from .structures import CaseInsensitiveDict
 from .exceptions import InvalidURL
@@ -42,7 +42,7 @@
     """Returns an internal sequence dictionary update."""
 
     if hasattr(d, 'items'):
-        d = d.items()
+        d = list(d.items())
 
     return d
 
@@ -116,7 +116,7 @@
 def guess_filename(obj):
     """Tries to guess the filename of the given object."""
     name = getattr(obj, 'name', None)
-    if (name and isinstance(name, basestring) and name[0] != '<' and
+    if (name and isinstance(name, str) and name[0] != '<' and
             name[-1] != '>'):
         return os.path.basename(name)
 
@@ -164,7 +164,7 @@
         raise ValueError('cannot encode objects that are not 2-tuples')
 
     if isinstance(value, collections.Mapping):
-        value = value.items()
+        value = list(value.items())
 
     return list(value)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/__init__.py	(refactored)
@@ -1,3 +1,3 @@
-from __future__ import absolute_import
+
 
 from . import urllib3
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py	(refactored)
@@ -20,7 +20,7 @@
 
 
 def detect(aBuf):
-    if ((version_info < (3, 0) and isinstance(aBuf, unicode)) or
+    if ((version_info < (3, 0) and isinstance(aBuf, str)) or
             (version_info >= (3, 0) and not isinstance(aBuf, bytes))):
         raise ValueError('Expected a bytes object, not a unicode object')
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardetect.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardetect.py	(refactored)
@@ -13,7 +13,7 @@
 
 """
 
-from __future__ import absolute_import, print_function, unicode_literals
+
 
 import argparse
 import sys
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py	(refactored)
@@ -22,7 +22,7 @@
 
 
 if sys.version_info < (3, 0):
-    base_str = (str, unicode)
+    base_str = (str, str)
 else:
     base_str = (bytes, str)
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/_collections.py	(refactored)
@@ -238,19 +238,19 @@
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
@@ -301,7 +301,7 @@
             yield val[0], ', '.join(val[1:])
 
     def items(self):
-        return list(self.iteritems())
+        return list(self.items())
 
     @classmethod
     def from_httplib(cls, message): # Python 2
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connection.py	(refactored)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/exceptions.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/__init__.py

@@ -8,7 +8,7 @@
 try:  # Python 3
     from http.client import HTTPConnection as _HTTPConnection, HTTPException
 except ImportError:
-    from httplib import HTTPConnection as _HTTPConnection, HTTPException
+    from http.client import HTTPConnection as _HTTPConnection, HTTPException
 
 
 class DummyConnection(object):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/connectionpool.py	(refactored)
@@ -9,8 +9,8 @@
 try:  # Python 3
     from queue import LifoQueue, Empty, Full
 except ImportError:
-    from Queue import LifoQueue, Empty, Full
-    import Queue as _  # Platform-specific: Windows
+    from queue import LifoQueue, Empty, Full
+    import queue as _  # Platform-specific: Windows
 
 
 from .exceptions import (
@@ -180,7 +180,7 @@
         self.proxy_headers = _proxy_headers or {}
 
         # Fill the queue up so that doing get() on it will block properly
-        for _ in xrange(maxsize):
+        for _ in range(maxsize):
             self.pool.put(None)
 
         # These are mostly for testing and debugging purposes.
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py	(refactored)
@@ -126,7 +126,7 @@
         parts = []
         iterable = header_parts
         if isinstance(header_parts, dict):
-            iterable = header_parts.items()
+            iterable = list(header_parts.items())
 
         for name, value in iterable:
             if value:
@@ -145,7 +145,7 @@
             if self.headers.get(sort_key, False):
                 lines.append('%s: %s' % (sort_key, self.headers[sort_key]))
 
-        for header_name, header_value in self.headers.items():
+        for header_name, header_value in list(self.headers.items()):
             if header_name not in sort_keys:
                 if header_value:
                     lines.append('%s: %s' % (header_name, header_value))
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py	(refactored)
@@ -3,7 +3,7 @@
 try:  # Python 3
     from urllib.parse import urljoin
 except ImportError:
-    from urlparse import urljoin
+    from urllib.parse import urljoin
 
 from ._collections import RecentlyUsedContainer
 from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py	(refactored)
@@ -1,7 +1,7 @@
 try:
     from urllib.parse import urlencode
 except ImportError:
-    from urllib import urlencode
+    from urllib.parse import urlencode
 
 from .filepost import encode_multipart_formdata
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py	(refactored)
@@ -1,7 +1,7 @@
 try:
     import http.client as httplib
 except ImportError:
-    import httplib
+    import http.client
 import zlib
 import io
 from socket import timeout as SocketTimeout
@@ -10,7 +10,7 @@
 from .exceptions import (
     ProtocolError, DecodeError, ReadTimeoutError, ResponseNotChunked
 )
-from .packages.six import string_types as basestring, binary_type, PY3
+from .packages.six import string_types as str, binary_type, PY3
 from .connection import HTTPException, BaseSSLError
 from .util.response import is_fp_closed
 
@@ -114,7 +114,7 @@
         self._original_response = original_response
         self._fp_bytes_read = 0
 
-        if body and isinstance(body, (basestring, binary_type)):
+        if body and isinstance(body, (str, binary_type)):
             self._body = body
 
         self._pool = pool
@@ -321,7 +321,7 @@
         headers = r.msg
         if not isinstance(headers, HTTPHeaderDict):
             if PY3: # Python 3
-                headers = HTTPHeaderDict(headers.items())
+                headers = HTTPHeaderDict(list(headers.items()))
             else: # Python 2
                 headers = HTTPHeaderDict.from_httplib(headers)
 
@@ -398,7 +398,7 @@
         except ValueError:
             # Invalid chunked protocol response, abort.
             self.close()
-            raise httplib.IncompleteRead(line)
+            raise http.client.IncompleteRead(line)
 
     def _handle_chunk(self, amt):
         returned_chunk = None
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py	(refactored)
@@ -7,7 +7,7 @@
 try:
     from http.client import HTTPSConnection
 except ImportError:
-    from httplib import HTTPSConnection
+    from http.client import HTTPSConnection
 from logging import getLogger
 from ntlm import ntlm
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/__init__.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/__init__.py	(refactored)
@@ -1,4 +1,4 @@
-from __future__ import absolute_import
+
 
 from . import ssl_match_hostname
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py	(refactored)
@@ -3,9 +3,9 @@
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
@@ -79,7 +79,7 @@
     def clear(self):
         'od.clear() -> None.  Remove all items from od.'
         try:
-            for node in self.__map.itervalues():
+            for node in self.__map.values():
                 del node[:]
             root = self.__root
             root[:] = [root, root, None]
@@ -162,12 +162,12 @@
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
@@ -203,7 +203,7 @@
         try:
             if not self:
                 return '%s()' % (self.__class__.__name__,)
-            return '%s(%r)' % (self.__class__.__name__, self.items())
+            return '%s(%r)' % (self.__class__.__name__, list(self.items()))
         finally:
             del _repr_running[call_key]RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/connection.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/request.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/response.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/ssl_.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/timeout.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/url.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py

 
@@ -238,7 +238,7 @@
 
         '''
         if isinstance(other, OrderedDict):
-            return len(self)==len(other) and self.items() == other.items()
+            return len(self)==len(other) and list(self.items()) == list(other.items())
         return dict.__eq__(self, other)
 
     def __ne__(self, other):
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py	(refactored)
@@ -39,10 +39,10 @@
 
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
@@ -228,7 +228,7 @@
     advance_iterator = next
 except NameError:
     def advance_iterator(it):
-        return it.next()
+        return it.__next__()
 next = advance_iterator
 
 
@@ -242,11 +242,11 @@
         return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)
 else:
     def get_unbound_function(unbound):
-        return unbound.im_func
+        return unbound.__func__
 
     class Iterator(object):
 
-        def next(self):
+        def __next__(self):
             return type(self).__next__(self)
 
     callable = callable
@@ -291,10 +291,10 @@
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
 
@@ -338,19 +338,19 @@
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
@@ -358,12 +358,12 @@
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
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/retry.py	(refactored)
@@ -200,7 +200,7 @@
     def is_exhausted(self):
         """ Are we out of retries? """
         retry_counts = (self.total, self.connect, self.read, self.redirect)
-        retry_counts = list(filter(None, retry_counts))
+        retry_counts = list([_f for _f in retry_counts if _f])
         if not retry_counts:
             return False
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_browser.py	(refactored)
@@ -105,25 +105,25 @@
 
     def displayMetadata(self):
         self.setDefaultGraphicsView()
-        aquisitionStart = parser.parse(str(self.singleMetaInDic[u'acquisition_start']))
+        aquisitionStart = parser.parse(str(self.singleMetaInDic['acquisition_start']))
         strAcquisitionStart = aquisitionStart.strftime('%Y-%m-%d %H:%M (%Z)')
         # print(aquisitionStart.strftime('%Y-%m-%d %I:%M %p (%Z)'))
-        aquisitionEnd = parser.parse(str(self.singleMetaInDic[u'acquisition_end']))
+        aquisitionEnd = parser.parse(str(self.singleMetaInDic['acquisition_end']))
         strAcquisitionEnd = aquisitionEnd.strftime('%Y-%m-%d %H:%M (%Z)')
         # print(aquisitionEnd.strftime('%Y-%m-%d %I:%M %p (%Z)'))
 
-        gsdForDisplay = float(int(self.singleMetaInDic[u'gsd'] * 100)) / 100
-        fileSizeInMb = float(self.singleMetaInDic[u'file_size']) / (1000 * 1000)
+        gsdForDisplay = float(int(self.singleMetaInDic['gsd'] * 100)) / 100
+        fileSizeInMb = float(self.singleMetaInDic['file_size']) / (1000 * 1000)
         fileSizeInMb = float(int(fileSizeInMb * 100)) / 100
         # fileSizeInMb = self.singleMetaInDic[u'file_size'] / (1024 * 1024)
 
-        strTitle = 'TITLE:\n' + self.singleMetaInDic[u'title'] + '\n'
+        strTitle = 'TITLE:\n' + self.singleMetaInDic['title'] + '\n'
         self.lbTitle.setWordWrap(True)
         self.lbTitle.setText(strTitle)
 
-        strPlatform = self.singleMetaInDic[u'platform']
+        strPlatform = self.singleMetaInDic['platform']
         strGsdForDisplay = str(gsdForDisplay) + ' m'
-        strProvider = self.singleMetaInDic[u'provider']
+        strProvider = self.singleMetaInDic['provider']
         strFileSizeInMb = str(fileSizeInMb) + ' MB'
 
         self.lbText0.setText(strPlatform)
@@ -141,8 +141,8 @@
 
     def displayThumbnail(self):
         isDownloadSuccess = False
-        urlThumbnail = self.singleMetaInDic[u'properties'][u'thumbnail']
-        imageId = self.singleMetaInDic[u'_id']
+        urlThumbnail = self.singleMetaInDic['properties']['thumbnail']
+        imageId = self.singleMetaInDic['_id']
         prefix = str(imageId) + '_'
         imgAbspath = self.thumbnailManager.downloadThumbnail(urlThumbnail, prefix)
 
@@ -159,7 +159,7 @@
         return isDownloadSuccess
 
     def downloadFullImage(self):
-        urlFullImage = self.singleMetaInDic[u'uuid']
+        urlFullImage = self.singleMetaInDic['uuid']
         imgFileName = urlFullImage.split('/')[-1]
         defaultDir = os.path.join(os.path.expanduser('~'), 'oam_images')
         imgAbsPath = os.path.join(defaultDir, imgFileName)
@@ -183,7 +183,7 @@
                 urlFullImage, imgAbsPath, addLayer)
 
             if self.checkBoxSaveMeta.isChecked():
-                urlImgMeta = self.singleMetaInDic[u'meta_uri']
+                urlImgMeta = self.singleMetaInDic['meta_uri']
                 # posLastDots = imgAbsPath.rfind('.')
                 # imgMetaAbsPath = imgAbsPath[0:posLastDots] + '_meta.json'
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_search_dialog.py	(refactored)
@@ -31,7 +31,7 @@
 from PyQt4.Qt import *
 from qgis.gui import QgsMessageBar
 
-from img_browser import ImgBrowser
+from .img_browser import ImgBrowser
 from module.module_access_oam_catalog import OAMCatalogAccess
 from module.module_geocoding import nominatim_search
 
@@ -119,7 +119,7 @@
             self.startSearch()
 
     def test(self, *argv):
-        print(str(argv))
+        print((str(argv)))
 
     def createQueriesSettings(self):
         self.settings.setValue('CHECKBOX_LOCATION', True)
@@ -247,7 +247,7 @@
 
         for singleMetaInDict in metadataInList:
             item = QListWidgetItem()
-            item.setText(singleMetaInDict[u'title'])
+            item.setText(singleMetaInDict['title'])RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/setting_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/help/source/conf.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_dropbox.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_googledrive.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_command_window.py

             item.setData(Qt.UserRole, singleMetaInDict)
             self.listWidget.addItem(item)
 
@@ -299,7 +299,7 @@
             elif self.comboBoxOrderBy.currentText() == 'GSD':
                 dictQueries['order_by'] = "gsd"
 
-            print(self.comboBoxOrderBy.currentText())
+            print((self.comboBoxOrderBy.currentText()))
 
 
             if self.radioButtonAsc.isChecked():
@@ -314,7 +314,7 @@
             self.refreshListWidget(metadataInList)
 
         except Exception as e:
-            print(repr(e))
+            print((repr(e)))
             qMsgBox = QMessageBox()
             qMsgBox.setWindowTitle('Message')
             qMsgBox.setText("Please make sure if you entered valid data" +
@@ -377,8 +377,8 @@
                     self.displayThumnailDownloadError)
 
                 pos = self.pos()
-                print(pos.x())
-                print(pos.y())
+                print((pos.x()))
+                print((pos.y()))
                 pos.setX(pos.x() + 400)
                 pos.setY(pos.y() + 20)
                 self.imgBrowser.move(pos)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/img_uploader_wizard.py	(refactored)
@@ -35,7 +35,7 @@
 import traceback
 
 from module.module_handle_metadata import ImgMetadataHandler
-from upload_progress_window import UploadProgressWindow
+from .upload_progress_window import UploadProgressWindow
 from module.module_gdal_utilities import ReprojectionCmdWindow
 from module.module_validate_files import validate_layer, validate_file
 from module.module_img_utilities import ThumbnailCreation
@@ -219,7 +219,7 @@
                         item = QListWidgetItem()
                         item.setText(os.path.basename(filename))
                         item.setData(Qt.UserRole, os.path.abspath(filename))
-                        print(item.data(Qt.UserRole))
+                        print((item.data(Qt.UserRole)))
                         self.sources_list_widget.addItem(item)
                         self.added_sources_list_widget.addItem(item.clone())
                         self.source_file_edit.setText('')
@@ -570,7 +570,7 @@
         imgMetaHdlr = ImgMetadataHandler(file_abspath)
         imgMetaHdlr.extractMetaInImagery()
         metaForUpload = dict(
-            imgMetaHdlr.getMetaInImagery().items() + metaInputInDict.items())
+            list(imgMetaHdlr.getMetaInImagery().items()) + list(metaInputInDict.items()))
         strMetaForUpload = str(json.dumps(metaForUpload))
 
         json_file_abspath = file_abspath + '_meta.json'
@@ -747,7 +747,7 @@
 
     def loadMetadataReviewBox(self):
         json_file_abspaths = []
-        for index in xrange(self.sources_list_widget.count()):
+        for index in range(self.sources_list_widget.count()):
             file_abspath = str(
                 self.sources_list_widget.item(index).data(Qt.UserRole))
             json_file_abspath = ''
@@ -787,7 +787,7 @@
                 'Please check the lisence term.',
                 level=QgsMessageBar.WARNING)
         else:
-            for index in xrange(self.sources_list_widget.count()):
+            for index in range(self.sources_list_widget.count()):
                 upload_file_abspath = str(
                     self.added_sources_list_widget.item(index).data(Qt.UserRole))
                 # create thumbnail
@@ -862,7 +862,7 @@
         # print('fileAbsPath: ' + fileAbsPath)
 
         # print(str(self.added_sources_list_widget.count()))
-        for index in xrange(0, self.added_sources_list_widget.count()):
+        for index in range(0, self.added_sources_list_widget.count()):
             refFileAbsPath = str(
                 self.added_sources_list_widget.item(index).data(Qt.UserRole))
             # print('refFileAbsPath: ' + refFileAbsPath)
@@ -871,7 +871,7 @@
                 break
 
         # print(str(self.sources_list_widget.count()))
-        for index in xrange(0, self.sources_list_widget.count()):
+        for index in range(0, self.sources_list_widget.count()):
             refFileAbsPath = str(
                 self.sources_list_widget.item(index).data(Qt.UserRole))
             # print('refFileAbsPath: ' + refFileAbsPath)
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/gui/upload_progress_window.py	(refactored)
@@ -105,15 +105,15 @@
                     dropboxAccessToken=None):
 
         # testing purpose only
-        print(str(storageType))
-        print(str(uploadFileAbspaths))
-        print(str(uploadOptions))
-        print(str(awsBucketKey))
-        print(str(awsBucketSecret))
-        print(str(awsBucketName))
-        print(str(googleClientSecret))
-        print(str(googleAppName))
-        print(str(dropboxAccessToken))
+        print((str(storageType)))
+        print((str(uploadFileAbspaths)))
+        print((str(uploadOptions)))
+        print((str(awsBucketKey)))
+        print((str(awsBucketSecret)))
+        print((str(awsBucketName)))
+        print((str(googleClientSecret)))
+        print((str(googleAppName)))
+        print((str(dropboxAccessToken)))
 
         # make sure if it's ready to upload
         startFlag = False
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/help/source/conf.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/help/source/conf.py	(refactored)
@@ -44,8 +44,8 @@
 master_doc = 'index'
 
 # General information about the project.
-project = u'OpenAerialMap'
-copyright = u'2013, Humanitarian OpenStreetMap Team (HOT)'
+project = 'OpenAerialMap'
+copyright = '2013, Humanitarian OpenStreetMap Team (HOT)'
 
 # The version info for the project you're documenting, acts as replacement for
 # |version| and |release|, also used in various other places throughout the
@@ -182,8 +182,8 @@
 # Grouping the document tree into LaTeX files. List of tuples
 # (source start file, target name, title, author, documentclass [howto/manual]).
 latex_documents = [
-  ('index', 'OpenAerialMap.tex', u'OpenAerialMap Documentation',
-   u'Humanitarian OpenStreetMap Team (HOT)', 'manual'),
+  ('index', 'OpenAerialMap.tex', 'OpenAerialMap Documentation',
+   'Humanitarian OpenStreetMap Team (HOT)', 'manual'),
 ]
 
 # The name of an image file (relative to this directory) to place at the top of
@@ -215,6 +215,6 @@
 # One entry per manual page. List of tuples
 # (source start file, name, description, authors, manual section).
 man_pages = [
-    ('index', 'TemplateClass', u'OpenAerialMap Documentation',
-     [u'Humanitarian OpenStreetMap Team (HOT)'], 1)
+    ('index', 'TemplateClass', 'OpenAerialMap Documentation',
+     ['Humanitarian OpenStreetMap Team (HOT)'], 1)
 ]
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_oam_catalog.py	(refactored)
@@ -28,7 +28,7 @@
 # import urllib2
 import requests
 import json
-from StringIO import StringIO
+from io import StringIO
 
 
 class OAMCatalogAccess:
@@ -49,7 +49,7 @@
     def getMetadataInList(self):
         jMetadataInStr = self.downloadMetadata()
         metadadaInDic = json.loads(jMetadataInStr)
-        metadataInList = metadadaInDic[u'results']
+        metadataInList = metadadaInDic['results']
         return metadataInList
 
     def downloadMetadata(self):
@@ -66,7 +66,7 @@
 
             count = 0
             for key in self.dictQueries:
-                print(str(key) + " " + str(self.dictQueries[key]))
+                print((str(key) + " " + str(self.dictQueries[key])))
                 if (self.dictQueries[key] is not None and
                         self.dictQueries[key] != ''):
                     if count == 0:
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py	(original)RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_gdal_utilities.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_geocoding.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_validate_files.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/qgis_interface.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_oam_client_dialog.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_resources.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py
RefactoringTool: Refactored /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py
RefactoringTool: No changes to /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py
RefactoringTool: Files that need to be modified:
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/__init__.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/auth_handler.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/awslambda/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/beanstalk/wrapper.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/stack.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudformation/template.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/distribution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/identity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/invalidation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/logging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/object.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/origin.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudfront/signers.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudhsm/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/optionstatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch/sourceattribute.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/optionstatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearch2/search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudsearchdomain/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cloudtrail/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/codedeploy/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/identity/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/cognito/sync/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/configservice/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/contrib/ymlmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/datapipeline/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/directconnect/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/batch.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/condition.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/item.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/schema.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb/types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/fields.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/items.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/results.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/dynamodb2/types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/address.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/attributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/blockdevicemapping.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/bundleinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/buyreservation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/ec2object.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/image.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instanceinfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/instancetype.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/keypair.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/launchspecification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/networkinterface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/placementgroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/regioninfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/reservedinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/snapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotdatafeedsubscription.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotinstancerequest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/spotpricehistory.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/tag.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volume.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/volumestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/zone.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/datapoint.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/dimension.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/listelement.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/cloudwatch/metric.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/attributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/healthcheck.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/instancestate.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listelement.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/listener.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/loadbalancer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/policies.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2/elb/securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ec2containerservice/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ecs/item.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elasticache/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/elastictranscoder/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/bootstrap_action.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/emrobject.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/instance_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/emr/step.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/file/simpleresultset.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/fps/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/concurrent.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/job.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/glacier/response.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/iam/summarymap.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kinesis/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/kms/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/logs/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/machinelearning/__init__.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/opsworks/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/bootstrap.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/config.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/copybot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/helloworld.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/launch_ami.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/scriptbase.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/startup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/pyami/installers/ubuntu/apache.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/rds2/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/redshift/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryrequest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/awsqueryservice.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/roboto/param.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/healthcheck.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/hostedzone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/record.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/status.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/zone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/route53/domains/__init__.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sdb/__init__.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/ses/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sns/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/attributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/batchresults.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/bigmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/jsonmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/message.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/messageattributes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sqs/queue.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/sts/credentials.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/support/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer1_decisions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/swf/layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/customergateway.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vpc/dhcpoptions.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/fps/test_verify_signature.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/awslambda/test_awslambda.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/beanstalk/test_wrapper.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudformation/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudhsm/test_cloudhsm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch/test_layers.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch2/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudsearch2/test_layers.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cloudtrail/test_cloudtrail.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/codedeploy/test_codedeploy.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/identity/test_cognito_identity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/cognito/sync/test_cognito_sync.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/configservice/test_configservice.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/datapipeline/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/directconnect/test_directconnect.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb/test_table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_highlevel.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/dynamodb2/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/autoscale/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/cloudwatch/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/elb/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2/vpc/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ec2containerservice/test_ec2containerservice.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elasticache/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/elastictranscoder/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/emr/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/glacier/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/cb_test_harness.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_basic.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_generation_conditionals.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_downloads.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_resumable_uploads.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_storage_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/test_versioning.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/testcase.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/gs/util.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/iam/test_password_policy.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kinesis/test_kinesis.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/kms/test_kms.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/logs/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/logs/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/mws/test.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/opsworks/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_db_subnet_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds/test_promote_modify.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/rds2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/redshift/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_alias_resourcerecordsets.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_health_check.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_resourcerecordsets.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/test_zone.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/route53/domains/test_route53domains.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/mock_storage_service.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_bucket.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connect_to_region.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_cors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_encryption.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_https_cert_validation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_mfa.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multidelete.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_multipart.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_pool.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/s3/test_versioning.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sdb/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ses/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/ses/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sns/test_sns_sqs_subscription.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_bigmessage.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sqs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/storage_uri/test_storage_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_cert_verification.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/sts/test_session_token.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/support/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/integration/swf/test_cert_verification.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/mocks.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/run-doctest.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/selenium_support.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/test_disable_hit.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/test_regioninfo.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_sigv4.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/auth/test_stsanon.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/awslambda/test_awslambda.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_exception.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/beanstalk/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudformation/test_stack.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_distribution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_invalidation_list.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudfront/test_signed_urls.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch/test_search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_document.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearch2/test_search.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudsearchdomain/test_cloudsearchdomain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/cloudtrail/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/directconnect/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_batch.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb/test_types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/dynamodb2/test_table.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_address.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_blockdevicemapping.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_ec2object.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancestatus.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_instancetype.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_networkinterface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_reservedinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_securitygroup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_snapshot.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_spotinstance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/test_volume.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/autoscale/test_group.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/cloudwatch/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_attribute.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_listener.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ec2/elb/test_loadbalancer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ecs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/elasticache/test_api_interface.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_emr_responses.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/emr/test_instance_group_args.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_concurrent.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_job.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_layer2.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_vault.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/glacier/test_writer.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/iam/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kinesis/test_kinesis.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/kms/test_kms.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/logs/test_layer1.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/machinelearning/test_machinelearning.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_cors_configuration.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_key.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_keyfile.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_lifecycle.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_tagging.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_uri.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/s3/test_website.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/ses/test_identity.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sns/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_message.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sqs/test_queue.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sts/test_connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/sts/test_credentials.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer1_decisions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_actors.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_base.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_domain.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/swf/test_layer2_types.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/utils/test_utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/unit/vpc/__init__.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/filechunkio.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/filechunkio-1.6/filechunkio/tests.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/setup.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/distance.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/geopy-1.11.0/geopy/exc.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/api.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/auth.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/certs.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/cookies.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/hooks.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/models.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/sessions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/status_codes.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/structures.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/utils.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5freq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/big5prober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardetect.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/chardistribution.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetgroupprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/charsetprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/codingstatemachine.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/compat.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/constants.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/cp949prober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/escsm.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/eucjpprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrfreq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euckrprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwfreq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/euctwprober.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312freq.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/chardet/gb2312prober.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/exceptions.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/fields.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/filepost.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/poolmanager.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/request.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/response.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/ntlmpool.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/contrib/pyopenssl.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ordered_dict.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/__init__.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/connection.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/util/request.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_dropbox.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_googledrive.py
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
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities.py
RefactoringTool: /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/utilities_progress_bar.py
RefactoringTool: Warnings/messages while refactoring:
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/boto/vendored/six.py ###
RefactoringTool: Line 491: Calls to builtin next() possibly shadowed by global binding
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/boto-2.38.0/tests/mturk/cleanup_tests.py ###
RefactoringTool: Line 37: You should use a for loop here
RefactoringTool: Line 38: You should use a for loop here
RefactoringTool: ### In file /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/ext_libs/requests-2.7.0/requests/packages/urllib3/packages/six.py ###
RefactoringTool: Line 232: Calls to builtin next() possibly shadowed by global binding

+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_access_s3.py	(refactored)
@@ -148,9 +148,9 @@
             'OAM',
             level=QgsMessageLog.INFO)
 
-        if u'id' in post_dict.keys():
-            ts_id = post_dict[u'id']
-            time = post_dict[u'queued_at']
+        if 'id' in list(post_dict.keys()):
+            ts_id = post_dict['id']
+            time = post_dict['queued_at']
             QgsMessageLog.logMessage(
                 'Tile service #%s triggered on %s\n' % (ts_id,time),
                 'OAM',
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_download_images.py	(refactored)
@@ -24,7 +24,7 @@
 """
 
 import sys, os, time
-import urllib2
+import urllib.request, urllib.error, urllib.parse
 import json
 from PyQt4 import QtCore
 from PyQt4.QtGui import *
@@ -51,7 +51,7 @@
         # print(imgAbspath)
         if not os.path.exists(imgAbspath):
             try:
-                response = urllib2.urlopen(urlThumbnail)
+                response = urllib.request.urlopen(urlThumbnail)
                 chunkSize = 1024 * 16
                 f = open(imgAbspath, 'wb')
                 while True:
@@ -75,10 +75,10 @@
     def downloadImgMeta(urlImgMeta, imgMetaAbsPath):
         try:
             f = open(imgMetaAbsPath, 'w')
-            f.write(urllib2.urlopen(urlImgMeta).read())
+            f.write(urllib.request.urlopen(urlImgMeta).read())
             f.close()
         except Exception as e:
-            print(str(e))
+            print((str(e)))
 
         return True
 
@@ -333,7 +333,7 @@
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
@@ -120,8 +120,8 @@
                   adfGeoTransform[4] * x +
                   adfGeoTransform[5] * y)
     else:
-        print "BBOX might be wrong. Transformation coefficient " + \
-            "could not be fetched from raster"
+        print("BBOX might be wrong. Transformation coefficient " + \
+            "could not be fetched from raster")
         return (x, y)
 
     # Report the georeferenced coordinates
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_handle_metadata.py	(refactored)
@@ -63,7 +63,7 @@
             self.extractGsd()
             return True
         else:
-            print "Error: could not open the gdaldataset."
+            print("Error: could not open the gdaldataset.")
             return False
 
     def extractProjName(self):
@@ -140,8 +140,8 @@
             geoX = geoTransform[0] + geoTransform[1] * x + geoTransform[2] * y
             geoY = geoTransform[3] + geoTransform[4] * x + geoTransform[5] * y
         else:
-            print "BBOX might be wrong. Transformation coefficient " + \
-                "could not be fetched from raster"
+            print("BBOX might be wrong. Transformation coefficient " + \
+                "could not be fetched from raster")
             return (x, y)
 
         # Report the georeferenced coordinates
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/module/module_img_utilities.py	(refactored)
@@ -24,6 +24,6 @@
                 im = im.resize(size)
                 im.save(outfile, "PNG")
             except Exception as e:
-                print(e, infile)
+                print((e, infile))
 
         return outfile
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_init.py	(refactored)
@@ -11,7 +11,7 @@
 import os
 import unittest
 import logging
-import ConfigParser
+import configparser
 
 LOGGER = logging.getLogger('QGIS')
 
@@ -47,7 +47,7 @@
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
@@ -18,7 +18,7 @@
 
 from oam_client_dialog import OpenAerialMapDialog
 
-from utilities import get_qgis_app
+from .utilities import get_qgis_app
 QGIS_APP = get_qgis_app()
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_qgis_environment.py	(refactored)
@@ -20,7 +20,7 @@
     QgsCoordinateReferenceSystem,
     QgsRasterLayer)
 
-from utilities import get_qgis_app
+from .utilities import get_qgis_app
 QGIS_APP = get_qgis_app()
 
 
--- /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py	(original)
+++ /home/geopro/Documents/osGeoLive/salientrobot-dev/oam-qgis-plugin/OpenAerialMap/test/test_translations.py	(refactored)
@@ -7,7 +7,7 @@
      (at your option) any later version.
 
 """
-from utilities import get_qgis_app
+from .utilities import get_qgis_app
 
 __author__ = 'ismailsunni@yahoo.co.id'
 __date__ = '12/10/2011'
@@ -26,12 +26,12 @@
 
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
@@ -26,7 +26,7 @@
         from PyQt4 import QtGui, QtCore
         from qgis.core import QgsApplication
         from qgis.gui import QgsMapCanvas
-        from qgis_interface import QgisInterface
+        from .qgis_interface import QgisInterface
     except ImportError:
         return None, None, None, None
 

Process finished with exit code 0
```

