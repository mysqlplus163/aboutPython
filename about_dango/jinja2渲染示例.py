#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/25

"""
jinja2演示示例
"""

import socket

import pymysql


def f1():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select uid, name, department_id from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(user_list)

    with open("jinja2示例.html") as f:
        source_data = f.read()

    # 使用jinja2模板渲染
    from jinja2 import Template
    template = Template(source_data)
    data = template.render(user_list=user_list)

    return data


def f2():
    return "ooo->f2"


routers = [
    ("/jinja2", f1),
    ("/ooo", f2),
]


def run():
    s = socket.socket()
    s.bind(("127.0.0.1", 8080))
    s.listen(5)
    while True:
        conn, addr = s.accept()  # 暂时挂起
        data = conn.recv(8096)
        data = str(data, encoding="utf-8")
        head, body = data.split("\r\n\r\n")
        value_list = head.split("\r\n")
        method, url, protocal = value_list[0].split(" ")

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for i in routers:
            if i[0] == url:
                func_name = i[1]
                break  # 找到一个不需要往下找了
        if func_name:  # 如果有这个函数
            response = func_name()
        else:
            response = "404"

        conn.send(bytes(response, encoding="UTF-8"))
        conn.close()


if __name__ == '__main__':
    run()