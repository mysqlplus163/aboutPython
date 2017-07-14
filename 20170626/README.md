# 迭代器

迭代 
软件开发非常常见 -> 迭代更新
 
1. 重复
2. 下一次 是基于 上一次的 结果之上


## 模拟一下迭代


## 可迭代对象

能被for循环的/有__iter__()


## 迭代器

可迭代对象调用__iter__()方法得到的就是迭代器.

迭代器的特征：
1. 都有__iter__、__next__方法
2. 调用它的__next__方法，得到迭代器里面的元素
3. 没有元素了，就抛出StopIteration


迭代器的特点：

优点：
1. 它不依赖索引
2. 惰性计算，节省内存 list1 = [1, 2, 3, 4, 5]

缺点：
1. 没有索引灵活 -> 只能从头到尾一个一个取
2. 一次性，只能往后取，不能退回


## for循环的实质

```python

dict1 = {"Alex": 122, "Seven": 5000, "Egon": 3000, "Andy": 50}
# 得到一个迭代器
ret = dict1.__iter__()
# ret = iter(dict1)

# for循环的实质
while True:
    try:
        # 依次取元素
        print(ret.__next__())  # 取迭代器的下一个元素
        # print(next(ret))
    except StopIteration:
        break
```

## 补充

obj.__iter__()  <==>  iter(obj)
obj.__next__()  <==>  next(obj)

len(obj)  -> obj.__len__()









