# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:38
@Project:InterView_Book
@Filename:45_解码方法.py
@description:
题目描述
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

输入描述:
一串编码过的数字，比如12

输出描述:
解码方法的总数
"""

def solve(s):
	n = len(s)
	x_1 = 1
	for i in range(n):
		if i == 0:
			x_2 = 1
		else:
			if int(s[i - 1:i + 1]) <= 26:
				x_1, x_2 = x_2, (x_1 + x_2)
			else:
				x_1 = x_2
	return x_2



if __name__ == "__main__":
	s = input().strip()
	x_2 = solve(s)
	print(x_2)