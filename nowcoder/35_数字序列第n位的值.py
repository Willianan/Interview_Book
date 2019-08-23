# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:54
@Project:InterView_Book
@Filename:35_数字序列第n位的值.py
@description:
题目描述
有一个无限长的数字序列1，2，2，3，3，3，4，4，4，4，5，5，5，5，5。。。
（数字序列从1开始递增，且数字k在该序列中正好出现k次），求第n项是多少

输入描述:
输入为一个整数n

输出描述:
输出一个整数，即第n项的值
"""

if __name__ == "__main__":
	n = int(input())
	count, num = 1, 1
	while num < n:
		count += 1
		num += count
	print(count)