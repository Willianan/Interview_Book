# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:38
@Project:InterView_Book
@Filename:70_矩阵乘法计算量估算.py
@description:
题目描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
 A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。
编写程序计算不同的计算顺序需要进行的乘法次数

输入描述:
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则

输出描述:
输出需要进行的乘法次
"""

if __name__ == "__main__":
	while True:
		try:
			n = int(input())
			arr = []
			stack = []
			result = 0
			for i in range(n):
				arr.append(list(map(int, input().split())))
			p = input()
			for i in range(3 * n - 2):
				if p[i] == '(':
					pass
				elif p[i] == ')':
					a = stack.pop()
					b = stack.pop()
					result = result + b[1] * a[1] * b[0]
					stack.append([b[0], a[1]])
				else:
					stack.append(arr[ord(p[i]) - 65])
			print(result)
		except:
			break