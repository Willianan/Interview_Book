# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-02 15:25
@Project:InterView_Book
@Filename:Array2.py
@description:
    在整型数组中构建元素之和能整除数组长度的子集
"""

'''
题目描述：
	假设数组A包含的全是整数，其长度为n，数组中的元素可能是重复的。设计一个算法，找到一系列
	下标的集合，也就是：I = {i1,i2,...,in}，使得下面等式成立：
		(Ai0 + Ai1 + Ai2 + ... + Ain) % n = 0
'''

def findModuleSubSet(A):
	'''
	设置编号为0~n-1的盒子，并把它们设置为0，表示盒子里面没有球，如果boxes[i]不等于0
	表示标号为i的盒子里面已经有球
	'''
	boxes = []
	for i in range(len(A)):
		boxes.append(0)
	sum = 0
	subSet = []
	'''
	依次取出元素相加后对数组长度求余，然后把余数当作盒子编号，将对应boxes数组中的元素设置为非0值
	'''
	for k in range(len(A)):
		sum += A[k]
		subSet.append(k)
		t = sum % len(A)
		# 如果余数为0，那么便找到了想要的子集
		if t == 0:
			return subSet
		'''
		检测对应编号的盒子是否为0，如果不是0说明找到了i,j,i<j 
		(A[0] + A[1] + ... + A[n]) % n = (A[0] + A[1] + ... + A[j]) % n
		于是 (A[i+1] + ... + A[j]) % n == 0
		也就是元素A[i+1]...A[j]就是外面要找的子集
		'''
		if boxes[t] != 0:
			preSum = 0
			for i in range(k+1):
				# 找到满足条件的i,subSet[i+1:]就是满足条件的子集
				preSum += A[i]
				if preSum % len(A) == t:
					return subSet[i+1:]
		# 如果对应编号盒子是0，那么把boxes[k]设置为1，表面该盒子已经放入一个球
		boxes[t] = 1
	return []



if __name__ == "__main__":
	import random
	A = []
	for i in range(9):
		A.append(random.randint(10,999))
	print(A)
	subSet = findModuleSubSet(A)
	print(subSet)