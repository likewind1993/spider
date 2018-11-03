#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 14:15
# @Author  : likewind
# @mail    : likewind1993@163.com
# @File    : data.py
import re
import urllib.request as request
from page_parse import PageParse

class Data(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.page_parse = PageParse()
        self.content = None
    def define_content(self, data_format):
        self.content = data_format


    def parsePage(self, pages):
        self.page_parse.add_page(pages)
        content = self.page_parse.parse()

        return content

    def parsePage(self, page):
        reg = 'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        img_list = re.findall(imgre, page)

        reg = 'href="(.+?\.html)"'
        htmlre = re.compile(reg)
        html_list = re.findall(htmlre, page)


        return img_list, html_list
    def download(self, file_list):
        print("Contains images: {} ".format(len(file_list)))
        for i in range(len(file_list)):
            image_url = file_list[i]
            image_name = image_url.split('/')[-1]
            request.urlretrieve(image_url, self.folder_path+image_name)

