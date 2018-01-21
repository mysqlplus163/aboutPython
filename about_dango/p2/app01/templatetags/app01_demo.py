#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/17

from django import template
register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "")


@register.filter(name="addSB")
def add_sb(value):
    return "{} SB".format(value)


@register.simple_tag(name="plus")
def plus(a, b, c):
    return "{} + {} + {}".format(a, b, c)
