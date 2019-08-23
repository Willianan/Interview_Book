# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:04
@Project:InterView_Book
@Filename:65_查找两个字符串a,b中最长公共字串.py
@description:
题目描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。

输入描述:
输入两个字符串

输出描述:
返回重复出现的字符
"""
def solve(string1,string2):
	n = 0
	commonString = ''
	if len(string1) > len(string2):
		string1, string2 = string2, string1
	for i in range(len(string1) + 1):
		if string1[i - n:i] in string2:
			commonString = string1[i - n:i]
			n += 1
	return commonString


if __name__ == "__main__":
	while True:
		try:
			str1 = input()
			str2 = input()
			print(solve(str1,str2))
		except:
			break