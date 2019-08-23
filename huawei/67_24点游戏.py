# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:19
@Project:InterView_Book
@Filename:67_24点游戏.py
@description:
题目描述
问题描述：给出4个1-10的数字，通过加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字。[数字允许重复，但每个数字仅允许使用一次，测试用例保证无异常数字]
输出：
true or false

输入描述:
输入4个int整数

输出描述:
返回能否得到24点，能输出true，不能输出false
"""


def f(res, n):
	x = False
	if len(n) == 1:
		if n[0] == res:
			return True
		else:
			return False
	for i in range(len(n)):
		a = n[i]
		b = n[:]
		b.remove(a)
		x = x or f(res - a, b) or f(res * a, b) or f(res / a, b) or f(res + a, b)
	return x


if __name__ == "__main__":
	while True:
		try:
			n = input().split()
			flag = False
			if len(n) != 4:
				print('false')
				break
			for i in range(4):
				n[i] = float(n[i])
			if f(24.0, n):
				print('true')
			else:
				print('false')
		except:
			break
