# -*- coding: utf-8 -*-
# @Time : 2024/6/23 10:34
# @Auth : xz_official
# @File : 滑块控件.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


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
        self.label = QLabel("hello, Pyqt", self)

        # 创建水平方向滑块
        self.slider = QSlider(Qt.Horizontal, self)

        self.slider.valueChanged.connect(self.slider_change)

        # 设置最大值和最小值
        self.slider.setMaximum(100)
        self.slider.setMinimum(1)

        # 设置步长
        self.slider.setSingleStep(1)

        # 设置刻度位置在滑块下方
        self.slider.setTickPosition(QSlider.TicksBelow)

        # 设置刻度间隔
        self.slider.setTickInterval(1)

        # 将滑块和label添加到垂直布局中
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.slider)

        # 设置垂直布局
        self.setLayout(self.v_layout)

    def slider_change(self):
        # 获取滑块的值
        value = self.slider.value()
        # 设置字体大小
        self.label.setFont(QFont("微软雅黑", value))
        # 将滑块的值显示在label中
        self.label.setText("当前值: {}".format(value))


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())