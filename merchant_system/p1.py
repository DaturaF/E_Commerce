#!/usr/bin/env python
#coding=utf-8

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\p1.ui'
#
# Created: Fri Apr 21 10:21:55 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from db import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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


class P1(object):
    def __init__(self):
        super(P1, self).__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(833, 386)
        self.form = Dialog
        self.num_flag = 0 # 表格的行数记录
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(700, 80, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 130, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 30, 101, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 30, 101, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.tableWidget = QtGui.QTableWidget(Dialog)

        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 651, 291))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels([u'下单时间', u'电话', u'送货地址', u'订单', u'总价'])
        for x in range(self.tableWidget.columnCount()):
            headItem = self.tableWidget.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setBackgroundColor(QColor(0, 60, 10))  # 设置单元格背景颜色
            headItem.setTextColor(QColor(200, 111, 30))  # 设置文字颜色
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        # 初始化表格
        self.set_table()

        # 开启监控线程
        threads = []
        t1 = threading.Thread(target=self.db_detective, args=())
        threads.append(t1)
        for t in threads:
            t.setDaemon(True)
            t.start()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.finish_order)
        self.pushButton_2.clicked.connect(self.cancel_order)
        self.pushButton_3.clicked.connect(self.all_order)
        self.pushButton_4.clicked.connect(self.change_message)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "电子商务系统", None))
        self.label.setText(_translate("Dialog", "新订单", None))
        self.pushButton.setText(_translate("Dialog", "完成订单", None))
        self.pushButton_2.setText(_translate("Dialog", "取消订单", None))
        self.pushButton_3.setText(_translate("Dialog", "查看全部订单", None))
        self.pushButton_4.setText(_translate("Dialog", "修改商品信息", None))

    def set_table(self):
        print 'set table'
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select confirm_time, phone, address, client_order, total_price from user_order where status =\'0\';'
        result = db.execute(sql)
        self.num_flag = len(result)-1
        while self.tableWidget.rowCount() < self.num_flag+1:
            self.tableWidget.insertRow(1)
        for i in range(len(result)):
            for j in range(len(result[i])):
                mes = result[i][j]
                newItem = QtGui.QTableWidgetItem(u"%s" % mes)
                self.tableWidget.setItem(i, j, newItem)
        db.db_close()


    def finish_order(self):
        num = self.tableWidget.currentRow()
        o_time = self.tableWidget.item(num, 0).text()
        o_phone = self.tableWidget.item(num, 1).text()
        o_order = self.tableWidget.item(num, 3).text()
        self.tableWidget.removeRow(num)
        self.num_flag -= 1
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'update user_order set status = \'1\' where confirm_time = \'%s\' and phone = \'%s\' and client_order = \'%s\';' % (
        o_time, o_phone, o_order)
        db.execute(sql)
        db.db_commit()
        db.db_close()
    def cancel_order(self):
        num = self.tableWidget.currentRow()
        o_time = self.tableWidget.item(num, 0).text()
        o_phone = self.tableWidget.item(num, 1).text()
        o_order = self.tableWidget.item(num, 3).text()
        self.tableWidget.removeRow(num)
        self.num_flag -= 1
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'update user_order set status = \'-1\' where confirm_time = \'%s\' and phone = \'%s\' and client_order = \'%s\';' % (o_time, o_phone, o_order)
        db.execute(sql)
        db.db_commit()
        db.db_close()

    def db_detective(self):
        print 'thread start'
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select confirm_time, phone, address, client_order, total_price from user_order ;'
        result = db.execute(sql)
        db.db_close()
        num = len(result)
        temp = num
        print 'ori num', num
        while True:
            db = DataBase()
            db.get_connect()
            db.execute('use e_commerce')
            sql = 'select confirm_time, phone, address, client_order, total_price from user_order ;'
            result = db.execute(sql)
            num = len(result)
            if num != temp:
                print 'new num', num, temp
                for i in range(num-temp):
                    self.num_flag += 1
                    self.tableWidget.insertRow(self.num_flag)
                    for j in range(len(result[0])):
                        mes = result[-i-1][j]
                        newItem = QtGui.QTableWidgetItem(u"%s" % mes)
                        self.tableWidget.setItem(self.num_flag, j, newItem)
                temp = num
            db.db_close()
            time.sleep(1)


    def all_order(self):
        pass
    def change_message(self):
        pass


