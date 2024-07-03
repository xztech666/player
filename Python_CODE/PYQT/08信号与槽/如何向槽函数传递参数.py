# -*- coding: utf-8 -*-
# @Time : 2024/7/3 21:06
# @Auth : xz_official
# @File : 如何向槽函数传递参数.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSlot


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.v_layout = None
        self.btn = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('如何向槽函数传递参数')
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()
        # 创建按钮
        self.btn = QPushButton('点击一下')
        info = {'name': 'xz_official', 'age': 18}
        info2 = {'name': 'Zhikuan', 'age': 18}
        self.btn.clicked.connect(lambda: self.show_info(info, info2))
        # 把按钮添加到布局
        self.v_layout.addWidget(self.btn)
        # 设置布局
        self.setLayout(self.v_layout)

    def show_info(self, info, info2):
        print(info, '\n', info2)

"""
    lambda表达式
    lambda表达式可以理解为匿名函数，即没有函数名的函数。
    lambda表达式的语法格式如下：
    lambda [arg1 [,arg2,.....argn]]:expression
    其中arg1、arg2、argn为参数，expression为返回值表达式。
    
    # 这是一个无参数的lambda函数，当调用时，它返回3的平方
    square = lambda: 3 * 3
    print(square())  # 输出：9
    
    # 这是一个接受两个参数x和y的lambda函数，用于计算并返回两数之和
    add = lambda x, y: x + y
    result = add(5, 7)  # 传入5和7作为参数
    print(result)  # 输出：12

    lambda表达式的优点：
    1.lambda表达式可以理解为匿名函数，即没有函数名的函数。
    2.lambda表达式的语法格式简单，便于理解。
    3.lambda表达式可以作为参数传递给其他函数。
    4.lambda表达式可以作为列表推导式中的表达式。
    5.lambda表达式可以作为字典推导式中的表达式。
    6.lambda表达式可以作为生成器推导式中的表达式。
    7.lambda表达式可以作为函数的返回值。
    8.lambda表达式可以作为函数的参数。
    9.lambda表达式可以作为函数的局部变量。
    10.lambda表达式可以作为函数的全局变量。
    11.lambda表达式可以作为函数的静态变量。
    12.lambda表达式可以作为函数的实例变量。
    13.lambda表达式可以作为函数的类变量。
    14.lambda表达式可以作为函数的静态方法。
    15.lambda表达式可以作为函数的实例方法。
    16.lambda表达式可以作为函数的类方法。
    17.lambda表达式可以作为函数的静态方法。
    18.lambda表达式可以作为函数的实例方法。
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWidget()
    main.show()
    sys.exit(app.exec_())