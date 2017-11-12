# day02 单表增删改查

现在我们就要把前面学到的知识都全部用起来了




我们干讲的话有点难度了
没有业务逻辑驱动，写不下去

我们用一个简单的项目
学员管理：
    表：
        班级
        学生
        老师
    单表操作：
        增
        删
        改
        查
    一对多操作：
        增
        删
        改
        查
    多对多操作
        增
        删
        改
        查

Django基础


把前端的知识都收拾起来

那我们接下来就开始具体的看一下这个项目。

我们不管是在学习过程中包括在以后的工作中，写项目的时候，都要先分析再动手写代码

来看我们这个项目，因为是一个学院管理系统，

我们要创建好数据库，也就是设计好数据库表

那我们就一点一点看一些 我们这个表都应该存储些什么数据呢？


班级表
id   title
1    全栈4期
2    全栈5期



学员表
id  name  班级ID(FK)

1    xxx   1

老师表
id   name
1    林海峰
2    苑日天


现在的问题是，老师和学生什么关系？应该有关系么？

学生跟班级有关系，老师和班级有关系，这样关系就健全了


老师班级关系表：
id      老师ID        班级ID
1       1               1


让学生把上面几个表创建好

表创建好之后，就开始写项目了


带着一起用PyCharm创建一个Django项目

写代码

直接操作数据

代码写在哪里？ 之前都是写在urls里面不好，怎么办呢？

自己创建一个目录叫app01，blablabla...

第一个练习：
    列出所有的班级

    HTML + SQL -> views.py

    先展示出所有的班级，


    class_list -->  class_list


    接下来自己搞一个在页面上添加新班级的页面

    在urls.py里面加一个对应关系

    add --> add_class

    添加搞定了

    那就删除了

    删除  就在每一行后面加上一个按钮

    删除是不是分很多细分动作：
      1.


    就是再添加一个对应关系

    delete  -->  delete_class

    删除成功直接跳转回班级列表

    这里补充一下： 重定向是浏览器再发一次请求 （location:xxx.com）

    修改怎么搞？

```python

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("update class set title=%s where id = %s", [title, nid,])
conn.commit()
cursor.close()
conn.close()
```


作业：
按照班级表把老师表的增删改查做完

尝试着用模态框的方式把添加删除做完，再有能力的把编辑搞一下










