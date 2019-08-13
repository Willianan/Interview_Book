# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 15:28
@Project:InterView_Book
@Filename:stack_2.py
@description:
    计算堆栈当前元素最大值
"""

'''
题目描述：
	给定一个堆栈，请给出时间复杂度O(1)的max实现
	解决该问题的步骤：
		(1)每次压入堆栈时，用一个变量maxVal记录堆栈当前最大值
		(2)创建一个新堆栈maxStack，当压入元素的值大于当前最大值时，将该元素压入maxStack
		(3)弹出一个元素时，如果弹出的元素是当前最大值，那么把maxStack顶部的元素也弹出，
		   然后把maxVal设置成maxStack顶部的元素
'''


import sys

class MaxStack:
	def __init__(self):
		self.stack = []
		self.maxStack = []
		self.maxVal = - sys.maxsize - 1

	def push(self,val):
		if val > self.maxVal:
			self.maxVal = val
			self.maxStack.append(val)
		self.stack.append(val)

	def peek(self):
		# 返回堆栈最顶部的元素但不弹出
		return self.stack[len(self.stack) - 1]

	def pop(self):
		if self.peek() == self.maxVal:
			self.maxStack.pop()
		self.maxVal = self.maxStack[len(self.maxStack) - 1]
		return self.stack.pop()

	def max(self):
		return self.maxStack[len(self.maxStack) - 1]


if __name__ == "__main__":
	ms = MaxStack()
	ms.push(5)
	ms.push(4)
	ms.push(2)
	ms.push(3)
	print("max val in stack is {0}".format(ms.max()))

	ms = MaxStack()
	ms.push(6)
	ms.push(1)
	ms.push(10)
	ms.push(8)
	print("max val in stack is {0}".format(ms.max()))

	ms.pop()
	ms.pop()
	print("max val in stack is {0}".format(ms.max()))