# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:44
@Project:InterView_Book
@Filename:4_字符串分隔.py
@description:
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组
"""

import sys


def solve(a,b):
	c = [a[i:i + 8] for i in range(0, len(a), 8)]
	d = [b[i:i + 8] for i in range(0, len(b), 8)]
	z = c + d
	for i in z:
		if len(i) < 8:
			x = i + (8 - len(i)) * '0'
			print(x)
		else:
			print(i)


if __name__ == "__main__":
	a = sys.stdin.readline().replace('\n', '')
	b = sys.stdin.readline().replace('\n', '')
	solve(a,b)
