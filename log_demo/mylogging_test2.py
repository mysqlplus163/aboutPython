#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
MyLogging Test
"""

import time
import logging
import my_logging2 as _  # 导入自定义的logging配置

logger = logging.getLogger(__name__)  # 生成logger实例


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始。。。")
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(2)
    else:
        logger.debug("over range... time:{}".format(time.time()))
    logger.info("中文测试结束。。。")

if __name__ == "__main__":
    demo()
