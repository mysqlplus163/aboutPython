#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/30

"""
something test...
"""
from django.shortcuts import render, HttpResponse


def base_test(r):
    return render(r, "anymore.html")


def l1(request):
    response = HttpResponse("OK, l1")
    response.set_signed_cookie("abc", 123456, salt="qnmd", max_age=30)
    return response


def l2(request):
    print(request.COOKIES)
    print(request.get_signed_cookie("abc", salt="qnmd"))
    res = HttpResponse("OK, l2")
    return res
