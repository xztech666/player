# -*- coding: utf-8 -*-
# @Time : 2024/6/30 21:28
# @Auth : xz_official
# @File : 树控件的基本使用.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon


class TreeWidgetDemo(QWidget):
    def __init__(self):
        super(TreeWidgetDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("树控件的基本使用")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建垂直布局
        self.layout = QVBoxLayout()

        # 创建树控件
        self.tree = QTreeWidget()
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置列标题
        self.tree.setHeaderLabels(["key", "value"])
        # 设置列宽
        self.tree.setColumnWidth(0, 200)
        # 创建根节点
        self.root = QTreeWidgetItem(self.tree)
        # 设置根节点的文本
        self.root.setText(0, "根节点")
        self.root.setText(1, "这是根节点")
        self.root.setIcon(0, QIcon("./1.jpg"))

        # 添加子节点  设置父节点
        self.child1 = QTreeWidgetItem(self.root)
        self.child1.setText(0, "子节点1")
        self.child1.setText(1, "这是子节点1")
        self.child1.setIcon(0, QIcon("./1.jpg"))

        # 点击事件
        self.tree.clicked.connect(self.tree_clicked)

        # 添加布局
        self.layout.addWidget(self.tree)
        # 设置布局
        self.setLayout(self.layout)

    def tree_clicked(self, index):
        # print(index.row())
        item = self.tree.currentItem()
        print(item.text(0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeWidgetDemo()
    main.show()
    sys.exit(app.exec_())