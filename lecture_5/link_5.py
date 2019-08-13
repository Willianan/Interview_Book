# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 10:36
@Project:InterView_Book
@Filename:link_5.py
@description:
    单向链表的奇偶排序
"""

'''
题目描述：
	给定一个单向链表，要求实现一个算法，把链表分为两部分，前一部分链表节点数值为偶数，
	后一部分链表节点数值全为奇数。
	要求算法不能分配多余内存，同时在操作链表时，不能更改节点内容，只能更改节点的next指针
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


class EvenOddListSorter:
	def __init__(self,listHead):
		self.listHead = listHead

	def sort(self):
		if self.listHead is None or self.listHead.next is None:
			return self.listHead
		# 将evenHead和oddHead分别指向首个偶数节点和奇数节点
		evenHead = self.listHead
		oddHead = self.listHead.next
		oddHeadCopy = oddHead
		while evenHead is not None and oddHead is not None:
			# 把evenHead.next指向oddHead.next
			evenTail = evenHead
			evenHead.next = oddHead.next
			evenHead = evenHead.next
			# 把oddHead.next指向evenHead.next
			if evenHead is not None:
				evenTail = evenHead
				oddHead.next = evenHead.next
				oddHead = oddHead.next
			# 把偶数队列和奇数队列首尾相连
			evenTail.next = oddHeadCopy
			return self.listHead


if __name__ == "__main__":
	util = ListUtility()
	head = util.createList(10)
	sorter = EvenOddListSorter(head)
	head = sorter.sort()
	util.printList(head)