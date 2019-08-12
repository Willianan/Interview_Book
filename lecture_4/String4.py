# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 15:51
@Project:InterView_Book
@Filename:String4.py
@description:
    Rabin-Karp字符串匹配算法
"""

'''
题目描述：
	给定两个字符串，S和T，其中S是要查找的字符串，T是被查找的文本，要求给出一个查找算法，
	找出S在T中第一次出现的位置
'''

class RabinKarp:
	def __init__(self,t,p,d,q):
		# t是搜索文本，p是匹配字符串，d是字符进制，q是求余素数
		self.T = t
		self.P = p
		self.d = d
		self.n = len(t)
		self.m = len(p)
		self.h = 1
		self.q = q
		# 计算h的值
		for i in range(self.m-1):
			self.h *= d
			self.h = self.h % q

	def match(self):
		p = 0
		t = 0
		# 预处理 计算p和T0
		for i in range(self.m):
			p = (self.d * p + ord(self.P[i]) - ord('a')) % self.q
			t = (self.d * t + ord(self.T[i]) - ord('a')) % self.q
		for s in range(self.n - self.m + 1):
			if p == t:
				# 如果求余后相同，那么就逐个字符比较
				for i in range(self.m):
					if i == self.m-1 and self.P[i] == self.T[s+i]:
						return s
					elif self.P[i] != self.T[s+i]:
						break
			if s <= self.n - self.m:
				# 从T(s)计算T(s+1)
				t =((self.d * (t - ord(self.T[s]) - ord('a')) * self.h) + (ord(self.T[s+self.m]) - ord('a'))) % self.q
				if t < 0:
					t += self.q
		return -1


if __name__ == "__main__":
	T = "abcdbaabcabaa"
	P = "abaa"
	rk = RabinKarp(T,P,26,29)
	s = rk.match()
	print("P is begin from {0} in T".format(s))