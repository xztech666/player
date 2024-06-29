# -*- coding: utf-8 -*-
# @Time : 2024/6/23 18:20
# @Auth : xz_official
# @File : 绘制文本.py
# @IDE : PyCharm
"""
绘图API:
1.绘制文本
2.各种图形(直线,点,椭圆,圆,狐)
3.图像

QPainter  绘制类
"""
# 引入系统模块
import sys
# 引入窗口类
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
# 引入绘图事件
from PyQt5.QtGui import QPaintEvent, QPainter, QFont
# 引入绘图类
from PyQt5.QtCore import Qt


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口属性
        self.setWindowTitle("绘制文本")

        # 设置窗口大小
        self.resize(500, 500)

    # 重写绘图事件
    def paintEvent(self, a0: QPaintEvent) -> None:
        # 创建画笔类
        painter = QPainter(self)
        # 开始绘制
        painter.begin(self)
        # 设置画笔颜色
        painter.setPen(Qt.blue)
        # 设置字体
        painter.setFont(QFont("微软雅黑", 20))
        # 绘制文本,居中
        painter.drawText(a0.rect(), Qt.AlignCenter, "Hello World!")
        # 结束绘制
        painter.end()

        """
        painter.drawText()的使用
            1.第一个参数是绘制的位置
            2.第二个参数是绘制的内容
            3.第三个参数是绘制的格式
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())