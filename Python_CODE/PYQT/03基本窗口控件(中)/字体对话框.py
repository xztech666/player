# -*- coding: utf-8 -*-
# @Time : 2024/6/23 17:55
# @Auth : xz_official
# @File : 字体对话框.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFontDialog, QLabel


class FontDialog(QWidget):
    def __init__(self):
        super(FontDialog, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("字体对话框")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel("hello, Pyqt", self)

        # 创建按钮
        self.btn = QPushButton("选择字体")

        # 将布局添加到窗口中
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.btn)

        # 将按钮的点击信号与change_font函数连接
        self.btn.clicked.connect(self.change_font)

        # 将布局设置为窗口的布局
        self.setLayout(self.v_layout)

    def change_font(self):
        # 打开字体对话框
        font, ok = QFontDialog.getFont()
        # 如果用户点击了OK按钮，则将字体应用到标签
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = FontDialog()
    main_window.show()
    sys.exit(app.exec_())