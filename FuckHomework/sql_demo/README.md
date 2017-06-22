# 基于函数的模拟SQL实现

## 解题思路

1. 获取输入的sql字符串
2. 从输入的字符串中解析出有用信息
3. 拿着解析出来的信息去过滤数据
4. 输出结果


## 框架实现

```python

def sql_parse():
    pass
    
def sql_do():
    pass

if __name__ == "__main__":
while True:
    sql = input("sql>>").strip()
    if sql:
        if sql.upper() == "EXIT":
            break
        else:
            sql_dic = sql_parse(sql)  # 解析
            ret = sql_do(sql_dic)
    else:
        continue
```