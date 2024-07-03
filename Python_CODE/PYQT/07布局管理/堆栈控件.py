# -*- coding: utf-8 -*-
# @Time : 2024/7/3 9:57
# @Auth : xz_official
# @File : 堆栈控件.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget, QListWidget, \
    QFormLayout, QLineEdit


class StackedWidgetDemo(QWidget):
    def __init__(self):
        super(StackedWidgetDemo, self).__init__()
        # 创建窗口标题
        self.setWindowTitle("堆栈控件")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建列表
        self.list_widget = QListWidget()
        self.list_widget.currentRowChanged.connect(self.display)
        # 添加列表项
        self.list_widget.insertItem(0, "联系方式")
        self.list_widget.insertItem(1, "个人信息")
        self.list_widget.insertItem(2, "教育程度")

        # 创建堆栈控件
        self.stacked_widget = QStackedWidget()

        """
        QStackedWidget
            QStackedWidget是Qt中一个特殊的容器控件，它可以容纳多个子控件，
            但是只会显示其中的一个子控件，并且只能显示一个子控件。
            QStackedWidget的子控件必须添加到QStackedWidget中，
            否则QStackedWidget将不会显示它。
            QStackedWidget的子控件可以通过setCurrentIndex()方法来显示，
            也可以通过setCurrentWidget()方法来显示。
            setCurrentIndex()方法接收一个整数参数，表示要显示的子控件的索引，
            setCurrentWidget()方法接收一个QWidget对象作为参数，表示要显示的子控件。
            QStackedWidget的子控件可以通过addWidget()方法来添加，
            也可以通过insertWidget()方法来添加，
            addWidget()方法接收一个QWidget对象作为参数，
        """

        # 创建三个子窗口
        self.w1 = QWidget()
        self.w2 = QWidget()
        self.w3 = QWidget()
        # 将子窗口添加到堆栈控件中
        self.stacked_widget.addWidget(self.w1)
        self.stacked_widget.addWidget(self.w2)
        self.stacked_widget.addWidget(self.w3)
        # 创建三个子窗口
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

        # 创建一个水平布局
        self.h_layout = QHBoxLayout()
        # 将水平布局添加到窗口中
        self.h_layout.addWidget(self.list_widget)
        self.h_layout.addWidget(self.stacked_widget)
        # 将水平布局添加到窗口中
        self.setLayout(self.h_layout)

    def tab1_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名1: ", QLineEdit())
        form_layout.addRow("密码1: ", QLineEdit())
        # 设置布局
        self.w1.setLayout(form_layout)

    def tab2_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名2: ", QLineEdit())
        form_layout.addRow("密码2: ", QLineEdit())
        # 设置布局
        self.w2.setLayout(form_layout)

    def tab3_ui(self):
        # 创建一个表单布局
        form_layout = QFormLayout()
        # 添加表单项
        form_layout.addRow("姓名3: ", QLineEdit())
        form_layout.addRow("密码3: ", QLineEdit())
        # 设置布局
        self.w3.setLayout(form_layout)

    def display(self, index):
        self.stacked_widget.setCurrentIndex(index)


"""
堆栈控件
    堆栈控件是Qt中最常用的一种控件，堆栈控件可以理解为窗口的堆栈，
    堆栈控件中的每个窗口都可以通过点击按钮进行切换，
    堆栈控件中的每个窗口都可以通过点击按钮进行切换。
    堆栈控件中的每个窗口都可以通过点击按钮进行切换。
    堆栈控件中的每个窗口都可以通过点击按钮进行切换。
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StackedWidgetDemo()
    main.show()
    sys.exit(app.exec_())