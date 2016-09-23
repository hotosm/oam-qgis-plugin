import os, sys
import time

from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, pyqtSignal


class CommandWindow(QWidget):

    started = pyqtSignal(int)
    finished = pyqtSignal(int)
    # cancelled = pyqtSignal(int)

    def __init__(self, title, cmd, optionsInList, index, parent=None):
        QWidget.__init__(self, parent=None)
        # QThread.__init__(self, parent=None)
        self.setWindowTitle(title)
        self.cmd = cmd
        self.optionsInList = optionsInList
        self.index = index

        self.strCmd = str(cmd) + ' '
        for eachOption in optionsInList:
            self.strCmd += eachOption + ' '

        # create objects
        self.label = QLabel(self.tr('Executing the command:\n' + self.strCmd))
        self.label.setFixedWidth(640)
        self.label.setWordWrap(True);
        self.te = QTextEdit()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.te)
        self.setLayout(layout)

        self.process = QtCore.QProcess(self)

    def run(self):
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        self.process.started.connect(self.processStarted)
        self.process.finished.connect(self.processFinished)
        self.process.start(self.cmd, self.optionsInList)

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        #print text.strip()
        self.te.insertPlainText(text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        #print text.strip()
        self.te.insertPlainText(text)

    def processStarted(self):
        self.started.emit(self.index)
        self.show()

    def processFinished(self):
        self.finished.emit(self.index)
        self.close()

    """
    def closeEvent(self, closeEvent):
        self.process.kill()
        self.cancelled.emit(self.index)
    """
