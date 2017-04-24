#!/usr/bin/python
# encoding:utf-8

"""
电子商务系统商家客户端入口
by: xf
2017.4.21
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from p1 import P1


import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Start_Up:
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.Form = QtGui.QWidget()
        self.window = P1()
        self. window.setupUi(self.Form)
        self.Form.show()
        sys.exit(self.app.exec_())


st = Start_Up()