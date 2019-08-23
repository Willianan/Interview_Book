# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:29
@Project:InterView_Book
@Filename:28_最少数量货物装箱问题.py
@description:
题目描述
有重量分别为3，5，7公斤的三种货物，和一个载重量为X公斤的箱子（不考虑体积等其它因素，只计算重量）
需要向箱子内装满X公斤的货物，要求使用的货物个数尽可能少（三种货物数量无限）

输入描述:
输入箱子载重量X(1 <= X <= 10000)，一个整数。

输出描述:
如果无法装满，输出 -1。
如果可以装满，输出使用货物的总个数。
"""




def NUM(x):
	# 三个箱子数量初始化
	n3, n5, n7 = 0, 0, 0
	# 考虑从最重的箱子装起
	n7 = x // 7
	while n7 >= 0:
		n5 = (x - n7 * 7) // 5
		while n5 >= 0:
			n3 = (x - n7 * 7 - n5 * 5) // 3
			if X == n3 * 3 + n5 * 5 + n7 * 7:
				return n3 + n5 + n7
			n5 -= 1
		n7 -= 1
	return -1

if __name__ == "__main__":
	X = int(input())
	n = NUM(X)
	print(n)