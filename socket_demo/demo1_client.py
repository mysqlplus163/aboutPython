#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/24

import socket

client = socket.socket()
client.connect(("localhost", 6969))


data = client.recv(1024).decode()
print(data, "请登录！")
print(data == "请登录！")
if data == "OK":
    print(1)
    user_name = input("user name:")
    client.send(bytes(user_name, encoding="utf-8"))
    pass_wd = input("pass word:")
    client.send(bytes(pass_wd, encoding="utf-8"))


