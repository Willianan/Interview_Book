# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 11:27
@Project:InterView_Book
@Filename:23_二叉搜索树的后序遍历序列.py
@description:
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
	def VerifySquenceOfBST(self, sequence):
		# write code here
		if not sequence:
			return False
		if len(sequence) == 1:
			return True
		length = len(sequence)
		root = sequence[-1]
		i = 0
		while sequence[i] < root:
			i = i + 1
		k = iz
		for j in range(i, length - 1):
			if sequence[j] < root:
				return False
		left_s = sequence[:k]
		right_s = sequence[k:length - 1]
		leftIs = True
		rightIs = True
		if len(left_s) > 0:
			leftIs = self.VerifySquenceOfBST(sequence=left_s)
		if len(right_s) > 0:
			rightIs = self.VerifySquenceOfBST(sequence=right_s)
		return leftIs and rightIs
