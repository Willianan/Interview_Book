# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 21:56
@Project:InterView_Book
@Filename:40_数组中只出现一次的数字.py
@description:
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""



class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		# write code here
		return list(self.dc(array, 0, len(array) - 1))

	def dc(self, array, start, end):
		res = set()
		if start > end:
			return res
		if start == end:
			return set(array[start:end + 1])
		mid = (start + end) // 2
		s1 = self.dc(array, start, mid)
		s2 = self.dc(array, mid + 1, end)
		return s1.union(s2).difference(s1.intersection(s2))

