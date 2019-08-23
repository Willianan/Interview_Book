# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:16
@Project:InterView_Book
@Filename:40_爱吃喵粮的小招喵.py
@description:
题目描述
小招喵喜欢吃喵粮。这里有 N 堆喵粮，第 i 堆中有 p[i] 粒喵粮。喵主人离开了，将在 H 小时后回来。
小招喵可以决定她吃喵粮的速度 K （单位：粒/小时）。每个小时，她将会选择一堆喵粮，从中吃掉 K 粒。
如果这堆喵粮少于 K 粒，她将吃掉这堆的所有喵粮，然后这一小时内不会再吃更多的喵粮。
小招喵喜欢慢慢吃，但仍然想在喵主人回来前吃掉所有的喵粮。
返回她可以在 H 小时内吃掉所有喵粮的最小速度 K（K 为整数）。

输入描述:
第一行输入为喵粮数组，以空格分隔的N个整数
第二行输入为H小时数

输出描述:
最小速度K
"""


import math

def check(mid,h):
	time = 0
	for i in num:
		time += math.ceil(i / mid)
	if time <= h:
		return True
	else:
		return False

def solve(num,h):
	left = 1
	right = max(num)
	while left <= right:
		mid = left + int((right - left) / 2)
		if check(mid,h):
			right = mid - 1
		else:
			left = mid + 1
	return left


if __name__ == "__main__":
	num = list(map(int, input().split()))
	h = int(input())
	left = solve(num,h)
	print(left)