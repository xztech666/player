# -*- coding: utf-8 -*-
# @Time : 2024/6/22 11:01
# @Auth : xz_official
# @File : 创建窗口.py
# @IDE : PyCharm

"""
实现窗口的三个类:
QMainWindow: 包含菜单栏,工具栏,状态栏和标题栏
QDialog: 模态对话框,用户必须关闭对话框才能继续操作
QWidget: 无标题栏,没有菜单栏,没有工具栏,没有状态栏

"""
# 导入交互模块
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("主窗口")

        # 设置窗口大小
        self.resize(400, 300)

        # 获得状态栏
        self.statusBar().showMessage("这是状态栏", 2000)

        # 设置窗口图标
        self.setWindowIcon(QIcon("./1.jpg"))

        # 让窗口居中显示

        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        # 移动窗口
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建窗口
    mainWindow = MainWindow()
    # 显示窗口
    mainWindow.show()
    # 退出程序
    sys.exit(app.exec_())
