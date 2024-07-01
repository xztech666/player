# -*- coding: utf-8 -*-
# @Time : 2024/6/29 16:38
# @Auth : xz_official
# @File : 单元格设置.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("单元格设置")
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
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        # 设置表头
        self.table.setHorizontalHeaderLabels(["姓名", "性别", "年龄"])
        # 添加数据  使用字符串的形式
        name = QTableWidgetItem("xz_official")
        age = QTableWidgetItem("18")
        sex = QTableWidgetItem("男")
        self.table.setItem(0, 0, name)
        self.table.setItem(0, 1, age)
        self.table.setItem(0, 2, sex)

        name1 = QTableWidgetItem("xz_official1")
        age1 = QTableWidgetItem("20")
        sex1 = QTableWidgetItem("男")
        self.table.setItem(1, 0, name1)
        self.table.setItem(1, 1, age1)
        self.table.setItem(1, 2, sex1)

        # 添加数据
        self.table.setItem(2, 0, QTableWidgetItem("xz_official2"))
        self.table.setItem(2, 1, QTableWidgetItem("18"))
        self.table.setItem(2, 2, QTableWidgetItem("男"))

        # 创建下拉列表
        self.bbox = QComboBox()
        self.bbox.addItems(["男", "女"])
        # 设置单元格
        self.table.setCellWidget(2, 2, self.bbox)

        # 添加数据, 设置字体类型和颜色
        name2 = QTableWidgetItem("xz_official3")
        name2.setFont(QFont("微软雅黑", 10))
        name2.setForeground(Qt.red)
        name2.setBackground(Qt.green)
        age2 = QTableWidgetItem("20")
        sex2 = QTableWidgetItem("男")
        self.table.setItem(3, 0, name2)
        self.table.setItem(3, 1, age2)
        self.table.setItem(3, 2, sex2)

        # 添加数据, 设置文本对齐方式
        name3 = QTableWidgetItem("xz_official4")
        name3.setTextAlignment(Qt.AlignCenter)
        age3 = QTableWidgetItem("20")
        age3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        sex3 = QTableWidgetItem("男")
        self.table.setItem(4, 0, name3)
        self.table.setItem(4, 1, age3)
        self.table.setItem(4, 2, sex3)

        # 添加数据, 设置单元格合并
        name4 = QTableWidgetItem("xz_official5")
        age4 = QTableWidgetItem("20")
        sex4 = QTableWidgetItem("男")
        # 合并单元格   5行0列合并2行1列
        self.table.setSpan(5, 0, 2, 1)
        self.table.setItem(5, 0, name4)
        self.table.setSpan(5, 1, 2, 1)
        self.table.setItem(5, 1, age4)
        self.table.setSpan(5, 2, 2, 1)
        self.table.setItem(5, 2, sex4)

        # 添加数据, 设置单元格只读
        name5 = QTableWidgetItem("xz_official6")
        name5.setFlags(Qt.ItemIsEnabled)
        age5 = QTableWidgetItem("20")
        age5.setFlags(Qt.ItemIsEnabled)
        sex5 = QTableWidgetItem("男")
        sex5.setFlags(Qt.ItemIsEnabled)
        self.table.setItem(7, 0, name5)
        self.table.setItem(7, 1, age5)
        self.table.setItem(7, 2, sex5)

        # 添加数据, 设置图文混排
        name6 = QTableWidgetItem(QIcon("./1.jpg"), "xz_official7")
        age6 = QTableWidgetItem("20")
        sex6 = QTableWidgetItem("男")
        self.table.setItem(8, 0, name6)
        self.table.setItem(8, 1, age6)
        self.table.setItem(8, 2, sex6)

        # 添加布局
        self.layout.addWidget(self.table)
        # 设置窗口布局
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Table()
    main.show()
    sys.exit(app.exec_())