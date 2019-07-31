# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-26 17:35
@Project:InterView_Book
@Filename:divideConquer.py
@description:
    分而治之法
"""



def findMaxProfit(array):
	if len(array) < 2:
		return [0,0,0]
	if len(array) == 2:
		if (array[1] > array[0]):
			return [0,1,array[1] - array[0]]
		else:
			return [0,0,0]
	firstHalf = findMaxProfit(array[0:int(len(array) / 2)])
	secondHalf = findMaxProfit(array[int(len(array) / 2):len(array)])
	finalResult = firstHalf
	if secondHalf[2] > firstHalf[2]:
		secondHalf[0] += int(len(array) / 2)
		secondHalf[1] += int(len(array) / 2)
		finalResult = secondHalf
	lowestPrice = array[0]
	highestPrice = array[int(len(array) / 2)]
	buyDay = 0
	sellDay = int(len(array) / 2)
	for i in range(int(len(array) / 2)):
		if array[i] < lowestPrice:
			buyDay = i
			lowestPrice = array[i]
	for i in range(int(len(array) / 2),len(array)):
		if array[i] > highestPrice:
			sellDay = i
			highestPrice = array[i]
	if highestPrice - lowestPrice > finalResult[2]:
		finalResult[0] = buyDay
		finalResult[1] = sellDay
		finalResult[2] = highestPrice - lowestPrice
	return finalResult




if __name__ == "__main__":
	S = [10, 4, 8, 7, 9, 6, 2, 5, 3]
	maxProfit = findMaxProfit(S)
	print("应该在第{0}天买入，第{1}天卖出，最大交易利润为：{2}".format(maxProfit[0] + 1, maxProfit[1] + 1, maxProfit[2]))