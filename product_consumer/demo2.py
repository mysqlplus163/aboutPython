#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/5

"""
生产者消费者模型 demo2
"""

import queue
import threading


q = queue.Queue(10)


def producer():
    count = 0
    while True:
        print("做包子：{}".format(count))
        q.put("包子{}".format(count))
        count += 1


def consumer():
    while q.qsize() > 0:
        print("吃包子：", q.get())

p = threading.Thread(target=producer, )
c = threading.Thread(target=consumer, )


p.start()
c.start()
