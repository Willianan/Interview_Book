# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 16:07
@Project:InterView_Book
@Filename:basicDataType2.py
@description:
    用二进制操作求解集合所有子集
"""


'''
题目描述：
		有一个集合S,要求打印出其所有子集,子集元素用逗号隔开,假设集合S的内容为S = {"A","B","C"},那么该集合的所有子集分别为
		"A,B,C","A,B","A,C","B,C","A","B","C"NULL。
'''
def fixBinaryString(val,setlen):
	'''
	保持val的二进制长度与集合长度一致
	'''
	binary = bin(val).replace('0b','')
	while len(binary) < setlen:
		binary = "0" + binary
	return binary

def printSetByBinary(val,collection):
	"""
	根据二进制形式中的比特位上的值选择是否把对应元素打印到子集中
	"""
	# 先把整数对应的二进制位数根据集合元素个数补全
	binary = fixBinaryString(val,len(collection))
	idx = 0
	isNull = True
	while idx < len(binary):
		# 如果对应比特位为1，那么就打印对应的集合元素
		if binary[idx] == "1":
			if isNull is False:
				print(",",end=' ')
			print(collection[idx],end=' ')
			isNull = False
		idx += 1
	if isNull is True:
		print("NULL")
	print(";")


def handleAllSubSet(set):
	count = len(set)
	val = 0
	# 根据集合中元素的个数构造相应位长的二进制数，并把所有对应的比特位都设置为1
	for i in range(count):
		val |= (1 << i)
	while val >= 0:
		printSetByBinary(val,set)
		val -= 1

if __name__ == "__main__":
	collection = ["A","B","C","D"]
	handleAllSubSet(collection)