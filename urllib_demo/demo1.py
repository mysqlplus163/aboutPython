#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/1

import base64
from urllib.parse import unquote, quote
# import OpenSSL
#
# s = """
# -----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAioyKUZT4nlKXG8sjihdl
# vB6ZmdLmFioUv/sHlf9kmYjbqPxZkrwtLIw5XQmk3kRn3uua8Rk4Qh/Qn/vF0oFt
# WPO6sS3wxGKJZcrrFF3Wz9l5SAYwK++DWzpxRqSWtJ6qrDw0UZuWZ8SKG8E8GVRB
# A6FChu9pyC386ql7nts4TZFWy3nY9ycGbXL8Imhd1UWujtiqzP7vEkkzCb+nDo1U
# LKs06UkqWVDUTJza5OTDntvZ5ZiZRjfsVhIW/sS0+TO5gat0QCxkRoEdmic0Mz3P
# 8H0PKzHbXp4wuDkLhE4snPyQsiAl37ZnXeB/51mNFlF7ewvTmk3zS0THrJqXpeGj
# RQIDAQAB
# -----END PUBLIC KEY-----
# """
#
# with open("public.pem", "rb") as f:
#     b = f.read()
# print(b)
# a = OpenSSL.crypto.load_publickey(OpenSSL.crypto.FILETYPE_PEM, b)
#
# print(a)

ptoken = "WWuJWU9hLhFUU55wNqHFgoubad6FbpvxiXFVTSFzSDUmeVeHF4E%2Fo4MCtOKvGxev1T%2FPl6KurL6ECYp5m5q7mNzAJiLTujF6HvAbUj1Xs0m6JBdaL7ETDT03FgY0pkctmET74P7JZtcI74JNwQMPOsckKeB1jGULOCzmIUcA4f9R1Mi2vwiht3%2BoyBadI11uyax3epLLHmXqKTtYJoHRg0wDt1VsHMh4sHK%2Bw7U1VS2hLMdTsNSVmEf9XAfO%2BkEcW8yc%2B2VQ4P9t4x5ZUsfKGLGN8eZJJoXS1IYn7dgH2ip9EYVsqWGiayLKZ78HWSV8EUuUbbgZAyprEoFwHi7xXQ%3D%3D"
print(unquote(ptoken))
print("-" * 120)
url_str = unquote(ptoken).encode("utf-8")
print(url_str)
print("=" * 120)
base64_str = base64.b64decode(url_str)
print(base64_str)

msg = "Original Text: <em>jiajiping@sogou-inc.com ||| 1400205722165 |||  Hello World!无意义明文串</em><hr/>"
ret = quote(msg)
print(ret)
ret = base64.b64encode(ret.encode())
print(ret)
print(ret.decode("gbk").encode("utf-8"))
