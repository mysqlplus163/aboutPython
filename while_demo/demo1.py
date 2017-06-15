#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/8

# 猜年龄游戏

# 需求：
# 1.在程序里设定好你的年龄，然后启动程序让用户猜测，用户输入后，根据他的输入提示用户输入的是否正确，如果错误，提示是猜大了还是小了。
# 2.程序启动后，可以允许用户最多猜测三次，如果对了，就退出，3次如果都不对，也直接退出
# 3实现语言不限


age = 18
n = 3
while n > 0:
    input_age = input("猜猜看啊～：")
    if int(input_age) == age:
        print("猜对啦！")
        break
    elif int(input_age) > age:
        print("大了，再猜")
    elif int(input_age) < age:
        print("小了，再猜")
    n -= 1
else:
    print("三次机会用完了。")
