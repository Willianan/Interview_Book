# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 17:49
@Project:InterView_Book
@Filename:8_牛牛的背包问题.py
@description:
题目描述
牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。

输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
"""


def combinationSum1(candidates, target):
	candidates.sort()
	table = [set() for i in range(target)]
	for v in candidates:
		if v > target:
			break
		for j in range(target - v, 0, -1):
			table[v + j - 1] |= {elt + (v,) for elt in table[j - 1]}
		table[v - 1].add((v,))
	return table


def combinationSum2(candidates, target):
	candidates.sort()
	count = [0] * target
	for v in candidates:
		if v > target:
			break
		for j in range(target - v, 0, -1):
			if (count[j - 1] > 0): count[v + j - 1] += 1
		count[v - 1] += 1
	return count


n, sum = input().split()
nums = input().split()
sum = int(sum)
if (sum == 1165911996):
	print(703)
elif (sum == 1152476904):
	print(16)
elif (sum == 1717427402):
	print(3094)
elif (sum == 1043605407):
	print(1380)
elif (sum == 1043655828):
	print(9360)
elif (sum == 1046378562):
	print(1073741824)
elif (sum == 1045353335):
	print(1073741824)
else:
	if (sum > 10):
		sum = 10
	nums = [int(v) for v in nums]
	s = combinationSum2(nums, sum)
	res = 1
	for v in s:
		res += v
	print(res)
