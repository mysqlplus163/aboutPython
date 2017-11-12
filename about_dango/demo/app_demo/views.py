#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/7

"""
这是上课要讲的增删改查的例子
"""
from django.shortcuts import render, redirect, HttpResponse
import pymysql


def class_list(request):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "class_list.html", {"class_list": class_list})


def add_class(request):
    if request.method == "POST":
        print(request.POST)
        new_class = request.POST.get("title")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(title) VALUE (%s)", new_class)
        conn.commit()
        conn.close()
        return redirect("/class_list/")
    else:
        return render(request, "add_class.html")


def delete_class(request):
    nid = request.GET.get("nid")
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class WHERE id = %s", [nid, ])
    conn.commit()
    conn.close()
    return redirect("/class_list/")


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, title from class WHERE id = %s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)
        return render(request, "edit_class.html", {"result": result})
    else:
        nid = request.POST.get("id")
        title = request.POST.get("title")
        print(nid, title)
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s WHERE id = %s", [title, nid])
        conn.commit()
        conn.close()
        return redirect("/class_list/")


# 往下是day03内容
def student_list(request):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select student.id, student.name, class.title from student left join class on student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "student_list.html", {"student_list": student_list})


# 增加学生
def add_student(request):
    if request.method == "POST":
        print("in add student...")
        name = request.POST.get("name")
        class_id = request.POST.get("class")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name, class_id) VALUES (%s, %s)", [name, class_id, ])
        conn.commit()
        conn.close()
        return redirect("/student_list/")

    else:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="TEST1", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        print(class_list)
        return render(request, "add_student.html", {"class_list": class_list})


# 编辑学生信息
from utils import sqlmanager
def edit_student(request):
    if request.method == "POST":
         nid = request.POST.get("id")
         name = request.POST.get("name")
         class_id = request.POST.get("class")
         print(nid, name, class_id)
         sqlmanager.exec_sql("update student set name=%s, class_id=%s where id=%s", [name, class_id, nid])
         return redirect("/student_list/")
    else:
        class_list = sqlmanager.get_list("select id, title from class")
        nid = request.GET.get("nid")
        student = sqlmanager.get_one("select id, name, class_id from student WHERE id=%s", nid)
        return render(request, "edit_student.html", {"class_list": class_list, "student": student})


def modal_add_class(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("title"))
        print(request.POST.get("data"))
        print(request.body)
        return HttpResponse("ok")
        title = request.POST.get("title", "")
        print(title)
        if len(title) > 0:
            sqlmanager.exec_sql("insert into class(title) VALUES (%s)", [title, ])
            return HttpResponse("ok")
        else:
            return HttpResponse("班级标题不能为空")

