#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/20

"""
Python3.5中引入了新语法async和await，让coroutine的代码更简洁易读

使用新语法：
1. 把之前的@asyncio.coroutine替换为async写在方法声明前
2. 把yield from替换为await

"""
import asyncio


# 原来Python3.4的写法
@asyncio.coroutine
def hello_old():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 使用Python3.5中新的语法
async def hello_new():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

