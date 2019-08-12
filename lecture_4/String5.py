# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 16:35
@Project:InterView_Book
@Filename:String5.py
@description:
    用有限状态自动机匹配字符串
"""

"""
题目描述：
	给定两个字符串，S和T，其中S是要查找的字符串，T是被查找的文本，要求
	给出一个查找算法，找出S在T中第一次出现的位置
"""


class StringAutomation:
	def __init__(self,P):
		# 用字典来表示状态机跳转表
		self.jumpTable = {}
		self.P = P
		# 为简单起见，在此假设文本和字符串又3个字符组成。如果要处理26个字符组成的文本，只要把下面
		# 变量改成26即可
		self.alphaSize = 3
		self.makeJumpTable()

	def makeJumpTable(self):
		m = len(self.P)
		for q in range(m):
			for k in range(self.alphaSize):
				Pq = self.P[0:q]
				# 构造每一个可能的输入字符
				c = chr(ord('a') + k)
				Pq += c
				# 查找从p的首字符开始连续的几个字符能构成Pq的后缀
				nextState = self.findSuffix(Pq)
				print("from state {0} receive input char {1} jump to state {2}".format(q,c,nextState))
				'''
				跳转表中每一行也是一个字典，一个字符对应一个状态节点
				'''
				jumpLine = self.jumpTable.get(q)
				if jumpLine is None:
					jumpLine = {}
				jumpLine[c] = nextState
				self.jumpTable[q] = jumpLine

	def findSuffix(self, Pq):
		# 查找从p的首字符开始，连续几个字符构成的字符串能成为Pq的后缀
		suffixLen = 0
		k = 0
		while k < len(Pq) and k < len(self.P):
			'''
			看看P从首字符开始总共有几个字符可以和字符串Pq最后k个字符形成的字符串相匹配
			'''
			i = 0
			while i <= k:
				if Pq[len(Pq)-1-k+i] != self.P[i]:
					break
				i += 1
			if i - 1 == k:
				'''
				这里加1，是因为数组的下标与对应的个数之间相差1
				'''
				suffixLen = k + 1
			k += 1
		return suffixLen

	def match(self,T):
		# 状态机初始时处于状态节点0
		q = 0
		print("Begin matching.........")
		'''
		依次读入文本T中的字符，然后查表看看状态机跳转节点，如果跳转到的节点编号与字符串
		P的长度一致，那表明文本T包含了字符串P
		'''
		for i in range(len(T)):
			# 根据状态节点获取跳转表中对应的一行
			jumpLine = self.jumpTable.get(q)
			oldState = q
			# 根据当前输入字符获取下一个状态
			q = jumpLine.get(T[i])
			if q is None:
				# 输入的字符无法跳转到有效的下一个状态节点，这表明跳转表的构建可能出错
				return -1
			print("In state {0} receive input {1} jump to state {2}".format(oldState,T[i],q))
			if q == len(self.P):
				# 状态节点编号如果与P的长度一致，则表明T包含了P
				return i-q-1
		return -1


if __name__ == "__main__":
	P = "ababaca"
	T = "baabababaca"
	sa = StringAutomation(P)
	pos = sa.match(T)
	if pos != -1:
		print("Match in position {0}".format(pos))