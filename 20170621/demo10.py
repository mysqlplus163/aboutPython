#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
# 装饰器的语法
# @装饰器的名字
# 被装饰的函数


def timer(func):
    def wrapper():  # 定义一个新函数
        start_time = time.time()  # 开始时间
        func()  # 调用下index函数
        stop_time = time.time()  # 结束时间
        print("耗时{}秒。".format(stop_time - start_time))
    return wrapper


@timer
def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页！")

index()
