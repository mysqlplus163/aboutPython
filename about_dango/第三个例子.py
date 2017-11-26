#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
第三个例子
URL对应函数
"""

import socket


sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    data_str = str(data, encoding="utf-8")  # 把收到的字节数据转换成字符串类型
    header = data_str.split("\r\n\r\n")  # 将请求的数据按照\r\n\r\n分割
    header_list = header[0].split("\r\n")  # 按\r\n分割header
    temp = header_list[0].split(" ")  # 按空格分割第一行
    url = temp[1]  # 取到请求的URL
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")  # 发送响应头
    if url == "/index/":
        conn.send(b"this is index page.")
    else:
        conn.send(b"404 not found.")
    conn.close()
