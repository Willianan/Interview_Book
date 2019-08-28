# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 21:54
@Project:InterView_Book
@Filename:5_用两个栈实现队列.py
@description:
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class solution:
	def __init__(self):
		self.stackA = []
		self.stackB = []

	def push(self,node):
		self.stackA.append(node)

	def pop(self):
		if self.stackB:
			return self.stackB.pop()
		elif not self.stackA:
			return None
		else:
			while self.stackA:
				self.stackB.append(self.stackA.pop())
			return self.stackB.pop()


