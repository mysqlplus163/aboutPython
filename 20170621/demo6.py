#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random


def index():
    start_time = time.time()

    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页！")

    stop_time = time.time()
    print("耗时{}秒。".format(stop_time - start_time))

index()
