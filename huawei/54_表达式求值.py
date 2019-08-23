# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:17
@Project:InterView_Book
@Filename:54_表达式求值.py
@description:
题目描述
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过100，合法的字符包括”+, -, *, /, (, )”，”0-9”，字符串
内容的合法性及表达式语法的合法性由做题者检查。本题目只涉及整型计算。

输入描述:
输入算术表达式

输出描述:
计算出结果值
"""


if __name__ == "__main__":
	while True:
		try:
			a = input()
			print(eval(a))
		except:
			break