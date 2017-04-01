#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/24

import socket,os,sys,pickle

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #找到路径
sys.path.insert(0, dir)     #添加路径
print(dir)

from conf import setting
print(setting.DB_DIR)
class Ser(object):
    def __init__(self,user,pwd,conn):
        self.user=user
        self.pwd=pwd
        self.conn=conn


    def load(self):
        a=os.path.join(setting.DB_DIR,'load')
        with open(a,'r') as f:
            while True:
                try:
                    a = pickle.load(f)
                    if self.user in a and a[self.user] == self.pwd:
                        return 1
                    elif self.user in a and a[self.user] != self.pwd:
                        return 2
                    elif self.user not in a:
                        return 3

                except Exception as e:
                    break



    def register(self):
        self.conn.send("开始注册！".encode('utf-8'))
        self.conn.send("请输入用户名：".encode('utf-8'))
        a = self.conn.recv(1024)
        self.conn.send("请输入密码：".encode('utf-8'))
        b = self.conn.recv(1024)
        user = a.decode()
        pwd = b.decode()
        dic={user:pwd}
        with open(setting.DB_DIR,'a') as f:
            pickle.dump(dic,f)
        os.mkdir('%s\%s'%(dir,user))
        self.conn.send("注册成功！".encode('utf-8'))

    def dir_list(self):
        pass

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',setting.PORT))
server.listen(5)
while True:
    conn,addr=server.accept()
    print("{0}已经连接".format(addr))
    while True:
        conn.send(bytes("请登陆！".encode('utf-8')))
        user = conn.recv(1024).decode()
        pwd = conn.recv(1024).decode()
        ser_opera=Ser(user,pwd,conn)
        i=ser_opera.load()
        if i == 1:
            msg='''
            1.查看文件目录
            2.上传文件
            3.下载文件
            4.断开连接
            '''
            conn.send(("登陆成功！请输入操作序号："
                      "%s"%msg).encode('utf-8'))
            num=(conn.recv(1024)).decode
            if num == '1':
                ser_opera.dir_list()
        if i ==2:
            conn.send("密码错误，请重新输入！".encode('utf-8'))
            continue
        if i ==3:
            conn.send("账号不存在，是否注册？Y/N".encode('utf-8'))
            a=(conn.recv(1024)).decode()
            if a == 'Y':
                ser_opera.register()
            else:
                conn.send("用户选择不注册或输入错误，连接断开！".encode('utf-8'))
                conn.close()
