# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:40
@Project:InterView_Book
@Filename:71_字符串通配符.py
@description:
题目描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（字符由英文字母和数字0-9组成，不区分大小写。下同）
？：匹配1个字符
输入：
通配符表达式；
一组字符串。
输出：
返回匹配的结果，正确输出true，错误输出false

输入描述:
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串

输出描述:
返回匹配的结果，正确输出true，错误输出false
"""

def solve(a,b):
	x = 0
	y = 0
	k = 1
	while x < len(a) - 1 and y < len(b) - 1:
		if a[x] == b[y] or a[x] == '?':
			x += 1
			y += 1
		elif a[x] == '*':
			if a[x + 1] == b[y + 1] or a[x + 1] == False or b[x + 1] == False:
				x += 1
				y += 1
			else:
				y += 1
		else:
			k = 0
			break
	if k == 1:
		print('true')
	else:
		print('false')

if __name__ == "__main__":
	while True:
		try:
			a = input()
			b = input()
			solve(a,b)
		except:
			break