#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/23

"""
手写socket
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
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"OK")
    conn.close()
