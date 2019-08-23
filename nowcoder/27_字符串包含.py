# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:26
@Project:InterView_Book
@Filename:27_字符串包含.py
@description:
题目描述
我们定义字符串包含关系：字符串A=abc，字符串B=ab，字符串C=ac，则说A包含B，A和C没有包含关系。

输入描述:
两个字符串，判断这个两个字符串是否具有包含关系，测试数据有多组，请用循环读入。

输出描述:
如果包含输出1，否则输出0.
"""

import sys

for line in sys.stdin.readlines():
	A, B = line.strip().split()
	if A in B or B in A:
		print(1)
	else:
		print(0)
