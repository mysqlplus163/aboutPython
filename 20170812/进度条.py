#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12

import time

def func():
    n = 10
    while n < 100:
        print("#" * (n//10), end="\r", flush=True)
        n += 10
        time.sleep(0.2)


if __name__ == '__main__':
    func()
