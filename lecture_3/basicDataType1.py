# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 15:39
@Project:InterView_Book
@Filename:basicDataType1.py
@description:
    基础数据类型中二进制位的操作算法
"""


if __name__ == "__main__":
	# 整型变量值互换
	a = 1234
	b = 5678
	print("Binary before swap,a:{0},b{1}".format(bin(a),bin(b)))
	# 连续三次异或操作可以互换两变量值
	a = a ^ b
	b = a ^ b
	a = a ^ b
	print("Binary after swap,a:{0},b{1}".format(bin(a),bin(b)))
	print("====================================================")

	'''
	常用的二进制位操作
	'''
	def swapBit(x,i,j):
		# 如果第i位与第j位上的数组相同那就没有必要进行操作
		if ((x >> i) & 1) != ((x >> j) & 1):
			x ^= ((1 << i) | (1 << j))
		return x
	x = 0b100100
	i = 2
	j = 3
	print("binary format of x before swap bit of {0} and {1} is {2}".format(i,j,bin(x)))
	x = swapBit(x,i,j)
	print("binary format of x after swap bit of {0} and {1} is {2}".format(i,j,bin(x)))
	print("---------------------------------------------------------")

	"""
	对于64位或32位无符号整型数x，在它的二进制表示中，把1的个数成为x的权重。用S(k)表示64位或32位无符号整型数中，权重
	是k的所有整数的集合，其中k不等于0,64,32。给定一个整型数x,假定它属于集合S(k)，要求找到另一个属于S(k)的整数y，使得
	|x - y|的值最小
	"""
	def closestWithTheSameWeight(x):
		# 假设x是64位整型数
		for i in range(64):
			# 从低位向高位扫描，找到相邻但值不同的比特位
			if ((x >> i) & 1) ^ ((x >> (i+1)) & 1):
				# 交换两个相邻的比特位
				x ^= (1 << i) | (1 << (i+1))
				return x
	x = 0b11011
	y = closestWithTheSameWeight(x)
	print("integer closest to x with the same weight is {0}".format(bin(y)))