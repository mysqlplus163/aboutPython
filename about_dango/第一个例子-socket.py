#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/22

import socket


s = socket.socket()

s.bind(("127.0.0.1", 8080))

s.listen(5)

while True:
    conn, addr = s.accept()  # 暂时挂起
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"123123")
    conn.close()

# 问题来了？--> 浏览器作为client端，给我们发送了什么？

# 发送和响应，都对应了头和身体

