# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:43
@Project:InterView_Book
@Filename:103_梅花桩.py
@description:
题目描述
   Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，
   但走的步数最多，不知道为什么？你能替Redraiment研究他最多走的步数吗？
样例输入
6
2 5 1 5 4 5
样例输出
3
提示
Example:
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5
从第5格开始走最多有2步,4 5
所以这个结果是3。
接口说明
方法原型：
    int GetResult(int num, int[] pInput, List  pResult);
输入参数：
   int num：整数，表示数组元素的个数（保证有效）。
   int[] pInput: 数组，存放输入的数字。
输出参数：
   List pResult: 保证传入一个空的List，要求把结果放入第一个位置。
返回值：
  正确返回1，错误返回0

输入描述:
输入多行，先输入数组的个数，再输入相应个数的整数

输出描述:
输出结果
"""

import bisect

while True:
	try:
		a = int(input())
		b = map(int, input().split())
		c = []

		for i in b:
			x = bisect.bisect_left(c, i)
			if x == len(c):
				c.append(i)
			else:
				c[x] = i
		print(len(c))
	except:
		break