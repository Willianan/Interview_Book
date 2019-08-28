# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 19:54
@Project:InterView_Book
@Filename:47_求n个数的和.py
@description:
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.sum = 0

	def Sum_Solution(self, n):
		# write code here
		def qiusum(n):
			self.sum += n
			n -= 1
			return n > 0 and self.Sum_Solution(n)

		qiusum(n)
		return self.sum