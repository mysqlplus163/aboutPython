#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 为什么要有装饰器？

# 开放封闭原则
# 1. 对扩展是开放的 ->需要不断的去扩展也已经存在的代码的功能
# 2. 对修改是封闭的 -> 不应该直接修改已有的源代码

# 总结一下
# 不修改源代码，不修改调用方式，还要加新功能

# 装饰器可以实现上面的需求

# 装饰器的本质：
# 任意可调用的对象，被装饰的对象也是任意可调用的对象。

# 函数就属于可调用的对象

# 装饰器的功能
# 1. 不修改源代码，不修改调用方式
# 2. 加新功能

