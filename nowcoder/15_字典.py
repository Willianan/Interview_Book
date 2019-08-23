# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:05
@Project:InterView_Book
@Filename:15_字典.py
@description:
题目描述
小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。
小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。
小易现在希望你能帮他找出第k个单词是什么。

输入描述:
输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 109), 以空格分割。

输出描述:
输出第k个字典中的字符串，如果无解，输出-1。
"""

import math



def C_fun(n, m):
	count = math.factorial(n + m) // ((math.factorial(n)) * (math.factorial(m)))
	return count

if __name__ == "__main__":
	n, m, k = [int(i) for i in input().split(" ")]
	s = ''
	count = C_fun(n, m)
	if k > count:
		print("-1")
	elif k <= count:
		while n > 0 and m > 0:
			temp = C_fun(n - 1, m)
			if k <= temp:
				s += 'a'
				n -= 1
			else:
				s += 'z'
				m -= 1
				k -= temp
		s += 'a' * n
		s += 'z' * m
		print(s)