# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 22:42
@Project:InterView_Book
@Filename:30_连续子数组的最大和.py
@description:
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,
他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向
量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个
负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向
量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子
序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, cur_sum = -0xffffff, 0
        for i in array:
            if cur_sum <= 0:
                cur_sum = i
            else:
                cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum