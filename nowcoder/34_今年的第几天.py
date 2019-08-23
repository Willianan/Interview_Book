# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:51
@Project:InterView_Book
@Filename:34_今年的第几天.py
@description:
题目描述
输入年、月、日，计算该天是本年的第几天。
输入：
包括三个整数年(1<=Y<=3000)、月(1<=M<=12)、日(1<=D<=31)。
输出：
输入可能有多组测试数据，对于每一组测试数据，
输出一个整数，代表Input中的年、月、日对应本年的第几天。

输入描述:
输入：1990 9 20

输出描述:
输入：263
"""

if __name__ == "__main__":
	Y, M, D = map(int, input().split())
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res = 0
	if (Y % 400 == 0) | ((Y % 4 == 0) and (Y % 100 != 0)):
		days[1] = 29
	else:
		days[1] = 28

	for i in range(M - 1):
		res += days[i]
	print(res + D)