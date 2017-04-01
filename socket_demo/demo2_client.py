#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/24

import socket,pickle
from conf import setting

class SSH():
    def __init__(self,host,client,port=setting.PORT):
        self.host=host
        self.port=port
        self.client=client

    def connect(self):
        self.client.connect((self.host,self.port))

    def user_load(self):
        user_name=input("请输入用户名：")
        self.client.send(bytes(user_name.encode("utf-8")))
        password=input("请输入密码：")

        self.client.send(bytes(password.encode("utf-8")))

def run():

    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip=input("请输入连接的IP地址：")
    link=SSH(ip,client)
    link.connect()
    data=client.recv(1024)
    data=data.decode()
    if data=="请登陆！":
        user_name = input("请输入用户名：")
        client.send(bytes(user_name.encode("utf-8")))
        password = input("请输入密码：")
        client.send(bytes(password.encode("utf-8")))
        #link.user_load()
