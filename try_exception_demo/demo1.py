#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/13


try:
    data = {"a": "b"}
    data["c"]
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)


try:
    l = [1, 2, 3, 4]
    l[4]
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)
