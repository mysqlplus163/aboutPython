#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
第二个例子，不同的URL返回不同的内容
"""

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 80))
sk.listen(5)


while True:
    conn, addr = sk.accept()
    # 有人来连接了
    # 看一下它要啥
    data = conn.recv(8096)
    print(data)
    print("*" * 50)
    header = str(data, encoding="utf-8").split("\r\n\r\n")
    header_list = header[0].split("\r\n")
    print(header_list[0])
    print("=" * 50)
    request = header_list[0].split(" ")
    url = request[1]
    print(url)
    conn.send(b"HTTP/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n")
    if url == "/index/":
        conn.send(bytes("这是主页", encoding="utf-8"))
    else:
        conn.send(b"404 not found")
    conn.close()
