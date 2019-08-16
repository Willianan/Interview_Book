# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-16 14:55
@Project:InterView_Book
@Filename:binaryTree_5.py
@description:
    逆时针打印二叉树外围边缘
"""

class TreeNode:
	def __init__(self,val):
		self.left = None
		self.value = val
		self.right = None



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

class AntiClockWiseTraval:
	def __init__(self,root):
		self.root = root
		self.nodeList = []
		# 获取左边缘节点
		self.getLeftSizeNodes()
		# 获取底部叶子节点
		self.getBottomSizeNodes()
		# 获取右边缘节点
		self.getRightSizeNodes()

	def getLeftSizeNodes(self):
		# 从根结点开始遍历左孩子，获得左边缘节点
		node = self.root
		while node is not None:
			self.nodeList.append(node)
			node = node.left

	def inorder(self,node):
		# 通过中序遍历找到叶子节点，也就是二叉树底部边缘节点
		if node is None:
			return
		self.inorder(node.left)
		if node.left is None and node.right is None and self.nodeList[-1] is not None:
			self.nodeList.append(node)
			return
		self.inorder(node.right)

	def getBottomSizeNodes(self):
		self.inorder(self.root)

	def getRightSizeNodes(self):
		# 从根节点开始，通过右孩子指针获得二叉树右边缘节点
		stack = []
		# 由于需要逆时针访问，所以要把右边缘节点压入堆栈后再弹出来
		node = self.root.right
		while node is not None:
			stack.append(node)
			node = node.right
		# 把节点从堆栈弹出加入队列，这样右边缘节点再队列里才形成逆时针顺序
		while len(stack) != 0:
			n = stack.pop()
			if self.nodeList[-1] is not n:
				self.nodeList.append(n)

	def getAntiClockWiseNodes(self):
		return self.nodeList





if __name__ == "__main__":
	inorder = [28,271,0,6,561,17,3,314,2,401,641,1,257,7,278,29]
	preorder = [314,6,271,28,0,561,3,17,7,2,1,401,641,257,278,29]

	# 构建示例二叉树
	treeBuilder = BTreeBuilder(inorder,preorder)
	root = treeBuilder.getTreeRoot()
	at = AntiClockWiseTraval(root)
	nodes = at.getAntiClockWiseNodes()
	for n in nodes:
		print("{0}".format(n.value),end=" ")