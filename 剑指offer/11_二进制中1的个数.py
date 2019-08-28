# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 22:45
@Project:InterView_Book
@Filename:11_二进制中1的个数.py
@description:
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

class Solution:
    def NumberOf1(self, n):
        count = 0
        for i in range(32):
            count += (n >> i)&1
        return count