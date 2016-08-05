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
        #self.cancelled.emit(self.index)

    def startCommandThread(self):
        self.cmdThread = CommandWorker(self.strCmd)
        self.cmdThread.start()
        #self.cmdThread.run()
        self.cmdThread.message.connect(self.updateTextEdit)
        self.cmdThread.finished.connect(self.finishTask)
        self.cmdThread.error.connect(self.displayErrorMessage)

    def updateTextEdit(self, c):
        self.te.insertPlainText(c)

    def finishTask(self, result):
        #print(str(result))
        self.cmdThread.exit()
        self.finished.emit(self.index)
        self.close()

    def displayErrorMessage(self, eMsg):
        #print(eMsg)
        pass


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
            p = subprocess.Popen(self.strCmd, shell=True, stdout=subprocess.PIPE)
            while self.isRunning:
                out = p.stdout.read(1)
                #out = p.stderr.read(1)
                if out == '' and p.poll() is not None:
                    break
                #sys.stdout.write(out)
                #print(str(out))
                self.message.emit(str(out))
                p.stdout.flush()
        except Exception as e:
            self.error.emit(str(e))
            self.isRunning = False

        if self.isRunning:
            self.finished.emit('success')
        else:
            self.finished.emit('fail')

    def stop(self):
        self.isRunning = False
