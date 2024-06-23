# -*- coding: utf-8 -*-
# @Time : 2024/6/22 21:00
# @Auth : xz_official
# @File : 按钮控件.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("按钮控件")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建按钮
        button1 = QPushButton("按钮1", self)
        button2 = QPushButton("按钮2", self)
        button3 = QPushButton(self)

        # 设置按钮选中状态
        button1.setCheckable(True)

        # 设置按钮是否可用
        button2.setEnabled(False)

        button3.setIcon(QIcon("1.jpg"))

        # 切换按钮选中状态
        button1.toggle()

        # 将按钮添加到布局中
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # 设置布局
        self.setLayout(layout)


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())
