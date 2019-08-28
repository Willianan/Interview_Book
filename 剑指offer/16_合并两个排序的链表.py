# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 10:41
@Project:InterView_Book
@Filename:16_合并两个排序的链表.py
@description:
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# 返回合并后列表
	def Merge(self, pHead1, pHead2):
		# write code here
		if pHead1 is None:
			return pHead2
		if pHead2 is None:
			return pHead1
		if pHead1.val > pHead2.val:
			head = pHead2
			pHead2 = pHead2.next
		else:
			head = pHead1
			pHead1 = pHead1.next
		p = head
		while pHead1 is not None and pHead2 is not None:
			if pHead1.val > pHead2.val:
				head.next = pHead2
				pHead2 = pHead2.next
			else:
				head.next = pHead1
				pHead1 = pHead1.next
			head = head.next
		if pHead1 is not None:
			head.next = pHead1
		if pHead2 is not None:
			head.next = pHead2
		return p
