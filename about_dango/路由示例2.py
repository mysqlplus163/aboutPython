#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/25

"""
自己写路由
"""

import socket


def f1():
    return "xxx->f1"


def f2():
    return "ooo->f2"


routers = [
    ("/xxx", f1),
    ("/ooo", f2),
]


def run():
    s = socket.socket()
    s.bind(("127.0.0.1", 8080))
    s.listen(5)
    while True:
        conn, addr = s.accept()  # 暂时挂起
        data = conn.recv(8096)

        head, body = data.split("\r\n\r\n")
        value_list = head.split("\r\n")
        method, url, protocal = value_list[0].split(" ")

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for i in routers:
            if i[0] == url:
                func_name = i[1]
                break  # 找到一个不需要往下找了
        if func_name:  # 如果有这个函数
            response = func_name()
        else:
            response = "404"

        conn.send(bytes(response, encoding="UTF-8"))
        conn.close()

if __name__ == '__main__':
    run()
