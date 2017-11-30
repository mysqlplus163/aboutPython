#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/30

from django.core.signing import Signer
from django.utils import baseconv
import time
from django.utils.encoding import force_bytes, force_str, force_text


class S7Signer(Signer):

    def timestamp(self):
        return baseconv.base62.encode(int(time.time()))

    def sign(self, value):
        value = force_str(value)
        value = ">>>" + value + "<<<"
        return value

    def unsign(self, value, max_age=None):
        return value[3:-3]
