"""
/***************************************************************************
 OpenAerialMap QGIS plugin
 Module for accessing images in local storage
 ***************************************************************************/
"""

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

import syslog, traceback


#under construction
#is it better to define class?

"""
def loadLayers(iface, dlg, .........):
    all_layers = self.iface.mapCanvas().layers()
    for layer in all_layers:
        if not self.dlg.layers_list_widget.findItems(layer.name(),Qt.MatchExactly):
            item = QListWidgetItem()
            item.setText(layer.name())
            item.setData(Qt.UserRole, layer.dataProvider().dataSourceUri())
            self.dlg.layers_list_widget.addItem(item)
    self.dlg.bar.clearWidgets()
    self.dlg.bar.pushMessage("INFO", "Source imagery for upload must be selected from layers or files.", level=QgsMessageBar.INFO)
"""
