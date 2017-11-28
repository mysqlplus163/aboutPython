#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/26


from django.shortcuts import render, redirect, HttpResponse


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def class_list(request):
    import pymysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, name from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "class_list.html", {"class_list": class_list})


def add_class(request):
    if request.method == "POST":
        new_class_name = request.POST.get("class_name")
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(name) VALUES (%s)", [new_class_name, ])
        conn.commit()
        conn.close()
        # return HttpResponse("OK")
        return redirect("/class_list/")
    else:
        return render(request, "add_class.html")


def delete_class(request):
    class_id = request.GET.get("class_id")
    import pymysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class WHERE id = %s", [class_id, ])
    conn.commit()
    conn.close()
    return redirect("/class_list/")


def edit_class(request):
    if request.method == "POST":
        class_id = request.POST.get("class_id")
        class_name = request.POST.get("class_name")
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set name=%s WHERE id =%s", [class_name, class_id, ])
        conn.commit()
        conn.close()
        return redirect("/class_list/")
    else:
        class_id = request.GET.get("class_id")
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, name from class WHERE id = %s", [class_id, ])
        class_record = cursor.fetchone()
        cursor.close()
        conn.close()

        return render(request, "edit_class.html", {"class": class_record})


def test(request):
    data = [
        {"age": 1},
        {"age": 2},
        {"age": 3}
    ]
    return render(request, "test.html", {"x": data, "y": "<h1>name</h1>"})