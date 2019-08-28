# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 10:34
@Project:InterView_Book
@Filename:15_反转链表.py
@description:
题目描述
	输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# 返回ListNode
	def ReverseList(self, pHead):
		# write code here
		if not pHead or not pHead.next:
			return pHead
		last = None
		while pHead:
			tmp = pHead.next
			pHead.next = last
			last = pHead
			pHead = tmp
		return last



