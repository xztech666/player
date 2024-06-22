# -*- coding: utf-8 -*-
# @Time : 2024/6/22 17:12
# @Auth : xz_official
# @File : QTextEdit的使用.py
# @IDE : PyCharm
"""
QTextEdit
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口标题
        self.setWindowTitle('QTextEdit')
        # 设置窗口的尺寸
        self.resize(400, 400)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建一个文本编辑器
        self.text = QTextEdit()
        # 创建按钮
        button_text = QPushButton('获取文本')
        button_html = QPushButton('获取HTML')
        # 为按钮绑定槽函数
        button_text.clicked.connect(self.show_text)
        button_html.clicked.connect(self.show_html)

        layout.addWidget(self.text)
        layout.addWidget(button_text)
        layout.addWidget(button_html)

        self.setLayout(layout)

    """
        定义一个槽函数，用于获取文本编辑器的文本内容
    """
    def show_text(self):
        self.text.setPlainText('文本编辑器中的文本内容')

    def show_html(self):
        self.text.setHtml('<font color="red">文本编辑器中的HTML内容</font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())