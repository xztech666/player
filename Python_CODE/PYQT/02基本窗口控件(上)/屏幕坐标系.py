# -*- coding: utf-8 -*-
# @Time : 2024/6/22 12:46
# @Auth : xz_official
# @File : 屏幕坐标系.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        # 继承QWidget
        super(MainWindow, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle('屏幕坐标系')
        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口位置
        self.move(300, 300)

        # 获取窗口坐标
        print("x:", self.x(), "y:", self.y())
        print("width: ", self.width(), "height: ", self.height())

        # 第二种获取方式
        print("x:", self.geometry().x(), "y:", self.geometry().y())
        print("width: ", self.geometry().width(), "height: ", self.geometry().height())


if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)
    # 创建窗口对象
    mainWindow = MainWindow()
    # 显示窗口
    mainWindow.show()
    # 退出程序
    sys.exit(app.exec_())
