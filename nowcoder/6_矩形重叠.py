# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 17:43
@Project:InterView_Book
@Filename:6_矩形重叠.py
@description:
题目描述
平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。
如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。
请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。

输入描述:
输入包括五行。
第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。

输出描述:
输出一个正整数, 表示最多的地方有多少个矩形相互重叠,如果矩形都不互相重叠,输出1。
"""

import sys

lines = sys.stdin.readlines()
n = int(lines[0].strip())
xs1 = map(int, lines[1].strip().split())
ys1 = map(int, lines[2].strip().split())
xs2 = map(int, lines[3].strip().split())
ys2 = map(int, lines[4].strip().split())
nums = []
for x1, x2, y1, y2 in zip(xs1, xs2, ys1, ys2):
	nums.append((x1, 1, y1, y2))
	nums.append((x2, -1, y1, y2))
nums.sort()

temp, res = [], 1
for x, flag, y1, y2 in nums:
	if (flag == 1):
		temp.append((y1, 1))
		temp.append((y2, -1))
	else:
		count = 0
		temp.sort()
		for y, f in temp:
			count += f
			res = max(res, count)
		temp.remove((y1, 1))
		temp.remove((y2, -1))
print(res)