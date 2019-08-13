# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 16:35
@Project:InterView_Book
@Filename:stack_6.py
@description:
    计算滑动窗口内的最大网络流量
"""

'''
题目描述：
	给定一根数组A，里面有n个流量点记录。同时给定滑动窗口大小w，A[i]格式为流量
	记录点(t,v)，其中时间t升序排列，要求设计一个算法，计算A中每个时间点在滑动窗口内的最大网络流量
'''

class window:
	def __init__(self,time,volumn):
		self.time = time
		self.volumn = volumn

	def getTime(self):
		return self.time
	def getVolumn(self):
		return self.volumn


class SlidingWindow:
	def __init__(self,winList,size):
		self.windowList = winList
		self.workingQueue = []
		self.maxQueue = []
		self.count = 0
		self.start = self.end = len(winList) - 1
		self.windowSize = size

		if len(winList) == 0 or size <= 0:
			raise RuntimeError("Invalid parameters")

	def printMaxVolumnForTimePoints(self):
		while self.end >= 0:
			self.findSlidingWindow()
			m = self.maxQueue[0]
			w = self.windowList[self.end]
			print("Max volunm from time: {0} in sliding window size is: {1}".format(w.getTime(),m.getVolumn()))
			if w == m:
				self.maxQueue = self.maxQueue[1:]
			self.end -= 1

	def findSlidingWindow(self):
		self.count = 1
		while self.start >= 0 and self.windowList[self.end].getTime() \
				- self.windowList[self.start].getTime() <= self.windowSize:
			if len(self.maxQueue) > 0 and self.windowList[self.start].getVolumn() > self.maxQueue[0].getVolumn():
				self.maxQueue = []
			self.start -= 1
			self.count += 1
		if self.start >= 0 and 	self.windowList[self.end].getTime() \
				- self.windowList[self.start].getTime() > self.windowSize:
			self.start += 1
			self.count -= 1

		if self.count > 0:
			self.buildMaxQueue()
		if len(self.maxQueue) == 0:
			self.maxQueue = self.workingQueue
			self.workingQueue = []

	def buildMaxQueue(self):
		s = 0
		if self.start > 0:
			s = self.start
		while self.count > 0 and s <= self.end:
			if len(self.workingQueue) == 0 or self.windowList[s].getVolumn() > self.workingQueue[0].getVolumn():
				self.workingQueue.insert(0,self.windowList[s])
			s += 1
			self.count -= 1
			self.start -= 1




if __name__ == "__main__":
	windowList = []
	windowList.append(window(1,10))
	windowList.append(window(3, 1))
	windowList.append(window(5, 4))
	windowList.append(window(7, 8))
	windowList.append(window(9, 3))
	windowList.append(window(12, 9))
	windowList.append(window(19, 4))

	sw = SlidingWindow(windowList,6)
	sw.printMaxVolumnForTimePoints()