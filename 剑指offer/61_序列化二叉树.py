# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 21:51
@Project:InterView_Book
@Filename:61_序列化二叉树.py
@description:
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层
序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号
表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	flag = -1

	def Serialize(self, root):
		s = ""
		s = self.recursionSerialize(root, s)
		return s

	def recursionSerialize(self, root, s):
		if root is None:
			s = '$,'
			return s
		s = str(root.val) + ','
		left = self.recursionSerialize(root.left, s)
		right = self.recursionSerialize(root.right, s)
		s += left + right
		return s

	def Deserialize(self, s):
		self.flag += 1
		l = s.split(',')
		if (self.flag >= len(s)):
			return None
		root = None
		if l[self.flag] != '$':
			root = TreeNode(int(l[self.flag]))
			root.left = self.Deserialize(s)
			root.right = self.Deserialize(s)
		return root
