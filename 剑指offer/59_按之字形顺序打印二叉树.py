# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:35
@Project:InterView_Book
@Filename:59_按之字形顺序打印二叉树.py
@description:
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""

from collections import deque


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def Print(self, pRoot):
		# write code here
		if not pRoot:
			return []
		res, tmp = [], []
		last = pRoot
		q = deque([pRoot])
		left_to_right = True
		while q:
			t = q.popleft()
			tmp.append(t.val)
			if t.left:
				q.append(t.left)
			if t.right:
				q.append(t.right)
			if t == last:
				res.append(tmp if left_to_right else tmp[::-1])
				left_to_right = not left_to_right
				tmp = []
				if q:
					last = q[-1]
		return res
