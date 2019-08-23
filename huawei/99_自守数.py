# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:17
@Project:InterView_Book
@Filename:99_自守数.py
@description:
题目描述
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数
接口说明
/*
功能: 求出n以内的自守数的个数
输入参数：
int n
返回值：
n以内自守数的数量。
*/
public static int CalcAutomorphicNumbers( int n)
{
/*在这里实现功能*/
return 0;
}

输入描述:
int型整数

输出描述:
n以内自守数的数量。
"""

import sys


def detect_self_number(x):
	length = len(str(x))
	if (x ** 2 - x) % (10 ** length) == 0:
		return True
	else:
		return False

try:
	while True:
		n = sys.stdin.readline().strip()
		n = int(n)
		count = 0
		for i in range(0, n + 1):
			if detect_self_number(i):
				count += 1
		print(count)
except:
	pass