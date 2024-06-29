# -*- coding: utf-8 -*-
# @Time : 2024/6/29 11:28
# @Auth : xz_official
# @File : 工具栏.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QTextEdit, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon


class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        # 创建工具栏
        self.setWindowTitle("工具栏")
        # 设置窗口大小
        self.resize(500, 500)

        # 设置工具栏
        self.file_toolbar = QToolBar("file", self)
        self.new = QAction(QIcon("./1.jpg"), "NEW", self)
        self.open = QAction(QIcon("./image.png"), "OPEN", self)

        # 添加到工具栏
        self.file_toolbar.addAction(self.new)
        self.file_toolbar.addAction(self.open)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBar()
    main.show()
    sys.exit(app.exec_())