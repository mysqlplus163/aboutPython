#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random


def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页！")


def timer(func):
    # func = index  # 这里写死了
    def wrapper():  # 定义一个新函数
        start_time = time.time()  # 开始时间
        func()  # 调用下index函数
        stop_time = time.time()  # 结束时间
        print("耗时{}秒。".format(stop_time - start_time))

    return wrapper

index = timer(index)  # 为了不修改调用方式，把新函数的返回值赋值给原函数名

index()

# 用一个 新函数 包了 原来的函数， 同时让 新函数 还叫 原来的函数的名字



