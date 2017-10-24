#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。保证肯定仅有一个结果。
例如，列表[1,2,5,4]与目标整数3，1+2=3，结果为(0, 1).

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, first in enumerate(nums):
            second = target - first
            if second in nums[i+1:]:
                i2 = nums[i+1:].index(second) + i + 1
                return [i, i2]


def find_two_sum_index(l, target):
    for i, first in enumerate(l):
        second = target - first
        if second in l[i+1:]:
            i2 = l[i+1:].index(second) + (i+1)
            return i, i2


if __name__ == '__main__':
    l = [1, 2, 4, 5]
    s = Solution()
    ret = s.twoSum(l, 3)
    print(ret)
    ret2 = find_two_sum_index(l, 3)
    print(ret2)
