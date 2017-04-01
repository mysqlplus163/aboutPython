#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/13

import socket

ip_port = ("127.0.0.1", 4444)
sk = socket.socket()

sk.connect(ip_port)
#
# sk.send(bytes("hello from client...", "utf-8"))
# recv_data = sk.recv(1024)
# print("receive from server:", str(recv_data, "utf-8"))

while True:
    input_data = input("==>").strip()
    if input_data == "exit":
        break
    if len(input_data) == 0:
        break
    sk.send(bytes(input_data, "utf-8"))
    recv_data = sk.recv(1024)
    print("receive from server:", str(recv_data, "utf-8"))

sk.close()
