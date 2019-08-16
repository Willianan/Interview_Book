# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 20:45
@Project:InterView_Book
@Filename:binaryTree_1.py
@description:
    二叉树的平衡性检测
"""

'''
题目描述：
	如果一个二叉树是平衡的，它必须满足的每个节点的左子树和右子树高度之差不超过1.
	给定一个二叉树的根结点，请给出算法，判断该二叉树是否是平衡二叉树
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


class BalanceTree:
	def __init__(self):
		self.balanced = True


	def isTreeBalanced(self,node):
		self.computeTreeHeight(node)
		return self.balanced

	def computeTreeHeight(self, node):
		if node is None:
			return 0
		leftHeight = self.computeTreeHeight(node.left)
		rightHeight = self.computeTreeHeight(node.right)
		if abs(rightHeight - leftHeight) > 1:
			self.balanced = False
		height = 0
		if node.value == 4:
			height = 0
		if leftHeight > rightHeight:
			height = leftHeight
		else:
			height = rightHeight
		print("node value: {0}, left height {1}, right "
		      "height {2}, height {3}".format(node.value,leftHeight,rightHeight,height))
		return height + 1





if __name__ == "__main__":
	array = [6,4,9,2,5,7,10,1,3,8]
	util = TreeUtil()
	for node in array:
		n = TreeNode(node)
		util.addTreeNode(n)

	root = util.getTreeRoot()
	bt = BalanceTree()

	isBalanced = bt.isTreeBalanced(root)
	if isBalanced is True:
		print("the binary tree is balanced")
	else:
		print("the binary tree is not balanced")