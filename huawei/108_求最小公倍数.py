# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:57
@Project:InterView_Book
@Filename:108_求最小公倍数.py
@description:
题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数
"""


import sys
while True:
    try:
        s = sys.stdin.readline().strip()
        a = int(s.split()[0])
        b = int(s.split()[1])
        m=a
        n=b
        while(a!=b):
            if a>b:
                a=a-b
            else:
                b=b-a
        print(int(m*n/a))
    except Exception:
        break