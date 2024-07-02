# -*- coding: utf-8 -*-
# @Time : 2024/7/1 21:59
# @Auth : xz_official
# @File : 多任务_定时器.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import QTimer,QDateTime


class TimerDemo(QWidget):
    def __init__(self):
        super(TimerDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("多任务_定时器")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建一个定时器
        self.timer = QTimer(self)
        # 设置定时器时间间隔
        self.timer.timeout.connect(self.showtime)

        # 创建标签
        self.label = QLabel("显示当前时间")
        # 创建按钮
        self.start = QPushButton("开始")
        self.start.clicked.connect(self.start_time)
        self.end = QPushButton("结束")
        self.end.clicked.connect(self.end_time)

        # 创建栅格布局
        self.grid_layout = QGridLayout()
        # 添加控件到栅格布局
        """
        self.label: 这是要添加到布局的控件对象。在这个例子中，self.label 是一个QLabel对象。
        0: 这是行索引，表示控件将在布局的第一行开始放置。
        0: 这是列索引，表示控件将在布局的第一列开始放置。
        1: 这是rowspan，表示控件将跨过的行数。在这个例子中，控件只占据一行。
        2: 这是columnspan，表示控件将跨过的列数。在这里，控件会占据两列。
        """
        self.grid_layout.addWidget(self.label, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.start, 1, 0)
        self.grid_layout.addWidget(self.end, 1, 1)

        # 设置窗口布局
        self.setLayout(self.grid_layout)

    def showtime(self):
        # 获取当前时间
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        # 将当前时间显示到标签上
        self.label.setText(current_time)

    def start_time(self):
        # 启动定时器  1000ms
        self.timer.start(1000)
        # 禁用按钮
        self.start.setEnabled(False)
        # 启用按钮
        self.end.setEnabled(True)

    def end_time(self):
        # 停止定时器
        self.timer.stop()
        # 禁用按钮
        self.end.setEnabled(False)
        # 启用按钮
        self.start.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TimerDemo()
    main.show()
    sys.exit(app.exec_())