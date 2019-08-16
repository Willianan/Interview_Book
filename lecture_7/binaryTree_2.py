# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 21:15
@Project:InterView_Book
@Filename:binaryTree_2.py
@description:
    镜像二叉树的检测
"""

'''
题目描述：
	要求给定一棵二叉树的根节点，判断该二叉树是否具备镜像特征
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

	def getSymmetricTree(self):
		n = TreeNode(314)
		n.left = TreeNode(6)
		n.left.right = TreeNode(2)
		n.left.right.right = TreeNode(3)

		n.right = TreeNode(6)
		n.right.left = TreeNode(2)
		n.right.left.left = TreeNode(3)


class SymmetricTree:
	def __init__(self,root):
		self.treeList1 = []
		self.treeList2 = []
		self.isSymmetric = False
		# 按照两种遍历方式层级遍历二叉树
		self.TreeToList(root,self.treeList1,True)
		self.TreeToList(root,self.treeList2,True)
		# 比较两个队列，看它们是否相同
		self.isSymmetric = self.compureList(self.treeList1,self.treeList2)


	def isTreeSymmetric(self):
		return self.isSymmetric

	def TreeToList(self, root, list, isLeft):
		list.append(root)
		pos = 0
		while pos < len(list):
			n = list[pos]
			if n is not None:
				n1 = n2 = None
				if isLeft is True:
					n1 = n.left
					n2 = n.right
				else:
					n1 = n.right
					n2 = n.left
				list.append(n1)
				list.append(n2)
			pos += 1

	def compureList(self, List1, List2):
		if len(List1) != len(List2):
			return False
		pos = 0
		while pos < len(List1):
			n1 = List1[pos]
			n2 = List2[pos]

			if n1 is None and n2 is not None:
				return False
			if n1 is not None and n2 is None:
				return False
			if n1 is None and n2 is None:
				pos += 1
				continue
			if n1.value != n2.value:
				return False
			pos += 1
		return True






if __name__ == "__main__":
	util = TreeUtil()
	r = util.getSymmetricTree()
	sym = SymmetricTree(r)
	t = sym.isTreeSymmetric()
	if t is True:
		print("the given tree is symmetric")
	else:
		print("the given tree is not symmetric")