# -*- coding: utf-8 -*-
# @Time : 2024/6/28 21:24
# @Auth : xz_official
# @File : 日历控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
from PyQt5.QtCore import QDate


class Calendar(QWidget):
    def __init__(self):
        super(Calendar, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("日历控件")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建日历控件
        self.calendar = QCalendarWidget(self)
        # 设置最小日期
        self.calendar.setMinimumDate(QDate(2024, 6, 1))
        # 设置最大日期
        self.calendar.setMaximumDate(QDate(2024, 6, 30))
        # 设置位置
        self.calendar.move(50, 50)
        # 显示网格
        self.calendar.setGridVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calendar()
    main.show()
    sys.exit(app.exec_())