# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-12 14:50
@Project:InterView_Book
@Filename:String6.py
@description:
    KMP算法————字符串匹配算法的创意巅峰
"""

"""
题目描述：
	给定两个字符串S和T，其中S是要查找的字符串，T是被查找的文本，要求给出一个查找算法，找出S在
	T中第一次出现的位置。
"""

class KMPStringMatcher:
	def __init__(self,P):
		self.P = P
		# 数组Pi用于存储最长后缀信息
		self.Pi = []
		self.Pi.append(-1)
		for i in range(1,len(self.P)):
			# Pi[i]== -2 尚未计算Pi[0....i]对应的最长后缀
			self.Pi.append(-2)
		# 计算最长后缀数组
		self.computePrefix()
		print(self.Pi)

	def computePrefix(self):
		m = len(self.P)
		# 只有一个字符组成的字符串没有长度比它更小的最长后缀
		self.Pi[0] = -1
		k = -1
		for q in range(1,m):
			while k >= 0 and self.P[k+1] != self.P[q]:
				k = self.Pi[k]
			if self.P[k+1] == self.P[q]:
				k = k + 1
			self.Pi[q] = k

	def match(self,T):
		n = len(T)
		m = len(self.P) - 1
		q = -1
		for i in range(n):
			# 当字符不匹配时，获取最长后缀
			while q > 0 and self.P[q+1] != T[i]:
				q = self.Pi[q]
			if self.P[q+1] == T[i]:
				q += 1
			if q == m:
				# 匹配成功
				return i - m
		return -1


if __name__ == "__main__":
	T = "abababacaba"
	P = "ababaca"
	kmp = KMPStringMatcher(P)
	pos = kmp.match(T)
	if pos != -1:
		print("P is contained in T from position {0}".format(pos))