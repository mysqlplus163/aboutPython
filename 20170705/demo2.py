#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
re.search
"""

import re  # 导入re模块

s = "life is short, you need Python."

# 不从字符串的开头匹配，而是检索整个字符串
# ret = re.search(r'Python', s)
# print(ret)
# print(ret.group())

ret = re.search(r'(?P<abc>.*) x (?P<name>.*)', s)
if ret:
    print(ret)
    print(ret.groups())
    print(ret.group("abc"))
else:
    print("没有匹配到")
# 确保ret是匹配到的对象，才对它调用group()
# print(ret)
# print(ret.group())
