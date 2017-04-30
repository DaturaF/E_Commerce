# -*- coding: utf-8 -*-
"""
电子商务系统日期检索界面
by: xf
2017.4.30
"""
# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\riqi.ui'
#
# Created: Thu Apr 27 20:12:59 2017
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


class Ui_riqi(object):
    def __init__(self):
        self.date = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(321, 294)
        self.form = Dialog
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 50, 296, 201))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 131, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 51, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(252, 260, 61, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.jiansuo)
        self.pushButton_2.clicked.connect(self.fanhui)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "日期检索", None))
        self.label.setText(_translate("Dialog", "选择要检索的日期", None))
        self.pushButton.setText(_translate("Dialog", "检索", None))
        self.pushButton_2.setText(_translate("Dialog", "返回", None))
        self.label_2.setText(_translate("Dialog", "提示信息", None))
        self.label_2.hide()

    def jiansuo(self):
        date = str(self.calendarWidget.selectedDate().toPyDate())
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select count(*) from user_order where confirm_time like \'%s%%\';' % date
        print sql
        result = db.execute(sql)
        if result[0][0]:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.darkGreen)
            self.label_2.setPalette(pe)
            self.label_2.setText(_translate("Dialog", "共%s条记录" % str(result[0][0]), None))
            self.label_2.show()
            self.date = date
        else:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.red)
            self.label_2.setPalette(pe)
            self.label_2.setText(_translate("Dialog", "无记录", None))
            self.label_2.show()
    def fanhui(self):
        self.form.close()

