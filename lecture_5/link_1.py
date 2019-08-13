# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-12 15:45
@Project:InterView_Book
@Filename:link_1.py
@description:
    递归式实现链表快速倒转
"""


'''
题目描述：
	给定一个链表，请对该链表实现反转
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
	utility = ListUtility()
	head = utility.createList(10)
	utility.printList(head)
	# 执行倒转算法，然后再次打印队列
	reverse = ListReverse(head)
	utility.printList(reverse.getReverseList())