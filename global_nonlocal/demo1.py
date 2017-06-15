#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/5


def scope_test():
    def do_local():
        spam = "local spam of do_local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam of do_nonlocal"

    def do_global():
        global spam
        spam = "global spam of do_global"
    spam = "test spam of scope_test"

    # do_local函数内部的赋值不影响scope_test作用域的spam
    do_local()
    print("After local assignment:", spam)

    # do_nonlocal函数内部的赋值影响scope_test作用域的spam，但是不影响全局的spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)

    # do_global函数内部的赋值影响全局的spam，但是不影响scope_test作用域的spam
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

