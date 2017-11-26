#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
使用自带的wsgiref
"""

from wsgiref.simple_server import make_server


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
