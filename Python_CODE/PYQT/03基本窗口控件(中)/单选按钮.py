# -*- coding: utf-8 -*-
# @Time : 2024/6/22 21:45
# @Auth : xz_official
# @File : 单选按钮.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("按钮控件")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建一个单选按钮
        man = QRadioButton("男")
        woman = QRadioButton("女")

        # 设置单选按钮的选中状态变化时触发的函数
        man.toggled.connect(lambda: self.btn_state_change(man))
        woman.toggled.connect(lambda: self.btn_state_change(woman))

        # 创建一个水平布局
        h_layout = QHBoxLayout()

        # 将单选按钮添加到水平布局中
        h_layout.addWidget(man)
        h_layout.addWidget(woman)

        # 设置水平布局为窗口的布局
        self.setLayout(h_layout)

    def btn_state_change(self, btn):
        """
            监听按钮状态变化事件。

            当按钮的状态发生变化（被选中或取消选中）时，此函数将被调用。它根据按钮的当前状态打印出相应的信息。

            参数:
            btn - QCheckBox 或具有 isChecked 方法的类似对象。这个参数代表了按钮对象本身。
        """
        if btn.isChecked():
            print(btn.text() + "按钮被选中")
        else:
            print(btn.text() + "按钮未被选中")


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())