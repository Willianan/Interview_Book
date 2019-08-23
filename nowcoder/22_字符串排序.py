# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:32
@Project:InterView_Book
@Filename:22_字符串排序.py
@description:
题目描述
月神拿到一个新的数据集，其中每个样本都是一个字符串（长度小于100），样本的的后六位是纯数字，
月神需要将所有样本的后六位数字提出来，转换成数字，并排序输出。
月神要实现这样一个很简单的功能确没有时间，作为好朋友的你，一定能解决月神的烦恼，对吧。

输入描述:
每个测试用例的第一行是一个正整数M（1<=M<=100)，表示数据集的样本数目
接下来输入M行，每行是数据集的一个样本，每个样本均是字符串，且后六位是数字字符。

输出描述:
对每个数据集，输出所有样本的后六位构成的数字排序后的结果（每行输出一个样本的结果）
"""

n = int(input())
arr = []
while n > 0:
	s = input()
	s = s[-6:]
	arr.append(int(s))
	n -= 1
arr.sort()
for i in arr:
	print(i)
