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
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("data"))
        return HttpResponse("OK")
    else:
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


import json
def modal_edit_class(request):
    if request.method == "POST":
        class_id = request.POST.get("class_id")
        class_name = request.POST.get("class_name")
        if class_name:
            modify("update class set name=%s where id=%s", [class_name, class_id])
            ret = {"status": 0, "msg": None}
        else:
            ret = {"status": 1, "msg": "班级名称不能为空"}
        return HttpResponse(json.dumps(ret))


def modal_delete_class(request):
    ret = {"status": 0, "msg": "删除成功"}
    return HttpResponse(json.dumps(ret))

def magic(data):
    tmp = {}
    for i in data:
        if i["id"] not in tmp:
            i["class_list"] = [i["cname"], ]
            tmp[i["id"]] = i
        else:
            tmp[i["id"]]["class_list"].append(i["cname"])
    return list(tmp.values())

def teacher_list(request):
    if request.method == "POST":
        pass
    else:
        teacher_list_o = get_list("select teacher.id, teacher.name, class.name as cname from teacher LEFT JOIN teacher2class on teacher.id = teacher2class.teacher_id LEFT JOIN class ON teacher2class.class_id = class.id")
        teacher_list = magic(teacher_list_o)
        return render(request, "teacher_list.html", {"teacher_list": teacher_list})


from tools.sql_master import create, SQLManager
def add_teacher(request):
    if request.method == "POST":

        class_list = request.POST.getlist("class_id")
        teacher_name = request.POST.get("teacher_name")
        # 创建老师
        teacher_id = create("insert into teacher(name) VALUES (%s)", [teacher_name, ])
        # 更新teacher2class表
        # 多次链接，多次提交
        # for i in class_list:
        #     modify("insert into teacher2class(teacher_id, class_id) VALUES (%s, %s)", [teacher_id, i])
        #
        # # 一次链接，多次提交
        # db = SQLManager()
        # for i in class_list:
        #     db.moddify("insert into teacher2class(teacher_id, class_id) VALUES (%s, %s)", [teacher_id, i])
        # db.close()
        #
        # 一次链接，一次提交
        data_list = []
        for i in class_list:
            tmp = [teacher_id, i]
            data_list.append(tmp)

        db = SQLManager()
        db.multi_modify("insert into teacher2class(teacher_id, class_id) VALUES (%s, %s)", data_list)
        db.close()
        return redirect("/teacher_list/")


    else:
        class_list = get_list("select id, name from class")
        return render(request, "add_teacher.html", {"class_list": class_list})


def edit_teacher(request):

    if request.method == "POST":
        teacher_id = request.POST.get("teacher_id")
        class_ids = request.POST.getlist("class_id")
        # 更新
        db = SQLManager()
        teacher_class_ids = db.get_list("select class_id from teacher2class WHERE teacher_id=%s", [teacher_id, ])
        old_class_ids = [i["class_id"] for i in teacher_class_ids]
        # 粗暴更新
        del_id_list = []
        add_id_list = []
        for i in old_class_ids:
            del_id_list.append((teacher_id, i))
        for j in class_ids:
            add_id_list.append((teacher_id, j))
        db.multi_modify("DELETE from teacher2class WHERE teacher_id=%s AND class_id=%s", del_id_list)
        db.multi_modify("insert into teacher2class(teacher_id, class_id) VALUES (%s, %s)", add_id_list)
        db.close()
        return redirect("/teacher_list")

    else:

        teacher_id = request.GET.get("teacher_id")
        # db = SQLManager()
        # class_list = db.get_list("select id, name from class")
        # teacher_info = db.get_list("SELECT teacher.id, teacher.name, teacher2class.class_id FROM teacher  LEFT JOIN teacher2class ON teacher.id = teacher2class.teacher_id WHERE teacher.id=%s;", [teacher_id])
        # db.close()

        with SQLManager() as db:
            class_list = db.get_list("select id, name from class")
            teacher_info = db.get_list("SELECT teacher.id, teacher.name, teacher2class.class_id FROM teacher  LEFT JOIN teacher2class ON teacher.id = teacher2class.teacher_id WHERE teacher.id=%s;", [teacher_id])

        # print(db.get_list("select id, name from class"))
        ret = teacher_info[0]
        ret["class_ids"] = [ret["class_id"], ]
        for i in teacher_info[1:]:
            ret["class_ids"].append(i["class_id"])

        return render(request, "edit_teacher.html", {"class_list": class_list, "teacher": ret})
