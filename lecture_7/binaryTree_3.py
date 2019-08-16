# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 21:36
@Project:InterView_Book
@Filename:binaryTree_3.py
@description:
    二叉树的Morris遍历法
"""

'''
题目描述：
	如果二叉树的高度很大，且系统分配给函数调用堆栈的内存有限，当递归调用层次太多时，就会
	影响程序的性能。请给出空间复杂度为O(1)的二叉树遍历法
'''


class TreeNode:
	def __init__(self,val):
		self.left = None
		self.value = val
		self.right = None


class TreeUtil:
	def __init__(self):
		self.root = None

	def addTreeNode(self,node):
		if self.root is None:
			self.root = node
			return
		currenNode = self.root
		prevNode = self.root
		while currenNode is not None:
			prevNode = currenNode
			if currenNode.value > node.value:
				currenNode = currenNode.left
			else:
				currenNode =currenNode.right
		if prevNode.value > node.value:
			prevNode.left = node
		else:
			prevNode.right = node

	def getTreeRoot(self):
		return self.root

class MorrisTraval:
	def __init__(self,root):
		self.root = root

	def traval(self):
		n = self.root
		while n is not None:
			if n.left is None:
				print("{0}".format(n.value),end=' ')
				n = n.right
			else:
				pre = self.getPredecessor(n)
				if pre.right is None:
					pre.right = n
					n = n.left
				elif pre.right is n:
					pre.right = None
					print("{0}".format(n.value),end=" ")
					n = n.right

	def getPredecessor(self, n):
		pre = n
		if n.left is not  None:
			pre = pre.left
			while pre.right is not None and pre.right is not n:
				pre = pre.right
		return pre


if __name__ == "__main__":
	nodes = [6,4,9,2,5,7,10,1,3,8]
	util = TreeUtil()
	for n in nodes:
		node = TreeNode(n)
		util.addTreeNode(node)
	root = util.getTreeRoot()
	mt = MorrisTraval(root)
	mt.traval()