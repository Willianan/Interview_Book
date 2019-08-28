# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-25 11:22
@Project:InterView_Book
@Filename:21_栈的压入弹出序列.py
@description:
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
	def IsPopOrder(self, pushV, popV):
		if not pushV or len(pushV) != len(popV):
			return 0
		stack = []
		for i in pushV:
			stack.append(i)
			while len(stack) and stack[-1] == popV[0]:
				stack.pop()
				popV.pop(0)
		if len(stack):
			return 0
		return 1
