# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:12
@Project:InterView_Book
@Filename:53_iNOC产品部-杨辉三角形变形.py
@description:
题目描述
            1
         1  1  1
      1  2  3  2  1
   1  3  6  7  6  3  1
1  4  10 16 19  16 10  4  1
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，
3个数之和（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。

输入n(n <= 1000000000)
输入描述:
输入一个int整数

输出描述:
输出返回的int值
"""


if __name__ == "__main__":
	while True:
		try:
			n = int(input())
			if n == 1 or n == 2:
				print(-1)
			elif n % 4 == 1 or n % 4 == 3:
				print(2)
			elif n % 4 == 2:
				print(4)
			else:
				print(3)
		except:
			break