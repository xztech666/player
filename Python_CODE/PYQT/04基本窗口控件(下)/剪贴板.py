# -*- coding: utf-8 -*-
# @Time : 2024/6/28 20:29
# @Auth : xz_official
# @File : 剪贴板.py
# @IDE : PyCharm
# 引入系统模块
import sys
# 引入窗口类
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
# 引入图像类
from PyQt5.QtGui import QPixmap


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口
        self.setWindowTitle("剪贴板")

        # 设置窗口大小
        self.resize(500, 500)

        # 创建一个栅格布局
        grid_layout = QGridLayout()
        # 创建按钮
        copy_text = QPushButton("复制文本")
        copy_text.clicked.connect(self.copy_text)
        paste_text = QPushButton("粘贴文本")
        paste_text.clicked.connect(self.paste_text)
        copy_image = QPushButton("复制图片")
        copy_image.clicked.connect(self.copy_image)
        paste_image = QPushButton("粘贴图片")
        paste_image.clicked.connect(self.paste_image)
        # 创建一个标签
        self.label = QLabel("文本")
        self.label2 = QLabel("图片")
        self.label2.setPixmap(QPixmap("./image.png"))
        # 将按钮添加到栅格布局中
        grid_layout.addWidget(copy_text, 0, 0)
        grid_layout.addWidget(paste_text, 0, 1)
        grid_layout.addWidget(copy_image, 1, 0)
        grid_layout.addWidget(paste_image, 1, 1)
        grid_layout.addWidget(self.label, 2, 0, 1, 2)
        grid_layout.addWidget(self.label2, 3, 0, 1, 2)
        """
        label: 要添加到布局的控件对象，本例中是一个标签（Label）。
        2: 控件所在的行数索引，从0开始计数。这意味着 label 将被放置在第3行。
        0: 控件所在的列数索引，同样从0开始计数。所以 label 位于第1列。
        1: 跨行数，表示 label 在垂直方向上占用的行数。值为1意味着它只占1行。
        2: 跨列数，表示 label 在水平方向上占用的列数。值为2意味着它横跨2列。
        """

        # 设置窗口布局
        self.setLayout(grid_layout)

    def copy_text(self):
        # 获取剪贴板
        clipboard = QApplication.clipboard()
        # 复制文本
        clipboard.setText("Hello World!")
    def paste_text(self):
        # 获取剪贴板
        clipboard = QApplication.clipboard()
        # 从剪贴板里面获取内容
        text = clipboard.text()
        # 设置标签文本
        self.label.setText(text)
    def copy_image(self):
        # 获取剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("./1.jpg"))
    def paste_image(self):
        # 获取剪贴板
        clipboard = QApplication.clipboard()
        # 从剪贴板里面获取内容
        pixmap = clipboard.pixmap()
        # 设置标签图片
        self.label2.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())