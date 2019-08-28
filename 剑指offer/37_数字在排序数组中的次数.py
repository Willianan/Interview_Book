# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 11:28
@Project:InterView_Book
@Filename:37_数字在排序数组中的次数.py
@description:
题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
	def GetNumberOfK(self, data, k):
		# write code here
		if len(data) == 0:
			return 0
		return data.count(k)