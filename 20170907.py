#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/7

"""
1. 用户名不能和数据库中的用户名重复，不能和手机号重复

    登陆可以使用 用户名或手机号 + 密码 登陆

    用户名：
        中文 > 2 英文 > 4
"""

import re
# 判断用户名


def check_username(username):
    # if not re.search(r'[^\u4e00-\u9fa50-9a-zA-Z]+', username) and len(username) <= 16:
    #     if len(username) <= 20:
    #         if len(username) == len(bytes(username, "UTF-8")):
    #             print(username, "全是英文，没有中文")
    #             if len(bytes(username, "UTF-8")) < 3:
    #                 print("用户名最短为2个汉字或3个英文字符")
    #         elif len(bytes(username, "UTF-8")) == 3 * len(username):
    #             print(username, "全是中文，没有英文")
    #             if len(bytes(username, "UTF-8")) < 6:
    #                 print("用户名最短为2个汉字或3个英文字符")
    #         else:
    #             print(username, "中英文混合")
    #             if len(bytes(username, "UTF-8")) < 4:
    #                 print("用户名最短为2个汉字或3个英文字符")
    #     else:
    #         print("用户名不能超过20位字符")
    # else:
    #     print(username, "用户名不能含有非法字符")
    # print("=" * 80)

    if re.search(r'[^\u4e00-\u9fa50-9a-zA-Z]+', username):
        print("用户名不能含有非法字符")

    if get_username_length(username) < 3:
        print("用户名最短为2个汉字或3个英文字符")

    if get_username_length(username) > 20:
        print("用户名最长为10个汉字或20个英文字符")




    print(username, end=" ")
    ret = re.match(r'^[\u4e00-\u9fa5]{2,10}$|^[0-9a-zA-Z]{3,20}$|^[\u4e00-\u9fa5]{1,}[\u4e00-\u9fa50-9a-zA-Z]{1,}$|^[0-9a-zA-Z]{1,}[\u4e00-\u9fa5]{1,}$', username)
    print(ret)


def get_username_length(username):
    row_l = len(username)
    utf8_l = len(username.encode('utf-8'))
    return (utf8_l - row_l) / 2 + row_l


if __name__ == '__main__':
    username_list = ["村长", "cunzhang", "村长123", "_abc", "张三@", "\\u4e00", "\u4e00", "u4e00123", "\u4e00abc", "a一", "1好", "sasadakdhsakjdhashdlhfhladf;lhfahjjadfafa fda dafdfa", "一二三四五六七八九十", "0一二三四五六七八九十", "零一二三四五六七八九十"]

    for username in username_list:
        check_username(username)
