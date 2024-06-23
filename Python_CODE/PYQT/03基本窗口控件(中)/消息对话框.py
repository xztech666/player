# -*- coding: utf-8 -*-
# @Time : 2024/6/23 15:26
# @Auth : xz_official
# @File : 消息对话框.py
# @IDE : PyCharm
"""
对话框分类
    1. 消息对话框
        1.关于对话框
        2.错误对话框
        3.警告对话框
        4.提问对话框
        5.消息对话框
    2.颜色对话框
    3.文件对话框
    4.字体对话框
    5.输入对话框
    
    
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


class MessageBox(QWidget):
    def __init__(self):
        super(MessageBox, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("消息对话框")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建按钮
        self.btn_about = QPushButton("关于对话框")
        self.btn_error = QPushButton("错误对话框")
        self.btn_warning = QPushButton("警告对话框")
        self.btn_question = QPushButton("提问对话框")
        self.btn_message = QPushButton("消息对话框")

        # 信号与槽连接
        self.btn_about.clicked.connect(self.show_about_dialog)
        self.btn_error.clicked.connect(self.show_error_dialog)
        self.btn_warning.clicked.connect(self.show_warning_dialog)
        self.btn_question.clicked.connect(self.show_question_dialog)
        self.btn_message.clicked.connect(self.show_message_dialog)

        # 添加按钮
        self.v_layout.addWidget(self.btn_about)
        self.v_layout.addWidget(self.btn_error)
        self.v_layout.addWidget(self.btn_warning)
        self.v_layout.addWidget(self.btn_question)
        self.v_layout.addWidget(self.btn_message)

        # 设置布局
        self.setLayout(self.v_layout)

    def show_about_dialog(self):
        QMessageBox.about(self, "关于对话框", "这是一个关于对话框")

    def show_error_dialog(self):
        QMessageBox.critical(self, "错误对话框", "这是一个错误对话框")

    def show_warning_dialog(self):
        QMessageBox.warning(self, "警告对话框", "这是一个警告对话框")

    def show_question_dialog(self):
        rv = QMessageBox.question(self, "提问对话框", "这是一个提问对话框")
        if QMessageBox.Yes == rv:
            print("点击了Yes")
        else:
            print("点击了No")

    def show_message_dialog(self):
        QMessageBox.information(self, "消息对话框", "这是一个消息对话框")
        print("点击了确定")


"""
关于对话框
    QMessageBox.about(self, title, text)
    self: 窗口对象
    title: 窗口标题
    text: 窗口内容
    
错误对话框
    QMessageBox.critical(self, title, text)
    self: 窗口对象
    title: 窗口标题
    text: 窗口内容
    
警告对话框
    QMessageBox.warning(self, title, text)
    self: 窗口对象
    title: 窗口标题
    text: 窗口内容
    
提问对话框
    QMessageBox.question(self, title, text)
    self: 窗口对象
    title: 窗口标题
    text: 窗口内容
    
消息对话框
    QMessageBox.information(self, title, text)
    self: 窗口对象
    title: 窗口标题
    text: 窗口内容
"""

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = MessageBox()
    # 显示窗口
    main_window.show()
    # 运行应用程序
    sys.exit(app.exec_())