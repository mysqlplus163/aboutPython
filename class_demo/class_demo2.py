#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/9

class Pater():

    def __init__(self, current_page):
        self.current_page = current_page
        self.per_item = 10


    @property
    def start(self):
        val = (self.current_page - 1) * self.per_item
        return val

    @property
    def end(self):
        val = self.current_page * self.per_item
        return val


p = Pater(10)
print(p.start)
