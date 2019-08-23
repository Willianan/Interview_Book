# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 17:01
@Project:InterView_Book
@Filename:9_提取不重复的整数.py
@description:
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""


def sovle(strings):
	list = []
	for i in strings[::-1]:
		if i not in list:
			list.append(i)
	strings1 = ''
	for i in list:
		strings1 += i
	return strings1

if __name__ == "__main__":
	strings = input()
	string = sovle(strings)
	print(string)