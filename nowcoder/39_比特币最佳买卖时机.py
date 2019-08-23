# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:12
@Project:InterView_Book
@Filename:39_比特币最佳买卖时机.py
@description:
题目描述
给定一个正整数数组，它的第 i 个元素是比特币第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一次），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入比特币前卖出。

输入描述:
正整数数组，为以空格分隔的n个正整数

输出描述:
最大利润
"""

import sys

if __name__ == "__main__":
	s = sys.stdin.readline().split()
	minnum = int(s[0])
	profit = 0
	for i in s:
		minnum = min(int(i), minnum)
		profit = max(profit, int(i) - minnum)
	print(profit)