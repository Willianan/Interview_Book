# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 22:52
@Project:InterView_Book
@Filename:12_数值的整数次方.py
@description:
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""

class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        result = 1
        if exponent>0:
            for i in range(exponent):
                result = result * base
            return result
        if exponent<0:
            abs_exponent = (-1)*exponent
            for i in range(abs_exponent):
                result = result * base
            result = 1.0/result
            return result