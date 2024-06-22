# -*- coding: utf-8 -*-
# @Time : 2024/6/22 15:31
# @Auth : xz_official
# @File : label的基本用法.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

"""
QLabel的基本用法
"""

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口的标题
        self.setWindowTitle('Label基本用法')
        # 设置窗口的尺寸
        self.resize(500, 500)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建label
        label = QLabel("uername")
        label2 = QLabel("<div style='color:red;'>password</div>")
        # 创建一个label，用来显示图片
        label3 = QLabel()
        # 设置label的提示信息
        label3.setToolTip("这个是一张图片!")
        # 设置label的图片
        label3.setPixmap(QPixmap("./1.jpg"))
        # 将label添加到布局中
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # 设置布局
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
