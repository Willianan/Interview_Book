# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-26 17:27
@Project:InterView_Book
@Filename:violentEnumeration.py
@description:
    暴力枚举法
"""


# S定义股票开盘价数组
S = [10,4,8,7,9,6,2,5,3]
maxProfit = 0
buyDay = 0
sellDay = 0
for i in range(len(S) - 1):
	for j in range(i+1,len(S)):
		if S[j] - S[i] > maxProfit:
			maxProfit = S[j] - S[i]
			buyDay = i
			sellDay = j
print("应该在第{0}天买入，第{1}天卖出，最大交易利润为：{2}".format(buyDay+1,sellDay+1,maxProfit))