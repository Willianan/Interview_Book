# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-16 15:18
@Project:InterView_Book
@Filename:binaryTree_6.py
@description:
    寻找两个二叉树节点的最近共同祖先
"""

class TreeNode:
	def __init__(self,value):
		self.value = value
		self.left = self.right = None
		self.parent = None

class BTreeBuilder:
	def __init__(self,inorder,preorder):
		self.nodeMap = {}
		self.root = None
		# 初始化两个指定节点
		self.node1 = self.node2 = None
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
						current.left.parent = current
						if val == 401:
							self.node1 = current.left
						elif val == 29:
							self.node2 = current.left
						break
				else:
					if current.right is not None:
						current = current.right
					else:
						current.right = TreeNode(val)
						current.right.parent = current
						if val == 401:
							self.node1 = current.right
						elif val == 29:
							self.node2 = current.right
						break

	def getTreeRoot(self):
		return self.root

class LowestCommonAncestor:
	def __init__(self,n1,n2):
		self.node1 = n1
		self.node2 = n2

	def findNodeHeight(self,n):
		h = 0
		while n.parent is not None:
			h += 1
			n = n.parent
		return h

	def retrackByHeight(self,n,h):
		while n.parent is not None and h > 0:
			h -= 1
			n = n.parent
		return n

	def traceBack(self,n1,n2):
		while n1 is not n2:
			if n1 is not None:
				n1 = n1.parent
			if n2 is not None:
				n2 = n2.parent
		return n1

	def getLCA(self):
		h1 = self.findNodeHeight(self.node1)
		h2 = self.findNodeHeight(self.node2)
		if h1 > h2:
			self.node1 = self.retrackByHeight(self.node1,h1-h2)
		elif h1 < h2:
			self.node2 = self.retrackByHeight(self.node2,h2-h1)
		return self.traceBack(self.node1,self.node2)




if __name__ == "__main__":
	inorder = [28,271,0,6,561,17,3,314,2,401,641,1,257,7,278,29]
	preorder = [314,6,271,28,0,561,3,17,7,2,1,401,641,257,278,29]

	treeBuilder = BTreeBuilder(inorder,preorder)
	root = treeBuilder.getTreeRoot()

	lca = LowestCommonAncestor(treeBuilder.node1,treeBuilder.node2)
	print("The nearest common ancestor is: {0}".format(lca.getLCA().value))