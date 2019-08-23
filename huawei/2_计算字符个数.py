# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:37
@Project:InterView_Book
@Filename:2_计算字符个数.py
@description:
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述:
输出输入字符串中含有该字符的个数。
"""

import sys

if __name__ == "__main__":
	input_str = sys.stdin.readline().strip().lower()
	target_char = sys.stdin.readline().strip().lower()
	print(input_str.count(target_char))