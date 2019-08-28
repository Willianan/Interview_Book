# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:02
@Project:InterView_Book
@Filename:56_删除链表中重复的节点.py
@description:
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def deleteDuplication(self, pHead):
		# write code here
		if pHead is None or pHead.next is None:
			return pHead
		head1 = pHead.next
		if head1.val != pHead.val:
			pHead.next = self.deleteDuplication(pHead.next)
		else:
			while pHead.val == head1.val and head1.next is not None:
				head1 = head1.next
			if head1.val != pHead.val:
				pHead = self.deleteDuplication(head1)
			else:
				return None
		return pHead
