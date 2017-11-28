#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/26


from django.shortcuts import render, redirect, HttpResponse
import pymysql


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("password")
        if username == "alex" and passwd == "dashabi":
            return redirect("/class_list/")
    else:
        return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def class_list(request):
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
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(name) VALUES (%s)", [new_class_name, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/class_list/")
    else:
        return render(request, "add_class.html")


def delete_class(request):
    class_id = request.GET.get("class_id")
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
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set name=%s WHERE id =%s", [class_name, class_id, ])
        conn.commit()
        conn.close()
        return redirect("/class_list/")
    else:
        class_id = request.GET.get("class_id")
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

def student_list(request):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("SELECT student.id, student.name, class.name AS class_name from student LEFT JOIN class ON student.class_id = class.id;")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "student_list.html", {"students": student_list})


def add_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        print(student_name, class_id)
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name, class_id) VALUES (%s, %s)", [student_name, class_id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/student_list/")
    else:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, name from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, "add_student.html", {"class_list": class_list})


from tools.sql_master import get_list, get_one, modify
def edit_student(request):

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        modify("update student set name=%s, class_id= %s WHERE id=%s", [student_name, class_id, student_id])
        return redirect("/student_list/")
    else:
        student_id = request.GET.get("student_id")
        class_list = get_list("select id, name from class")
        student = get_one("select id, name, class_id from student where id=%s", [student_id, ])
        return render(request, "edit_student.html", {"class_list": class_list, "student": student})


def modal_add_class(request):
    if request.method == "POST":
        class_name = request.POST.get("class_name")

        if class_name:
            modify("insert into class(name) VALUES (%s)", [class_name, ])
            return HttpResponse("OK")
        else:
            return HttpResponse("班级名称不能为空")
    else:
        return HttpResponse("不OK")

