#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/8

"""
sql管理
"""
import pymysql


# 进行sql查询
def get_list(sql, args=None):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


# 进行sql查询
def get_one(sql, args=None):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


# 执行sql语句
def exec_sql(sql, args=None):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    conn.close()