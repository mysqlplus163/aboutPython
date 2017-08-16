#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/2

import logging

formater1 = logging.Formatter("%(asctime)s - %(levelname)s %(message)s")

fh1 = logging.FileHandler("test1.log")
fh2 = logging.FileHandler("test1.log")

ch = logging.StreamHandler()

fh1.setFormatter(formater1)
fh2.setFormatter(formater1)
ch.setFormatter(formater1)

logger1 = logging.getLogger("demo")

logger1.setLevel(10)

logger1.addHandler(fh1)
logger1.addHandler(fh2)
logger1.addHandler(ch)

logger1.error("error")
