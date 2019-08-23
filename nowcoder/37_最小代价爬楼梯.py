# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:02
@Project:InterView_Book
@Filename:37_最小代价爬楼梯.py
@description:
题目描述
你需要爬上一个N层的楼梯，在爬楼梯过程中， 每阶楼梯需花费非负代价，第i阶楼梯花费代价表示为cost[i]， 一旦你付出了代价，你可以在该阶基础上往上爬一阶或两阶。
你可以从第 0 阶或者 第 1 阶开始，请找到到达顶层的最小的代价是多少。
N和cost[i]皆为整数，且N∈[2,1000]，cost[i]∈ [0, 999]。

输入描述:
输入为一串半角逗号分割的整数，对应cost数组，例如
10,15,20

输出描述:
输出一个整数，表示花费的最小代价
"""
import sys

def solve(lines):
	for i in lines:
		array.append(int(i))
	length1 = len(array)
	output1 = []
	if length1 <= 2:
		print(min(array))
	else:
		for i in range(length1):
			if i == 0 or i == 1:
				output1.append(array[i])
				continue
			output1.append(min(output1[-1], output1[-2]) + array[i])
		print(min(output1[-1], output1[-2]))



if __name__ == "__main__":
	array = []
	lines = sys.stdin.readline().strip().split(',')
	solve(lines)
