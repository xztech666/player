# -*- coding: utf-8 -*-
# @Time : 2024/7/2 22:35
# @Auth : xz_official
# @File : 表单布局.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QLabel


class FormLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()  # 使用super()的简化形式
        self.v_layout = None
        self.user_line_edit = None
        self.password_line_edit = None
        self.btn = None
        self.label = None
        self.label2 = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("表单布局")
        self.resize(500, 500)

        # 分别为用户名和密码创建QLineEdit实例
        self.user_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.btn = QPushButton("提交")
        self.label = QLabel("hello, Pyqt")
        self.label2 = QLabel("啥都没有!!!")

        form_layout = QFormLayout(self)  # 直接在构造函数中传入self可以省略setLayout步骤
        form_layout.addRow("用户名", self.user_line_edit)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        form_layout.addRow("密码", self.password_line_edit)  # 使用单独的密码行编辑器
        form_layout.addRow(self.btn, self.label)
        form_layout.addRow(self.label2)

        self.btn.clicked.connect(self.show_text)

    def show_text(self):
        # 显示用户名输入框的内容，并清空输入框
        user_text = self.user_line_edit.text()
        self.label.setText(user_text)
        self.label2.setText("密码输入框的内容是: " + self.password_line_edit.text())
        self.user_line_edit.clear()  # 清空用户名输入框
        self.password_line_edit.clear()  # 若需要，也可以清空密码输入框


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormLayoutDemo()
    main.show()
    sys.exit(app.exec_())
