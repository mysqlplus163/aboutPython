#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
re.sub
"""
import re
# s = "life is short, you need Python.  # 人生苦短，我用Python。"

# 字符串自带的replace()替换
# print(s.replace("# 人生苦短，我用Python。", ""))

# 删除#及后面的内容（把#及后面的字符替换成空字符串）
# s1 = re.sub(r'#.*$', "", s)
# print("去掉注释后：", s1)


# 示例2
# 将匹配的数字乘于2
def double(ret):
    num = int(ret.group("num"))  # 注意要转成int类型
    return str(num * 2)  # 将乘以2后的结果转成str类型

s = "1 + 2 = 3"
s1 = re.sub(r'(?P<num>\d+)', double, s)  # 分组命名匹配
print("re.sub替换后：", s1)
