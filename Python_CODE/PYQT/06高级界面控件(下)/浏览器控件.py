# -*- coding: utf-8 -*-
# @Time : 2024/7/2 17:42
# @Auth : xz_official
# @File : 浏览器控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, \
    QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class BrowserDemo(QMainWindow):
    def __init__(self):
        super(BrowserDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("浏览器控件")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建一个浏览器
        self.browser = QWebEngineView()
        # 加载网页
        self.browser.load(QUrl("https://xzkcnb.link"))

        # 将浏览器控件添加到窗口中
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BrowserDemo()
    main.show()
    sys.exit(app.exec_())