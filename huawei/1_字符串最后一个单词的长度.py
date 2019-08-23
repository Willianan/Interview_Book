# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:35
@Project:InterView_Book
@Filename:1_字符串最后一个单词的长度.py
@description:
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。
"""


if __name__ == "__main__":
	s = input()
	print(len(s.split()[-1]))