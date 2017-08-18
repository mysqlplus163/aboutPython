#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/16

"""
带参数的装饰器
"""

def d(arg):
    def foo(func):
        def bar(*args, **kwargs):
            print(arg)
            func(*args, **kwargs)
        return bar
    return foo

@d(100)
def hello(name):
    print("Hello {}.".format(name))


# def foo(func):
#     def bar():
#         # 这里需要根据装饰器的参数做判断
#         func()
#     return bar

# 根据参数的不同，做不同的操作


if __name__ == '__main__':
    hello("Andy")
