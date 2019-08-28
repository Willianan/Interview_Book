# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 22:28
@Project:InterView_Book
@Filename:42_和为S的两个数字.py
@description:
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""

from collections import Counter


class Solution:
	def FindNumbersWithSum(self, array, tsum):
		# write code here
		m = Counter(array)
		for i in array:
			if tsum - i in m:
				if i != tsum - i:
					return (i, tsum - i)
				if m[i] > 1:
					return (i, i)
		return []