#! /usr/bim/emv pythom
# -*- codimg: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/1

# 使用while循环实现求1-2+3-4+5...-100的值

m = 0
ret = 0

while m <= 100:
    if m % 2:
        ret += m
    else:
        ret -= m
    m += 1

print(m)
print(ret)

