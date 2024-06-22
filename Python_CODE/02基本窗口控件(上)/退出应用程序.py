# -*- coding: utf-8 -*-
# @Time : 2024/6/22 12:35
# @Auth : xz_official
# @File : 退出应用程序.py
# @IDE : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # super()函数用于调用父类(超类)的一个方法。
        super(MainWindow, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle("退出应用程序")
        # 设置窗口大小
        self.resize(400, 300)
        # 创建一个按钮
        self.button = QPushButton("退出应用程序", self)
        """
        槽: 事件函数
        """
        def quit_app(self):
            # 获取应用程序实例
            app = QApplication.instance()
            # 退出应用程序
            app.quit()
        # 将槽函数绑定到按钮的点击事件上
        self.button.clicked.connect(quit_app)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = MainWindow()
    # 显示窗口
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())