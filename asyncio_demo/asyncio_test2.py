#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/20

"""
asyncio demo2
"""

import threading
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world! ({})".format(threading.currentThread()))
    yield from asyncio.sleep(1)
    print("Hello again! ({})".format(threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
