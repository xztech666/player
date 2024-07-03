# -*- coding: utf-8 -*-
# @Time : 2024/7/3 18:00
# @Auth : xz_official
# @File : 信号与槽的自动连接.py
# @IDE : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QMetaObject, pyqtSlot


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.v_layout = None
        self.confirm_btn = None
        self.cancel_btn = None
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('信号与槽的自动连接')
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()

        # 创建按钮
        self.confirm_btn = QPushButton('确定', self)
        self.cancel_btn = QPushButton('取消', self)

        # 设置按钮的ObjectName
        self.confirm_btn.setObjectName('confirm')
        self.cancel_btn.setObjectName('cancel')

        # 将按钮添加到垂直布局中
        self.v_layout.addWidget(self.confirm_btn)
        self.v_layout.addWidget(self.cancel_btn)

        # 设置窗口布局
        self.setLayout(self.v_layout)

        # 自动连接槽函数
        QMetaObject.connectSlotsByName(self)
        """
        QMetaObject.connectSlotsByName(self) 是 PyQt 或者 Qt for Python 中的一个便捷函数，用于自动连接信号和槽。
        它的作用是根据对象名称自动将对象中的 slots（槽函数）与具有相应命名约定的 signals（信号）相连接。
        这种方式可以简化代码，减少手动连接信号与槽的工作量。
        !!!--具体工作原理如下：
        命名约定：为了使 connectSlotsByName 能够正常工作，需要遵循一定的命名规范。通常，槽函数的名称应该以 "on_" 开头，后跟发送信号的对象名称（不包括前缀如 ui.），再接信号的名称，所有单词首字母大写。
            例如，如果有一个按钮 pushButton 的 clicked 信号，对应的槽函数应命名为 on_pushButtonClicked。
        自动连接：当你调用 QMetaObject.connectSlotsByName(self) 时，Qt 的元对象系统会遍历当前对象（self）中的所有孩子对象，查找符合上述命名约定的槽函数，并尝试找到匹配的信号进行自动连接。
            这样，无需显式调用 connect 方法，就可以完成信号与槽的连接。
        适用场景：此方法特别适用于由 UI 设计器（如 Qt Designer）生成的用户界面代码，其中包含大量的组件和交互逻辑。通过遵循命名约定，可以在 UI 文件转换为 Python 代码后，快速建立信号与槽的连接。
        """

    @pyqtSlot()  # 自动连接槽函数
    def on_confirm_clicked(self):
        print('this is confirm!')

    @pyqtSlot()
    def on_cancel_clicked(self):
        print('this is cancel!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())