# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 10:24
@Project:InterView_Book
@Filename:34_第一个只出现一次的字符.py
@description:
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        index = 0
        if len(s) == 0:
            return -1
        for x in s:
            if s.count(x) == 1:
                return index
            index += 1