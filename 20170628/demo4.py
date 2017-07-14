#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 倒计时的例子


def countdown(n):
    print("倒计时开始")
    while n > 0:
        yield n
        n = n - 1
    print("发射")

ret = countdown(5)  # 得到生成器
# print(next(ret))  # 打印倒计时开始"，暂停 返回n -->5
# print(next(ret))  # n = 4, 暂停 返回n -->4
# print(next(ret))  # n = 3, 暂停 返回n -->3
# print(next(ret))  # n = 2, 暂停 返回n -->2
# print(next(ret))  # n = 1, 暂停 返回n -->1
# print(next(ret))  # n = 0, 不满足while循环条件 打印 发射 ，抛出异常

# for i in ret:
#     print(i)

# for i in [5, 4, 3, 2, 1]:
#     print(i)
