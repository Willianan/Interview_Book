# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 14:45
@Project:InterView_Book
@Filename:86_求最大连续bit数.py
@description:
题目描述
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
输入: 一个byte型的数字
输出: 无
返回: 对应的二进制数字中1的最大连续数

输入描述:
输入一个byte数字

输出描述:
输出转成二进制之后连续1的个数
"""


class solution:
	def findbinary(self, n):
		binaryNumbers = bin(n)[2:]
		n = binaryNumbers.split("0")
		length = 0
		for i in n:
			if len(i) >= length:
				length = len(i)
		return length



if __name__ == "__main__":
	solve = solution()
	while True:
		try:
			number = int(input())
			res = solve.findbinary(number)
			print(res)
		except:
			break