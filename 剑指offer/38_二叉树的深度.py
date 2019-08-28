# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 21:30
@Project:InterView_Book
@Filename:38_二叉树的深度.py
@description:
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

from collections import deque
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def TreeDepth(self, pRoot):
		# write code here
		if pRoot is None:
			return 0
		dq = deque()
		layer = 1
		dq.append((pRoot,1))
		while dq:
			node,layer = dq.popleft()
			if node.left:
				dq.append((node.left,layer + 1))
			if node.right:
				dq.append((node.right,layer + 1))
		return layer