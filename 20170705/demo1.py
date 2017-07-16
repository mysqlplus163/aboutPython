#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
re.match
"""

import re  # 导入re模块

s = "life is short, you need Python."

# ret = re.match(r'life', s)
# print(ret)
# print(ret.span())

# 忽略大小写的标志位
# ret = re.match(r'Life', s, re.IGNORECASE)  # re.I
# print(ret)

# ret = re.match(r'Python', s)
# print(ret)

# 组
# ret = re.match(r'(life)', s)
# print(ret.group())  # 通过.group()可以获取到具体的匹配项
# print(ret.groups())
#
# ret2 = re.match(r'(.*) is (.*)', s)
# print(ret2.groups())
# print("第一个组:", ret2.group(1))
# print("第二个组:", ret2.group(2))

# 分组命名匹配
ret = re.match(r'(?P<abc>.*) is (?P<name>.*)', s)
if ret:
    print("匹配到啦")
    print('ret.group(1):', ret.group(1))
    print('ret.group("abc"):', ret.group("abc"))
    print('ret.group("name"):', ret.group("name"))
    print(ret.groups())
else:
    print("没有匹配到")

