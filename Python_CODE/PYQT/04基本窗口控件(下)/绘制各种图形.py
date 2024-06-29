# -*- coding: utf-8 -*-
# @Time : 2024/6/26 21:18
# @Auth : xz_official
# @File : 绘制各种图形.py
# @IDE : PyCharm
# 引入系统模块
import sys
# 引入窗口类
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# 引入绘图事件
from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QPen, QImage
# 引入绘图类
from PyQt5.QtCore import Qt, QPoint, QRect


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口属性
        self.setWindowTitle("绘制各种图形")

        # 设置窗口大小
        self.resize(500, 500)

    def paintEvent(self, a0: QPaintEvent) -> None:
        # 创建画笔类
        painter = QPainter()
        # 开始绘制
        painter.begin(self)
        # 设置画笔
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        # 绘制弧线  100,100为起始坐标  100,100为宽高  0,360为起始角度,结束角度 16为角度单位
        # painter.drawArc(100, 100, 100, 100, 0, 360 * 16)
        painter.drawArc(100, 100, 100, 100, 0, 90 * 16)
        # 绘制闭合的弧形   100,100为起始坐标  100,100为宽高  0,90为起始角度,结束角度 16为角度单位
        painter.drawChord(100, 100, 100, 100, 0, 90 * 16)
        # 绘制扇形  100,100为起始坐标  100,100为宽高  0,90为起始角度,结束角度 16为角度单位
        painter.drawPie(100, 100, 100, 100, 0, 90 * 16)
        # 绘制椭圆形   100,100为起始坐标  100,100为宽高
        painter.drawEllipse(100, 100, 100, 100)

        # 创建点
        Points = [QPoint(100, 100), QPoint(200, 100), QPoint(200, 200), QPoint(100, 200)]
        # 绘制多边形
        painter.drawPolygon(Points)

        # 创建图片
        image = QImage("./1.jpg")
        # 创建矩形对象   100,100为起始坐标  image.width(),image.height()为宽高
        rect = QRect(100, 100, image.width(), image.height())
        # 绘制图片
        painter.drawImage(rect, image)

        # 结束绘制
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())