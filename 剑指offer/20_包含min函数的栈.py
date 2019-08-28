# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 11:16
@Project:InterView_Book
@Filename:20_包含min函数的栈.py
@description:
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, node):
		# write code here
		self.stack.append(node)
		if not self.min_stack or node <= self.min_stack[-1]:
			self.min_stack.append(node)

	def pop(self):
		# write code here
		if self.stack[-1] == self.min_stack[-1]:
			self.min_stack.pop()
		self.stack.pop()

	def top(self):
		# write code here
		return self.stack[-1]

	def min(self):
		# write code here
		return self.min_stack[-1]
