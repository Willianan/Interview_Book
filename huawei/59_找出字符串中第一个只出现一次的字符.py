# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:40
@Project:InterView_Book
@Filename:59_找出字符串中第一个只出现一次的字符.py
@description:
 题目描述
找出字符串中第一个只出现一次的字符

输入描述:
输入一个非空字符串

输出描述:
输出第一个只出现一次的字符，如果不存在输出-1
"""


if __name__ == "__main__":
	while True:
		try:
			res = input()
			count = []
			for i in res:
				if res.count(i) == 1:
					count.append(i)
			if count:
				print(count[0])
			else:
				print(-1)
		except:
			break