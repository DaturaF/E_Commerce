# -*- coding: utf-8 -*-
"""
电子商务系统信息修改界面
by: xf
2017.4.29
"""
# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\xiugai.ui'
#
# Created: Thu Apr 27 20:13:23 2017
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


class Ui_xiugai(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 286)
        self.form = Dialog
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 750, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels([u'商品名', u'商品id', u'商品描述', u'单价(元)', u'商品单位', u'图片路径'])
        for x in range(self.tableWidget.columnCount()):
            headItem = self.tableWidget.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setBackgroundColor(QColor(0, 60, 10))  # 设置单元格背景颜色
            headItem.setTextColor(QColor(200, 111, 30))  # 设置文字颜色
        # self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.set_table()
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(700, 10, 61, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 10, 68, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 10, 68, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 400, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 250, 71, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.baocun)
        self.pushButton_2.clicked.connect(self.fanhui)
        self.pushButton_3.clicked.connect(self.tianjia)
        self.pushButton_4.clicked.connect(self.shanchu)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "商品信息修改", None))
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.blue)
        self.label.setPalette(pe)
        self.label.setText(_translate("Dialog", "请在下表中进行编辑修改", None))
        self.pushButton.setText(_translate("Dialog", "保存", None))
        self.pushButton_3.setText(_translate("Dialog", "添加商品", None))
        self.pushButton_4.setText(_translate("Dialog", "删除商品", None))
        self.label_2.setText(_translate("Dialog", "提示信息", None))
        self.label_2.hide()
        self.pushButton_2.setText(_translate("Dialog", "返回主页", None))

    def set_table(self):
        print 'set table'
        db = DataBase()
        db.get_connect()
        db.execute('use e_commerce')
        sql = 'select commodity_name, commodity_id, commodity_describe, commodity_price, commodity_unit, commodity_image from commodity_list;'
        result = db.execute(sql)
        self.num_flag = 1
        if result:
            self.num_flag = len(result)-1
            while self.tableWidget.rowCount() < self.num_flag + 1:
                self.tableWidget.insertRow(1)
            for i in range(len(result)):
                for j in range(len(result[i])):
                    mes = result[i][j]
                    newItem = QtGui.QTableWidgetItem(u"%s" % mes)
                    self.tableWidget.setItem(i, j, newItem)
            db.db_close()
        else:
            for j in range(6):
                newItem = QtGui.QTableWidgetItem(u"")
                self.tableWidget.setItem(0, j, newItem)

    def tianjia(self):
        self.num_flag += 1
        self.tableWidget.insertRow(self.num_flag)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.darkGreen)
        self.label_2.setPalette(pe)
        self.label_2.setText(_translate("Dialog", "添加成功，完成全部更改时请点击‘保存’同步到数据库", None))
        self.label_2.show()

    def shanchu(self):
        num = self.tableWidget.currentRow()
        self.tableWidget.removeRow(num)
        self.num_flag -= 1
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.darkGreen)
        self.label_2.setPalette(pe)
        self.label_2.setText(_translate("Dialog", "删除成功，完成全部更改时请点击‘保存’同步到数据库", None))
        self.label_2.show()

    def fanhui(self):
        self.form.close()

    def baocun(self):
        flag = True
        print 'num', self.num_flag
        for i in range(self.num_flag):
            for j in range(6):
                # print self.tableWidget.item(i, j).text()
                if self.tableWidget.item(i, j).text() == '':
                    flag = False
                    break

        if not flag:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.red)
            self.label_2.setPalette(pe)
            self.label_2.setText(_translate("Dialog", "信息不完整，请检查修改后重试。", None))
            self.label_2.show()
        else:
            try:
                db = DataBase()
                db.get_connect()
                db.execute('use e_commerce')
                sql = 'truncate commodity_list;'
                db.execute(sql)
                # db.db_commit()

                for i in range(self.num_flag+1):
                    n_name = self.tableWidget.item(i, 0).text()
                    n_id = self.tableWidget.item(i, 1).text()
                    n_describe = self.tableWidget.item(i, 2).text()
                    n_price = self.tableWidget.item(i, 3).text()
                    n_unit = self.tableWidget.item(i, 4).text()
                    n_image = self.tableWidget.item(i, 5).text()
                    sql = 'insert into commodity_list (commodity_name, commodity_id, commodity_describe, commodity_price, commodity_unit, commodity_image) values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (n_name, n_id, n_describe, n_price, n_unit, n_image)
                    print sql
                    db = DataBase()
                    db.get_connect()
                    db.execute('use e_commerce')
                    db.execute(sql)
                    db.db_commit()
                db.db_close()
                pe = QPalette()
                pe.setColor(QPalette.WindowText, Qt.darkGreen)
                self.label_2.setPalette(pe)
                self.label_2.setText(_translate("Dialog", "保存成功", None))
                self.label_2.show()
            except:
                pe = QPalette()
                pe.setColor(QPalette.WindowText, Qt.red)
                self.label_2.setPalette(pe)
                self.label_2.setText(_translate("Dialog", "网络错误，请稍后重试。", None))
                self.label_2.show()

