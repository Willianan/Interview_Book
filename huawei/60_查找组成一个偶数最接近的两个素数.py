# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:43
@Project:InterView_Book
@Filename:60_查找组成一个偶数最接近的两个素数.py
@description:
题目描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对

输入描述:
输入一个偶数

输出描述:
输出两个素数
"""


def judge(number):
	for i in range(2, number // 2 + 1):
		if number % i == 0:
			return False
	return True

def func(n):
	res = []
	if n == 4:
		res = [2, 2]
	else:
		for i in range(n // 2, n):
			if judge(i) and judge(n - i):
				res = [n - i, i]
				break
	return res


if __name__ == "__main__":
	while True:
		try:
			N = int(input())
			res = func(N)
			for i in res:
				print(i)
		except:
			break
