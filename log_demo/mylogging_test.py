#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
MyLogging Test
"""

import time
import logging
import my_logging  # 导入自定义的logging配置
import my_logging_demo2

logger = logging.getLogger('mmmm')  # 生成logger实例


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始。。。")
    for i in range(1000):
        logger.debug("中文测试-哈哈哈-哈哈哈哈i:{}".format(i) * 100)
        time.sleep(0.5)
    else:
        logger.debug("over range... time:{}".format(time.time()))
    logger.info("中文测试结束。。。")

if __name__ == "__main__":
    my_logging.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置
    demo()
    my_logging_demo2.demo()

