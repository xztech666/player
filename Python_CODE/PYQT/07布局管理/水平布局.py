# -*- coding: utf-8 -*-
# @Time : 2024/7/2 22:20
# @Auth : xz_official
# @File : 水平布局.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class HBoxDemo(QWidget):
    def __init__(self):
        super(HBoxDemo, self).__init__()
        self.h_layout = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("水平布局")
        self.resize(300, 200)
        self.h_layout = QHBoxLayout()
        self.button1 = QPushButton("按钮1")
        self.button2 = QPushButton("按钮2")
        self.button3 = QPushButton("按钮3")
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.h_layout.addWidget(self.button3)
        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxDemo()
    main.show()
    sys.exit(app.exec_())