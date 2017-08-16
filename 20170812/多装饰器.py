#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/15

"""
多装饰器装饰同一个函数时的执行顺序
"""


def d1(func):
    print("d1")

    def inner1():
        print("inner1")
        return "<i>{}</i>".format(func())

    return inner1


def d2(func):
    print("d2")

    def inner2():
        print("inner2")
        return "<b>{}</b>".format(func())

    return inner2


@d1
@d2
def index():
    return "Hello Andy"

# index = d2(index)  ==> print("d2") ==> index = inner2
# index = d1(index)  ==> print("d1") ==> index = d1(inner2) ==> inner1

ret = index()  # 调用index() ==> inner1()  ==> <i>inner2()</i>  ==> <i><b>inner1()</b></i> ==> <i><b>Hello Andy</b></i>
print(ret)
