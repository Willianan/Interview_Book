# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:49
@Project:InterView_Book
@Filename:46_按字节截取字符串.py
@description:
题目描述
编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。
但是要保证汉字不被截半个，如"我ABC"4，应该截为"我AB"，输入"我ABC汉DEF"6，
应该输出为"我ABC"而不是"我ABC+汉的半个"。

输入描述:
输入待截取的字符串及长度

输出描述:
截取后的字符串
"""

if __name__ == "__main__":
	while True:
		try:
			a, n = input().split()
			n = int(n)
			if a[n - 1].isalpha():
				print(a[:n])
			else:
				print(a[:n - 1])
		except:
			break