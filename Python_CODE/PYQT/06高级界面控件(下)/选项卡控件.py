# -*- coding: utf-8 -*-
# @Time : 2024/7/1 20:16
# @Auth : xz_official
# @File : 选项卡控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit


class TabWidgetDemo(QTabWidget):
    def __init__(self):
        super(TabWidgetDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("树控件的基本使用")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建三个窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # 添加选项卡
        self.addTab(self.tab1, "选项卡1")
        self.addTab(self.tab2, "选项卡2")
        self.addTab(self.tab3, "选项卡3")

        # 调用方法
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

    def tab1_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名1: ", QLineEdit())
        form_layout.addRow("密码1: ", QLineEdit())

        self.tab1.setLayout(form_layout)

    def tab2_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名2: ", QLineEdit())
        form_layout.addRow("密码2: ", QLineEdit())
        # 设置布局
        self.tab2.setLayout(form_layout)

    def tab3_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名3: ", QLineEdit())
        form_layout.addRow("密码3: ", QLineEdit())
        # 设置布局
        self.tab3.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabWidgetDemo()
    main.show()
    sys.exit(app.exec_())