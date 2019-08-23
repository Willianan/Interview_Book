# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 9:58
@Project:InterView_Book
@Filename:13_表达式求值.py
@description:
题目描述
今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如：
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，能够获得的最大值。

输入描述:
一行三个数a，b，c (1 <= a, b, c <= 10)

输出描述:
能够获得的最大值
"""

import sys
a, b, c = [int(i) for i in sys.stdin.readline().strip().split()]
print(max(a*b+c, a*c+b, b*c+a, a*(b+c), b*(c+a), c*(a+b), a+b+c, a*b*c))