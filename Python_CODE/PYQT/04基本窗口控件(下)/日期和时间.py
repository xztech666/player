# -*- coding: utf-8 -*-
# @Time : 2024/6/29 10:38
# @Auth : xz_official
# @File : 日期和时间.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit
from PyQt5.QtCore import QDate, QTime, QDateTime


class DateAndTime(QWidget):
    def __init__(self):
        super(DateAndTime, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("日期和时间")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建垂直布局
        vbox_layout = QVBoxLayout()
        # 创建日期和时间编辑控件
        self.dateEdit = QDateTimeEdit(self)
        self.dateEdit1 = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置日期格式
        self.dateEdit1.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # 设置日历弹出
        self.dateEdit1.setCalendarPopup(True)
        # 将控件添加到布局
        vbox_layout.addWidget(self.dateEdit)
        vbox_layout.addWidget(self.dateEdit1)

        # 设置布局
        self.setLayout(vbox_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateAndTime()
    main.show()
    sys.exit(app.exec_())