#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/29

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restframework_demo.settings")
import django
django.setup()

from app01 import models

ret1 = models.Book.objects.all()
for i in ret1:
    print(i.days)

ret2 = models.Book.objects.filter(days__gt=100)
print(ret2)
