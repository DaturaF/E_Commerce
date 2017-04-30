# -*- coding: utf-8 -*-
"""
电子商务系统电话检索界面
by: xf
2017.4.30
"""
# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\dianhua.ui'
#
# Created: Thu Apr 27 20:12:32 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from db import *

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


class Ui_dianhua(object):
    def __init__(self):
        self.phone = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(252, 132)
        self.form = Dialog

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 151, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 30, 61, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 90, 61, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.jiansuo)
        self.pushButton_2.clicked.connect(self.fanhui)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "电话检索", None))
        self.label.setText(_translate("Dialog", "请输入要检索的电话号", None))
        self.pushButton.setText(_translate("Dialog", "检索", None))
        self.pushButton_2.setText(_translate("Dialog", "返回", None))
        self.label_2.setText(_translate("Dialog", "提示信息", None))

    def jiansuo(self):
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select count(*) from user_order where phone = \'%s\';' % self.lineEdit.text()
        result = db.execute(sql)
        if result[0][0]:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.darkGreen)
            self.label_2.setPalette(pe)
            self.label_2.setText(_translate("Dialog", "共%s条记录"  % str(result[0][0]), None))
            self.label_2.show()
            self.phone = self.lineEdit.text()
        else:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.red)
            self.label_2.setPalette(pe)
            self.label_2.setText(_translate("Dialog", "无记录", None))
            self.label_2.show()

    def fanhui(self):
        self.form.close()

