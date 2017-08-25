#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/20

"""
装饰类
"""


# 定义一个类装饰器
class D(object):
    def __call__(self, cls):
        class Inner(cls):
            # 重写被装饰类的f方法
            def f(self):
                print("Hello Andy.")
        return Inner


@D()
class C(object):  # 被装饰的类
    # 有一个实例方法
    def f(self):
        print("Hello world.")


if __name__ == '__main__':
    c = C()
    c.f()
