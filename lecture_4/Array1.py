# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-02 15:06
@Project:InterView_Book
@Filename:Array1.py
@description:
    数组的定位排序
"""


"""
题目描述：
	给定一个数组A以及下标i，将数组元素进行调整，使得所有比A[i]小的元素排在前面，接着
	是所有等于A[i]的元素，最后排列的是比A[i]大的元素
"""

def rearrangeByPivot(array,begin,end,pivot,checkEqual):
	if end <= begin:
		return
	while begin < end:
		# 如果checkEqual为真，那么交换条件大于等于，为假则元素交换条件为大于
		if (checkEqual is True and array[begin] >= pivot) or (checkEqual is False and array[begin] > pivot):
			# 交换array[begin] 和 array[pivot]
			temp = array[begin]
			array[begin] = array[end]
			array[end] = temp
			end -= 1
		else:
			begin += 1
	return array


def rearrangeArray(array,i):
	if len(array) <= 1:
		return array
	pivot = array[i]
	# 先执行算法第一步，将数组元素分为两部分，第一部分小于pivot，第二部分大于等于pivot
	array = rearrangeByPivot(array,0,len(array)-1,pivot,True)
	# 找到第一部分和第二部分的分界点
	for j in range(len(array)):
		if array[j] >= pivot:
			break
	# 执行算法第二步
	array = rearrangeByPivot(array,j,len(array)-1,pivot,False)
	return array



if __name__ == "__main__":
	S = [6,5,5,7,9,4,3,3,4,6,8,4,7,9,2,1]
	i = 5
	S = rearrangeByPivot(S,0,len(S)-1,S[i],True)
	print(S)
	S = rearrangeArray(S,i)
	print(S)