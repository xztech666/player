# -*- coding: utf-8 -*-
# @Time : 2024/7/3 10:05
# @Auth : xz_official
# @File : 布局嵌套.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.v_layout = None
        self.h_layout = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('布局嵌套')
        self.resize(500, 500)

        # 创建按钮
        self.button1 = QPushButton('按钮1')
        self.button2 = QPushButton('按钮2')
        self.button3 = QPushButton('按钮3')

        # 创建垂直布局
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.button3)

        # 创建水平布局
        self.h_layout = QHBoxLayout()
        self.h_layout.addLayout(self.v_layout)

        # 设置窗口布局
        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())