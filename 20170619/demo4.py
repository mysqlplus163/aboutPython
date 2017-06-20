#! /usr/bin/env python
# -*- coding: utf-8 -*-


def foo(a, b):
    print(a)
    print(b)

# 按位置传参
# foo(1, 2)
# foo(2, 1)

# 按照关键字传参
# foo(a=10, b=20)
# foo(b=10, a=20)

# 混着用
# foo(1, b=2)

# foo(1, a=1, b=2)  # 不能这么写

foo(1, a=2)


