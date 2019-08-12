# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-02 15:53
@Project:InterView_Book
@Filename:Array3.py
@description:
    计算等价类
"""


'''
题目描述：
	假设集合S:{1,2,...,n-1}，同时又两个数组A和B，它们的元素都来自于集合S，而且长度都是m。
	A、B两个数组来确定集合S中元素的等价关系，假如A[k]与B[k]是等价的，那么S便会划分成几个不相交的等价类子集
'''

class Number:
	# Number表示单独一个数字自己形成的集合
	def __init__(self,val):
		self.val = val
		self.set = []
		self.visited = False
		self.set.append(val)


# EquivalClass用于构造数字等价类
class EquivalClass:
	def __init__(self,n,A,B):
		# 先将集合S={1,2,..,n-1}中的每个元素各自构造成只包含自己的集合
		self.numArray = []
		for i in range(n):
			# 每一个Number都是只包含数字i本身的等价类
			self.numArray.append(Number(i))
		for i in range(len(A)):
			a = A[i]
			b = B[i]
			# A[i]和B[i]两个元素属于等价类，所有与该元素等价的元素都可以合成一个等价类集合
			self.makeSet(self.numArray[a],self.numArray[b])

	def makeSet(self,numberA,numberB):
		# 将两个等价类的元素合并成一个等价类，numberA.set存储的是所有与numberA.val等价的元素
		numberA.set.extend(numberB.set)
		numberB.set = numberA.set

	def printAllEquivalSet(self):
		for i in range(len(self.numArray)):
			self.printEquivalSet(self.numArray[i])

	def printEquivalSet(self,number):
		# 如果元素对应的等价类集合已经打印过，那么就越过
		if number.visited is True:
			return
		number.visited = True
		print("{",end='')
		for i in range(len(number.set)):
			print("{0}".format(number.set[i]),end=" ")
			self.numArray[number.set[i]].visited = True
		print("}")




if __name__ == "__main__":
	n = 7
	A = [1,5,3,6]
	B = [2,1,0,5]
	equival = EquivalClass(n,A,B)
	equival.printAllEquivalSet()