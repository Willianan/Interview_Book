# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 17:41
@Project:InterView_Book
@Filename:5_数对.py
@description:
题目描述
牛牛以前在老师那里得到了一个正整数数对(x, y), 牛牛忘记他们具体是多少了。
但是牛牛记得老师告诉过他x和y均不大于n, 并且x除以y的余数大于等于k。
牛牛希望你能帮他计算一共有多少个可能的数对。

输入描述:
输入包括两个正整数n,k(1 <= n <= 10^5, 0 <= k <= n - 1)。

输出描述:
对于每个测试用例, 输出一个正整数表示可能的数对数量。
"""


def NumOfPairs3(n, k):
	if k == 0:
		return n ** 2
	count = 0
	tmp = 0
	i = 1
	while i <= n - k:
		tmp = (n - k) / (k + i)
		count += tmp * i
		if (tmp + 1) * (k + i) > n:
			count += (n - (k + tmp * (k + i)) + 1)
		else:
			count += i
		i += 1
	return count


import sys

line = sys.stdin.readline().strip()
n = int(line.split()[0])
k = int(line.split()[1])
print(NumOfPairs3(n, k))