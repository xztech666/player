# -*- coding: utf-8 -*-
# @Time : 2024/7/3 21:31
# @Auth : xz_official
# @File : 整合案例.py
# @IDE : PyCharm
"""
    实现数据更新:  信号  槽  多线程  网络请求
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import requests
import json

class GetDataThread(QThread):
    # 自定义信号
    update_data = pyqtSignal(list)

    def __init__(self):
        super(GetDataThread, self).__init__()

    def run(self):
        url = "https://i.news.qq.com/web_feed/getPCList"
        params = '{"base_req":{"from":"pc"},"forward":"2","qimei36":"0_b2b3c2943f76b","device_id":"0_b2b3c2943f76b","flush_num":1,"channel_id":"news_news_tech","item_count":12,"is_local_chlid":"0"}'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Referer": "https://news.qq.com/",
            "Origin": "https://news.qq.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        response = requests.post(url, data=params, headers=headers)

        data_list = json.loads(response.text)["data"]
        # 获取标题  列表表达式
        titles = [data["title"] for data in data_list]

        # 发射/触发 信号
        self.update_data.emit(titles)

class UpdateDateDemo(QWidget):
    def __init__(self):
        super(UpdateDateDemo, self).__init__()
        self.v_layout = None
        self.load_btn = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("更新数据")
        self.resize(500, 500)

        # 创建垂直布局
        self.v_layout = QVBoxLayout()
        self.load_btn = QPushButton("点击加载更多数据")
        self.load_btn.clicked.connect(self.load_data)

        # 将按钮添加到布局中
        self.v_layout.addWidget(self.load_btn)
        # 设置布局
        self.setLayout(self.v_layout)

    def load_data(self):
        # 创建线程
        self.get_data_thread = GetDataThread()
        # 信号与槽的连接
        self.get_data_thread.update_data.connect(self.update_data)
        # 启动线程
        self.get_data_thread.start()
        """
        优化后的代码在以下几个地方进行了修改：
        
        原始代码:
            def load_data(self):
                # 创建线程
                get_data_thread = GetDataThread()
                # 信号与槽的连接
                get_data_thread.updata_data.connect(self.update_data)
                # 启动线程
                get_data_thread.start()
                
        优化代码:
            def load_data(self):
                # 创建线程
                self.get_data_thread = GetDataThread()
                # 信号与槽的连接
                self.get_data_thread.update_data.connect(self.update_data)
                # 启动线程
                self.get_data_thread.start()

        
        GetDataThread 线程的生命周期管理：
        
        在原始代码中，GetDataThread 线程是在 load_data 方法中创建的局部变量。这可能导致线程对象在方法执行结束后被垃圾回收。
        在优化后的代码中，GetDataThread 线程实例被设置为 UpdateDateDemo 类的实例属性 (self.get_data_thread)，这确保了线程对象在整个 UpdateDateDemo 实例的生命周期内是有效的，并避免了线程对象被垃圾回收。
        属性初始化：
        
        在优化后的代码中，将 self.get_data_thread 定义为 UpdateDateDemo 类的属性。这使得每次调用 load_data 方法时，都会创建一个新的线程，并且上一个线程会被正确管理。
        """
    def update_data(self, data):
        for title in data:
            label = QLabel(title)
            self.v_layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = UpdateDateDemo()
    main.show()
    sys.exit(app.exec_())
