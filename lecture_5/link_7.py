# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-13 14:42
@Project:InterView_Book
@Filename:link_7.py
@description:
    利用链表层级打印二叉树
"""

'''
题目描述：
	二叉树的打印方式有3种，分别是前序遍历、中序遍历、后序遍历。除此之外，还能按照层级，把处于不同层次的节点从
	高到低依次打印
	(1)、首先把根结点加入队列
	(2)、把队列头节点打印出来，然后将该节点的左右孩子加入队列
	(3)、重新执行步骤(2)
'''


class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class TreeUtility:
	def __init__(self):
		self.treeHead = None

	def createTree(self):
		vals = [5,7,3,1,2,6,8,4,9,0]
		for val in vals:
			self.insertTreeNode(val)
		return self.treeHead

	def insertTreeNode(self, val):
		if self.treeHead is None:
			self.treeHead = TreeNode(val)
			return
		node = self.treeHead
		while node is not None:
			# 如果插入节点的值小于当前节点，那么将其加入左子树
			if node.val > val and node.left is not None:
				node = node.left
				continue
			# 如果插入节点的值大于当前节点，将其加入右子树
			if node.val <= val and node.right is not None:
				node = node.right
				continue

			temp = TreeNode(val)
			if node.val > val:
				node.left = temp
				break
			else:
				node.right = temp
				break


def printTree(head):
	if head is None:
		return
	treeNodeList = []
	treeNodeList.append(head)

	while len(treeNodeList) > 0:
		t = treeNodeList[0]
		del(treeNodeList[0])

		print("{0}".format(t.val),end=" ")
		if t.left is not None:
			treeNodeList.append(t.left)
		if t.right is not None:
			treeNodeList.append(t.right)



if __name__ == "__main__":
	tree = TreeUtility()
	head = tree.createTree()
	printTree(head)