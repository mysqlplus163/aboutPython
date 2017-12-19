#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/13

"""
a pymysql demo
"""
import pymysql


# TODO: 上传之前删掉密码
conn = pymysql.connect(host="127.0.0.1", user="root", password="root1234", database="TEST1", charset="utf8")
cursor = conn.cursor()

# try:
#     sql = "insert into user1(name, password) VALUES (%s, %s);"
#     rows = cursor.executemany(sql, [("egon1", "123"), ("alex", "123"), ("Bob", "123")])
#     conn.commit()
# except Exception as e:
#     conn.rollback()
# cursor.close()
# conn.close()

# sql = "insert into user1(name, password) VALUES (%s, %s);"
# rows = cursor.executemany(sql, [("egon1", "123"), ("alex", "123"), ("Bob", "123")])
# conn.commit()
# cursor.close()
# conn.close()

# sql = """
# CREATE TABLE USER1 (
#   id INT auto_increment PRIMARY KEY ,
#   name CHAR(10) NOT NULL UNIQUE,
#   age TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;
# """
# ret = cursor.execute(sql)
# cursor.close()
# conn.close()
#
# print(ret)


# 增
# sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
# username = "Alex"
# age = 18
# cursor.execute(sql, [username, age])
# conn.commit()
# cursor.close()
# conn.close()

# 删
# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="你的数据库地址", user="用户名",password="密码",database="数据库名",charset="utf8")# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# sql = "DELETE FROM USER1 WHERE id=%s;"
# try:
#     cursor.execute(sql, [4])
#     # 提交事务
#     conn.commit()
# except Exception as e:
#     # 有异常，回滚
#     conn.rollback()
# cursor.close()
# conn.close()

# 改
# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="你的数据库地址", user="用户名",password="密码",database="数据库名",charset="utf8")# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 修改数据的SQL语句
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

# 查
# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="你的数据库地址", user="用户名",password="密码",database="数据库名",charset="utf8")# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 查询数据的SQL语句
sql = "SELECT id,name,age from USER1 WHERE id=1;"
# 执行SQL语句
cursor.execute(sql)
# 获取单条查询数据
ret = cursor.fetchone()
cursor.close()
conn.close()
# 打印下查询结果
print(ret)


# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="你的数据库地址", user="用户名",password="密码",database="数据库名",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
data = [("Alex", 18), ("Egon", 20), ("Yuan", 21)]
try:
    # 批量执行多条插入SQL语句
    cursor.executemany(sql, data)
    # 提交事物
    conn.commit()
except Exception as e:
    # 有异常，回滚事务
    conn.rollback()
cursor.close()
conn.close()