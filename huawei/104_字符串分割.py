# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:46
@Project:InterView_Book
@Filename:104_字符串分割.py
@description:
题目描述
连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
首先输入一个整数，为要输入的字符串个数。

输入描述:
首先输入数字n，表示要输入多少个字符串。连续输入字符串(输出次数为N,字符串长度小于100)。

输出描述:
按长度为8拆分每个字符串后输出到新的字符串数组，长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
"""

while True:
    try:
        a = int(input())
        for i in range(a):
            s = input()
            while len(s)>8:
                print(s[:8])
                s = s[8:]
            print(s.ljust(8,'0'))
    except:
        break