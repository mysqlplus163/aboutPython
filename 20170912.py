#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/12

# TODO: Git提交测试
import requests

ret = requests.get("http://video.study.163.com/edu-video/nos/flv/2016/11/08/1004394065_bec17c2d7b154e83ae31d5267bab4956_sd.flv?ak=99ed7479ee303d1b1361b0ee5a4abcee8d410c59b20d1952ce47bc3cbea6202329b1ebc7e944906139cb1a42f667619881ff0b41d7645d7f25d1cab58b2e2f1b0015e48ffc49c659b128bfe612dda086d65894b8ef217f1626539e3c9eb40879c29b730d22bdcadb1b4f67996129275fa4c38c6336120510aea1ae1790819de86e0fa3e09eeabea1b068b3d9b9b6597acf0c219eb000a69c12ce9d568813365b3e099fcdb77c69ca7cd6141d92c122af")
with open("xx.flv", "wb") as f:
    f.write(ret.content)

