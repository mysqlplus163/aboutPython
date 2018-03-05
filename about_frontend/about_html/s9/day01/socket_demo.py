#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/4

import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 8000))

sk.listen(5)


while True:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")  # 浏览器和我约定了一个消息格式
    with open("data.txt", "rb") as f:
        conn.send(f.read())
    conn.close()
