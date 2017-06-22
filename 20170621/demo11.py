#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random


def auth(func):
    def a():  # 内部函数 写 验证信息
        username = input("用户名：")
        password = input("密码：")
        if username == "andy" and password == "123":
            print("验证通过！")
            func()  # index()
        else:
            print("验证失败")
    return a


@auth  # --> index = auth(index)
def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页！")


@auth
def home():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问个人主页！")

# index()  # --> a()
home()


