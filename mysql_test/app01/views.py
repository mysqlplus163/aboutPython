from django.shortcuts import render

# Create your views here.
import hashlib


def get_md5(s):
    s = str(s).encode("utf-8")
    h = hashlib.md5()
    h.update(s)
    return h.hexdigest()


if __name__ == "__main__":
    r = get_md5(4)
    print(r)

"""
c4ca4238a0b923820dcc509a6f75849b
c81e728d9d4c2f636f067f89cc14862c
eccbc87e4b5ce2fe28308fd9f2a7baf3
a87ff679a2f3e71d9181a67b7542122c

select host from app01_hostinfo group by md5;
select hostname from 表名 group by md5;
"""