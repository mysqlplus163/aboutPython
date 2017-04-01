#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/11

"""
asyncio demo6
生产者消费者问题

"""

import threading
import queue

q = queue.Queue()


def producer(name):
    for i in range(10):
        print("<{}> 做完了[包子{}]。".format(name, i))
        q.put("包子{}".format(i))

    print("开始等包子卖完...")
    q.join()
    print("包子都卖完了...")


def consumer(name):
    while q.qsize() > 0:
        print("<{}> 买走了 [{}]。".format(name, q.get()))
        q.task_done()  # 包子卖完了


if __name__ == "__main__":
    p = threading.Thread(target=producer, args=("厨子", ))
    c = threading.Thread(target=consumer, args=("戏子", ))
    p.start()
    c.start()
