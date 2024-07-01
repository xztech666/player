# -*- coding: utf-8 -*-
# @Time : 2024/7/1 21:59
# @Auth : xz_official
# @File : 多任务_定时器.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit


class TimerDemo(QWidget):
    def __init__(self):
        super(TimerDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("多任务_定时器")
        # 设置窗口大小
        self.resize(500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TimerDemo()
    main.show()
    sys.exit(app.exec_())