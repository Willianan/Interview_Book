# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 22:11
@Project:InterView_Book
@Filename:25_复杂链表复制.py
@description:
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，
输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None


def iter_node(root):
	while root:
		yield root
		root = root.next


class Solution:
	# 返回 RandomListNode
	def Clone(self, pHead):
		mem = dict()
		for i, n in enumerate(iter_node(pHead)):
			mem[id(n)] = i
		lst = [RandomListNode(n.label) for n in iter_node(pHead)]
		for t, f in zip(iter_node(pHead), lst):
			if t.next:
				f.next = lst[mem[id(t.next)]]
			if t.random:
				f.random = lst[mem[id(t.random)]]
		return lst[0] if lst else None
