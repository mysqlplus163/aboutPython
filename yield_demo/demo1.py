#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/16

import time


def tail(filename):
    with open(filename, "r", encoding="utf-8", buffering=1) as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                print("No new line...")
                time.sleep(3)


if __name__ == '__main__':
    while True:
        print(next(tail("demo1.txt")))
