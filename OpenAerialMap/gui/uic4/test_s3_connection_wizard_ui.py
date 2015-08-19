# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test_s3_connection_wizard.ui'
#
# Created: Tue Aug 18 19:35:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(450, 295)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.start_message = QtGui.QLabel(self.wizardPage1)
        self.start_message.setGeometry(QtCore.QRect(100, 50, 221, 41))
        self.start_message.setObjectName(_fromUtf8("start_message"))
        self.lbInstruct = QtGui.QLabel(self.wizardPage1)
        self.lbInstruct.setGeometry(QtCore.QRect(100, 80, 221, 41))
        self.lbInstruct.setObjectName(_fromUtf8("lbInstruct"))
        self.lbAccKeyID_0 = QtGui.QLabel(self.wizardPage1)
        self.lbAccKeyID_0.setGeometry(QtCore.QRect(120, 130, 81, 17))
        self.lbAccKeyID_0.setObjectName(_fromUtf8("lbAccKeyID_0"))
        self.lbSecretAccKey_0 = QtGui.QLabel(self.wizardPage1)
        self.lbSecretAccKey_0.setGeometry(QtCore.QRect(120, 150, 101, 17))
        self.lbSecretAccKey_0.setObjectName(_fromUtf8("lbSecretAccKey_0"))
        self.lbBucketName_0 = QtGui.QLabel(self.wizardPage1)
        self.lbBucketName_0.setGeometry(QtCore.QRect(120, 170, 81, 17))
        self.lbBucketName_0.setObjectName(_fromUtf8("lbBucketName_0"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.inputSecretAccKey = QtGui.QPlainTextEdit(self.wizardPage2)
        self.inputSecretAccKey.setGeometry(QtCore.QRect(140, 90, 221, 31))
        self.inputSecretAccKey.setObjectName(_fromUtf8("inputSecretAccKey"))
        self.lbBucketName_1 = QtGui.QLabel(self.wizardPage2)
        self.lbBucketName_1.setGeometry(QtCore.QRect(20, 140, 81, 17))
        self.lbBucketName_1.setObjectName(_fromUtf8("lbBucketName_1"))
        self.inputBucketName = QtGui.QPlainTextEdit(self.wizardPage2)
        self.inputBucketName.setGeometry(QtCore.QRect(140, 130, 221, 31))
        self.inputBucketName.setObjectName(_fromUtf8("inputBucketName"))
        self.lbSecretAccKey_1 = QtGui.QLabel(self.wizardPage2)
        self.lbSecretAccKey_1.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.lbSecretAccKey_1.setObjectName(_fromUtf8("lbSecretAccKey_1"))
        self.inputAccKeyID = QtGui.QPlainTextEdit(self.wizardPage2)
        self.inputAccKeyID.setGeometry(QtCore.QRect(140, 50, 221, 31))
        self.inputAccKeyID.setObjectName(_fromUtf8("inputAccKeyID"))
        self.lbAccKeyID_1 = QtGui.QLabel(self.wizardPage2)
        self.lbAccKeyID_1.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.lbAccKeyID_1.setObjectName(_fromUtf8("lbAccKeyID_1"))
        Wizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.btnTestConn = QtGui.QPushButton(self.wizardPage3)
        self.btnTestConn.setGeometry(QtCore.QRect(260, 190, 111, 27))
        self.btnTestConn.setObjectName(_fromUtf8("btnTestConn"))
        self.listWidget = QtGui.QListWidget(self.wizardPage3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 411, 161))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        Wizard.addPage(self.wizardPage3)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Wizard", None))
        self.start_message.setText(_translate("Wizard", "AWS S3 Connection Test Wizard", None))
        self.lbInstruct.setText(_translate("Wizard", "Please prepare following info:", None))
        self.lbAccKeyID_0.setText(_translate("Wizard", "Access Key ID", None))
        self.lbSecretAccKey_0.setText(_translate("Wizard", "Secret Access Key", None))
        self.lbBucketName_0.setText(_translate("Wizard", "Bucket Name", None))
        self.lbBucketName_1.setText(_translate("Wizard", "Bucket Name", None))
        self.lbSecretAccKey_1.setText(_translate("Wizard", "Secret Access Key", None))
        self.lbAccKeyID_1.setText(_translate("Wizard", "Access Key ID", None))
        self.btnTestConn.setText(_translate("Wizard", "Test Connection", None))

