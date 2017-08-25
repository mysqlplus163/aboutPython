#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/25

"""
自己写路由
"""

import socket


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

    if url == "/xxx":
        conn.send(b"xxx")
    else:
        conn.send(b"404")
