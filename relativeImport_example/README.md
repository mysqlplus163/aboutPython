# 相对导入（relative import）


## 包和模块的概念


Python的程序由包（package）、模块（module）和函数组成。
包是由一系列模块组成的集合。


模块是处理某一类问题的函数和类的集合。
模块把一组相关的函数或代码组织到一个文件中。
一个文件就是一个模块。模块由代码、函数或类组成。

## Python中的import

当Python导入一个模块时，Python首先查找当前路径，然后查找lib目录、site-packages目录（Python\Lib\site-packages）和环境变量PATHONPATH设置的目录。
如果导入的模块没有找到，就在以上路径依次搜索一下是否含有这个模块。
可以通过sys.path语句查看模块导入时的查找路径。
sys.path是一个列表，按顺序查找。

