#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/11

"""
第一天
"""
from django.shortcuts import HttpResponse, render, redirect

def test1(request):
    return HttpResponse("OK")


def test2(request):
    return render(request, "view1Test.html", {
        "value": "aaa",
        "user_list": [4, 5, 6],
        "black_list": [1, 2, 3],
        "some_list": ["a", "b", "c", "d"],
        "foo_list": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    })


def test3(request):
    return redirect("http://www.luffycity.com/")
