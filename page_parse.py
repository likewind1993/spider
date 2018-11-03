#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/3 10:59
# @Author  : likewind
# @mail    : likewind1993@163.com
# @File    : page_parse.py
from bs4 import BeautifulSoup
import requests
import urllib3

class PageParse(object):
    def __init__(self, data_format = None, pages = None):
        self.pages = []
        self.data_format = []
        if pages is not None:
            self.pages.append(pages)
        if data_format is not None:
            self.data_format.append(data_format)

    def parse(self):
        for i in range(len(self.data_format)):


        for i in range(len(self.pages)):
            cur_page = self.pages[i]

            bs = BeautifulSoup(cur_page)
            content = bs.find('div', class_='content-text word').get_text()

        return None

    def add_page(self, page):
        self.pages.append(page)
def main():
    page_parse = PageParse()
    url = 'https://www.qiushibaike.com/article/119001682'
    http = urllib3.PoolManager()
    respones = http.request('GET', url)
    data = respones.data.decode()
    bs = BeautifulSoup(data, "html.parser")


    print(content)

if __name__ == '__main__':
    main()