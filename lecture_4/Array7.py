# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 10:40
@Project:InterView_Book
@Filename:Array7.py
@description:
    二维数组的旋转遍历
"""

'''
题目描述
	假定由一个二维数组，要求将数组中的元素以顺时针的螺旋方式打印出来
	要求实现一个函数，使得数组的元素能按照顺时针方向打印出来
'''


class MatrixSpiral:
	def __init__(self,n):
		# 先构造一个n*n二维数组，并初始化
		self.array = [[0] * n for i in range(n)]
		for i in range(n):
			for j in range(n):
				self.array[i][j] = i * n + j + 1
			print(self.array[i])
		self.size = n
		# top、right、bottom、left表示4个指针
		self.top = 0
		self.right = n - 1
		self.bottom = n - 1
		self.left = 0

	def spiralPrint(self):
		# 根据4个指针的指向打印二维数组元素
		while self.top <= self.bottom and self.left <= self.right:
			# 先打印top指向的行
			for i in range(self.left,self.right+1):
				print(self.array[self.top][i],end=' ')
			# 打印right指向的列
			for i in range(self.top+1,self.bottom+1):
				print(self.array[i][self.right],end=' ')
			# 打印bottom指向的行
			for i in range(self.bottom-1,self.left-1,-1):
				print(self.array[self.bottom][i],end=' ')
			# 打印left指向的列
			for i in range(self.bottom-1,self.top,-1):
				print(self.array[i][self.left],end=' ')

			self.top += 1
			self.right -= 1
			self.bottom -= 1
			self.left += 1


if __name__ == "__main__":
	m = MatrixSpiral(5)
	m.spiralPrint()