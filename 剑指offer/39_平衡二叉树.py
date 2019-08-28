# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-26 21:44
@Project:InterView_Book
@Filename:39_平衡二叉树.py
@description:
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def IsBalanced_Solution(self, pRoot):
		# write code here
		if pRoot == None:
			return True
		if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
			return False
		return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

	def TreeDepth(self, pRoot):
		# write code here
		if pRoot == None:
			return 0
		nLeft = self.TreeDepth(pRoot.left)
		nRight = self.TreeDepth(pRoot.right)
		return max(nLeft + 1, nRight + 1)
