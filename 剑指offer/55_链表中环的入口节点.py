# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 20:56
@Project:InterView_Book
@Filename:55_链表中环的入口节点.py
@description:
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def EntryNodeOfLoop(self, pHead):
		if pHead == None or pHead.next == None or pHead.next.next == None:
			return None
		low = pHead.next
		fast = pHead.next.next
		while low != fast:
			if fast.next == None or fast.next.next == None:
				return None
			low = low.next
			fast = fast.next.next
		fast = pHead
		while low != fast:
			low = low.next
			fast = fast.next
		return fast
