#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
mac上实验socket
"""

import socket


sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    # 等待有人来连接
    # 看它要啥
    data = conn.recv(8096)
    print(data)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"ok from s7")
    conn.close()