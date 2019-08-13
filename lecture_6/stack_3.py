# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 15:43
@Project:InterView_Book
@Filename:stack_3.py
@description:
    使用堆栈判断括号匹配
"""

'''
题目描述：
	给定一个括号字符串，判断左右括号是否匹配
'''


class ParenMatch:
	def __init__(self,parens):
		self.parens = parens
		self.stack = []

	def isMatch(self):
		for c in self.parens:
			if c == "(":
				self.stack.append(c)
			elif c == ")":
				if len(self.stack) == 0:
					return False
				self.stack.pop()
			else:
				raise RuntimeError("Illegal character")
		if len(self.stack) != 0:
			return False
		return True


if __name__ == "__main__":
	s = "((())(()))"
	pm = ParenMatch(s)
	print("the matching result is :{0}".format(pm.isMatch()))