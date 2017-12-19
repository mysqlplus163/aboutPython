#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/13

# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host=“你的数据库地址”, user=“用户名”,password=“密码”,database=“数据库名”,charset=“utf8”)
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
sql = "UPDATE USER1 SET age=%s WHERE name=%s;"
username = "Alex"
age = 80
try:
    # 执行SQL语句
    cursor.execute(sql, [age, username])
    # 提交事物
    conn.commit()
except Exception as e:
    # 有异常，回滚事物
    conn.rollback()
cursor.close()
conn.close()