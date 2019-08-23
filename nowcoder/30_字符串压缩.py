# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:35
@Project:InterView_Book
@Filename:30_字符串压缩.py
@description:
题目描述
对字符串进行RLE压缩，将相邻的相同字符，用计数值和字符值来代替。例如：aaabccccccddeee，则可用3a1b6c2d3e来代替。

输入描述:
输入为a-z,A-Z的字符串，且字符串不为空，如aaabccccccddeee

输出描述:
压缩后的字符串，如3a1b6c2d3e
"""


def sub(s):
	count = 1
	res = ''
	for i in range(1, len(s)):
		if s[i - 1] == s[i]:
			count += 1
		else:
			res += str(count) + s[i - 1]
			count = 1
	res += str(count)
	res += s[-1]
	return res


if __name__ == '__main__':
	s = input()
	print(sub(s))
