# -*- coding: utf-8 -*-
# @Time : 2024/6/29 10:54
# @Auth : xz_official
# @File : 菜单栏.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QMessageBox, QVBoxLayout, \
    QTextEdit, QWidget, QFileDialog


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        # 设置菜单栏
        self.setWindowTitle("菜单栏")
        # 设置窗口大小
        self.resize(500, 500)

        # 创建菜单栏
        menu = self.menuBar()
        file = menu.addMenu("文件")
        edit = menu.addMenu("编辑")
        view = menu.addMenu("查看")
        HELP = menu.addMenu("帮助")
        # 创建菜单栏的子菜单
        file_new = QAction("新建", self)
        file_open = QAction("打开", self)
        file_save = QAction("保存", self)
        file_exit = QAction("退出", self)
        # 添加子菜单到菜单栏
        file.addAction(file_new)
        file.addAction(file_open)
        file.addAction(file_save)
        file.addAction(file_exit)
        # 绑定事件
        file_new.triggered.connect(self.new_file)
        file_open.triggered.connect(self.open_file)
        # 添加子菜单到菜单栏
        edit_copy = QAction("复制", self)
        edit_cut = QAction("剪切", self)
        edit_paste = QAction("粘贴", self)
        edit.addAction(edit_copy)
        edit.addAction(edit_cut)
        edit.addAction(edit_paste)
        # 添加子菜单到菜单栏
        view_status = QAction("状态栏", self)
        view_tool = QAction("工具栏", self)
        view.addAction(view_status)
        view.addAction(view_tool)
        # 添加子菜单到菜单栏
        help_about = QAction("关于", self)
        help_help = QAction("更多", self)
        HELP.addAction(help_about)
        HELP.addAction(help_help)

        # 创建垂直布局
        layout = QVBoxLayout()
        # 创建多行文本框
        self.text = QTextEdit()
        # 将文本框添加到垂直布局
        layout.addWidget(self.text)
        # 添加菜单栏到窗口  因为主窗口无法直接添加
        # 创建窗口
        self.window = QWidget()
        # 设置窗口布局
        self.window.setLayout(layout)
        # 将窗口添加到主窗口
        self.setCentralWidget(self.window)

    def open_file(self):
        # 创建文件对话框
        file_dialog = QFileDialog()
        # 显示文件对话框
        file_dialog.exec_()
        # 判断文件对话框是否被点击
        if file_dialog.result() == QFileDialog.Accepted:
            # 获取文件路径
            file_path = file_dialog.selectedFiles()[0]
            # 打开文件
            with open(file_path, "r", encoding="utf-8") as f:
                # 读取文件内容
                content = f.read()
                # 将文件内容显示到文本框
                self.text.setText(content)
                QMessageBox.information(self, "提示", "文件打开成功")

    def new_file(self):
        # 显示消息框
        QMessageBox.information(self, "提示", "新建文件")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())