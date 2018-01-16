#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/16

"""
URLConf的一些测试
"""
from django.shortcuts import HttpResponse, render
from django.core.urlresolvers import reverse


def url_test(request, *args):
    print(args)
    print(reverse("booktest", args=("2018",)))

    # return HttpResponse("OK")
    return render(request, "view02/view02.html")
