# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-16 16:26
@Project:InterView_Book
@Filename:heap_1.py
@description:
    使用堆排序实现系统Timer机制
"""

'''
题目描述：
	Timer时钟机制
'''

import sys

class HeapSort:
	def __init__(self,array):
		self.heapSize = len(array)
		self.heapArray = array

	def parent(self,i):
		# 获得父结点在数组中的下标
		return int(i/2)

	def left(self,i):
		# 获得左孩子在数组中的下标
		return 2 * i

	def right(self,i):
		# 获得右孩子在数组中的下标
		return 2*i+1

	def maxHeapify(self,i):
		i += 1
		l = self.left(i)
		r = self.right(i)
		i -= 1
		l -= 1
		r -= 1
		largest = -1
		if l < self.heapSize and self.heapArray[l] > self.heapArray[i]:
			largest = l
		else:
			largest = i
		if r < self.heapSize and self.heapArray[r] > self.heapArray[largest]:
			largest = r
		if largest != i:
			temp = self.heapArray[i]
			self.heapArray[i] = self.heapArray[largest]
			self.heapArray[largest] = temp
			self.maxHeapify(largest)

	def buildMaxHeap(self):
		i = int(self.heapSize / 2)
		while i >= 0:
			self.maxHeapify(i)
			i -= 1
		return self.heapArray

	def maximun(self):
		return self.heapArray[0]

	def extractMaximun(self):
		if self.heapSize < 1:
			return None
		max = self.heapArray[0]
		self.heapArray[0] = self.heapArray[self.heapSize - 1]
		self.heapSize -= 1
		self.heapArray.pop()
		self.maxHeapify(0)
		return max

	def increaseKey(self,i,k):
		if self.heapArray[i] == k:
			return
		self.heapArray[i] = k
		while i > 0 and self.heapArray[self.parent(i)] < self.heapArray[i]:
			temp = self.heapArray[self.parent(i)]
			self.heapArray[self.parent(i)] = self.heapArray[i]
			self.heapArray[i] = temp
			i = self.parent(i)

	def insert(self,val):
		self.heapArray.append(-sys.maxsize)
		self.heapSize += 1
		self.increaseKey(self.heapSize - 1,val)
		return self.heapArray



if __name__ == "__main__":
	A = [1,2,3,4,7,8,9,10,14,16]
	hs = HeapSort(A)
	heap = hs.buildMaxHeap()
	for i in heap:
		print("{0}".format(i),end=" ")

	print("max value is {0}".format(hs.extractMaximun()))
	print("max value after calling extractMaximun is {0}".format(hs.maximun()))
	hs.increaseKey(8,17)
	print("Maximun element after calling increaseKey is {0}".format(hs.maximun()))
	hs.insert(20)
	print("Maximun element after calling insert is {0}".format(hs.maximun()))
