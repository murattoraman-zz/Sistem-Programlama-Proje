# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemArayuz.ui'
#
# Created: Sun Mar 27 00:31:43 2016
#      by: PyQt4 UI code generator 4.11.2
#

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QListWidget, QListWidgetItem, QApplication
import subprocess

islem = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
cikti = islem.communicate()[0]
dosya2=open("/root/Desktop/dosya3.txt","w")

dosya = open("/root/Desktop/dosya3.txt","w")
dosya.write(str(cikti))
dosya.close()
liste={}
liste=cikti.splitlines()
i=0
for i in liste:
    dosya2.write(i.decode("utf-8"))
    dosya2.write('''\n''')

with open("/root/Desktop/dosya3.txt", "r+") as dosya2:
    print(dosya2.read())
dosya.close()


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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(846, 576)
        self.lstKaldir = QtGui.QListWidget(Form)
        self.lstKaldir.setGeometry(QtCore.QRect(0, 20, 851, 501))
        self.lstKaldir.setObjectName(_fromUtf8("lstKaldir"))
        self.btnKaldir = QtGui.QPushButton(Form)
        self.btnKaldir.setGeometry(QtCore.QRect(12, 530, 821, 29))
        self.btnKaldir.setObjectName(_fromUtf8("btnKaldir"))

        with open("/root/Desktop/dosya3.txt", "r+") as dosya2:
            i=0
            for i in liste:
                 self.lstKaldir.addItem(dosya2.readline())


        dosya.close()
        dosya2.close()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnKaldir.setText(_translate("Form", "Kaldır", None))



app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()




sys.exit(app.exec_())
