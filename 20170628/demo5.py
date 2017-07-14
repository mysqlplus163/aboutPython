#! /usr/bin/env python
# -*- coding: utf-8 -*-


def countdown(n):
    print("倒计时开始")
    while n > 0:
        yield n
        n = n - 1
    print("发射")

# ret = countdown(5)  # 得到生成器
# print(next(ret))
# print(next(ret))
# print(" == for == ")
# for i in ret:
#     print(i)

# 一次性，不能后退


print(next(countdown(5)))
print(next(countdown(5)))
ret = countdown(5)
print(next(ret))
ret = countdown(5)
print(next(ret))



# print(countdown(5), countdown(5))
