# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 10:11
@Project:InterView_Book
@Filename:link_4.py
@description:
    获取重合列表的第一个相交节点
"""

'''
题目描述：
	要求设计一个时间复杂度为O(n)的算法，返回链表相交时第一个节点。
'''


class Node:
	def __init__(self,val):
		self.next = None
		self.value = val

class ListUtility:
	def __init__(self):
		self.head = None
		self.tail = None

	def createList(self,nodeNum):
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

	def printList(self,head):
		while head is not None:
			print("{0} ->".format(head.value),end=' ')
			head = head.next
		print("null")


	def getNodeByIdx(self,num):
		node = self.head
		while num > 0:
			if node is not None:
				node = node.next
			num -= 1
		return node


class ListIntersetFinder:
	def __init__(self,listHead1,listHead2):
		self.listHead1 = listHead1
		self.listHead2 = listHead2
		# t1 + t2
		self.firstListLen = self.getListLen(self.listHead1)
		# t3 + t2
		self.secondListLen = self.getListLen(self.listHead2)
		# t1 + t3
		self.lenAfterReverse = 0

	def getFirstIntersetNode(self):
		listReverse = ListReverse(self.listHead2)
		# 先把队列2倒转
		reverseHead = listReverse.getReverseList()
		# 倒转后，从队列1的头节点开始遍历，直到队列2的头节点
		self.lenAfterReverse = self.getListLen(self.listHead1)
		t3 = ((self.lenAfterReverse - self.firstListLen) + self.secondListLen -1) / 2
		steps = self.secondListLen - t3 - 1
		while steps > 0:
			reverseHead = reverseHead.next
			steps -= 1
		return reverseHead

	def getListLen(self, head):
		len = 0
		while head is not None:
			head = head.next
			len += 1
		return len


class ListReverse:
	def __init__(self,head):
		self.listHead = head
		self.newHead = None

	def recursiveReverse(self,node):
		if node is None or node.next is None:
			self.newHead = node
			return node
		head = self.recursiveReverse(node.next)
		head.next = node
		node.next = None
		return node

	def getReverseList(self):
		self.recursiveReverse(self.listHead)
		return self.newHead



if __name__ == "__main__":
	util1 = ListUtility()
	util2 = ListUtility()

	list1 = util1.createList(9)
	list2 = util2.createList(3)

	# 构造重叠队列
	node = util1.getNodeByIdx(4)
	tail = util2.getNodeByIdx(2)
	tail.next = node

	checker = ListIntersetFinder(list1,list2)
	interset = checker.getFirstIntersetNode()
	print("The first interset node is : {0}".format(interset.value))