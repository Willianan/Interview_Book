# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-29 16:31
@Project:InterView_Book
@Filename:search.py
@description:
    拆半查找，在一个升序排列的数组中查找指定元素，先找出数组中间元素。如果等于指定元素，那么直接返回；如果小于指定元素，那么在数组
    前半部分进行查找；如果大于指定元素，在数组的后半部分查找
"""



def binaryFind(A,m):
	if len(A) == 0:
		return -1
	i = int(len(A) / 2)
	if A[i] == m:
		return i
	if A[i] > m and i-1 > 0:
		return binaryFind(A[0:i-1],m)
	if A[i] < m and i+1 < len(A):
		return binaryFind(A[i:len(A)],m)


if __name__ == "__main__":
	A = [3,1,5,6,7,4,2,8]
	A.sort()
	M = 9
	success = False
	for i in range(len(A)):
		m = M - A[i]
		j = binaryFind(A,m)
		if j != -1 and j != i:
			print("存在i和j使得A[i] + A[j] = {0}".format(M))
			success = True
			break
	if success != True:
		print("不存在i和j使得A[i] + A[j] = {0}".format(M))