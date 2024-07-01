# -*- coding: utf-8 -*-
# @Time : 2024/6/29 15:44
# @Auth : xz_official
# @File : 表格控件plus.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("表格控件plus")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建垂直布局
        self.layout = QVBoxLayout()

        # 数据列表
        students = [
            {"name": "张三", "age": 18, "sex": "man"},
            {"name": "李四", "age": 19, "sex": "woman"},
            {"name": "王五", "age": 20, "sex": "man"},
            {"name": "赵六", "age": 21, "sex": "woman"},
            {"name": "孙七", "age": 22, "sex": "man"},
            {"name": "周八", "age": 23, "sex": "woman"},
            {"name": "吴九", "age": 24, "sex": "man"},
            {"name": "郑十", "age": 25, "sex": "woman"},
        ]

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(students))
        self.table.setColumnCount(len(students[0]))

        # 设置表头
        headers = list(students[0].keys())
        self.table.setHorizontalHeaderLabels(headers)

        # 填充数据  key
        for i, student in enumerate(students):
            for j, key in enumerate(headers):
                item = QTableWidgetItem(str(student[key]))
                self.table.setItem(i, j, item)
        """
        遍历学生列表：
        for i, student in enumerate(students):
        这行代码使用enumerate函数遍历学生列表students，同时获取每个学生的索引i和学生数据student。students是一个包含多个学生信息的列表，每个学生的信息可以是一个字典。
        
        遍历表头：
        for j, key in enumerate(headers):
        这行代码使用enumerate函数遍历表头headers，同时获取每个表头的索引j和表头名称key。headers是一个包含表格列标题的列表。
        
        获取学生数据并创建表格项：
        item = QTableWidgetItem(str(student[key]))
        这行代码通过key从学生数据student中获取对应的值，并将其转换为字符串(必须使用字符串的形式!!)，然后创建一个QTableWidgetItem对象。QTableWidgetItem是Qt中的一个类，用于表示表格中的一个单元格。
        
        设置表格项：
        self.table.setItem(i, j, item)
        这行代码将创建的QTableWidgetItem对象放置在表格控件self.table的第i行，第j列的位置。

        结合起来，这段代码的作用是：
        对于每个学生student，它遍历所有的表头headers。
        对于每个表头key，它从学生信息中提取相应的值，创建一个表格项（单元格）。
        然后将这个单元格放置在表格中的适当位置。
        """

        # 添加布局
        self.layout.addWidget(self.table)
        # 设置窗口布局
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Table()
    main.show()
    sys.exit(app.exec_())