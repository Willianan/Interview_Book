# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:28
@Project:InterView_Book
@Filename:42_跳格子游戏.py
@description:
题目描述
假设你正在玩跳格子（所有格子排成一个纵列）游戏。需要 跳完n 个格子你才能抵达终点。
每次你可以跳 1 或 2 个格子。你有多少种不同的方法可以到达终点呢？
注意：给定 n 是一个正整数。

输入描述:
格子数n

输出描述:
跳完n个格子到达终点的方法
"""


def get_way(n):
	a, b = 1, 2
	for i in range(3, n + 1):
		c = a + b
		a = b
		b = c
	print(b)


if __name__ == "__main__":
	n = int(input())
	get_way(n)