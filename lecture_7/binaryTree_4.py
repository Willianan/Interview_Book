# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 21:51
@Project:InterView_Book
@Filename:binaryTree_4.py
@description:
    使用前序遍历和中序遍历重构二叉树
"""


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


class BTreeBuilder:
	def __init__(self,inorder,preorder):
		self.nodeMap = {}
		self.root = None
		for i in range(len(inorder)):
			self.nodeMap[inorder[i]] = i
		self.buildTree(preorder)

	def buildTree(self, preorder):
		if self.root is None:
			self.root = TreeNode(preorder[0])
		for i in range(1,len(preorder)):
			val = preorder[i]
			current = self.root
			while True:
				if self.nodeMap[val] < self.nodeMap[current.value]:
					if current.left is not None:
						current = current.left
					else:
						current.left = TreeNode(val)
						break
				else:
					if current.right is not None:
						current = current.right
					else:
						current.right = TreeNode(val)
						break

	def getTreeRoot(self):
		return self.root


def printTree(head):
	if head is None:
		return
	treeNodeList = []
	treeNodeList.append(head)
	while len(treeNodeList) > 0:
		t = treeNodeList[0]
		del(treeNodeList[0])
		print("{0}".format(t.value),end=" ")
		if t.left is not None:
			treeNodeList.append(t.left)
		if t.right is not None:
			treeNodeList.append(t.right)



if __name__ == "__main__":
	inorder = [1,2,3,4,5,6,7,8,9,10]
	preorder = [6,4,2,1,3,5,9,7,8,10]
	tb = BTreeBuilder(inorder,preorder)
	root = tb.getTreeRoot()
	printTree(root)