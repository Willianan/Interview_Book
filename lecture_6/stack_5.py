# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 16:11
@Project:InterView_Book
@Filename:stack_5.py
@description:
    堆栈元素的在线排序
"""

'''
题目描述：
	给定一根存在整数数据的堆栈，能使用的堆栈操作有：peek，获得堆栈顶部元素但不弹出：pop,
	弹出堆栈顶部元素:push，压入一个元素:empty,判断堆栈是否为空。
	要求只能使用以上这几种堆栈操作，在不用new显式分配新内存的情况下，将堆栈元素从大到小排列。
'''

class StackSorter:
	def __init__(self):
		pass
	def sortByRecursion(self,stack):
		if len(stack) == 0:
			return stack
		v = stack.pop()
		stack = self.sortByRecursion(stack)
		stack = self.insert(stack,v)
		return stack

	def insert(self, stack, val):
		if len(stack) == 0 or val <= stack[len(stack) - 1]:
			stack.append(val)
			return stack
		t = stack.pop()
		self.insert(stack,val)
		stack.append(t)
		return stack


if __name__ == "__main__":
	stack = [3,2,5,6,1,4]
	st = StackSorter()
	s = st.sortByRecursion(stack)
	print(s)


