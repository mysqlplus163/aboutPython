#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/3


i = 0
name = input("name:").strip()

if name == "":
    print("...")
elif name == "1":
    print("1")
else:
    while True:
        for i in range(3):
            p = input("password:").strip()
            if i < 2:
                print("...")
            elif i == 2 and p:
                print("...")
                o = input("out?:").strip()
                if o.upper() != "N":
                    exit()
            i += 1

#
# i = 0
#
# while True:
#     for i in range(3):
#         name = input("name:").strip()
#         p = input("password:").strip()
#         if name == "":
#             print("...")
#         elif name == "1":
#             print("1")
#         elif i < 2:
#             print("...")
#         elif i == 2 and p:
#             print("...")
#             o = input("out?:").strip()
#             if o.upper() != "N":
#                 exit()
#         i += 1
