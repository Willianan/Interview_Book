# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 20:50
@Project:InterView_Book
@Filename:53_表示数值的字符串.py
@description:
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False