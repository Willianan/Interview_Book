# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 10:02
@Project:InterView_Book
@Filename:Array6.py
@description:
		二维数组的启发式搜索算法
"""

'''
题目描述
	Sukudo棋盘是一种逻辑游戏，它由9x*9的网格组成。玩法是要求每一行，每一列、每3*3的子网格都由1~9个数字填充，
	且每行每列每个子网格填充的数字都不重复。给定一个9*9的二维数组，请给出满足条件的填充算法
'''

class Sukudo:
	def __init__(self):
		# 构造一个9*9数组作为棋盘
		self.sukudoBoard = [[0] * 9 for i in range(9)]
		# 通过启发式搜索查找满足条件的数字填充方式
		res = self.setSukudoBoard(0,0)
		if res is True:
			self.printSukudoBoard()
		else:
			print("No satisfy answer!")

	def setSukudoBoard(self, x, y):
		# 使用启发式搜索填充棋盘
		if y >= 9:
			y = 0
			x += 1
		if x >= 9:
			return True
		# 在给定位置从1到9九个数字中选取一个满足条件的来填充
		for value in range(1,10):
			# 检测数字是否满足条件
			if self.checkValid(x,y,value) is True:
				self.sukudoBoard[x][y] = value
				# 设置下一个位置的数字
				if self.setSukudoBoard(x,y+1) is True:
					return True
		# 当前位置找不到合适的数字填充，返回到上一步
		self.sukudoBoard[x][y] = 0
		return False

	def printSukudoBoard(self):
		for i in range(9):
			for j in range(9):
				print("{0}".format(self.sukudoBoard[i][j]),end=' ')
			print()

	def checkValid(self, i, j, value):
		# 检测在第i行第j列放置数值value是否满足条件
		for k in range(9):
			# 检测数字所在行有没有出现重复
			if k != j and self.sukudoBoard[i][k] == value:
				return False
			# 检测数字所在列是否出现重复
			if k != i and self.sukudoBoard[k][j] == value:
				return False
		# 找到对应的3*3子网格，查看数字是否出现重复
		subX = int(i / 3) * 3
		subY = int(j / 3) * 3
		for p in range(subX,subX+3):
			for q in range(subY,subY+3):
				if p != i and q != j and self.sukudoBoard[p][q] == value:
					return False
		return True



if __name__ == "__main__":
	s = Sukudo()