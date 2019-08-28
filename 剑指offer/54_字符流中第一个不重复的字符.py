# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 20:53
@Project:InterView_Book
@Filename:54_字符流中第一个不重复的字符.py
@description:
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前
两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，
第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


class Solution:
	# 返回对应char
	def __init__(self):
		self.s = ''
		self.dict1 = {}

	def FirstAppearingOnce(self):
		# write code here
		for i in self.s:
			if self.dict1[i] == 1:
				return i
		return '#'

	def Insert(self, char):
		# write code here
		self.s = self.s + char
		if char in self.dict1:
			self.dict1[char] += 1
		else:
			self.dict1[char] = 1
