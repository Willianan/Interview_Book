# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:40
@Project:InterView_Book
@Filename:28_素数伴侣.py
@description:
 题目描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选
方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将
2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会
希望你寻找出“最佳方案”。
输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。
输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

输入描述:
输入说明
1 输入一个正偶数n
2 输入n个整数

输出描述:
求得的“最佳方案”组成“素数伴侣”的对数。
"""


def prime_judge(n):
	m = int(n ** 0.5)
	if n % 2 == 0:
		return False
	else:
		for i in range(m + 1)[3::2]:
			if n % i == 0:
				return False
	return True


def group_lst(lst):  ##分奇偶
	a = []
	b = []
	for i in lst:
		if int(i) % 2 == 1:
			a.append(int(i))
		else:
			b.append(int(i))
	return (a, b)


def matrix_ab(a, b):
	matrix = [[0 for i in range(len(b))] for i in range(len(a))]
	for ii, i in enumerate(a):
		for jj, j in enumerate(b):
			if prime_judge(i + j) == True:
				matrix[ii][jj] = 1
	return matrix


def find(x):
	for index, i in enumerate(b):
		if matrix[x][index] == 1 and used[index] == 0:
			used[index] = 1
			if connect[index] == -1 or find(connect[index]) != 0:
				connect[index] = x
				return 1
	return 0

if __name__ == "__main__":

	while True:
		try:
			n = int(input())
			m = input().split()
			(a, b) = group_lst(m)
			matrix = matrix_ab(a, b)
			connect = [-1 for i in range(len(b))]
			count = 0
			for i in range(len(a)):
				used = [0 for j in range(len(b))]
				if find(i):
					count += 1
			print(count)
		except:
			break