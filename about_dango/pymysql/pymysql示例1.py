#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/9

import pymysql

username = input("用户名>>:")
password = input("密码>>:")

conn = pymysql.connect(host="localhost", user="root", password="root1234", database="s8", charset="utf8")
cursor = conn.cursor()

sql = "select * from userinfo where username='%s' and password='%s'" %(username, password)
print(sql)
ret = cursor.execute(sql)
print(ret)

cursor.close()
conn.close()

if ret:
    print("登陆成功")
else:
    print("登录失败")

