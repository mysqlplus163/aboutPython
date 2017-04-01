#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/28

"""
定制的admin base
"""
from django.http import HttpResponse
from django.shortcuts import render


class ModelAdminBase(object):
    add_form = None
    list_display = ()
    list_per_page = 20
    choice_fields = ()
    fk_fields = ()
    filter_horizontal = ()
    model = None
    onclick_fields = {}
    change_page_onclick_fields = {}

    readable_table = False
    search_fields = []
    readonly_fields = []

    default_actions = ["delete_selected", ]

    def delete_selected(self, request):
        """
        删除选中的项
        """
        selected_ids = request.POST.get("selected_ids")
        if selected_ids:
            selected_id_list = selected_ids.split(",")  # 逗号分割id字符串，得到id列表
        else:
            raise ValueError("nothing got selected")

        to_del_objs = self.model.objects.filter(id__in=selected_id_list)
        return render(request, "html", {"to_del_objs": to_del_objs})

    delete_selected.short_description = "删除选中的数据"


def register(admin_dic, model, admin_class):
    """
    注册admin
    :param admin_dic: 所有的注册在admin的表
    :param model: models里面的表
    :param admin_class: 要注册在admin里的model表
    """
    # 如果要注册的表能和models里面的表对应上就注册到admin_dic
    if model._meta.db_table not in admin_dic:
        admin_dic[model._meta.db_table] = admin_class  # ???为什么要用app名_表名的格式注册
    else:
        raise Exception
