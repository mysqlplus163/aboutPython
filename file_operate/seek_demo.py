#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/26

import time


def tail(arg):
    with open(arg, encoding="utf-8") as f:
        f.seek(0, 2)
        while True:
            f1 = f.readline().strip()
            if f1:
                yield f1
            else:
                print("out...")
                time.sleep(1)


if __name__ == "__main__":
    t = tail("temp2.txt")
    while True:
        print(next(t))
