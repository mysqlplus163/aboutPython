#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import logging
logger = logging.getLogger(__name__)


def func(s):
    try:
        assert isinstance(s, str)
    except AssertionError as e:
        print(str(e))
        logger.debug(str(e))
    print(s)
    print("over")


def main():
    func(1.1)


if __name__ == "__main__":
    main()
