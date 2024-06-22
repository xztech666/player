# -*- coding: utf-8 -*-
# @Time : 2024/6/21 21:46
# @Auth : xz_official
# @File : pyqt.py
# @IDE : PyCharm

"""

gui: 图形化界面
适合用来开发的语言:
c#
c++
java
python

pyqt5

qt是一个C++的图形库

使用 pyuic5.exe 将ui文件转换为py文件

pyuic5 -o login.py login.ui
"""

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello World")
widget.show()
sys.exit(app.exec_())