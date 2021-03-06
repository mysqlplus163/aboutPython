#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/20

"""
asyncio demo
"""

import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
