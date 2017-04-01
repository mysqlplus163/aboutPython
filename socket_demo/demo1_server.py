#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/24

import socket

server = socket.socket()
server.bind(("localhost", 6969))
server.listen()

print("我开始等电话了")
conn, addr = server.accept()
print("电话来了")


conn.send(bytes("OK".encode('utf-8')))
user = conn.recv(1024).decode()
passwd = conn.recv(1024).decode()
print("user:", user)
print("passwd:", passwd)

server.close()
