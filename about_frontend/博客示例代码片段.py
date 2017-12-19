#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/6

while True:
    age = input("猜猜看啊：").strip()
    try:
        age = int(age)

        if age > 100:
            print("大了")
        elif age < 100:
            print("小了")
        else:
            print("对了")
            break
    except ValueError:
        print("错了")
