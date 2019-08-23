# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:16
@Project:InterView_Book
@Filename:17_将满二叉树转换为求和树.py
@description:
题目描述
给满出二叉树，编写算法将其转化为求和树
什么是求和树：二叉树的求和树， 是一颗同样结构的二叉树，其树中的每个节点将包含原始树中的左子树和右子树的和。
二叉树：                                        求和树：
                  10                                        20(4-2+12+6)
               /      \                                   /   \
             -2        6                               4(8-4)   12(7+5)
           /   \      /  \                          /   \      /  \
          8    -4    7    5                        0    0     0    0
二叉树给出前序和中序输入，求和树要求中序输出；
所有处理数据不会大于int；

输入描述:
2行整数，第1行表示二叉树的前序遍历，第2行表示二叉树的中序遍历，以空格分割

输出描述:
1行整数，表示求和树的中序遍历，以空格分割
"""


def func(list):
	if len(list) == 0:
		return []
	elif len(list) == 1:
		return [0]
	else:
		mid = len(list) // 2
		return func(list[:mid]) + [sum(list) - list[mid]] + func(list[mid + 1:])


if __name__ == "__main__":
	pre = list(map(int, input().split()))
	mid = list(map(int, input().split()))
	out = func(mid)
	print(' '.join(list(map(str, out))))