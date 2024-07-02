# -*- coding: utf-8 -*-
# @Time : 2024/7/2 17:21
# @Auth : xz_official
# @File : 多任务_多线程.py
# @IDE : PyCharm
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QLCDNumber
from PyQt5.QtCore import QTimer, QDateTime, QThread, pyqtSignal


class WorkThread(QThread):
    def __init__(self):
        super(WorkThread, self).__init__()

    # 自定义信号
    signal = pyqtSignal()

    def run(self):
        while True:
            # print("子线程执行")
            time.sleep(1)
            # 发射信号
            self.signal.emit("子线程执行")


class TheadDemo(QWidget):
    # 创建一个变量
    second = 0

    def __init__(self):
        super(TheadDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("计时器")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建一个垂直布局
        self.v_layout = QVBoxLayout()

        # 创建一个线程
        self.thread = WorkThread()
        self.thread.signal.connect(self.showtime)

        # 创建一个显示时间的标签
        self.lcd = QLCDNumber(self)
        # 创建按钮
        self.start = QPushButton("开始")
        # 绑定一个槽函数
        self.start.clicked.connect(self.start_time)
        # 将控件添加到布局
        self.v_layout.addWidget(self.lcd)
        self.v_layout.addWidget(self.start)
        # 将布局添加到窗口中
        self.setLayout(self.v_layout)

    def start_time(self):
        self.thread.start()

    def showtime(self):
        self.second += 1
        self.lcd.display(self.second)


"""
    多线程
    1.创建一个线程
    2.创建一个信号
    3.将信号绑定到槽函数
    4.将线程启动
"""
"""
    多任务
    1.创建一个线程
    2.创建一个信号
    3.将信号绑定到槽函数
    4.将线程启动
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TheadDemo()
    main.show()
    sys.exit(app.exec_())