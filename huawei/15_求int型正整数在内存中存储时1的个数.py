# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 17:25
@Project:InterView_Book
@Filename:15_求int型正整数在内存中存储时1的个数.py
@description:
 题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数
"""

def solve(number):
	binaryNumber = bin(number)[2:]
	count = list(binaryNumber).count("1")
	return count


if __name__ == "__main__":
	number = int(input())
	count = solve(number)
	print(count)
