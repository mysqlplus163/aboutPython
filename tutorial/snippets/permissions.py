#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/14

"""
定制对象级别的权限控制
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    定制权限允许只有创建者修改
    """

    def has_object_permission(self, request, view, obj):
        # 因为所有请求都有读权限，所以我们要允许GET, HEAD or OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写权限只开放给片段的拥有者
        return obj.owner == request.user
