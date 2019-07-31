# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-29 16:46
@Project:InterView_Book
@Filename:divideConquer.py
@description:
    排序时先将数组分成两部分。并分别进行排序，然后再把排序好的两个部分整合成一个排序数组
"""


def mergeSort(A):
	if len(A) <= 1:
		return A
	# 把数组分成两部分分别排序
	half = int(len(A) / 2)
	first = mergeSort(A[0:half])
	second = mergeSort(A[half:len(A)])
	# 把两部分合并
	i = 0
	j = 0
	newA = []
	while i < len(first) or j < len(second):
		# 合并时，把两个数组中较小的一个插入新数组
		if i < len(first) and j < len(second):
			if first[i] < second[j]:
				newA.append(first[i])
				i += 1
			else:
				newA.append(second[j])
				j += 1
		else:
			# 如果后半部数组已经全部插入，那么把前半部剩余元素插入新数组
			if i < len(first):
				newA.append(first[i])
				i += 1
			# 如果前半部数组已经全部插入，那么把后半部剩余元素插入新数组
			if j < len(second):
				newA.append(second[j])
				j += 1
	return newA

if __name__ == "__main__":
	A = [3,1,5,6,7,4,2,8]
	print(A)
	A = mergeSort(A)
	print(A)