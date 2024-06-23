# -*- coding: utf-8 -*-
# @Time : 2024/6/23 10:13
# @Auth : xz_official
# @File : 下拉列表控件.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel

"""
QComboBox
"""


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("按钮控件")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建label
        self.label = QLabel("你选择的编程语言是: Python", self)

        # 创建下拉列表控件
        self.combo_box = QComboBox(self)

        # 添加选项
        self.combo_box.addItem("Python")
        self.combo_box.addItem("Java")
        self.combo_box.addItem("C++")

        self.combo_box.currentIndexChanged.connect(self.combo_box_change)

        # 将控件添加到布局中
        self.v_layout.addWidget(self.combo_box)
        self.v_layout.addWidget(self.label)

        # 将布局添加到窗口中
        self.setLayout(self.v_layout)

    def combo_box_change(self):
        """
        下拉列表控件的currentIndexChanged信号
        :return:
        """
        text = self.combo_box.currentText()
        # 设置label的文本
        self.label.setText(f"你选择的编程语言是: {text}" )


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())