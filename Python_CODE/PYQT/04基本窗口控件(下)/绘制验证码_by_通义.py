# -*- coding: utf-8 -*-
# @Time : 2024/6/24 21:31
# @Auth : xz_official
# @File : 绘制验证码_by_通义.py
# @IDE : PyCharm

import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QPaintEvent
from PyQt5.QtCore import Qt


class PainterText(QWidget):
    def __init__(self):
        super(PainterText, self).__init__()

        # 设置窗口属性
        self.setWindowTitle("绘制验证码")

        # 设置窗口大小
        self.resize(500, 500)

        # 验证码相关属性
        self.code_length = 4  # 验证码长度
        self.code = self.generate_code()  # 生成验证码

    def generate_code(self):
        """生成随机验证码"""
        characters = string.ascii_letters + string.digits  # 字母加数字
        return ''.join(random.choice(characters) for _ in range(self.code_length))

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        # 设置字体
        font = QFont("Arial", 30)
        painter.setFont(font)

        # 遍历验证码中的每个字符并绘制
        for index, char in enumerate(self.code):
            # 为每个字符随机设置颜色
            color = QColor(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
            painter.setPen(color)

            # 计算字符位置，确保它们之间有间隔
            x = (self.width() - painter.fontMetrics().width(self.code)) // 2 + index * 35
            y = (self.height() - painter.fontMetrics().height()) // 2

            # 绘制字符
            painter.drawText(x, y, char)

        # 绘制结束，此处无需显式调用 end()，因为在 with 语句中会自动处理
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PainterText()
    main_window.show()
    sys.exit(app.exec_())
