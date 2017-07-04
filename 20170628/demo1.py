#! /usr/bin/env python
# -*- coding: utf-8 -*-


def g():
    print("嘿, 生成器")
    print("嘿, 生成器")
    print("嘿, 生成器")
    print("嘿, 生成器")
    yield 1, 2, "abd"
    # return 1

ret = g()  # ret现在是一个生成器

# for i in ret:
#     print(i)

# print(next(ret))

x = next(ret)
print(x)

# print(ret.__next__())

# print(ret)

