# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:45
@Project:InterView_Book
@Filename:45_名字的漂亮度.py
@description:
题目描述
给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。

输入描述:
整数N，后续N个名字

输出描述:
每个名称可能的最大漂亮程度
"""
def solve(a):
	b, result = [], [0] * a
	for i in range(a):
		b.append(input())
	for i in range(a):
		c = set(list(b[i]))
		d = []
		for j in c:
			d.append(b[i].count(j))
			d.sort(reverse=True)
		for k in range(len(d)):
			result[i] = result[i] + d[k] * (26 - k)
	return result

if __name__ == "__main__":
	while True:
		try:
			a = int(input())
			result = solve(a)
			for i in range(a):
				print(result[i])
		except:
			break