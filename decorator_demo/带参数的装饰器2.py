#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/16

"""
带参数的装饰器
"""


def d(a=None):  # 定义一个外层函数，给装饰器传参数--role
    def foo(func):  # foo是我们原来的装饰器函数，func是被装饰的函数
        def bar(*args, **kwargs):  # args和kwargs是被装饰器函数的参数
            # 根据装饰器的参数做一些逻辑判断
            if a:
                print("欢迎来到{}页面。".format(a))
            else:
                print("欢迎来到首页。")
            # 调用被装饰的函数，接收参数args和kwargs
            func(*args, **kwargs)
        return bar
    return foo


@d()
def index(name):
    print("Hello {}.".format(name))


@d("电影")
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
