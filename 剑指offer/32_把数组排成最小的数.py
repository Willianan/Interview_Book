# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 10:12
@Project:InterView_Book
@Filename:32_把数组排成最小的数.py
@description:
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num=map(str,numbers)
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)