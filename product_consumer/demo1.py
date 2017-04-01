#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/5

"""
生产者消费者模型 demo1
"""

import queue
import threading


q = queue.Queue(10)


def producer():
    for i in range(10):
        q.put("包子{}".format(i))


def consumer():
    while q.qsize() > 0:
        print("吃包子：", q.get())

p = threading.Thread(target=producer, )
c = threading.Thread(target=consumer, )


p.start()
c.start()
