#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/25

import os
import logging

log_path = os.path.join(os.getcwd(), "test.log")

simple_logger = logging.getLogger("simple")  # 设置一个simple logger
# simple_logger.setLevel(logging.DEBUG)  # 设置一下logger记录器的日志级别，默认是WARNING

fh = logging.FileHandler(log_path, "a")

formatter = logging.Formatter("%(asctime)s %(message)s %(levelname)s")
fh.setFormatter(formatter)

fh.setLevel(logging.DEBUG)  # 设置handler的日志级别，logger -> handler，所以logger记录器的级别要低于handler的

simple_logger.addHandler(fh)

simple_logger.debug("debug test")
simple_logger.info("info test")
simple_logger.warning("warning test")
simple_logger.critical("critical test")

