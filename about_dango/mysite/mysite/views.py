#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/26


from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
import pymysql
from functools import wraps


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        print(next_url)
        print("-" * 100)
        print(request.get_signed_cookie("login", salt="S7", default=None))
        print(request.get_signed_cookie("login", salt="S7", default=None) == "yes")
        if request.get_signed_cookie("login", salt="S7", default=None) == "yes":
            print("已经登录的用户...")
            return func(request, *args, **kwargs)
        else:
            print("没有登录的用户，跳转刚到登录页面...")
            return redirect("/login/?nexturl={}".format(next_url))
    return inner


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("password")
        print(username, passwd)
        if username == "alex" and passwd == "dashabi":
            print("登陆成功...")
            next_url = request.GET.get("nexturl")
            print(next_url)
            print("=" * 80)
            if next_url:
                response = redirect(next_url)
            else:
                response = redirect("/class_list/")
            response.set_signed_cookie("login", "yes", salt="S7")
            return response
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


@check_login
def class_list(request):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, name from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "class_list.html", {"class_list": class_list})


@check_login
def add_class(request):
    print(request.COOKIES)
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
    print(request.body)
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

@check_login
def student_list(request):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("SELECT student.id, student.name, class.name AS class_name from student LEFT JOIN class ON student.class_id = class.id;")
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, "student_list.html", {"students": student_list})


def add_student(request):
    # 如果是POST请求表示前端提交数据过来
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name, class_id) VALUES (%s, %s)", [student_name, class_id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/student_list/")
    # 前端不发送POST请求情况下默认返回新增学生信息页面
    else:
        # 因为我们新添加学生信息的时候需要指定所属的班级
        # 所以需要先查询出所有的班级信息，填充到页面上
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id, name from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, "add_student.html", {"class_list": class_list})


from tools.sql_master import get_list, get_one, modify
# def edit_student(request):
#     if request.method == "POST":
#         student_id = request.POST.get("student_id")
#         student_name = request.POST.get("student_name")
#         class_id = request.POST.get("class_id")
#         modify("update student set name=%s, class_id= %s WHERE id=%s", [student_name, class_id, student_id])
#         return redirect("/student_list/")
#     else:
#         student_id = request.GET.get("student_id")
#         class_list = get_list("select id, name from class")
#         student = get_one("select id, name, class_id from student where id=%s", [student_id, ])
#         return render(request, "edit_student.html", {"class_list": class_list, "student": student})

@check_login
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
    print(request.body)
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
        with SQLManager() as db:
            class_list = db.get_list("select id, name from class")
            teacher_info = db.get_list("SELECT teacher.id, teacher.name, teacher2class.class_id FROM teacher  LEFT JOIN teacher2class ON teacher.id = teacher2class.teacher_id WHERE teacher.id=%s;", [teacher_id])
        ret = teacher_info[0]
        ret["class_ids"] = [ret["class_id"], ]
        for i in teacher_info[1:]:
            ret["class_ids"].append(i["class_id"])
        return render(request, "edit_teacher.html", {"class_list": class_list, "teacher": ret})


def logout(request):
    rep = redirect("/login/")
    rep.delete_cookie("login")
    return rep

# 以下为二次更新

def delete_student(request):
    # 从GET请求的URL中取到要删除的学生ID
    student_id = request.GET.get("student_id")
    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 删除指定的学生
    sql = "delete from student WHERE id=%s;"
    # 执行SQL语句
    cursor.execute(sql, [student_id, ])
    conn.commit()
    conn.close()
    # 删除成功，跳转到学生列表页
    return redirect("/student_list/")

def edit_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        # 更新学生表的SQL
        sql = "update student set name=%s, class_id= %s WHERE id=%s;"
        # 连接数据库
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, [student_name, class_id, student_id])
        cursor.close()
        conn.close()
        # 更新完学生信息之后跳转到学生列表页面
        return redirect("/student_list/")
    else:
        # 要编辑学生信息就需要在页面上把当前学生的信息以及所有的班级信息都展示出来
        # 取到要编辑的学生的ID
        student_id = request.GET.get("student_id")
        # 连接数据库
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 取到所有的班级信息
        get_class_sql = "select id, name from class;"
        cursor.execute(get_class_sql)
        class_list = cursor.fetchall()
        get_student_sql = "select id, name, class_id from student where id=%s;"
        cursor.execute(get_student_sql, [student_id, ])
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, "edit_student.html", {"class_list": class_list, "student": student})


def teacher_list(request):
    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select teacher.id, teacher.name, class.name as cname from teacher LEFT JOIN teacher2class on teacher.id = teacher2class.teacher_id LEFT JOIN class ON teacher2class.class_id = class.id;"
    cursor.execute(sql)
    teacher_list_o = cursor.fetchall()
    # 将查询到的数据类型转换一下
    teacher_list = magic(teacher_list_o)
    return render(request, "teacher_list.html", {"teacher_list": teacher_list})


def delete_teacher(request):
    # 从GET请求的URL中取到要删除的老师ID
    teacher_id = request.GET.get("student_id")
    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 删除指定的老师
    sql = "delete from teacher WHERE id=%s;"
    # 执行SQL语句
    cursor.execute(sql, [teacher_id, ])
    conn.commit()
    conn.close()
    # 删除成功，跳转到老师列表页
    return redirect("/teacher_list/")


def add_teacher(request):
    pass


def search(request):
    if request.method == "POST":
        search_str = request.POST.get("search_str")
        print(search_str)
        print("=" * 120)
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root1234", db="mysite", charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        search_str = "%{}%".format(search_str)
        cursor.execute("select id, name from class where name LIKE %s;", [search_str, ])
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, "class_list.html", {"class_list": class_list})


def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request:
    :return:
    """
    if request.method == "POST":
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["file"].name
        # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for chunk in request.FILES["file"].chunks():
                # 写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")

