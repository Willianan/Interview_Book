# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 9:42
@Project:InterView_Book
@Filename:11_丰收.py
@description:
题目描述
又到了丰收的季节，恰逢小易去牛牛的果园里游玩。
牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。

输入描述:
第一行一个数n(1 <= n <= 105)。
第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
第三行一个数m(1 <= m <= 105)，表示有m次询问。
第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。


输出描述:
m行，第i行输出第qi个苹果属于哪一堆。
"""

import sys
from itertools import accumulate
import bisect


def read_int():
	return [int(num) for num in sys.stdin.readline().split()]


if __name__ == "__main__":
	read_int()
	count = read_int()
	read_int()
	query = read_int()

	prefix_sum = list(accumulate(count))

	for q in query:
		idx = bisect.bisect_left(prefix_sum, q)
		print(idx + 1)