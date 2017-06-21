#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/16

s = 'ab;cd|efg|hi,jkl|mn\opq;rst,uvw/xyz'
sign = ';|\/,'


def my_split(s, sign):
    s1 = [s]

    for i in sign:
        t = []
        print(list(map(lambda x: x.split(i), s1)))
        map(lambda x: s1.extend(x.split(i)), s1)
        print(t)
        # t = list(map(lambda x: t.extend(x.split(i)), s1))
        #
        print(t)
    # s = t
    # return s

# print(my_split(s, sign))

if __name__ == '__main__':
    t = []
    for i in sign:
        t.append(s.split(i))
    print(t)
    for j in t:
        pass

