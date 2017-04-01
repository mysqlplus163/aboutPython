from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app01.custom_admin import enable_admin
from app01 import custom_admin
from app01 import forms
from app01 import models
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.http import HttpResponseNotFound, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import resolve


def table_change(request, table_name, obj_id):
    table_name = request.resolver_match.app_name + "_" + table_name
    print("table change:", table_name, obj_id)
    print(enable_admin)
    if table_name in enable_admin:  # 如果表名在admin中注册了
        admin_class = enable_admin[table_name]  # 获得models中的那个类
        print("admin_class", admin_class)
        obj = admin_class.model.objects.get(id=obj_id)  # 从数据库中获取到要修改的那个对象
        fields = []  # 定义一个前端展示的字段名的列表
        print("admin_class.model._meta:", admin_class.model._meta)
        print("=" * 50)
        print(admin_class.model._meta.fields)
        print(dir(admin_class.model._meta))
        for field_obj in admin_class.model._meta.fields:  # 这个表的所有字段，包括外键和一对一
            if field_obj.editable:  # 判断是不是可修改的字段（自带的方法，因为有的字段不支持编辑，比如ID）
                fields.append(field_obj.name)
        print("-" * 50)
        print(dir(admin_class.model._meta.many_to_many))
        print(admin_class.model._meta.many_to_many)
        for field_obj in admin_class.model._meta.many_to_many:  # 多对多的字段需要这么遍历
            fields.append(field_obj.name)
        # 创建动态的modelform
        model_form = forms.create_form(admin_class.model, fields, admin_class)

        if request.method == "POST":
            form_obj = model_form(request.POST, instance=obj)
            if form_obj.is_valid():
                form_obj.save()
        else:
            form_obj = model_form(instance=obj)
        return render(
            request,
            "index.html",
            {
                "form_obj":  form_obj,
            }
        )
    else:
        raise Http404(" url {} not found".format(table_name))


def table_add(request, table_name):
    print("table add:", table_name)
    if table_name in enable_admin:  # 如果表明在admin中注册了
        admin_class = enable_admin[table_name]
        fields = []
        for field_obj in admin_class.model._meta.fields:
            if field_obj.editable:  # ???
                fields.append(field_obj.name)
        for field_obj in admin_class.model._meta.many_to_many:
            fields.append(field_obj.name)
        # 如果没有特殊定制的form,就动态创建一个
        if not admin_class.add_form:
            model_form = forms.create_form(
                admin_class.model,
                fields,
                admin_class,
                form_create=True
            )
        # 否则使用指定的form
        else:
            model_form = admin_class.add_form
        if request.method == "POST":
            form_obj = model_form(request.POST)
            if form_obj.is_valid():
                form_obj.save()
                redirect_url = "{}/change/{}".format(request.path.strip("/add"), form_obj.instance.id)
                return redirect(redirect_url)
            if request.POST.get("_continue"):  # 添加另外一个
                form_obj = model_form()
        else:
            form_obj = model_form()
        return render(
            request,
            "table_add.html",
            {
                "form_obj": form_obj,
            }
        )
    else:
        raise Http404("url {} not found".format(table_name))


def table_del(request, table_name, obj_id):
    print("table del:", table_name)
    if table_name in enable_admin:  # 如果表明在admin中注册了
        admin_class = enable_admin[table_name]
        obj = admin_class.model.objects.get(id=obj_id)

        return render(
            request,
            "table_delete.html",
            {
                "model_name": admin_class.model._meta.verbose_name,
                "model_table_name": admin_class.model._meta.model_name,
                "model_db_table": admin_class.model._meta.db_table,
                "obj": obj,
                "app_label": obj._meta.app_label
            }
        )
    else:
        return Http404("url {} not found".format(table_name))


def index(request):
    print(resolve(request.path).app_name)
    print(request.resolver_match.app_name)
    print("=" * 50)
    print(dir(request.resolver_match))
    print(request.resolver_match.url_name)
    print(request.resolver_match.func)
    print(request.resolver_match.namespace)
    print(request.resolver_match.namespaces)
    print(request.resolver_match.view_name)
    return render(request, "base.html")
