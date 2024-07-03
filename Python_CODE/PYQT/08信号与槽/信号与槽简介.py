# -*- coding: utf-8 -*-
# @Time : 2024/7/3 16:23
# @Auth : xz_official
# @File : 信号与槽简介.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
"""
信号与槽组合起来是为了实现一些特定的功能,需要三个条件:
1.有信号
2.有槽
3.信号的触发条件
"""


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('信号与槽')
        self.resize(500, 500)

        # 创建一个垂直布局
        self.layout = QVBoxLayout()

        # 创建一个按钮
        self.btn = QPushButton('点击发送信号')
        self.btn.clicked.connect(self.btn_clicked)
        """
            连接信号与槽: 这行代码表示当self.btn的clicked信号被触发时，它将调用self.btn_clicked方法作为响应。这里只是建立了信号和槽函数之间的连接，并没有立即执行btn_clicked方法。
            self.btn.clicked.connect(self.btn_clicked()):
                这种写法是错误的，因为它尝试将self.btn_clicked()函数的返回值（如果有的话）作为槽函数连接到信号上，而不是函数本身。
                在实例化时，这会导致btn_clicked方法立即被执行一次，并且因为没有传递信号的预期参数（如QMouseEvent在某些情况下），可能会引发错误或不符合预期的行为。
                正确的做法是只传递方法的引用，即不带括号。
        """
        # 将按钮添加到布局中
        self.layout.addWidget(self.btn)
        # 设置布局
        self.setLayout(self.layout)

    def btn_clicked(self):
        print('按钮被点击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    # 显示窗口
    w.show()
    sys.exit(app.exec_())