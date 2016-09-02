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

import os, sys
import subprocess, time

from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, pyqtSignal


class CommandWindow(QWidget):

    finished = pyqtSignal(int)
    cancelled = pyqtSignal(int)

    def __init__(self, title, strCmd, index, parent=None):
        QWidget.__init__(self, parent=None)
        self.setWindowTitle(title)
        self.strCmd = strCmd
        self.index = index

        # create objects
        self.label = QLabel(self.tr('Executing the command:\n' + self.strCmd))
        self.label.setFixedWidth(640)
        self.label.setWordWrap(True)
        self.te = QTextEdit()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.te)
        self.setLayout(layout)

    def closeEvent(self, closeEvent):
        self.cmdThread.stop()
        # self.cancelled.emit(self.index)

    def startCommandThread(self):
        self.cmdThread = CommandWorker(self.strCmd)
        self.cmdThread.start()
        # self.cmdThread.run()
        self.cmdThread.message.connect(self.updateTextEdit)
        self.cmdThread.finished.connect(self.finishTask)
        self.cmdThread.error.connect(self.displayErrorMessage)

    def updateTextEdit(self, c):
        self.te.insertPlainText(c)

    def finishTask(self, result):
        # print(str(result))
        self.cmdThread.exit()
        self.finished.emit(self.index)
        self.close()

    def displayErrorMessage(self, eMsg):
        # print(eMsg)
        qMsgBox = QMessageBox()
        qMsgBox.setWindowTitle('Message')
        qMsgBox.setText("Error: " + eMsg)
        qMsgBox.exec_()


class CommandWorker(QThread):

    message = pyqtSignal(str)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, strCmd, parent=None):
        QThread.__init__(self, parent=None)
        self.strCmd = strCmd
        self.isRunning = True

    def run(self):

        try:
            print(os.name)
            print(sys.platform)

            if sys.platform == 'win32':
                import win32con
                p = subprocess.Popen(self.strCmd,
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     creationflags=win32con.CREATE_NO_WINDOW)
            else:
                p = subprocess.Popen(self.strCmd,
                                     shell=True,
                                     stdout=subprocess.PIPE)

            while self.isRunning:
                out = p.stdout.read(1)
                # out = p.stderr.read(1)
                if out == '' and p.poll() is not None:
                    break
                # sys.stdout.write(out)
                # print(str(out))
                self.message.emit(str(out))
                p.stdout.flush()
        except Exception as e:
            if '6' in str(e):
                p = subprocess.call(self.strCmd)
            else:
                self.error.emit(str(e))
                self.isRunning = False

        if self.isRunning:
            self.finished.emit('success')
        else:
            self.finished.emit('fail')

    def stop(self):
        self.isRunning = False
