# -*- coding: utf-8 -*-
# @Time : 2024/6/22 10:53
# @Auth : xz_official
# @File : main.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import *  # 导入所有类


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
