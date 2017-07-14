#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/3

"""
生成随机4位验证码
"""

import random


def get_code(n):
    """
    生成指定位数的随机验证码，包含数字和字母
    :param n: 随机验证码位数
    :return:
    """
    code = ""
    for i in range(n):
        number = random.randint(0, 9)  # 生成数字
        letter = chr(random.randint(65, 90))
        aim = random.choice([number, letter])
        code += str(aim)
    return code

if __name__ == '__main__':
    ret = get_code(4)
    print(ret)
