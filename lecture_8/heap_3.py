# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:47
@Project:InterView_Book
@Filename:heap_3.py
@description:
    快速获取数组中点的相邻区域点
"""

"""
题目描述：
	假定给你一个含有n个元素的数组，要求设计一个复杂度为O(n)的算法，
	找出距离数组中点最近的k个元素
"""
import random

def findElementWithPos(array,pos):
	if len(array) < 1 or pos >= len(array):
		return None
	# 随机在数组中抽取一个元素
	p = random.randint(0,len(array)-1)
	pivot = array[p]
	begin = 0
	end = len(array) - 1
	while begin != end:
		if array[begin] >= pivot:
			temp = array[end]
			array[end] = array[begin]
			array[begin] = temp
			end -= 1
		else:
			begin += 1
	if array[begin] < pivot:
		begin += 1
	if begin == pos:
		return pivot
	if begin > pos:
		return findElementWithPos(array[:begin],pos)
	else:
		return findElementWithPos(array[begin:],pos-begin)

class HeapPairSort:
	def __init__(self,array):
		self.heapSize = len(array)
		self.heapArray = array

	def parent(self,i):
		return int(i/2)

	def left(self,i):
		return 2*i

	def right(self,i):
		return 2*i+1

	def maxHeapify(self,i):
		i += 1
		l = self.left(i)
		r = self.right(i)
		i -= 1
		l -= 1
		r -= 1
		largest = -1
		if l < self.heapSize and self.heapArray[l].val > self.heapArray[i].val:
			largest = l
		else:
			largest = i
		if r < self.heapSize and self.heapArray[r].val > self.heapArray[largest].val:
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

	def maxMun(self):
		return self.heapArray[0]

	def extractMaxMun(self):
		if self.heapSize < 1:
			return None
		max = self.heapArray[0]
		self.heapArray[0] = self.heapArray[self.heapSize - 1]
		self.heapSize -= 1
		self.heapArray.pop()
		self.maxHeapify(0)
		return max

	def increaseKey(self,i,k):
		if self.heapArray[i].val >= k:
			return
		self.heapArray[i].val = k
		while i > 0 and self.heapArray[self.parent(i)].val < self.heapArray[i].val:
			self.heapArray[self.parent(i)].exchange(self.heapArray[i])
			i = self.parent(i)

	def insert(self,pair):
		import sys
		p = Pair(-sys.maxsize,pair.begin,pair.end)
		self.heapArray.append(p)
		self.heapSize += 1
		self.increaseKey(self.heapSize-1,pair.val)
		return self.heapArray


class Pair:
	def __init__(self,val,begin,end):
		self.val = val
		self.begin = begin
		self.end = end

	def exchange(self,pair):
		v = self.val
		b = self.begin
		e = self.end

		self.val = pair.val
		self.begin = pair.begin
		self.end = pair.end

		pair.val = v
		pair.begin = b
		pair.end = e

if __name__ == "__main__":
	array = [1,-5,3,7,1000,2,-10]
	element = findElementWithPos(array,3)
	print(element)

	array = [7,14,10,12,2,11,29,3,4]
	mid = findElementWithPos(array,4)
	print("mid point of array is :",mid)
	pairArray = []
	for i in range(len(array)):
		p = Pair(abs(array[i] - mid),i,i)
		pairArray.append(p)

	k = 5
	hps = HeapPairSort(pairArray[0:k])
	for i in range(k+1,len(pairArray)):
		if pairArray[i].val < hps.maxMun().val:
			hps.extractMaxMun()
			hps.insert(pairArray[i])
	print("{0} elements that are closet to mid pointare:".format(k))
	for i in range(hps.heapSize):
		pos = hps.heapArray[i].begin
		print("{0}".format(array[pos]),end=' ')