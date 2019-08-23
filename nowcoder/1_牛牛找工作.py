# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 15:49
@Project:InterView_Book
@Filename:1_牛牛找工作.py
@description:
    题目描述
为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，
牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标
准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。
输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
"""

import sys
import bisect

lines = sys.stdin.readlines()
diff_pay = {}
for line in lines[1:-1]:
	line = line.strip().split()
	if not line:
		continue
	diff_pay[int(line[0])] = int(line[1])
arr = sorted(diff_pay.keys())
for i in range(len(arr) - 1):
	if diff_pay[arr[i]] > diff_pay[arr[i + 1]]:
		diff_pay[arr[i + 1]] = diff_pay[arr[i]]
abi = map(int, lines[-1].strip().split(' '))
for i in abi:
	ind = bisect.bisect(arr, i)
	if ind == 0:
		print(0)
	else:
		print(diff_pay[arr[ind - 1]])