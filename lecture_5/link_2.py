# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-12 16:08
@Project:InterView_Book
@Filename:link_2.py
@description:
    链表成环检测
"""

'''
题目描述：
	检测给定链表是否形成一个环是常见的面试题目。给定一个链表，要求设计算法，判断链表中是否有节点
	形成一个环：如果有，给出构成循环的节点个数。要求算法时间复杂度为O(N),空间复杂度为O(1)
'''


class Node:
	def __init__(self, val):
		self.next = None
		self.value = val
		self.visited = False


class ListUtility:
	def __init__(self):
		self.head = None
		self.tail = None

	def createList(self, nodeNum):
		# 生成还有nodeNum个节点的列表
		if nodeNum <= 0:
			return None
		head = None
		val = 0
		node = None
		# 构造给定节点的队列，每个节点数值依次递增
		while nodeNum > 0:
			if head is None:
				head = Node(val)
				node = head
			else:
				node.next = Node(val)
				node = node.next
				self.tail = node
			val += 1
			nodeNum -= 1
		self.head = head
		return head

	def createCircleList(self, totalNodeNum, circleNodeNum):
		if totalNodeNum < circleNodeNum:
			return None
		head = self.createList(totalNodeNum)
		temp = head
		stepCount = totalNodeNum - circleNodeNum
		while stepCount > 0:
			head.next = temp.next.next
			stepCount -= 1
		return head


	def printList(self, head):
		while head is not None:
			print("{0} ->".format(head.value), end=' ')
			head.visited = True
			head = head.next
		print("null")


class CircleList:
	def __init__(self):
		self.stepOne = None
		self.stepTwo = None
		self.visitCount = 0
		self.lenOfFirstVisit = 0
		self.lenOfSecondVisit = 0
		self.stepCount = 0

	def getCircleLength(self, head):
		self.stepOne = head
		self.stepTwo = head

		while self.visitCount < 2:
			if self.goOneStep() is False or self.goTwoStep() is False:
				break
			self.stepCount += 1
			# 记录两指针相遇时前进的次数
			if self.stepOne == self.stepTwo:
				self.visitCount += 1
				if self.visitCount == 1:
					self.lenOfFirstVisit = self.stepCount
				if self.visitCount == 2:
					self.lenOfSecondVisit = self.stepCount
		return self.lenOfSecondVisit - self.lenOfFirstVisit

	def goOneStep(self):
		if self.stepOne is None or self.stepOne.next is None:
			return False
		self.stepOne = self.stepOne.next
		return True

	def goTwoStep(self):
		if self.stepTwo is None or self.stepTwo.next is None or self.stepTwo.next.next is None:
			return False
		self.stepTwo = self.stepTwo.next.next
		return True


if __name__ == "__main__":
	util = ListUtility()
	head = util.createCircleList(10, 6)
	util.printList(head)
	cl = CircleList()
	lens = cl.getCircleLength(head)
	print("len of circle len is is: {0}".format(lens))
