# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 16:31
@Project:InterView_Book
@Filename:93_数的判断.py
@description:
 题目描述
编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，
并且所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），
能满足以上条件，返回true；不满足时返回false。

输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false
"""


def In(i, length, rest, result, diff):
	if i == length:
		return result == diff
	else:
		return In(i + 1, length, rest, result + rest[i], diff) or In(i + 1, length, rest, result - rest[i], diff)


while True:
	try:
		N = int(input())
		arr = list(map(int, input().split()))
		_5num, _5sum, _3num, _3sum, rest = [], 0, [], 0, []
		for i in arr:
			if i % 5 == 0:
				_5num.append(i)
			elif i % 3 == 0:
				_3num.append(i)
			else:
				rest.append(i)
		_5sum = sum(_5num)
		_3sum = sum(_3num)
		print(str(In(0, len(rest), rest, 0, _5sum - _3sum)).lower())
	except:
		break
