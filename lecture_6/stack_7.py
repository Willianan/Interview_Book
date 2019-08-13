# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 17:04
@Project:InterView_Book
@Filename:stack_7.py
@description:
    使用堆栈模拟队列
"""

'''
题目描述：
	用两个堆栈模拟队列时，必须要支持两种操作：enqueue和dequeue。前者在队列末尾加入一个元素，
	后者把队列头部的元素取出。要求实现时不能分配超过O(1)内存，并且jinxm次enqueue和dequeue操作
	时，时间复杂度必须是O(m)
'''


class StackQueue:
	def __init__(self):
		self.stackA = []
		self.stackB = []

	def enqueue(self,v):
		self.stackA.append(v)

	def dequeue(self):
		if len(self.stackB) == 0:
			while len(self.stackA) > 0:
				self.stackB.append(self.stackA.pop())
		return self.stackB.pop()


if __name__ == "__main__":
	sq = StackQueue()
	print("enqueue:")
	for i in range(6):
		sq.enqueue(i)
		print("{0}".format(i),end=' ')
	print("\ndequeue:")
	for i in range(6):
		print("{0}".format(sq.dequeue()),end=" ")