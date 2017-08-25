#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/16

"""
带参数的装饰器1
"""


# 三层嵌套1
def f1():

    def f2():
        name = "Andy"

        def f3():
            print(name)
        return f3

    return f2


# # 三层嵌套2
# def f1():
#     name = "Andy"
#     def f2():
#         def f3():
#             print(name)
#         return f3
#     return f2

# def f1(func):
#     def f2(*arg, **kwargs):
#         func(*arg, **kwargs)
#     return f2


# def d(name):
#     def f1(func):
#         def f2(*arg, **kwargs):
#             print(name)
#             func(*arg, **kwargs)
#         return f2
#     return f1



# @d(100)
# def hello(name):
#     print("Hello {}.".format(name))


# def foo(func):
#     def bar():
#         # 这里需要根据装饰器的参数做判断
#         func()
#     return bar

# 根据参数的不同，做不同的操作


if __name__ == '__main__':
    f = f1()  # f --> f2
    ff = f()  # ff --> f3
    ff()  # ff()  --> f3()  --> print(name)

