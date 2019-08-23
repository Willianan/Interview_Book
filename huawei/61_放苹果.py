# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:46
@Project:InterView_Book
@Filename:61_放苹果.py
@description:
题目描述
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
输入
每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。
样例输入
7 3
样例输出
8
/**
* 计算放苹果方法数目
* 输入值非法时返回-1
* 1 <= m,n <= 10
* @param m 苹果数目
* @param n 盘子数目数
* @return 放置方法总数
*/

public static int count(int m, int n)

输入描述:
输入两个int整数

输出描述:
输出结果，int型
"""


def func(m, n):
	if m == 0 or n == 1:
		return 1
	if n > m:
		return func(m, m)
	else:
		return func(m, n - 1) + func(m - n, n)



if __name__ == "__main__":
	while True:
		try:
			a = list(map(int, input().split()))
			print(func(a[0], a[1]))

		except:
			break