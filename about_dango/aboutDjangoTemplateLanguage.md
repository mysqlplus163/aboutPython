---
title: Django模板系统
date: 2017-11-27 10:00:00
tags: [Python, Django]
categories: Django
draft: true

---

本文解释了Django模板系统的语法。

<!--more-->

Django的模板语言旨在在功能强大和易用性之间取得平衡。
它的设计让那些习惯使用HTML的人感觉舒适。
如果你对其他基于文本的模板语言（如Smarty或Jinja2）熟悉的话，那么你就会发现它们像Django的模板系统一样。


## 模板

模板只是一个文本文件。它可以生成任何基于文本的格式（HTML，XML，CSV等）。
一个模板包含变量，当模板被处理时它们被替换为值，以及控制模板逻辑的`tags`（标签）。

下面是一个简单的基本模板。每个元素将在本文后面解释。

```jinja2
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
```