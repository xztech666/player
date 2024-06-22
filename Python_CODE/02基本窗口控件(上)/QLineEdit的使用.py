# -*- coding: utf-8 -*-
# @Time : 2024/6/22 16:02
# @Auth : xz_official
# @File : QLineEdit的使用.py
# @IDE : PyCharm

"""
QLineEdit:
单行文本输入框

QLineEdit的基本用法
1.QLineEdit的基本用法
2.QLineEdit的信号与槽


显示模式
1.QLineEdit.Normal
    显示模式为普通模式，用户可以输入文本，也可以选中文本，但不能修改文本。
2.QLineEdit.ReadOnly
    显示模式为只读模式，用户可以选中文本，但不能修改文本。
3.QLineEdit.Password
    显示模式为密码模式，用户可以输入文本，但不能看到输入的文本。
4.QLineEdit.PasswordEchoOnEdit
    显示模式为密码模式，用户可以输入文本，但看到输入的文本。
5.QLineEdit.NoEcho
    显示模式为不显示模式，用户不能输入文本，也不能看到输入的文本。


"""
import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口的标题
        self.setWindowTitle("QLineEdit的基本用法")
        # 设置窗口的尺寸
        self.resize(500, 500)

        # 创建表单布局
        form = QFormLayout()
        # 创建一个单行文本输入框
        line1 = QLineEdit()
        line2 = QLineEdit()
        line3 = QLineEdit()
        line4 = QLineEdit()
        # 设置显示模式
        line1.setEchoMode(QLineEdit.Normal)
        line2.setEchoMode(QLineEdit.Password)
        line3.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        line4.setEchoMode(QLineEdit.NoEcho)
        # 将单行文本输入框添加到表单布局中
        form.addRow("username", line1)
        form.addRow("password", line2)
        form.addRow("PasswordEchoOnEdit", line3)
        form.addRow("NoEcho", line4)

        """
            限制内容的输入
        """
        line5 = QLineEdit()
        # 创建一个整形验证器
        int_validator = QIntValidator()
        # 设置范围
        int_validator.setRange(1, 99)
        # 设置验证器
        line5.setValidator(int_validator)
        form.addRow("整数", line5)

        """
            限制内容的输入
        """
        line6 = QLineEdit()
        # 创建一个浮点数验证器
        double_validator = QDoubleValidator()
        # 设置范围
        double_validator.setRange(1, 99, 2)
        # 设置小数位数
        # double_validator.setDecimals(2)

        # 设置浮点数的表示方式为标准表示法
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        # 设置验证器
        line6.setValidator(double_validator)
        form.addRow("浮点数", line6)

        """
            限制内容的输入
        """
        # 只能输入数字和字母
        line7 = QLineEdit()
        # 创建一个正则表达式验证器
        reg = QRegExp("[a-zA-Z0-9]+$")
        # 创建一个正则表达式验证器
        reg_validator = QRegExpValidator()
        # 设置正则表达式
        reg_validator.setRegExp(reg)
        # 设置验证器
        line7.setValidator(reg_validator)
        form.addRow("正则表达式", line7)

        """
            格式限制
        """
        line8 = QLineEdit()
        line8.setInputMask("0000-00-00")
        form.addRow("日期", line8)

        # 将表单布局设置为窗口的主布局
        self.setLayout(form)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())