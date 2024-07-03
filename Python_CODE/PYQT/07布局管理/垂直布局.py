# -*- coding: utf-8 -*-
# @Time : 2024/7/2 22:26
# @Auth : xz_official
# @File : 垂直布局.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class VBoxDemo(QWidget):
    def __init__(self):
        super(VBoxDemo, self).__init__()
        self.v_layout = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("垂直布局")
        self.resize(300, 200)

        self.v_layout = QVBoxLayout()

        self.button1 = QPushButton("按钮1")
        self.button2 = QPushButton("按钮2")
        self.button3 = QPushButton("按钮3")

        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.button3)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxDemo()
    main.show()
    sys.exit(app.exec_())