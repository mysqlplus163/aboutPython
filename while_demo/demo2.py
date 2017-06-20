#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/10


import sys
import time


if __name__ == '__main__':
    count = 0
    while count < 10:
        for i in range(10):
            sys.stdout.write("#")
            sys.stdout.flush()
            time.sleep(0.5)
        else:
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(0.5)
    count += 1
