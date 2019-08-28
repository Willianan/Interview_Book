# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 22:35
@Project:InterView_Book
@Filename:8_跳台阶.py
@description:
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 1
        elif number<= 2:
            return number
        else:
            a = 1
            b = 2
            for i in range(2,number):
                tmp = a+b
                a=b
                b=tmp
            return b