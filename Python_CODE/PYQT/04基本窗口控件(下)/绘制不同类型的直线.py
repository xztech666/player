# -*- coding: utf-8 -*-
# @Time : 2024/6/24 21:33
# @Auth : xz_official
# @File : 绘制不同类型的直线.py
# @IDE : PyCharm
# 引入系统模块
import sys
# 引入窗口类
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# 引入绘图事件
from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QPen
# 引入绘图类
from PyQt5.QtCore import Qt


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口属性
        self.setWindowTitle("绘制直线")

        # 设置窗口大小
        self.resize(500, 500)

    def paintEvent(self, a0: QPaintEvent) -> None:
        # 创建画笔类
        painter = QPainter()
        # 开始绘制
        painter.begin(self)
        # 创建画笔
        pen = QPen(Qt.red, 3, Qt.SolidLine)    # 默认是实线
        # pen = QPen(Qt.red, 3, Qt.DashLine)
        # pen = QPen(Qt.red, 3, Qt.DotLine)
        # pen = QPen(Qt.red, 3, Qt.DashDotLine)

        # 设置画笔
        painter.setPen(pen)
        # 绘制直线 0,0 到 100,100(x,y)坐标
        painter.drawLine(0, 0, 100, 100)
        # 结束绘制
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())