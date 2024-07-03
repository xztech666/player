# -*- coding: utf-8 -*-
# @Time : 2024/7/3 8:22
# @Auth : xz_official
# @File : 堆栈布局.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('堆栈布局')
        # 设置窗口尺寸
        self.resize(300, 200)
        # 创建水平布局
        hbox = QHBoxLayout()

        # 创建垂直布局
        vbox = QVBoxLayout()
        for i in range(1, 5):
            button = QPushButton('Button' + str(i))
            vbox.addWidget(button)
            vbox.addStretch()
            hbox.addLayout(vbox)

        # 设置窗口布局
        self.setLayout(hbox)
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())