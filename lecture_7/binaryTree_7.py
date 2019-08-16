# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-16 15:50
@Project:InterView_Book
@Filename:binaryTree_7.py
@description:
    设计搜索输入框的输入提示功能
"""

class TreeNode:
	def __init__(self):
		self.s = ""
		self.map = {}

	def setString(self,strings):
		# 设置节点对应字符串
		self.s = strings

	def getString(self):
		return self.s

	def nextNode(self,b):
		# 根据字符构造当前节点的子节点
		if self.map.get(b,None) is None:
			n = TreeNode()
			self.map[b] = n
		return self.map[b]

	def getNode(self,b):
		return self.map[b]

	def getAllNextNodes(self):
		arr = []
		begin = ord('a')
		end = ord('z') + 1
		for i in range(begin,end):
			n = self.map.get(chr(i),None)
			if n is not None:
				arr.append(n)
		return arr


class TrieBuilder:
	def __init__(self):
		self.root = TreeNode()
		self.stack = []

	def addWord(self,s):
		node = self.root
		for i in range(len(s)):
			node = node.nextNode(s[i])
		node.setString(s)

	def addNodeListToStack(self,nodes):
		for node in nodes:
			self.stack.append(node)

	def getAllWordsByPrefix(self,prefix):
		node = self.root
		for i in range(len(prefix)):
			node = node.getNode(prefix[i])
			if node is None:
				return None
		self.addNodeListToStack(node.getAllNextNodes())
		allWords = []
		while len(self.stack) > 0:
			n = self.stack.pop()
			allWords.append(n.getString())
			self.addNodeListToStack(n.getAllNextNodes())
		return allWords


if __name__ == "__main__":
	dictionary = ['tea','to','ted','ten','A','in','inn']
	tb = TrieBuilder()
	for word in dictionary:
		tb.addWord(word)
	prefixWords = tb.getAllWordsByPrefix('t')
	print("words with prifix of t are: ")
	for word in prefixWords:
		print("{0}".format(word),end=" ")