#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/31

from itertools import chain

# 将多个迭代对象合成一个迭代对象
ret1 = list(chain([1, 2, 3], ("a", "b", "c")))
print(ret1)


# 将多个迭代对象合成一个迭代对象
ret2 = list(chain.from_iterable([[1, 2, 2, 4], [1, 2, 3, 4]]))
print(ret2)


print(dir(chain))

print(str("A"))
