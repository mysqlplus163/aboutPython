---
title: Django入门
date: 2017-09-10 10:00:00
tags: [Python, Django]
categories: Django

---

Django是Python中一个非常强大的Web框架。

<!--more-->

Django的内容非常多，在这里不能详尽的列出。


## 路由

1.单一路由
```python

url(r'^login/', views.login),

```

2.基于正则的路由匹配
```python

url(r'^login/', views.login),
url(r'^book/(\d*)', views.book),

```

3.添加额外参数
```python

url(r'^manage/(?P<name>\w*)', views.manage, {'id': 10}),

```
4.为路由匹配规则命名
```python

url(r'^home', views.home, name='home'),
url(r'^index/(\d*)', views.index, name='index'),

```

对路由匹配规则命名之后就可以在多处使用：
- 在模板文件中使用：`{% url 'index' 10 %}`

- 在函数中使用：`reverse('index', args=(10, )) `

- model也可以通过reverse来获取具体对象的路由

5.根据APP来进行路由分发
```python

url(r'^app01/', include('app01.urls')),

```

6.使用命名空间



## 模板

## model


## form


## MiddleWare(中间件)


## admin



