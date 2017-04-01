#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/22

"""
彩色输出/color print

color设置格式说明：
color = \033[显示方式;前景色;背景色m

code:
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见

说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
"""

END = '\033[0m'

# standard color  标准颜色
BLACK = '\033[0;30;0m'  # <==> \033[30m
RED = '\033[0;31;0m'
GREEN = '\033[0;32;0m'
YELLOW = '\033[0;33;0m'
BLUE = '\033[0;34;0m'
PURPLE = '\033[0;35;0m'
CYAN = '\033[0;36;0m'
WHITE = '\033[0;37;0m'

# highlight color  高亮显示
RED_H = '\033[1;31m'  # <==> '\033[1;31;1m'
GREEN_H = '\033[1;32;1m'
YELLOW_H = '\033[1;33;1m'
BLUE_H = '\033[1;34;1m'
PURPLE_H = '\033[1;35;1m'
CYAN_H = '\033[1;36;1m'
WHITE_H = '\033[1;37m'


def color_print(s, color="RED"):
    print(globals()[color.upper()], s, END)


if __name__ == '__main__':
    print(RED, "我的颜色", END)
    print(RED_H, "我的颜色", END)
    print('RED', "我的颜色", 'END')
    color_print("你好啊，我的哥。", "yellow")

