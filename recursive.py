#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
赵慧喆question
"""


def func(n, num):
    num += 1
    n *= num
    print("乘法结果：", n)
    if num > 5:
        return n
    print("n:", n)
    print("num:", num)
    func(n, num)  # 这里不加return，就不会把返回值返回到上一层（当第5次调用func的时候，触发num>5，此时return 的n没法传给第四次的func)

r = func(1, 1)
print(r)


def l1(n):
    print("这是l1")
    return n


def f1():
    l1(1)  # l1()是有return值的，这里只写一个l1()，他的返回值f1()是收不到的。递归也是一样的，只不过递归调用的是自己，这里调用的是l1()

ret1 = f1()  # 没有返回值，ret默认就是None
print(ret1)


"""
同理，看下面这个

"""

def l2(n):
    n -= 1
    print("这是l2")
    return n


def f2(n):
    l2(n)  # 这里l2是单独的作用域，l2把n -= 1/如果写成n = l2(n)，就相当于把l2()的返回值赋值给了f2()中的n
    print(n)  # 这里打印出来的n还是2
    if n == 1:  # 不成立，所以不运行
        return n
    l2(n)  # 没有接受l2()的返回值，所以f2()也没有返回值

ret2 = f2(2)
print(ret2)

"""
return 就是把右边的数(变量或者函数的返回值)返回给他的调用者
return func()，就相当于  a = func(),return a   这两语句
"""


# 1*2+3*4+...+ 99*100
def func(n=1):
    ret = n * (n + 1)
    if n < 100-2:
        return ret + func(n+2)
    else:
        return ret
print(func(1))

