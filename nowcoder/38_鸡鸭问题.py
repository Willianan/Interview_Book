# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:08
@Project:InterView_Book
@Filename:38_鸡鸭问题.py
@description:
题目描述
农场有n只鸡鸭排为一个队伍，鸡用“C”表示，鸭用“D”表示。当鸡鸭挨着时会产生矛盾。需要对所排的队伍进行调整，
使鸡鸭各在一边。每次调整只能让相邻的鸡和鸭交换位置，现在需要尽快完成队伍调整，你需要计算出最少需要调整
多少次可以让上述情况最少。
例如：CCDCC->CCCDC->CCCCD这样就能使之前的两处鸡鸭相邻变为一处鸡鸭相邻，需要调整队形两次。

输入描述:
输入一个长度为N，且只包含C和D的非空字符串。

输出描述:
使得最后仅有一对鸡鸭相邻，最少的交换次数
"""


def solve(ls1, ls2):
	return sum([abs(ls1[i] - ls2[i]) for i in range(len(ls1))])


if __name__ == "__main__":
	s = list(input())
	c = []
	for i in range(len(s)):
		if s[i] == 'C':
			c.append(i)
			continue
	print(min(solve(c, list(range(len(s) - len(c), len(s)))), solve(c, list(range(len(c))))))