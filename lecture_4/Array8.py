# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 11:01
@Project:InterView_Book
@Filename:Array8.py
@description:
    矩阵的90度旋转
"""

'''
题目描述：
	给定一个二维数组，将其顺时针旋转90度
'''


class MatrixRotate:
	def __init__(self,n):
		# 初始化矩阵
		self.matrix = [[0] * n for i in range(n)]
		for i in range(n):
			for j in range(n):
				self.matrix[i][j] = i * n + j + 1
		self.size = n
		self.top = 0
		self.right = n - 1
		self.bottom = n - 1
		self.left = 0

		# 用top_mov,right_mov,bottom_mov,left_mov表示4个指针挪动后的位置
		self.top_mov = self.left
		self.right_mov = self.top
		self.bottom_mov = self.right
		self.left_mov = self.bottom
		self.printMatrix()

	def printMatrix(self):
		for i in range(self.size):
			print(self.matrix[i])


	def rotate(self):
		while self.top < self.bottom and self.left < self.right:
			# 获得4个指针指向的元素
			top_val = self.matrix[self.top][self.top_mov]
			right_val = self.matrix[self.right_mov][self.right]
			bottom_val = self.matrix[self.bottom][self.bottom_mov]
			left_val = self.matrix[self.left_mov][self.left]

			# 对指针指向的元素进行轮换
			self.matrix[self.top][self.top_mov] = left_val
			self.matrix[self.right_mov][self.right] = top_val
			self.matrix[self.bottom][self.bottom_mov] = right_val
			self.matrix[self.left_mov][self.left] = bottom_val

			# 移动4个指针
			self.top_mov += 1
			self.right_mov += 1
			self.bottom_mov -= 1
			self.left_mov -= 1

			# 如果指针指向的元素都转移完毕，让4个指针指向下一层
			if self.top_mov >= self.right:
				self.top += 1
				self.right -= 1
				self.bottom -= 1
				self.left += 1

				self.top_mov = self.left
				self.right_mov = self.top
				self.bottom_mov = self.right
				self.left_mov = self.bottom




if __name__ == "__main__":
	print("matrix before rotate:")
	mr = MatrixRotate(5)
	mr.rotate()
	print("matrix after rotate:")
	mr.printMatrix()