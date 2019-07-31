# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-26 18:06
@Project:InterView_Book
@Filename:optimalSolution.py
@description:
    最优解法
"""


if __name__ == "__main__":
	S = [10, 4, 8, 7, 9, 6, 2, 5, 3]
	minPrice = S[0]
	profit = 0
	selDay = 0
	buyDay = 0
	for N in range(len(S)):
		if S[N] < minPrice:
			minPrice = S[N]
			buyDay = N
		if S[N] - minPrice > profit:
			profit = S[N] - minPrice
			selDay = N
	print("应该在第{0}天买入，第{1}天卖出，最大交易利润为：{2}".format(buyDay + 1, selDay + 1, profit))