# -*- coding: utf-8 -*-
# @Time : 2024/6/29 12:08
# @Auth : xz_official
# @File : 表格控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("表格控件")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建垂直布局
        self.layout = QVBoxLayout()
        """
        1. 创建表格控件
        2. 设置表格控件行数和列数
        3. 设置表头
        4. 添加数据
        """
        # 创建表格控件
        self.table = QTableWidget()
        # 设置表格控件行数和列数
        self.table.setRowCount(4)
        self.table.setColumnCount(3)
        # 设置表头
        self.table.setHorizontalHeaderLabels(["姓名", "性别", "年龄"])
        # 添加数据  使用字符串的形式
        name = QTableWidgetItem("xz_official")
        age = QTableWidgetItem("18")
        sex = QTableWidgetItem("男")
        self.table.setItem(0, 0, name)
        self.table.setItem(0, 1, sex)
        self.table.setItem(0, 2, age)

        name1 = QTableWidgetItem("xz_official1")
        age1 = QTableWidgetItem("20")
        sex1 = QTableWidgetItem("男")
        self.table.setItem(1, 0, name1)
        self.table.setItem(1, 1, sex1)
        self.table.setItem(1, 2, age1)

        # 添加布局
        self.layout.addWidget(self.table)
        # 设置布局
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Table()
    main.show()
    sys.exit(app.exec_())