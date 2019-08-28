# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 11:16
@Project:InterView_Book
@Filename:36_两个链表的第一个公共节点.py
@description:
题目描述
输入两个链表，找出它们的第一个公共结点。
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def FindFirstCommonNode(self, pHead1, pHead2):
		# write code here
		if  pHead1 is None or pHead2 is None:
			return
		list1 = []
		node1 = pHead1
		node2 = pHead2
		while node1:
			list1.append(node1.val)
			node1 = node1.next
		while node2:
			if node2.val in list1:
				return node2
			else:
				node2 = node2.next

