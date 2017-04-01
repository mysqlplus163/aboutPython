#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/5

"""
生产者消费者模型 demo3
"""

import queue
import time
import threading


q = queue.Queue(10)


def producer():
    count = 0
    while True:
        print("做包子：{}".format(count))
        q.put("包子{}".format(count))
        count += 1


def consumer():
    while True:
        print("吃包子：", q.get())
        time.sleep(2)

p = threading.Thread(target=producer, )
c = threading.Thread(target=consumer, )


p.start()
c.start()
