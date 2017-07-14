#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/25

import os
import logging

# log_path = os.path.join(os.getcwd(), "test.log")

logging.basicConfig(level=logging.DEBUG)

simple_logger = logging.getLogger("simple")  # 设置一个simple logger
simple_logger.setLevel(level=logging.DEBUG)
print(simple_logger.getEffectiveLevel())


simple_logger.debug("debug test ...")
simple_logger.info("info test ...")
simple_logger.warning("warning test ...")
simple_logger.critical("critical test ...")
