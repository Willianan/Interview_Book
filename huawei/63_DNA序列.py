# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:54
@Project:InterView_Book
@Filename:63_DNA序列.py
@description:
题目描述
一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列
中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这
个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。

输入描述:
输入一个string型基因序列，和int型子串的长度

输出描述:
找出GC比例最高的子串,如果有多个输出第一个的子串
"""


def solve(x,y):
	max = 0
	output = x[0: int(y)]
	for n in range(len(x) - int(y) + 1):
		number = 0
		for m in x[n: n + int(y)]:
			if m == 'C' or m == 'G':
				number += 1
		if number / int(y) > max:
			max = number / int(y)
			output = x[n: n + int(y)]
	return output
if __name__ == "__main__":
	while True:
		try:
			x = input()
			y = input()
			output = solve(x,y)
			print(output)
		except:
			break