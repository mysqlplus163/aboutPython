#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/6

import socket


sk = socket.socket()

sk.bind(("127.0.0.1", 8080))
sk.listen(5)


while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.secd(b"<h1>Hello world!</h1>")
    conn.close()


