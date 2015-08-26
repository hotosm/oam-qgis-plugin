import os, sys
from PyQt4 import QtGui, uic
from PyQt4.QtGui import *

sys.path.append(os.path.join(os.path.dirname(__file__), 'uic4'))
from test_s3_connection_wizard_ui import Ui_Wizard

from test_s3_connection import *

#WIZARD_CLASS, _ = uic.loadUiType(os.path.join(
#    os.path.dirname(__file__), 'ui/imagery_upload_wizard.ui'))

class TestS3ConnectionWizard(QtGui.QWizard):
    def __init__(self, parent=None):
        """Constructor."""
        super(TestS3ConnectionWizard, self).__init__(parent)
        self.ui = Ui_Wizard()
        self.ui.setupUi(self)

        #register event handlers
        self.ui.btnTestConn.clicked.connect(self.connect_s3)

    def connect_s3(self):
        accKeyID = unicode(self.ui.inputAccKeyID.toPlainText())
        secretAccKey = unicode(self.ui.inputSecretAccKey.toPlainText())
        bucketName = unicode(self.ui.inputBucketName.toPlainText())
        rs = connect_s3(accKeyID, secretAccKey, bucketName)

        for key in rs:
            item = QListWidgetItem()
            item.setText(str(key))
            self.ui.listWidget.addItem(item)
