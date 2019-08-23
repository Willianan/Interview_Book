# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-16 17:04
@Project:InterView_Book
@Filename:heap_2.py
@description:
    波浪形数组的快速排序法
"""

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

class WaveArraySorter:
	def __init__(self,array):
		self.waveArray = []
		self.originalArray = array
		self.waveBegin = 0
		self.waveEnd = 0
		self.pairArray = []
		self.findWaveAndSort()

	def findWaveAndSort(self):
		i = self.waveBegin
		waveDown = False
		while i < len(self.originalArray) - 1:
			if self.originalArray[i] > self.originalArray[i+1]:
				waveDown = True
			risingAgain = self.originalArray[i] < self.originalArray[i+1]
			reachingEnd = (i+1 == len(self.originalArray) - 1)
			if (waveDown is True and risingAgain) or reachingEnd:
				if reachingEnd is True:
					self.waveEnd = i + 1
				else:
					self.waveEnd = i
				self.sortWave()
				p = Pair(self.waveArray[self.waveEnd],self.waveBegin,self.waveEnd)
				self.pairArray.append(p)
				self.waveBegin = i + 1
				waveDown = False
			i += 1

	def sortWave(self):
		begin = self.waveBegin
		end = self.waveEnd
		while begin <= end:
			if self.originalArray[begin] < self.originalArray[end]:
				self.waveArray.append(self.originalArray[begin])
				begin += 1
			else:
				self.waveArray.append(self.originalArray[end])
				end -= 1

	def getWaveSortedArray(self):
		return self.waveArray


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

if __name__ == "__main__":
	wave = [57,131,493,294,221,339,418,452,442,190,230,310,510,432,271,280,350,631,450,332]
	ws = WaveArraySorter(wave)
	hps = HeapPairSort(ws.pairArray)
	hps.buildMaxHeap()
	count = len(wave) - 1
	wave = []
	waveSortedArray = ws.getWaveSortedArray()

	while count >= 0:
		max = hps.extractMaxMun()
		wave.insert(0,max.val)
		if max.end > max.begin:
			max.end -= 1
			max.val = waveSortedArray[max.end]
			hps.insert(max)
		count -= 1

	print(wave)