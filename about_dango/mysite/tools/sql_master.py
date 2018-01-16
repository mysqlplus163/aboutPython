#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/27
import pymysql

# 定义一个数据库相关的配置项
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "passwd": "root1234",
    "db": "mysite",
    "charset": "utf8"
}


# 查询多条数据函数
def get_list(sql, args=None):
    conn = pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        passwd=DB_CONFIG["passwd"],
        db=DB_CONFIG["db"],
        charset=DB_CONFIG["charset"]
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


# 查询单挑数据函数
def get_one(sql, args=None):
    conn = pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        passwd=DB_CONFIG["passwd"],
        db=DB_CONFIG["db"],
        charset=DB_CONFIG["charset"]
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


# 修改记录
def modify(sql, args=None):
    conn = pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        passwd=DB_CONFIG["passwd"],
        db=DB_CONFIG["db"],
        charset=DB_CONFIG["charset"]
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


# 创建记录
def create(sql, args=None):
    conn = pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        passwd=DB_CONFIG["passwd"],
        db=DB_CONFIG["db"],
        charset=DB_CONFIG["charset"]
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    # 返回刚才创建的那条数据的ID
    last_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return last_id


class SQLManager(object):

    # 初始化实例方法
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            passwd=DB_CONFIG["passwd"],
            db=DB_CONFIG["db"],
            charset=DB_CONFIG["charset"]
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询多条数据
    def get_list(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    # 查询单条数据
    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    # 执行单条SQL语句
    def moddify(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 执行多条SQL语句
    def multi_modify(self, sql, args=None):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    # 创建单条记录的语句
    def create(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        last_id = self.cursor.lastrowid
        return last_id

    # 关闭数据库cursor和连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 进入with语句自动执行
    def __enter__(self):
        return self

    # 退出with语句块自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

