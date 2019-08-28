# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 20:12
@Project:InterView_Book
@Filename:49_把字符串转换成整数.py
@description:
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        else:
            if s[0]>'9' or s[0]<'0':
                a=0
            else:
                a=int(s[0])*10**(len(s)-1)
            if len(s)>1:
                for i in range(1,len(s)):
                        if s[i]>='0' and s[i]<='9':
                            a=a+int(s[i])*10**(len(s)-1-i)
                        else:
                            return 0
        if s[0]=='+':
            return a
        if s[0]=='-':
            return -a
        return a
