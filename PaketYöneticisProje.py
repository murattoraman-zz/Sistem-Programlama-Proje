# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme4.ui'
#
# Created: Wed Mar 30 13:24:33 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QListWidget, QListWidgetItem, QApplication
import subprocess
from subprocess import call

islem = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
cikti = islem.communicate()[0]
duzgun = cikti.decode("utf-8")
liste=[]
liste=duzgun.split()


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
    def yazdir(self,item):
        print(item.text())
        self.secildi = item.text()


    def butonBasildi(self,item):
        print("Basildi Kaldir!")


        os.system("gnome-terminal -e 'apt-get remove '"+self.secildi)


    def butonYenile(self,item):
        print("Basildi Yenile!")
        islem2 = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
        cikti2 = islem2.communicate()[0]
        duzgun2 = cikti2.decode("utf-8")
        liste2=[]
        liste2=duzgun2.split()
        self.lstKaldir.clear()

        i=0
        for i in range(0,len(liste2),2):
            self.lstKaldir.addItem(liste2[i])

    def butonGuncelle(self):
        os.system("gnome-terminal -e 'apt-get update '")


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(833, 554)
        self.lstKaldir = QtGui.QListWidget(Form)
        self.lstKaldir.setGeometry(QtCore.QRect(10, 20, 801, 401))
        self.lstKaldir.setObjectName(_fromUtf8("lstKaldir"))
        self.btnKaldir = QtGui.QPushButton(Form)
        self.btnKaldir.setGeometry(QtCore.QRect(40, 430, 141, 29))
        self.btnKaldir.setObjectName(_fromUtf8("btnKaldir"))
        self.btnYenile = QtGui.QPushButton(Form)
        self.btnYenile.setGeometry(QtCore.QRect(300, 440, 141, 29))
        self.btnYenile.setObjectName(_fromUtf8("btnYenile"))
        self.btnGuncelle = QtGui.QPushButton(Form)
        self.btnGuncelle.setGeometry(QtCore.QRect(600, 440, 141, 29))
        self.btnGuncelle.setObjectName(_fromUtf8("btnGuncelle"))

        i=0
        for i in range(0,len(liste),2):
            self.lstKaldir.addItem(liste[i])

        self.lstKaldir.itemClicked.connect(self.yazdir)


        self.btnKaldir.clicked.connect(self.butonBasildi)
        self.btnYenile.clicked.connect(self.butonYenile)
        self.btnGuncelle.clicked.connect(self.butonGuncelle)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Paket Yöneticisi v1.00", None))
        self.btnKaldir.setText(_translate("Form", "Kaldır", None))
        self.btnYenile.setText(_translate("Form", "Liste Yenile", None))
        self.btnGuncelle.setText(_translate("Form", "Guncelle", None))



app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())

