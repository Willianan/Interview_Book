# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 15:52
@Project:InterView_Book
@Filename:stack_4.py
@description:
    使用堆栈解决汉诺塔问题
"""

'''
题目描述：
	有3根杆子，其中一根上有n快铁饼，铁饼由小到大依次从上往下排列，要求把杆1上的铁饼挪到杆2上，
	杆3可以作为铁饼转移的中转站。当转移铁饼时，必须保证小铁饼只能放到大铁饼的上头，请给出移动步骤。
'''



class HanoiMove:
	def __init__(self,stackNum,stackFrom,stackTo):
		if stackNum <= 0 or stackFrom == stackTo or stackFrom < 0 or stackTo < 0:
			raise RuntimeError("Invalid parameters")
		self.stackFrom = stackFrom
		self.stackTo = stackTo
		self.hanoiMove = []
		self.moveHanoiStack(self.stackFrom,self.stackTo,1,stackNum)


	def printMoveSteps(self):
		if len(self.hanoiMove) == 1:
			print(self.hanoiMove.pop())
			return
		s = self.hanoiMove.pop()
		self.printMoveSteps()
		print(s)

	def moveHanoiStack(self, stackFrom, stackTo, top, bottom):
		s = "Moving ring " + str(bottom) + " from stack " + str(stackFrom) + " to " + str(stackTo)
		if bottom - top == 0:
			self.hanoiMove.append(s)
			return
		other = stackFrom
		for i in range(1,4):
			if i != stackFrom and i != stackTo:
				other = i
				break
		self.moveHanoiStack(stackFrom,other,top,bottom - 1)
		self.hanoiMove.append(s)
		self.moveHanoiStack(other,stackTo,top,bottom - 1)


if __name__ == "__main__":
	hm = HanoiMove(3,1,2)
	hm.printMoveSteps()