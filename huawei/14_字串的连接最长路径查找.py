# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 17:21
@Project:InterView_Book
@Filename:14_字串的连接最长路径查找.py
@description:
题目描述
给定n个字符串，请对n个字符串按照字典序排列。

输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。

输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
"""

if __name__ == "__main__":
	n = int(input())
	l = []
	for i in range(n):
		l.append(input())
	l.sort()
	for x in l:
		print(x)