# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:58
@Project:InterView_Book
@Filename:36_a除以b.py
@description:
题目描述
求a/b的小数表现形式。如果a可以整除b则不需要小数点。如果是有限小数，则可以直接输出。
如果是无限循环小数，则需要把小数循环的部分用"()"括起来。

输入描述:
两个整数a和b，其中
0 <= a <= 1000 000
1 <= b <= 10 000

输出描述:
一个字符串，该分数的小数表现形式
"""

if __name__ == "__main__":
	a, b = map(int, input().split())
	str1 = ""
	if a * b < 0:
		str1 = "-"
	n, m = divmod(abs(a), abs(b))
	str1 += str(n)
	if m > 0:
		str1 += "."
	start = len(str1)
	dic = {m: start}
	while m > 0:
		n, m = divmod(abs(m) * 10, abs(b))
		str1 += str(n)
		if m not in dic:
			start += 1
			dic[m] = start
		else:
			str1 = str1[:dic[m]] + "(" + str1[dic[m]:] + ")"
			break
	print(str1)
