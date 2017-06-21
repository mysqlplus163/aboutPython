#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/21

import time
import random


def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页。")


def home():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问个人主页。")


def timer(func):  # 传一个func参数和下面func = index一样都是在my_index函数内部定义了一个局部变量
    def wrapper():  # 设置一个参数
        start_time = time.time()
        func()  # 在这个函数内部调用下func
        stop_time = time.time()
        print("耗时{}秒。".format(stop_time - start_time))
    return wrapper

index = timer(index)
index()
home = timer(home)
home()
