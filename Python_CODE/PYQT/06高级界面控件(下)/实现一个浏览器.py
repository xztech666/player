# -*- coding: utf-8 -*-
# @Time : 2024/7/2 21:54
# @Auth : xz_official
# @File : 实现一个浏览器.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class BrowserDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = None
        self.url_edit = None
        self.go_button = None
        self.back_button = None
        self.forward_button = None
        self.home_button = None
        self.refresh_button = None
        # 初始化UI
        self.init_ui()

    def init_ui(self):
        # 创建窗口标题
        self.setWindowTitle("自定义浏览器")
        # 设置窗口大小
        self.resize(900, 600)

        # 创建浏览器对象
        self.browser = QWebEngineView()
        # 加载默认网址
        self.browser.load(QUrl("https://google.com"))
        # 将浏览器对象设置为窗口中心
        self.setCentralWidget(self.browser)

        # 创建导航栏
        self.url_edit = QLineEdit()
        # 设置提示文本
        self.url_edit.setPlaceholderText("请输入网址")
        # 按下回车键时触发事件
        self.url_edit.returnPressed.connect(self.load_url)

        # 创建按钮
        self.go_button = QPushButton("Go")
        # 点击按钮时触发事件
        self.go_button.clicked.connect(self.load_url)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.browser.forward)

        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.load_home_page)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.browser.reload)

        # 创建导航栏布局  水平布局
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.refresh_button)
        nav_layout.addWidget(self.go_button)
        nav_layout.addWidget(self.home_button)

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.url_edit)
        layout.addLayout(nav_layout)
        layout.addWidget(self.browser)

        # 创建中心部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_url(self):
        url = self.url_edit.text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        try:
            qurl = QUrl(url)
            if qurl.isValid():
                self.browser.load(qurl)
                self.url_edit.setText(url)
            else:
                QMessageBox.warning(self, "错误", "无效的网址，请检查后重试。")
        except Exception as e:
            QMessageBox.critical(self, "加载错误", f"加载页面时发生错误: {str(e)}")

    def load_home_page(self):
        home_page = "https://google.com"  # 可以改为让用户自定义
        self.browser.load(QUrl(home_page))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BrowserDemo()
    main.show()
    sys.exit(app.exec_())