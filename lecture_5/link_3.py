# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 9:59
@Project:InterView_Book
@Filename:link_3.py
@description:
    在O(1)时间内删除单链表非末尾节点
"""

'''
题目描述：
	对于一个单向连接的链表，给定某个非末尾的任意节点，要求在O(1)时间内删除该节点
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

def deleteNode(node):
	if node.next is None:
		return
	# 把下一个节点的值复制到当前节点
	node.value = node.next.value
	# 把当前节点的next指针指向下下个节点
	node.next = node.next.next


if __name__ == "__main__":
	util = ListUtility()
	head = util.createList(10)
	print("List before node deletion:")
	util.printList(head)

	# 删除节点
	nodeDelete = 2
	node = head
	while nodeDelete > 0:
		node = node.next
		nodeDelete -= 1
	# 调用deleteNode删除该节点
	deleteNode(node)
	print("List after node deletion:")
	util.printList(head)