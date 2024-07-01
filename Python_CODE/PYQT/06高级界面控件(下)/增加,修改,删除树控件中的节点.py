# -*- coding: utf-8 -*-
# @Time : 2024/7/1 19:43
# @Auth : xz_official
# @File : 增加,修改,删除树控件中的节点.py
# @IDE : PyCharm
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton


class TreeWidgetDemo(QWidget):
    def __init__(self):
        super(TreeWidgetDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("增加,修改,删除树控件中的节点")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建水平布局
        self.h_layout = QHBoxLayout()

        # 创建按钮
        self.add_btn = QPushButton("增加节点")
        self.update_btn = QPushButton("修改节点")
        self.delete_btn = QPushButton("删除节点")

        # 将按钮添加到水平布局中
        self.h_layout.addWidget(self.add_btn)
        self.h_layout.addWidget(self.update_btn)
        self.h_layout.addWidget(self.delete_btn)

        # 绑定按钮点击事件
        self.add_btn.clicked.connect(self.add_node)
        self.update_btn.clicked.connect(self.update_node)
        self.delete_btn.clicked.connect(self.delete_node)

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

        # 往垂直布局里面添加水平布局
        self.v_layout.addLayout(self.h_layout)
        # 往垂直布局里面添加树控件
        self.v_layout.addWidget(self.tree)

        # 设置窗口布局
        self.setLayout(self.v_layout)

    def add_node(self):
        # 获取当前选中的节点
        item = self.tree.currentItem()
        # 创建节点  继承父节点
        node = QTreeWidgetItem(item)
        node.setText(0, "新节点")
        node.setText(1, "这是新节点")

    def update_node(self):
        # 获取当前选中的节点
        item = self.tree.currentItem()
        item.setText(0, "修改节点")

    def delete_node(self):
        # 获取当前选中的节点
        item = self.tree.currentItem()
        # 获取根节点的父节点  不可见的
        root = self.tree.invisibleRootItem()
        if item.parent():
            # 删除节点 父节点删除子节点
            item.parent().removeChild(item)
        else:
            root.removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeWidgetDemo()
    main.show()
    sys.exit(app.exec_())