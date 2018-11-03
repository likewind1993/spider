#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 14:13
# @Author  : likewind
# @mail    : likewind1993@163.com
# @File    : connection.py
import requests
import urllib.request as request



class Connection(object):
    def __init__(self, url):
        self.url = url

    def open_url(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        }
        req = request.Request(url=url, headers=headers, method='GET')
        response = request.urlopen(req)
        html = ""
        if response.status == 200:
            html = response.read()
            html = html.decode("gbk","ignore")

        return html
