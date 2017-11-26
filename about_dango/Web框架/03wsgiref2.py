#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
wsgiref
"""

from wsgiref.simple_server import make_server


def index():
    return [b'index']


def login():
    return [b'login']


# 设置一个URL和函数的对应关系
url_func_map = (
        ('/index/', index),
        ('/login/', login),
    )


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # 设置HTTP响应的状态码和头信息
    url = environ['PATH_INFO']  # 取到用户输入的url
    func = None
    for item in url_func_map:
        if item[0] == url:
            func = item[1]  # 找得到对应函数
            break
    if func:
        return func()
    else:
        return [b'404 not found']


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
