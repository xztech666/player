# -*- coding: utf-8 -*-
# @Time : 2024/6/23 17:25
# @Auth : xz_official
# @File : 文件对话框.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QTextEdit


class FileDialog(QWidget):
    def __init__(self):
        super(FileDialog, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("文件对话框")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建一个按钮
        self.btn = QPushButton("请选择文件")

        # 创建一个多行文本框
        self.text_edit = QTextEdit()

        # 添加按钮点击事件
        self.v_layout.addWidget(self.btn)
        self.v_layout.addWidget(self.text_edit)

        self.btn.clicked.connect(self.show_file_dialog)

        # 设置窗口布局
        self.setLayout(self.v_layout)

    def show_file_dialog(self):
        file = QFileDialog()
        file.exec_()
        files = file.selectedFiles()
        selected_file = files[0]
        # 打开文件
        fp = open(selected_file, 'r', encoding='utf-8')
        # 读取文件内容
        content = fp.read()
        # 关闭文件
        fp.close()
        # 将文件内容写入多行文本框
        self.text_edit.setText(content)


if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = FileDialog()
    # 显示窗口
    main_window.show()
    # 进入程序的主循环，并通过exit函数确保程序完整退出
    sys.exit(app.exec_())