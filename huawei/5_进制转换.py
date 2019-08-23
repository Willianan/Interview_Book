# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:47
@Project:InterView_Book
@Filename:5_进制转换.py
@description:
题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。
"""

if __name__ == "__main__":
	while True:
		try:
			n = input()
			s = eval(n)
			print(str(s))
		except:
			break