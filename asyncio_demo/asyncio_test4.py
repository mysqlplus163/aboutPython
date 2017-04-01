#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/20

"""
asyncio demo4
利用asyncio的异步网络连接去获取sina、sohu、网易的网站首页
"""

import asyncio


async def wget(host):
    print("wget {}...".format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n" .format(host)
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print("{} header > {}".format(host, line.decode("utf-8").rstrip()))
    # 忽略body,关闭socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ["www.sina.com.cn", "www.sohu.com", "www.163.com"]]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
