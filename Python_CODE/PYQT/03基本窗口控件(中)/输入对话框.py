# -*- coding: utf-8 -*-
# @Time : 2024/6/23 18:05
# @Auth : xz_official
# @File : 输入对话框.py
# @IDE : PyCharm
"""
输入对话框: QInputDialog
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt


class InputDialog(QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()
        # 设置窗口标题
        self.setWindowTitle("输入对话框")

        # 设置窗口尺寸
        self.resize(500, 500)

        # 创建表单布局
        self.form_layout = QFormLayout()

        # 创建按钮
        self.btn = QPushButton("请选择编程语言")

        # 创建单行输入框
        self.line_edit = QLineEdit()

        # 将按钮与槽函数关联
        self.btn.clicked.connect(self.show_input_dialog)

        # 将表单布局添加到窗口中
        self.form_layout.addRow(self.btn, self.line_edit)

        # 设置窗口布局
        self.setLayout(self.form_layout)

    def show_input_dialog(self):
        items = ["Python", "Java", "C++", "C", "C#", "JavaScript", "PHP", "Ruby", "Go", "Swift"]
        lang, is_ok = QInputDialog.getItem(self, "编程语言列表", "请选择编程语言", items, 0, False)
        if is_ok:
            # 将选中的编程语言显示到单行输入框中
            self.line_edit.setText(lang)

"""
QInputDialog.getItem(self, title, label, items, current, editable)
    title: 窗口标题
    label: 窗口提示信息
    items: 列表选项
    current: 默认选项
    editable: 是否可编辑
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = InputDialog()
    main.show()
    sys.exit(app.exec_())