# -*- coding: utf-8 -*-
# @Time : 2024/6/22 22:38
# @Auth : xz_official
# @File : 复选按钮.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("复选按钮")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建一个水平布局
        layout = QHBoxLayout()

        # 创建一个复选框
        apple = QCheckBox("苹果")
        banana = QCheckBox("香蕉")

        # 绑定状态改变事件
        apple.stateChanged.connect(lambda: self.btn_state_change(apple))
        banana.stateChanged.connect(lambda: self.btn_state_change(banana))

        # 将复选框添加到布局中
        layout.addWidget(apple)
        layout.addWidget(banana)

        # 设置默认选中状态
        self.setLayout(layout)

    # 状态改变事件
    def btn_state_change(self, btn):
        if btn.isChecked():
            print(btn.text(), "选中")
        else:
            print(btn.text(), "未选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())