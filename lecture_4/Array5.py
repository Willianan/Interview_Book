# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-02 16:51
@Project:InterView_Book
@Filename:Array5.py
@description:
    数组的序列变换
"""



"""
题目描述：
	给定数组A，并给定一个变化序列P，将变换序列应用到数组A上，得到新的数组B。调整过程中不允许分配新内存
"""

class ArrayPermutation:
	def __init__(self,A,P):
		self.A = A
		self.P = P
		self.doPermutation()

	def doPermutation(self):
		for i in range(len(A)):
			# 计算A[i]右移后的位置
			change = self.relocate(i)
			temp = self.A[change]
			# 把A[i ... change-1]间的元素右移一位
			self.makeShilf(i,change)
			self.A[i] = temp


	def relocate(self,i):
		change = self.P[i]
		k = 0
		j = 0
		while j < i:
			if self.P[j] > change:
				k += 1
			j += 1
		return change + k


	def makeShilf(self,begin,end):
		i = end
		while i > begin:
			self.A[i] = self.A[i-1]
			i -= 1
	def getPermutation(self):
		return self.A


if __name__ == "__main__":
	A = [1,2,3,4,5,6]
	P = [3,1,5,4,0,2]
	ap = ArrayPermutation(A,P)
	print("array after permutation is:")
	print(ap.getPermutation())