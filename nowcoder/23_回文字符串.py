# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:35
@Project:InterView_Book
@Filename:23_回文字符串.py
@description:
题目描述
最大回文子串是被研究得比较多的一个经典问题。最近月神想到了一个变种，对于一个字符串，如果不要求子串连续，
那么一个字符串的最大回文子串的最大长度是多少呢。

输入描述:
每个测试用例输入一行字符串（由数字0-9，字母a-z、A-Z构成），字条串长度大于0且不大于1000.

输出描述:
输出该字符串的最长回文子串的长度。（不要求输出最长回文串，并且子串不要求连续）
"""


def func(s):
	dp = {}
	def helper(b, e):
		if b == e:
			return 1
		if b > e:
			return 0
		if (b, e) in dp:
			return dp[(b, e)]
		ans = 0
		if s[b] == s[e]:
			ans = helper(b + 1, e - 1) + 2
		else:
			ans = max(helper(b + 1, e), helper(b, e - 1))
		dp[(b, e)] = ans
		return ans
	return helper(0, len(s) - 1)


import sys

s = sys.stdin.readline().strip()
print(func(s))