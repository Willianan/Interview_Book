# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:44
@Project:InterView_Book
@Filename:32_求连续子数组的最大和.py
@description:
题目描述
一个非空整数数组，选择其中的两个位置，使得两个位置之间的数和最大。
如果最大的和为正数，则输出这个数；如果最大的和为负数或0，则输出0

输入描述:
3,-5,7,-2,8

输出描述:
13
"""

if __name__ == "__main__":
	x = [int(i) for i in input().split(',')]
	res = 0
	d = [0] * len(x)
	d[0] = max(0, x[0])
	res = max(res, d[0])
	for i in range(1, len(x)):
		d[i] = max(d[i - 1] + x[i], 0)
		res = max(res, d[i])
	print(res)