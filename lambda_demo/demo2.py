#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/19

l = ['columnfamily=wbxsitewebdomain', 'keyspace=ks_j2ee_global', 'type=ColumnFamilies']

# {'columnfamily':'wbxsitewebdomain','keyspace':'ks_j2ee_global','type':'ColumnFamilies'}

d = dict({x.split("=")[0]: x.split("=")[1] for x in l})
print(d)

if __name__ == "__main__":
    pass
