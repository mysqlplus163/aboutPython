#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/21

import re

# text = 'This is some text -- with punctuation.\nA second line.'
# pattern = r'(^\w+)|(\w+\S*$)'
# single_line = re.compile(pattern)
# multiline = re.compile(pattern, re.MULTILINE)
#
# print('Text:\n  {!r}'.format(text))
# print('Pattern:\n  {}'.format(pattern))
# print('Single Line :')
# for match in single_line.findall(text):
#     print('  {!r}'.format(match))
# print('Multline    :')
# for match in multiline.findall(text):
#     print('  {!r}'.format(match))

text2 = 'A first line.\nA second line.'

# pattern2 = r'^A'
#
# single_line = re.compile(pattern2)
# multiline = re.compile(pattern2, re.MULTILINE)
#
# print('Text:\n  {!r}'.format(text2))
# print('Pattern:\n  {}'.format(pattern2))
#
# print('Single Line :')
# for match in single_line.match(text2).group():
#     print('  {!r}'.format(match))
#
# print('Multline    :')
# for match in multiline.match(text2).group():
#     print('  {!r}'.format(match))

ret = re.findall(r'^A', text2, flags=re.MULTILINE)
print(ret.group())



