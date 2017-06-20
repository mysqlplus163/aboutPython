#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/13


# 使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和

# m = 0
# n = 2
# while n <= 100:
#     if n % 2 == 0:  # 偶数
#         m = m + n
#     else:
#         m = m - n
#     n += 1
# print(m)
#

# m2 = 0
# for i in range(2, 101):
#     if i % 2 == 1:  # 奇数
#         i = -i
#     m2 = m2 + i
# print(m2)


# 利用 map、lambda表达式 将所有是偶数的元素加100 l1 = [11, 22, 33, 44, 55]

l1 = [11, 22, 33, 44, 55]


# def func(arg):
#     return arg+1
#
# a = lambda x: x+1

# 三元运算
# name = alex if alex == "sb" else Rain

# x + 100 if x % 2 == 0 else x
ret = list(map(lambda x: x + 100 if x % 2 == 0 else x, l1))
print(ret)


def func(arg):
    arg.append(55)


li = [11, 22, 33, 44]

li = func(li)

print(li)
