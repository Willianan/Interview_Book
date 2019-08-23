# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 9:27
@Project:InterView_Book
@Filename:10_瞌睡.py
@description:
题目描述
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。
你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，
这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。

输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出描述:
小易这堂课听到的知识点的最大兴趣值。
"""

import sys

def max_score(array, flag, k):
	score = 0
	max_sum = 0
	func = lambda a, b: a * b
	list_3 = map(func, array, flag)
	list_3 = list(list_3)
	func2 = lambda a, b: a * (1 - b)
	list_4 = list(map(func2, array, flag))
	score = sum(list_3)
	sum_c = sum(list_4[0:k])
	for i in range(k, len(list_4)):
		sum_c += (list_4[i] - list_4[i - k])
		if (sum_c > max_sum):
			max_sum = sum_c
	return score + max_sum


if __name__ == "__main__":
	x = sys.stdin.readline().split()[0:2]
	x = list(map(int, x))
	n, k = x[0], x[1]

	array = sys.stdin.readline().split()[0:n]
	array = list(map(int, array))

	flag = sys.stdin.readline().split()[0:n]
	flag = list(map(int, flag))
	if (k == n):
		print(sum(array))
	else:
		print(max_score(array, flag, k))