# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:46
@Project:InterView_Book
@Filename:84_统计大写字母个数.py
@description:
题目描述
找出给定字符串中大写字符(即'A'-'Z')的个数
接口说明
原型：int CalcCapital(String str);
返回值：int

输入描述:
输入一个String数据

输出描述:
输出string中大写字母的个数
"""

while True:
	try:
		s = input().strip()
		count = 0
		for i in s:
			if ord('A') <= ord(i) <= ord('Z'):
				count += 1
		print(count)
	except:
		break
