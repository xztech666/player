# -*- coding: utf-8 -*-
# @Time : 2024/6/23 16:11
# @Auth : xz_official
# @File : 颜色对话框.py
# @IDE : PyCharm
"""
颜色对话框  QColorDialog
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPalette


class ColorDialog(QWidget):
    def __init__(self):
        super(ColorDialog, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("颜色对话框")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel("hello, Pyqt", self)

        # 创建按钮
        self.btn = QPushButton("单击调整字体颜色", self)

        # 将按钮的点击信号与show_color_dialog槽函数连接
        self.btn.clicked.connect(self.change_font_color)

        # 将布局添加到窗口中
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.btn)

        self.setLayout(self.v_layout)

    def change_font_color(self):
        color = QColorDialog.getColor()
        # 创建调色板
        palette = QPalette()
        # 设置调色板
        palette.setColor(QPalette.WindowText, color)
        # 设置标签的调色板
        self.label.setPalette(palette)


if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)
    # 创建窗口
    main_window = ColorDialog()
    # 显示窗口
    main_window.show()
    # 进入程序的主循环
    sys.exit(app.exec_())