#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/21


class Bar(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<Bar: {}>".format(self.name)


a = Bar("alex")
print(a)
