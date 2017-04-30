# -*- coding: utf-8 -*-
"""
电子商务系统订单界面
by: xf
2017.4.29
"""
# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\dingdan.ui'
#
# Created: Thu Apr 27 20:11:54 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dianhua import *
from riqi import *
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


class Ui_dingdan(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(673, 425)
        self.form = Dialog
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 651, 311))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels([u'下单时间', u'电话', u'送货地址', u'订单', u'总价', u'状态'])
        for x in range(self.tableWidget.columnCount()):
            headItem = self.tableWidget.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setBackgroundColor(QColor(0, 60, 10))  # 设置单元格背景颜色
            headItem.setTextColor(QColor(200, 111, 30))  # 设置文字颜色
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)  # 无法编辑
        # 初始化表格
        self.set_table()
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 390, 81, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 390, 71, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 390, 81, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 390, 81, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(585, 390, 71, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 20, 93, 28))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.s_wancheng)
        self.pushButton_2.clicked.connect(self.s_quanbu)
        self.pushButton_3.clicked.connect(self.s_quxiao)
        self.pushButton_4.clicked.connect(self.s_weiwancheng)
        self.pushButton_5.clicked.connect(self.fanhui)
        self.pushButton_6.clicked.connect(self.dianhua)
        self.pushButton_7.clicked.connect(self.riqi)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "订单信息检索", None))
        self.pushButton.setText(_translate("Dialog", "已完成订单", None))
        self.pushButton_2.setText(_translate("Dialog", "全部订单", None))
        self.pushButton_3.setText(_translate("Dialog", "已取消订单", None))
        self.pushButton_4.setText(_translate("Dialog", "未完成订单", None))
        self.pushButton_5.setText(_translate("Dialog", "返回主页", None))
        self.pushButton_6.setText(_translate("Dialog", "按电话号检索", None))
        self.pushButton_7.setText(_translate("Dialog", "按日期检索", None))


    def set_table(self, sql='select confirm_time, phone, address, client_order, total_price,status from user_order;'):
        if self.tableWidget.rowCount() > 1:
            self.tableWidget.clearContents()
            for i in range(2, self.tableWidget.rowCount()+1):
                self.tableWidget.removeRow(i)
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        result = db.execute(sql)
        self.num_flag = len(result)
        print 'num', self.num_flag
        while self.tableWidget.rowCount() < self.num_flag:
            self.tableWidget.insertRow(1)
        print 'w_row', self.tableWidget.rowCount()
        for i in range(len(result)):
            for j in range(len(result[i])-1):
                mes = result[i][j]
                newItem = QtGui.QTableWidgetItem(u"%s" % mes)
                self.tableWidget.setItem(i, j, newItem)
            if result[i][5] == '0':
                newItem = QtGui.QTableWidgetItem(u"未完成")
                self.tableWidget.setItem(i, 5, newItem)
            elif result[i][5] == '1':
                newItem = QtGui.QTableWidgetItem(u"已完成")
                self.tableWidget.setItem(i, 5, newItem)
            elif result[i][5] == '-1':
                newItem = QtGui.QTableWidgetItem(u"已取消")
                self.tableWidget.setItem(i, 5, newItem)
        db.db_close()
        print 'hangshu_qian', self.tableWidget.rowCount()
        self.tableWidget.removeRow(len(result)+1)
        print 'shanchu', len(result)+1
        print 'hangshu_hou', self.tableWidget.rowCount()

    def s_wancheng(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order where status =\'1\';')

    def s_quanbu(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order;')

    def s_quxiao(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order where status =\'-1\';')


    def s_weiwancheng(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order where status =\'0\';')

    def fanhui(self):
        self.form.close()

    def dianhua(self):
        # self.form.hide()
        Form1 = QtGui.QDialog()
        ui = Ui_dianhua()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
        self.form.show()
        if ui.phone:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.removeRow(i)
            self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order where phone =\'%s\';' % ui.phone)

    def riqi(self):
        # self.form.hide()
        Form1 = QtGui.QDialog()
        ui = Ui_riqi()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
        self.form.show()
        if ui.date:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.removeRow(i)
            self.set_table('select confirm_time, phone, address, client_order, total_price,status from user_order where confirm_time like \'%s%%\';' % ui.date)

