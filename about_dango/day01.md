# Django

## Web框架

自己实现一个简单的Web框架

实现最简单的功能

```python
import socket


s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.listen(5)

while True:
    conn, addr = s.accept()  # 暂时挂起
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"<h1>123123</h1>")
    conn.close()
```
然后引出有什么缺点？

不同的地址返回相同的内容！
怎么办？

创建一套自己的路由
不同的URL返回不同的内容

第一版：
```python
import socket


s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.listen(5)

while True:
    conn, addr = s.accept()  # 暂时挂起
    data = conn.recv(8096)
    data = str(data, encoding="utf-8")
    head, body = data.split("\r\n\r\n")
    value_list = head.split("\r\n")
    method, url, protocal = value_list[0].split(" ")

    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    if url == "/xxx":
        conn.send(b"xxx")
    else:
        conn.send(b"404")
```


第二版，把路由独立出来
```python
def f1():
    return "xxx->f1"


def f2():
    return "ooo->f2"


routers = [
    ("/xxx", f1),
    ("/ooo", f2),
]


def run():
    s = socket.socket()
    s.bind(("127.0.0.1", 8080))
    s.listen(5)
    while True:
        conn, addr = s.accept()  # 暂时挂起
        data = conn.recv(8096)
        data = str(data, encoding="utf-8")
        head, body = data.split("\r\n\r\n")
        value_list = head.split("\r\n")
        method, url, protocal = value_list[0].split(" ")

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for i in routers:
            if i[0] == url:
                func_name = i[1]
                break  # 找到一个不需要往下找了
        if func_name:  # 如果有这个函数
            result = func_name()
        else:
            result = "404"

        conn.send(bytes(result, encoding="UTF-8"))
        conn.close()
```

这第二版的路由本质上是什么呢？

是不是一个URL对应一个可执行函数，
不同的URL返回对应的Response

好，这个需求我们完善了，那还有没有其他的问题呢？

比如说，这是静态网站，数据都是写好在HTML文件里的
引申出来静态网站和动态网站的区别？

动态网站通常是有模板和数据这样的概念，一套共用的模板，

```python
import socket
import time


def f1():
    return "xxx->f1"


def f2():
    with open("tpl.html", "r") as f:
        source_data = f.read()
    result = source_data.replace("@@time@@", str(time.time()))
    return result


routers = [
    ("/xxx", f1),
    ("/ooo", f2),
]


def run():
    s = socket.socket()
    s.bind(("127.0.0.1", 8080))
    s.listen(5)
    while True:
        conn, addr = s.accept()  # 暂时挂起
        data = conn.recv(8096)
        data = str(data, encoding="utf-8")
        head, body = data.split("\r\n\r\n")
        value_list = head.split("\r\n")
        method, url, protocal = value_list[0].split(" ")

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for i in routers:
            if i[0] == url:
                func_name = i[1]
                break  # 找到一个不需要往下找了
        if func_name:  # 如果有这个函数
            response = func_name()
        else:
            response = "404"

        conn.send(bytes(response, encoding="UTF-8"))
        conn.close()

```

这些函数是用来做什么的呢？

是用来处理用户请求的，不同的请求返回不同的内容啊

现在这种方式，我在函数里面是没办法回去用户请求的一些数据什么的

那怎么办呢？我们可不可以用一个参数，来代替所有的用户请求？

用一个request参数来做这件事儿

```python


```

现在又有一个问题了，我们现在写的是一个静态网站，现在要写成一个动态网站。
现在数据是我们自己手写的，那我可不可以从数据库里找呢？

可以的

先来写一个简单的动态

用时间戳去替换

从这里引出来一个模板的概念


```python

```

再来个从数据库里查询数据的例子

使用pymysql

最后总结：

    1.HTTP 无状态 短连接
    2. 浏览器相当于 socket client端
       网站相当于 socket server端
    3. 自己写网站的话
       1. socket server端
       2. 根据URL不同执行不同的函数
          路由系统：
            URL -> 函数名
       3. 干活的函数
          具体的业务逻辑
       4. 返回 用户 字符串
          模板引擎渲染
            HTML充当模板 + 数据
          字符串



Django框架
    使用框架的话就要专注于业务层面的代码逻辑
    站在巨人的肩膀上去开发

    1. 安装
        pip3 install django

    2. 使用Django
        # django-admin startproject project名字  -> 在执行的目录就会生成一个同名文件夹

        进目录执行
        python3 manage.py runserver 127.0.0.0.1:8000

        然后就可以访问了

        上面是通过命令创建的

        下面介绍下如何使用PyCharm创建Django项目

        。。。

        目录介绍
        mysite
            misite
                - settings.py
                - url.py
                - wsgi.py
            manage.py xxx命令

        写一个最简单的例子
        在urls.py里面写函数
            from django.shorcut import HttpResponse
        引申出在单独的py文件里写函数

    接下来引到坑里面

        如何使用模板啊

        直接写文件名

    不行啊
    怎么办，用render

    from django.shortcut import render

    注意第一个参数要是request

    templates要与settings.py中的配置对应上



    手写登录的例子

        最基本的

        加样式
            直接在HTML上写样式
            写单独文件，如何导入？
                带大家看浏览器console里面的报错

                最后引出来如何设置静态文件目录

                在settings.py里面设置STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


最后总结一个Django项目的创建过程：
    1. 创建project
    2. 配置
        1. 模板文件路径

        2. 静态文件路径
    3. 我们刚开始学要做的事儿
        把settings.py里面的csrf中间件注释掉


把登录的例子讲完
不同的URL可以执行不用的函数
相同URL下面的不同请求方法也可以执行不同的代码

    request.method可以拿到请求的对象
    request.POST拿到请求的数据
        类似字典取值
        request.POST.get("xxx")

    登陆成功就跳转
        引出 redirect
    登录失败就返回当前页

    加报错信息