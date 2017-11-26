## 自定义Web框架

通过Python标准库中的`wsgiref`模块开发一个自己的Web框架。

### 框架

```python
from wsgiref.simple_server import make_server


def index():
    return [b'index']


def login():
    return [b'login']


# 设置一个URL和函数的对应关系
url_func_map = (
        ('/index/', index),
        ('/login/', login),
    )


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # 设置HTTP响应的状态码和头信息
    url = environ['PATH_INFO']  # 取到用户输入的url
    func = None
    for item in url_func_map:
        if item[0] == url:
            func = item[1]  # 找得到对应函数
            break
    if func:
        return func()
    else:
        return [b'404 not found']


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

```

### 模板

再上一个步骤中，我们对于login和index返回给用户浏览器的都是一个简单的字符串，现实中我们浏览器输入网址，返回的一般都是一个HTML页面。
本质上还是发字符串，但是发的是HTML字符串。
所以我们直接读取我们的HTML文件的内容，发送给用户即可。

```python

```


## Web开发模式
由最初的静态页面到MVC模式，再到现在前端的MVVM模式，Web开发越来越追求便捷和高效。

### MVC

Model-View-Controller

### MVVM


[MVC、MVP和MVVM的区别](http://www.ruanyifeng.com/blog/2015/02/mvcmvp_mvvm.html)