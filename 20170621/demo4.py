#! /usr/bin/env python
# -*- coding: utf-8 -*-


def foo():
    s = "Hello world!"
    def bar():
        print(s)
        print("ssss")
    return bar

func = foo()
print(func.__closure__)
