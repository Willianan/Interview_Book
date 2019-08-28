# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:55
@Project:InterView_Book
@Filename:62_二叉搜索树的第k个节点.py
@description:
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如,(5，3，7，2，4，6，8)中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 返回对应节点TreeNode
	def KthNode(self, pRoot, k):
		# write code here
		# 第三个节点是4
		# 前序遍历5324768
		# 中序遍历2345678
		# 后序遍历2436875
		# 所以是中序遍历，左根右
		global result
		result = []
		self.midnode(pRoot)
		if k <= 0 or len(result) < k:
			return None
		else:
			return result[k - 1]

	def midnode(self, root):
		if not root:
			return None
		self.midnode(root.left)
		result.append(root)
		self.midnode(root.right)
