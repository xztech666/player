# -*- coding: utf-8 -*-
# @Time : 2024/6/29 11:39
# @Auth : xz_official
# @File : 列表控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QHBoxLayout


class ListWidget(QWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("列表控件")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建列表控件
        self.list = QListWidget(self)
        # 创建水平布局
        self.layout = QHBoxLayout()
        # 添加数据
        self.list.addItem("星期一")
        self.list.addItem("星期二")
        self.list.addItem("星期三")
        self.list.addItem("星期四")
        self.list.addItem("星期五")
        self.list.itemClicked.connect(self.show_info)
        # 添加布局
        self.layout.addWidget(self.list)
        # 设置布局
        self.setLayout(self.layout)
    def show_info(self, item):
        # 获取点击的item
        print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidget()
    main.show()
    sys.exit(app.exec_())