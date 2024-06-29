# -*- coding: utf-8 -*-
# @Time : 2024/6/28 20:16
# @Auth : xz_official
# @File : 填充图形区域.py
# @IDE : PyCharm
# 引入系统模块
import sys
# 引入窗口类
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# 引入绘图事件
from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QPen, QImage, QBrush
# 引入绘图类
from PyQt5.QtCore import Qt, QPoint, QRect
"""
    绘制各种图形
"""


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口属性
        self.setWindowTitle("填充图形区域")

        # 设置窗口大小
        self.resize(500, 500)

    def paintEvent(self, a0: QPaintEvent) -> None:
        # 创建绘图对象
        painter = QPainter()
        # 开始绘制
        painter.begin(self)

        # 设置画刷
        brush = QBrush(Qt.red, Qt.Dense1Pattern)
        # brush = QBrush(Qt.red, Qt.Dense3Pattern)
        # 设置画刷
        painter.setBrush(brush)
        # 绘制矩形  矩形左上角坐标(100,100)，宽100，高100
        painter.drawRect(QRect(100, 100, 100, 100))

        # 结束绘制
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())