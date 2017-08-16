#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/13


# try:
#     data = {"a": "b"}
#     data["c"]
# except IndexError as e:
#     print("IndexError", e)
# except KeyError as e:
#     print("KeyError", e)

def func():
    l = [1, 2, 3, 4]
    return l[4]

def f2():
    return func()

def bar():
    try:
        ret = f2()
        print(ret)
    except IndexError as e:
        print("IndexError", e)
    except KeyError as e:
        print("KeyError", e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bar()
