#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/8


"""
model form
"""

from django import forms
from app02 import models


class HostGroup(forms.ModelForm):
    h = forms.ModelMultipleChoiceField(queryset=models.HostInfo.objects.all())

    class Meta:
        model = models.HostGroup
        fields = ["name", "h"]
