# -*- coding: utf-8 -*-
# @Time : 2024/6/23 11:40
# @Auth : xz_official
# @File : 计数器控件.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("按钮控件")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建计数器控件
        self.spin_box = QSpinBox(self)

        # 绑定计数器控件的valueChanged信号到on_value_changed槽函数
        self.spin_box.valueChanged.connect(self.on_value_changed)

        # 创建标签控件
        self.label = QLabel("当前值是: ", self)

        # 将计数器控件添加到布局中
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.spin_box)

        # 设置布局
        self.setLayout(self.v_layout)

    def on_value_changed(self, value):
        # 获取当前值
        current_value = self.spin_box.value()
        # 将当前值显示在标签控件中
        self.label.setText("当前值是: " + str(current_value))


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())