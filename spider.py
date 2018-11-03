#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 19:56
# @Author  : likewind
# @mail    : likewind1993@163.com
# @File    : spider.py
# @Software: sky-studio.cn

import re
from connection import Connection
from data import Data

class Spider(object):
    def __init__(self, folder_path, url):
        self.folder_path = folder_path
        self.connection = Connection(url)
        self.data = Data(self.folder_path)
        self.urls = []
        self.visited_urls = []
        self.urls.append(url)
        self.count = 0

    def start(self):
        self._next_page(self.urls)

    def _next_page(self, html_list):
        if self.count > 300 :
            return

        for i in range(len(html_list)):
            cur_url = html_list[i]
            if cur_url not in self.visited_urls:
                print("Page {}: ".format(self.count) + cur_url)
                page = self.connection.open_url(cur_url)
                image_list, url_list = self.data.parsePage(page)
                self.data.download(image_list)
                self.visited_urls.append(cur_url)
                self.count += 1
                self._next_page(url_list)

def main():
    save_path = './images/'
    start_url = 'http://www.jpmsg.com/meinv/View_14429.html'
    spider = Spider(save_path, start_url)
    spider.start()

if __name__ == '__main__':
    main()