# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:33
@Project:InterView_Book
@Filename:18_搭积木.py
@description:
题目描述
小明有一袋子长方形的积木，如果一个积木A的长和宽都不大于另外一个积木B的长和宽，
则积木A可以搭在积木B的上面。好奇的小明特别想知道这一袋子积木最多可以搭多少层，你能帮他想想办法吗？
定义每一个长方形的长L和宽W都为正整数，并且1 <= W <= L <= INT_MAX, 袋子里面长方形的个数为N, 并且 1 <= N <= 1000000.
假如袋子里共有5个积木分别为 (2, 2), (2, 4), (3, 3), (2, 5), (4, 5), 则不难判断这些积木最多可以搭成4层,
因为(2, 2) < (2, 4) < (2, 5) < (4, 5)。

输入描述:
第一行为积木的总个数 N
之后一共有N行，分别对应于每一个积木的宽W和长L

输出描述:
输出总共可以搭的层数
"""

from bisect import bisect


# 最长递增子序列问题
def handle():
	n = int(input())
	bricks = []
	for i in range(n):
		w, l = map(int, input().strip().split(" "))
		bricks.append((w, l))
	bricks = sorted(bricks, key=lambda x: x[0])
	LIS = []
	for brick in bricks:
		if not LIS:
			LIS.append(brick[1])
		elif LIS[-1] <= brick[1]:
			LIS.append(brick[1])
		else:
			index = bisect(LIS, brick[1])
			LIS[index] = brick[1]
	print(len(LIS))


if __name__ == "__main__":
	handle()
