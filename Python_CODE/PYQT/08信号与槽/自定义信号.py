# -*- coding: utf-8 -*-
# @Time : 2024/7/3 17:42
# @Auth : xz_official
# @File : 自定义信号.py
# @IDE : PyCharm
from PyQt5.QtCore import QObject, pyqtSignal


class MySignal(QObject):
    # 自定义信号
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(str)
    signal3 = pyqtSignal(dict)
    signal4 = pyqtSignal(str, int)

    def run(self):
        # 发射/触发 信号
        self.signal1.emit()

    def run2(self):
        self.signal2.emit("xz_official")

    def run3(self):
        self.signal3.emit({"name: ": "xz_official", "age: ": 18})

    def run4(self):
        self.signal4.emit("xz_official", 18)


class MySlot(QObject):
    # 自定义槽
    def print_info(self):
        print("print info!")

    def print_name(self, name):
        print("name:", name)

    def print_dict(self, info):
        print(info)

    def print_name_age(self, name, age):
        print("name:", name, "age:", age)


if __name__ == '__main__':
    my_signal = MySignal()
    my_slot = MySlot()

    my_signal.signal1.connect(my_slot.print_info)
    my_signal.run()

    my_signal.signal2.connect(my_slot.print_name)
    my_signal.run2()

    my_signal.signal3.connect(my_slot.print_dict)
    my_signal.run3()

    my_signal.signal4.connect(my_slot.print_name_age)
    my_signal.run4()