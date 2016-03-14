#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)

    mainWindow = QtGui.QMainWindow()
    mainWindow.setWindowTitle(u"Merhaba Dünya")
    mainWindow.show()

    return app.exec_()

if __name__ == "__main__": main()
