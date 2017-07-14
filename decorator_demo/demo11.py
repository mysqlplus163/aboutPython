#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/21

import time
import random

'''
def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页。")


def timer(func):  # 传一个func参数和下面func = index一样都是在my_index函数内部定义了一个局部变量
    # func = index  # 在外部函数定义一个局部变量
    def wrapper():  # 设置一个参数
        start_time = time.time()
        func()  # 在这个函数内部调用下func
        stop_time = time.time()
        print("耗时{}秒。".format(stop_time - start_time))
    return wrapper

index = timer(index)

index()
'''


def a(func):
    # func = index
    def b():
        print("开始")
        func()  # 相当于执行原来的index
        print("结束")
    return b


def c(func):  # 模拟一个登录验证的装饰器
    # func = index
    def b():
        username = input("用户名")


        password = input("密码").strip()
        if username == "Alex" and password == "123":
            func()  # 相当于执行原来的index
        else:
            print("验证失败")
    return b


@c
def home():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问个人主页。")


home()


#
# @a
# def index():
#     time.sleep(random.randrange(1, 5))  # 随机sleep几秒
#     print("欢迎访问首页。")

# x = a(index)
# x()


# index = a(index)
# index()














