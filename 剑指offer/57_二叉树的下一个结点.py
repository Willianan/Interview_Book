# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:05
@Project:InterView_Book
@Filename:57_二叉树的下一个结点.py
@description:
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None


class Solution:
	def GetNext(self, pNode):
		# write code here
		if not pNode:
			return pNode
		if pNode.right:
			left1 = pNode.right
			while left1.left:
				left1 = left1.left
			return left1
		while pNode.next:
			tmp = pNode.next
			if tmp.left == pNode:
				return tmp
			pNode = tmp
