#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

# with open("test.txt", "r") as f1:
#     print(f1.read())
# with open("test.txt", "r") as f2:
#     # print(f.tell())
#     # f.seek(27)
#     # f.write("abc")
#     f2.seek(5)
#     print(f2.read())
#     print(f2.tell())

# with open("temp", "a") as f:
#     print("hello")

# with open("test.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     print(f.tell())
#     data2 = f.read()
#
# print(data)
#
# print("=" * 50)
# print(data2)


# root_menu = {
#     "menu": "file,insert,design"
# }
#
# with open("test.txt", "w+") as f:
#     f.write("".join(list(root_menu.keys())) + ":")

import time
import random

while True:
    with open("temp2.txt", "a") as f:
        s = 10 * "{}".format(random.randrange(1, 10))
        f.write(s + "\n")
        time.sleep(1)
