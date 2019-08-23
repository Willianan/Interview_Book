# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 17:06
@Project:InterView_Book
@Filename:10_字符个数统计.py
@description:
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。
"""


def solve(string):
	count = 0
	stringArr = []
	for i in range(len(inputString)):
		if inputString[i] not in stringArr:
			stringArr.append(inputString[i])
	for i in range(len(stringArr)):
		if int(ord(stringArr[i])) < 127 and int(ord(stringArr[i]) > 0):
			count = count + 1
	return count


if __name__ == "__main__":
	inputString = input()
	count = solve(inputString)
	print(count)