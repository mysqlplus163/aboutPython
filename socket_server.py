#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/13


import socket

ip_port = ("127.0.0.1", 4444)
sk = socket.socket()

sk.bind(ip_port)

sk.listen(5)

print("server waiting...")
conn, add = sk.accept()
recv_data = conn.recv(1024)
print("receive from client:", str(recv_data, "utf-8"))
conn.send(recv_data)
while True:
    recv_data = conn.recv(1024)
    print("receive from client:", str(recv_data, "utf-8"))
    if len(recv_data) == 0:
        break
    conn.send(recv_data)

