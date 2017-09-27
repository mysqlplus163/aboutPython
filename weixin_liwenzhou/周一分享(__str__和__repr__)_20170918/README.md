# `__str__` VS `__repr__`

在上周一的文章里我说了下我所理解的面向对象。
由于本人能力所限，只能算是勉强介绍下面向对象编程的特点，纯粹是抛砖引玉，希望大家多多留言交流。

今天的文章顺着上周一的话题，说一说Python类中的`__str__`和`__repr__`方法。

Python中我们通过将一类事物的特性抽象出来，定义一个类。然后通过这个类实例化得到很多相应的对象。

首先我们定义一个`Car`类。

```python
>>> class Car(object):
...     def __init__(self, brand, color):
...         self.brand = brand  # 品牌
...         self.color = color  # 颜色
...
>>>
```

然后我们实例化一个Car对象：
```python
>>> c1 = Car("Audi", "red")  # 实例化
>>> c1  # 直接输入对象
<__main__.Car object at 0x000001F151770A20>
>>> print(c1)  # 打印对象
<__main__.Car object at 0x000001F151770A20>
```

我们在定义类的过程中，需要想办法让我们的类实例更明确和通俗易懂。
很显然，上面的输出结果既不明确，也不通俗易懂。

像这种情况，我们就可以通过定义`__str__`和`__repr__`方法，来让我们的自定义类实例可读性更好、更明确。

## `__str__`和`__repr__`介绍

那`__str__`和`__repr__`方法究竟是什么呢？

我们先来看一下下面的代码：
```python
>>> class Car(object):
...     def __init__(self, brand, color):
...         self.brand = brand
...         self.color = color
...
...     def __str__(self):
...         return "__str__ in Car"
...
...     def __repr__(self):
...         return "__repr__ in Car"
...
>>> c1 = Car("Audi", "red")
>>> print(c1)
__str__ in Car
>>> c1
__repr__ in Car
```

通过上面的代码我们就能够很清楚的发现：
当我们使用print(c1)时，实际上是执行了c1的`__str__`方法。直接输入C1输出的是调用`__repr__`方法的结果。

## `__str__`和`__repr__`的使用

通过上面的代码，我们可以发现通过使用`__str__`和`__repr__`方法可以使我们的实例对象更通俗易懂。
```python
>>> class Car(object):
...     def __init__(self, brand, color):
...         self.brand = brand
...         self.color = color
...
...     def __str__(self):
...         return "a {} {} Car".format(self.color, self.brand)
...
...     def __repr__(self):
...         return "Car({}, {})".format(self.brand, self.color)
...
>>> c1 = Car("Audi", "red")
>>> print(c1)
a red Audi Car
>>> c1
Car(Audi, red)
```
通过自定义实现的`__str__`和`__repr__`方法，这一次我们的c1对象就健壮了许多。

当然我们可以把上面的代码再优化下：
```python
>>> class Car(object):
...     def __init__(self, brand, color):
...         self.brand = brand
...         self.color = color
...
...     def __str__(self):
...         return f"a {self.color} {self.brand} Car"  # 使用3.6加入的'f-strings'
...
...     def __repr__(self):
...         return f"{self.__class__.__name__}({self.brand}, {self.color})"  # 动态获取类名
...
>>> c1 = Car("Audi", "red")
>>> print(c1)
a red Audi Car
>>> c1
Car(Audi, red)
```

## `__str__`和`__repr__`的区别

`__str__`：让你的类实例可读性更好。

`__repr__`：让你的类实例更明确。

这个就拿Python内置的日期对象为例，可以很形象地看出其中的区别：
```python
>>> import datetime
>>> today = datetime.date.today()  # today是datetime.date.today的一个实例
>>> print(today)  # __str__方法让实例可读性更好
2017-09-17
>>> today
datetime.date(2017, 9, 17)  # __repr__方法让实例更明确
```

## 补充

1. 如果你没有为你的类实例定义`__str__`方法的话，Python会返回`__repr__`的结果。
```pythhon
>>> class Car(object):
...     def __init__(self, brand, color):
...         self.brand = brand
...         self.color = color
...
...     def __repr__(self):  # 只定义一个__repr__方法
...         return f"{self.__class__.__name__}({self.brand}, {self.color})"  # 动态获取类名
...
>>> c1 = Car("Audi", "red")
>>> print(c1)  # 使用的就是__repr__返回的结果
Car(Audi, red)
```
所以当你自定义一个类时，**至少**要为你的类实例实现一个`__repr__`方法。

2. 内置的`str`和`repr`方法，本质上就是调用对象的`__str__`和`__repr__`方法。
```python
>>> import datetime
>>> today = datetime.date.today()  # today是datetime.date.today的一个实例
>>> str(today)  # 调用today的__str__方法
'2017-09-17'
>>> repr(today)  # 调用today的__repr__方法
'datetime.date(2017, 9, 17)'
```

3. 像列表、元祖等复杂的数据类型，默认都是使用的__repr__的结果来表示对象
```python
>>> import datetime
>>> today = datetime.date.today()  # today是datetime.date.today的一个实例
>>> [today]  # 默认使用__repr__的结果来表示对象
[datetime.date(2017, 9, 17)]
```

4. format格式化中支持**选择性**使用`__str__`或者`__repr__`返回的结果
```python
>>> import datetime
>>> today = datetime.date.today()  # today是datetime.date.today的一个实例
>>> f"{today!r}"  # 使用!r来指定使用__repr__返回的结果来进行格式化
'datetime.date(2017, 9, 17)'
>>> f"{today!s}"  # 使用!s来指定使用__str__返回的结果来进行格式化
'2017-09-17'
```

多看书、多写码。世界远比你想象的大。


