# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and
 upload imagery from/to the OAM catalog.
                            -------------------
        begin               : 2015-07-01
        copyright           : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email               : tassia@acaia.ca / yoji.salut@gmail.com
        git sha             : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import os
from builtins import str

from qgis.PyQt import uic
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *

# from qgis.PyQt.Qt import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/setting_dialog.ui'))


class SettingDialog(QDialog, FORM_CLASS):

    def __init__(self, iface, settings, parent=None):
        """Constructor."""
        super(SettingDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doi,
        # self.settingsng self.<objectname>, and you can use autoconnect
        # slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.iface = iface
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint |
                            Qt.WindowMinimizeButtonHint)

        self.settings = settings

        # register event handlers
        self.buttonBox.button(
            QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        self.buttonBox.button(
            QDialogButtonBox.Save).clicked.connect(self.saveSettings)

        # set the calendars
        self.sense_start_edit.setCalendarPopup(1)
        self.sense_start_edit.setDisplayFormat('dd.MM.yyyy HH:mm')
        self.sense_end_edit.setCalendarPopup(1)
        self.sense_end_edit.setDisplayFormat('dd.MM.yyyy HH:mm')

        # event handler for bucket name input
        # self.storage_combo_box.currentIndexChanged.connect(self.enableSpecify)

        self.hot_oam_catalog_check_box.stateChanged.connect(
            self.toggleHotOamCatalog)

        # initialize
        self.loadSettings()

        # temporarily set fixed values for some controls, and disable these controls
        # self.notify_oam_check.setCheckState(0)
        self.default_storage_combo_box.setCurrentIndex(0)
        self.google_client_secret_file_edit.setText('n.a.')
        self.google_application_name_edit.setText('n.a.')
        self.dropbox_access_token_edit.setText('n.a.')

        self.meta_storage_check_box.setCheckState(2)
        self.meta_bucket_name_edit.setText('same as storage')
        self.meta_key_id_edit.setText('same as storage')
        self.meta_secret_key_edit.setText('same as storage')

        # self.notify_oam_check.setEnabled(False)
        self.default_storage_type_label.setEnabled(False)
        self.default_storage_combo_box.setEnabled(False)
        self.google_client_secret_file_label.setEnabled(False)
        self.google_client_secret_file_edit.setEnabled(False)
        self.google_application_name_label.setEnabled(False)
        self.google_application_name_edit.setEnabled(False)
        self.dropbox_access_token_label.setEnabled(False)
        self.dropbox_access_token_edit.setEnabled(False)

        self.meta_storage_check_box.setEnabled(False)
        self.meta_bucket_name_edit.setEnabled(False)
        self.meta_key_id_edit.setEnabled(False)
        self.meta_secret_key_edit.setEnabled(False)

    def loadSettings(self):
        self.loadMetadataSettings()
        self.loadStorageSettings()
        self.loadOptionsSettings()

    def saveSettings(self):
        self.saveMetadataSettings()
        self.saveStorageSettings()
        self.saveOptionsSettings()

    def cancel(self):
        # close the Dialog
        pass

    def saveMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.settings.setValue('BASE_UUID', self.base_uuid_edit.text())
        self.settings.setValue('TITLE', self.title_edit.text())
        self.settings.setValue('PLATFORM',
                               self.platform_combo_box.currentIndex())
        self.settings.setValue('SENSOR', self.sensor_edit.text())
        self.settings.setValue('SENSE_START',
            self.sense_start_edit.dateTime().toString(Qt.ISODate))
        self.settings.setValue('SENSE_END',
            self.sense_end_edit.dateTime().toString(Qt.ISODate))
        self.settings.setValue('PROVIDER', self.provider_edit.text())
        self.settings.setValue('CONTACT', self.contact_edit.text())
        self.settings.endGroup()

    def saveOptionsSettings(self):

        self.settings.beginGroup("Options")
        self.settings.setValue('LICENSE',
                               self.license_check_box.isChecked())
        self.settings.setValue('REPROJECT',
                               self.reproject_check_box.isChecked())
        # self.settings.setValue('NOTIFY_OAM',
        #                        self.notify_oam_check.isChecked())
        self.settings.endGroup()

    def saveStorageSettings(self):

        self.settings.beginGroup("Storage")

        #if self.storage_combo_box.currentIndex() == 0:
        #    self.settings.setValue('S3_BUCKET_NAME',
        #                           'oam-qgis-plugin-test')
        #else:
        #    self.settings.setValue('S3_BUCKET_NAME',
        #                           self.specify_edit.text())

        self.settings.setValue('AWS_BUCKET_NAME',
                               self.aws_bucket_name_edit.text())
        self.settings.setValue('AWS_ACCESS_KEY_ID',
                               self.aws_key_id_edit.text())
        self.settings.setValue('AWS_SECRET_ACCESS_KEY',
                               self.aws_secret_key_edit.text())
        self.settings.setValue('GOOGLE_CLIENT_SECRET_FILE',
                               self.google_client_secret_file_edit.text())
        self.settings.setValue('GOOGLE_APPLICATION_NAME',
                               self.google_application_name_edit.text())
        self.settings.setValue('DROPBOX_ACCESS_TOKEN',
                               self.dropbox_access_token_edit.text())
        self.settings.setValue('DEFAULT_STORAGE',
                               self.default_storage_combo_box.currentIndex())

        self.settings.setValue('HOT_OAM_CATALOG',
                               self.hot_oam_catalog_check_box.isChecked())
        self.settings.setValue('CATALOG_URL',
                               self.catalog_url_edit.text())

        self.settings.endGroup()

    def loadMetadataSettings(self):
        self.settings.beginGroup("Metadata")
        self.base_uuid_edit.setText(self.settings.value('BASE_UUID'))
        self.title_edit.setText(self.settings.value('TITLE'))
        if self.settings.value('PLATFORM') is None:
            self.title_edit.setCursorPosition(0)
        else:
            self.platform_combo_box.setCurrentIndex(
                int(self.settings.value('PLATFORM')))
        self.sensor_edit.setText(self.settings.value('SENSOR'))
        self.sensor_edit.setCursorPosition(0)
        self.sense_start_edit.setDate(QDateTime.fromString(
            self.settings.value('SENSE_START'),
            Qt.ISODate).date())
        self.sense_start_edit.setTime(QDateTime.fromString(
            self.settings.value('SENSE_START'),
            Qt.ISODate).time())
        self.sense_end_edit.setDate(QDateTime.fromString(
            self.settings.value('SENSE_END'),
            Qt.ISODate).date())
        self.sense_end_edit.setTime(QDateTime.fromString(
            self.settings.value('SENSE_END'),
            Qt.ISODate).time())
        self.provider_edit.setText(self.settings.value('PROVIDER'))
        self.provider_edit.setCursorPosition(0)
        self.contact_edit.setText(self.settings.value('CONTACT'))
        self.contact_edit.setCursorPosition(0)
        self.settings.endGroup()

    def loadOptionsSettings(self):
        self.settings.beginGroup("Options")

        """
        Boolean values are converted into string and lower case for
        'if' statement, since PyQt sometimes returns 'true', just like C++,
        instead of 'True', Python style.
        Maybe we can use integer values (0 or 1), instead of using string.
        """
        if str(self.settings.value('LICENSE')).lower() == 'true':
            self.license_check_box.setCheckState(2)
        if str(self.settings.value('REPROJECT')).lower() == 'true':
            self.reproject_check_box.setCheckState(2)
        # if str(self.settings.value('NOTIFY_OAM')).lower() == 'true':
        #     self.notify_oam_check.setCheckState(2)

        self.settings.endGroup()

    def loadStorageSettings(self):
        self.settings.beginGroup("Storage")
        """
        bucket = self.settings.value('S3_BUCKET_NAME')
        storage_index = self.storage_combo_box.findText(
            bucket, Qt.MatchExactly)
        if not storage_index == -1:
            self.storage_combo_box.setCurrentIndex(storage_index)
        else:
            self.storage_combo_box.setCurrentIndex(
                self.storage_combo_box.findText(self.tr('other...')))
            self.specify_label.setEnabled(1)
            self.specify_edit.setEnabled(1)
            self.specify_edit.setText(
                self.settings.value('S3_BUCKET_NAME'))
        """
        self.aws_bucket_name_edit.setText(
            self.settings.value('AWS_BUCKET_NAME'))
        self.aws_bucket_name_edit.setCursorPosition(0)
        self.aws_key_id_edit.setText(
            self.settings.value('AWS_ACCESS_KEY_ID'))
        self.aws_key_id_edit.setCursorPosition(0)
        self.aws_secret_key_edit.setText(
            self.settings.value('AWS_SECRET_ACCESS_KEY'))
        self.aws_secret_key_edit.setCursorPosition(0)

        self.google_client_secret_file_edit.setText(
            self.settings.value('GOOGLE_CLIENT_SECRET_FILE'))
        self.google_application_name_edit.setText(
            self.settings.value('GOOGLE_APPLICATION_NAME'))
        self.dropbox_access_token_edit.setText(
            self.settings.value('DROPBOX_ACCESS_TOKEN'))

        if self.settings.value('DEFAULT_STORAGE'):
            self.default_storage_combo_box.setCurrentIndex(
                int(self.settings.value('DEFAULT_STORAGE')))
        else:
            self.default_storage_combo_box.setCurrentIndex(0)

        if self.settings.value('HOT_OAM_CATALOG') is None or \
            str(self.settings.value('HOT_OAM_CATALOG')).lower() == 'true':
            self.hot_oam_catalog_check_box.setCheckState(2)
        else:
            self.hot_oam_catalog_check_box.setCheckState(0)
            self.catalog_url_edit.setText(self.settings.value('CATALOG_URL'))

        self.settings.endGroup()

    def toggleHotOamCatalog(self):
        if self.hot_oam_catalog_check_box.isChecked():
            self.catalog_url_edit.setText('https://oam-catalog.herokuapp.com')
            self.catalog_url_edit.setEnabled(False)
        else:
            self.catalog_url_edit.setEnabled(True)
            self.catalog_url_edit.setText('')

    """
    def enableSpecify(self):
        if self.storage_combo_box.currentIndex() == 1:
            self.specify_label.setEnabled(1)
            self.specify_edit.setEnabled(1)
        else:
            self.specify_label.setEnabled(0)
            self.specify_edit.setText('')
            self.specify_edit.setEnabled(0)
    """
