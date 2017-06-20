#! /usr/bin/env python
# -*- coding: utf-8 -*-


def bar():
    print("in bar...")
    print("Hello world!")



def foo():
    print("in foo...")
    bar()


foo()
