# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 15:06
@Project:InterView_Book
@Filename:stack_1.py
@description:
    利用堆栈计算逆向波兰表达式
"""

'''
题目描述：
	给定一个逆向波兰表达式，要求选取一个合适的数据结构并设计算法，计算除表达式的值
	解决问题的步骤：
		(1)、如果当前字符是数字，把数字压入堆栈
		(2)、如果当前字符是运算符，从堆栈弹出两个元素，根据运算符做相应运算后，将结果压入堆栈
		(3)、当所有字符处理完毕后，堆栈上包含的数值就是表达式的值
'''


class ReversePolishExpr:
	def __init__(self,expr):
		self.expression = expr
		self.stack = []

	def calculation(self):
		exprs = self.expression.split(",")
		for expr in exprs:
			if self.isOperator(expr) and len(self.stack) < 2:
				raise RuntimeError("stack less than 2 elements")
			if self.isOperator(expr):
				self.doCalculation(expr)
			else:
				self.stack.append(int(expr))
		return self.stack.pop()

	def isOperator(self, expr):
		if len(expr) > 1:
			return False
		if expr == '+'or expr == '+' or expr == '*' or expr == '/':
			return True
		return False


	def doCalculation(self, operator):
		op1 = self.stack.pop()
		op2 = self.stack.pop()

		if operator == "+":
			self.stack.append(op1 + op2)
		elif operator == "-":
			self.stack.append(op1 - op2)
		elif operator == "*":
			self.stack.append(op1 * op2)
		elif operator == "/":
			self.stack.append(op1 / op2)


if __name__ == "__main__":
	rp = ReversePolishExpr("3,4,*,1,2,+,+")
	print("result of reverse polish expression is {0}".format(rp.calculation()))