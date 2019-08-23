# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:30
@Project:InterView_Book
@Filename:43_糖果分配.py
@description:
题目描述
假设你是一位很有爱的幼儿园老师，想要给幼儿园的小朋友们一些小糖果。但是，每个孩子最多只能给一块糖果。
对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的糖果的最小尺寸；并且每块糖果 j ，都有一
个尺寸 sj 。如果 sj >= gi ，我们可以将这个糖果 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽
可能满足越多数量的孩子，并输出这个最大数值。
注意：
你可以假设胃口值为正。一个小朋友最多只能拥有一块糖果。

输入描述:
第一行输入每个孩子的胃口值
第二行输入每个糖果的尺寸
孩子数和糖果数不超过1000

输出描述:
能满足孩子数量的最大值
"""

import sys

def func(weikou, size):
	weikou.sort()
	size.sort()
	i, j = 0, 0
	res = 0
	while i < len(weikou) and j < len(size):
		if weikou[i] <= size[j]:
			res += 1
			i += 1
			j += 1
		else:
			j += 1
	print(res)

if __name__ == "__main__":
	line1 = sys.stdin.readline().strip()
	weikou = list(int(e) for e in line1.split())
	line2 = sys.stdin.readline().strip()
	size = list(int(e) for e in line2.split())
	func(weikou, size)