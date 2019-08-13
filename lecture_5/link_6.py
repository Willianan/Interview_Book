# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 11:11
@Project:InterView_Book
@Filename:link_6.py
@description:
    双指针单向链表的自我复制
"""

'''
题目描述：
	要求设计一个算法，复制给定的Posting List。算法的时间复杂度是O(n)，算法除了分配节点所需
	内存外，不能分配多余内存。算法可以更改原队列，但改后需要将队列恢复原状
'''

import random

'''
Node用于表示队列中的节点，它包含两个域，value表示节点的值，next指向下一个节点
'''
class Node:
	def __init__(self,value):
		self.next = None
		self.value = value
		# 为了打印循环链表，加上标志
		self.visited = False
		# 增加jump指针
		self.jump = None

class ListUtility:
	def __init__(self):
		self.head = None
		self.tail = None
		self.map = {}
	def createList(self,nodeNum):
		# 生成含有nodeNum个节点的列表
		if nodeNum <= 0:
			return None
		self.listLength = nodeNum
		head = None
		value = 0
		node = None
		while nodeNum > 0:
			if head is None:
				head = Node(value)
				node = head
			else:
				node.next = Node(value)
				node = node.next
				self.tail = node
			self.map[value] = node
			value += 1
			nodeNum -= 1
		self.head = head
		return head

	def createJumpNode(self,head):
		while head is not None:
			n = random.randint(0,self.listLength - 1)
			head.jump = self.map[n]
			head = head.next


	def printPostingList(self,head):
		while head is not None:
			print("(node value: {0} jump value: {1}) ->".format(head.value,head.jump.value),end=" ")
			head = head.next
		print("null")
		
		
class PostingListCopy:
	def __init__(self,head):
		self.originalHead = head
		self.copyHead = None
		
	def copyPostingList(self):
		self.createPostingNodes()
		self.createJumpNodes()
		self.adjustNextPointer()
		return self.copyHead

	def createPostingNodes(self):
		node = None
		tempHead = self.originalHead
		# 先逐个复制原队列的每个节点
		while tempHead is not None:
			node = Node(tempHead.value)
			# 把复制节点的next指针指向原节点next指针指向的节点
			node.next = tempHead.next
			# 把原节点的next指针指向复制节点
			tempHead.next = node
			# 当前节点通过复制节点的next指针进入下一个节点
			tempHead = node.next

	def createJumpNodes(self):
		temp = self.originalHead
		# 指向复制队列的头节点
		self.copyHead = temp.next
		while temp is not None:
			cpNode = temp.next
			cpNode.jump = temp.jump.next
			temp = cpNode.next

	def adjustNextPointer(self):
		temp = self.originalHead
		while temp is not None:
			cpNode = temp.next
			temp.next = cpNode.next
			temp = temp.next
			if temp is not None:
				cpNode = temp.next
			else:
				cpNode.next = None


if __name__ == "__main__":
	util = ListUtility()
	head = util.createList(10)
	util.createJumpNode(head)
	util.printPostingList(head)

	pc = PostingListCopy(head)
	copyHead = pc.copyPostingList()
	print("print copied posting list:")
	util.printPostingList(copyHead)