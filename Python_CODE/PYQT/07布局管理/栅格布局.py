# -*- coding: utf-8 -*-
# @Time : 2024/7/2 22:30
# @Auth : xz_official
# @File : 栅格布局.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class GridLayoutDemo(QWidget):
    def __init__(self):
        super(GridLayoutDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle("栅格布局")
        self.resize(300, 200)
        # 创建栅格布局
        grid_layout = QGridLayout()
        # 设置间距
        grid_layout.setSpacing(10)
        grid_layout.addWidget(QPushButton("按钮1"), 0, 0)
        grid_layout.addWidget(QPushButton("按钮2"), 0, 1)
        grid_layout.addWidget(QPushButton("按钮3"), 1, 0)
        grid_layout.addWidget(QPushButton("按钮4"), 1, 1)
        grid_layout.addWidget(QPushButton("按钮5"), 2, 0)
        grid_layout.addWidget(QPushButton("按钮6"), 2, 1)

        self.setLayout(grid_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GridLayoutDemo()
    main.show()
    sys.exit(app.exec_())