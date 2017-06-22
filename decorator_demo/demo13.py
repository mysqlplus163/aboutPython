#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/21

import time
import random


def auth(func):
    def wrapper():
        name = input("用户名：").strip()
        password = input("密码：").strip()
        if name == "Andy" and password == "123":
            print("验证成功！")
            func()
        else:
            print("验证失败！")
    return wrapper


@auth
def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页。")


@auth
def home():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问个人主页。")


index()
home()

a = lambda x: x+1