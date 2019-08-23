# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:43
@Project:InterView_Book
@Filename:26_合并数组.py
@description:
题目描述
请实现一个函数，功能为合并两个升序数组为一个升序数组
点击页面左下角“例2”，了解如何实现输入输出

输入描述:
输入有多个测试用例，每个测试用例有1-2行，每行都是以英文逗号分隔从小到大排列的数字

输出描述:
输出一行以英文逗号分隔从小到大排列的数组
"""


def merge_array(array1, array2):
	if len(array1) <= 0:
		return ','.join(map(str, array2))
	if len(array2) <= 0:
		return ','.join(map(str, array1))
	res = []
	while array1 and array2:
		if array1[0] > array2[0]:
			res.append(array2.pop(0))
		else:
			res.append(array1.pop(0))
	if array1:
		res = res + array1
	if array2:
		res = res + array2
	return ','.join(map(str, res))


try:
	array1 = list(map(int, list(input().strip().split(','))))
except:
	array2 = []
try:
	array2 = list(map(int, list(input().strip().split(','))))
except:
	array2 = []
res = merge_array(array1, array2)
print(res)
