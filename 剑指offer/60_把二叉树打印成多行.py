# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:40
@Project:InterView_Book
@Filename:60_把二叉树打印成多行.py
@description:
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 返回二维列表[[1,2],[4,5]]
	def Print(self, pRoot):
		# write code here
		if not pRoot:
			return []
		res = []
		tmp = [pRoot]
		while tmp:
			size = len(tmp)
			row = []
			for i in tmp:
				row.append(i.val)
			res.append(row)
			for i in range(size):
				node = tmp.pop(0)
				if node.left:
					tmp.append(node.left)
				if node.right:
					tmp.append(node.right)
		return res