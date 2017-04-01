#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/16

#-*- coding:utf-8 -*-
def operator_collection(first_collection,second_collection,operator):
    chosen = True
    while chosen:
        if operator == '+':
            return '加和：',first_collection | second_collection
        elif operator == '-':
            return  '差分:',(first_collection - second_collection)
            #print  '差分:',(first_collection - second_collection)
        elif operator == '&':
            return '交集：',first_collection & second_collection
        elif operator == '^':
            return '对称差分:',first_collection ^ second_collection
        elif operator == '<':
            return 'first_collection中元素都在second_collection中，second_collection中有元素不在first_collection中：',first_collection < second_collection
        elif operator == '>':
            return 'second_collection中元素都在first_collection中，first_collection中有元素不在second_collection中：',first_collection > second_collection
        elif operator == 'in':
            return 'first_collection是否在second_collection中：',first_collection in second_collection
        elif operator == 'not in':
            return 'first_collection是否不在second_collection中：',first_collection not in second_collection
        elif operator == '==':
            return '是否具有相同元素：',first_collection == second_collection
        elif operator == '=<':
            return 'first_collection中所以元素都在second_collection中：',first_collection <= second_collection
        elif operator == '>=':
            return 'second_collection中所有的元素都在first_collection中:',first_collection >= second_collection
        elif operator == '!=':
            return  '不等价操作',first_collection != second_collection
        else:
            return 'please enter correct operator'
        chosen = False
if __name__ == '__main__':
    ret = operator_collection({1,2,3,4,5},{4,5,6,7,8},'-')
    print ret[0].decode('utf-8'), ret[1]
    s = '差分:'
    #s.decode('gbk').encode('gbk')
    print s