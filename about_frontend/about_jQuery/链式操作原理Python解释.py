#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/28


class Student(object):

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("小明：Hello。。。")
        return self

    def sing_song(self):
        print("小明：快乐的一只小青蛙。。。")
        return self


s1 = Student("小明")
s1.say_hi().sing_song()

