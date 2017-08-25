#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/16

"""
带参数的装饰器3 使用类
"""


class D(object):
    def __init__(self, a=None):
        self.a = a
        self.mode = "装饰"

    def __call__(self, *args, **kwargs):
        if self.mode == "装饰":
            self.func = args[0]  # 默认第一个参数是被装饰的函数
            self.mode = "调用"
            return self
        # 当self.mode == "调用"时，执行下面的代码（也就是调用使用类装饰的函数时执行）
        if self.a:
            print("欢迎来到{}页面。".format(self.a))
        else:
            print("欢迎来到首页。")
        self.func(*args, **kwargs)


@D()
def index(name):
    print("Hello {}.".format(name))


@D("电影")
def movie(name):
    print("Hello {}.".format(name))



# def foo(func):
#     def bar():
#         # 这里需要根据装饰器的参数做判断
#         func()
#     return bar

# 根据参数的不同，做不同的操作


if __name__ == '__main__':
    index("Andy")
    movie("Andy")
