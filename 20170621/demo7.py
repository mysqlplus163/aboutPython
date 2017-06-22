#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random


def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页！")


def wrapper(func):  # 定义一个新函数
    start_time = time.time()  # 开始时间
    func()  # 调用下index函数
    stop_time = time.time()  # 结束时间
    print("耗时{}秒。".format(stop_time - start_time))

# wrapper(index)
index = wrapper  #
index(index)  # 现在修改之后调用的时候需要传参数，这其实也是修改了调用方式

# 本身不需要参数（本身没有定义这个变量），但是内部又用到一个变量

