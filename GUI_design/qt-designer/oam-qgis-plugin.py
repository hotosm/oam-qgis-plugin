# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oam-qgis-plugin.ui'
#
# Created: Thu Jun 18 00:01:43 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(353, 425)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 301, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(85, 110, 81, 22))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 110, 81, 22))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.columnView = QtGui.QColumnView(self.tab)
        self.columnView.setGeometry(QtCore.QRect(20, 150, 261, 176))
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(25, 25, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 20, 166, 26))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.verticalScrollBar = QtGui.QScrollBar(self.tab)
        self.verticalScrollBar.setGeometry(QtCore.QRect(265, 150, 20, 176))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(25, 65, 101, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 60, 201, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.toolButton = QtGui.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(250, 20, 31, 26))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(30, 160, 58, 14))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(30, 180, 58, 14))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(30, 200, 58, 14))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(50, 125, 59, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(45, 150, 59, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(25, 175, 59, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(25, 200, 59, 14))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 225, 59, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 250, 59, 14))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(25, 275, 59, 14))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(25, 300, 59, 14))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 120, 191, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 145, 191, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 170, 191, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 195, 191, 22))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 220, 191, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 245, 191, 22))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 270, 191, 22))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 295, 191, 22))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 231, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 320, 89, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 320, 89, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalScrollBar_2 = QtGui.QScrollBar(self.tab_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(270, 30, 20, 81))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName(_fromUtf8("verticalScrollBar_2"))
        self.columnView_2 = QtGui.QColumnView(self.tab_2)
        self.columnView_2.setGeometry(QtCore.QRect(20, 30, 251, 81))
        self.columnView_2.setObjectName(_fromUtf8("columnView_2"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 80, 231, 16))
        self.label_17.setStyleSheet(_fromUtf8("background-color: rgb(215, 201, 255);"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 40, 231, 16))
        self.label_18.setStyleSheet(_fromUtf8("background-color: rgb(215, 201, 255);"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 58, 14))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.checkBox = QtGui.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 45, 251, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 75, 226, 20))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 105, 231, 20))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 135, 226, 20))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.progressBar = QtGui.QProgressBar(self.tab_4)
        self.progressBar.setGeometry(QtCore.QRect(95, 255, 186, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 290, 81, 22))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_10 = QtGui.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox = QtGui.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(95, 155, 191, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_5 = QtGui.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 290, 81, 22))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 290, 81, 22))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(25, 260, 59, 14))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_20 = QtGui.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.scrollArea = QtGui.QScrollArea(self.tab_4)
        self.scrollArea.setGeometry(QtCore.QRect(25, 45, 251, 96))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 94))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalScrollBar_3 = QtGui.QScrollBar(self.tab_4)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(270, 45, 16, 96))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName(_fromUtf8("verticalScrollBar_3"))
        self.label_21 = QtGui.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(20, 190, 58, 14))
        self.label_21.setStyleSheet(_fromUtf8("color: rgb(143, 143, 143);"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(20, 220, 58, 14))
        self.label_22.setStyleSheet(_fromUtf8("color: rgb(143, 143, 143);"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(95, 185, 191, 26))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(95, 215, 191, 26))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Add", None))
        self.pushButton_2.setText(_translate("Dialog", "Remove", None))
        self.label.setText(_translate("Dialog", "File:", None))
        self.label_12.setText(_translate("Dialog", "Layer:", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Layer 1", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.label_14.setText(_translate("Dialog", "File 1", None))
        self.label_15.setText(_translate("Dialog", "File 2", None))
        self.label_16.setText(_translate("Dialog", "Layer 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Imagery", None))
        self.label_2.setText(_translate("Dialog", "Title:", None))
        self.label_3.setText(_translate("Dialog", "Tags:", None))
        self.label_4.setText(_translate("Dialog", "Provider:", None))
        self.label_5.setText(_translate("Dialog", "Platform:", None))
        self.label_6.setText(_translate("Dialog", "Sensor:", None))
        self.label_7.setText(_translate("Dialog", "License:", None))
        self.label_8.setText(_translate("Dialog", "Website:", None))
        self.label_9.setText(_translate("Dialog", "Contact:", None))
        self.label_13.setText(_translate("Dialog", "Select elements to edit metadata:", None))
        self.pushButton_3.setText(_translate("Dialog", "Save", None))
        self.pushButton_7.setText(_translate("Dialog", "Restore", None))
        self.label_17.setText(_translate("Dialog", "Layer 1", None))
        self.label_18.setText(_translate("Dialog", "File 1", None))
        self.label_19.setText(_translate("Dialog", "File 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Metadata", None))
        self.checkBox.setText(_translate("Dialog", "Notify OAM of new resource", None))
        self.checkBox_2.setText(_translate("Dialog", "Trigger OAM tile service", None))
        self.checkBox_3.setText(_translate("Dialog", "Reproject to EPSG:3857", None))
        self.checkBox_4.setText(_translate("Dialog", "Convert format to GeoTIFF RGB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Options", None))
        self.pushButton_4.setText(_translate("Dialog", "Upload", None))
        self.label_10.setText(_translate("Dialog", "Storage:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "OAM S3 bucket", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Digital Globe", None))
        self.pushButton_5.setText(_translate("Dialog", "Pause", None))
        self.pushButton_6.setText(_translate("Dialog", "Resume", None))
        self.label_11.setText(_translate("Dialog", "Progress:", None))
        self.label_20.setText(_translate("Dialog", "Review full metadata:", None))
        self.label_21.setText(_translate("Dialog", "Address:", None))
        self.label_22.setText(_translate("Dialog", "Key:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Upload", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
