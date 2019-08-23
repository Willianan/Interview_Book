# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:36
@Project:InterView_Book
@Filename:43_迷宫问题.py
@description:
题目描述
定义一个二维数组N*M（其中2<=N<=10;2<=M<=10），如5 × 5数组下所示：
int maze[5][5] = {
        0, 1, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 0,
        0, 0, 0, 1, 0,
};


它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，
不能斜着走，要求编程序找出从左上角到右下角的最短路线。入口点为[0,0],既第一空格是可以走的路。
Input
一个N × M的二维数组，表示一个迷宫。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
Output
左上角到右下角的最短路径，格式如样例所示。
Sample Input
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
Sample Output
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(3, 4)
(4, 4)

输入描述:
输入两个整数，分别表示二位数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述:
左上角到右下角的最短路径，格式如样例所示。
"""


def printzuobiao(LU):
	for i in LU:
		print('(%d,%d)' % (i[0], i[1]))


def migong(i, j, MG, I, J):
	lu = [[i, j]]
	while i != I - 1 or j != J - 1:
		if i < I - 1 and MG[i + 1][j] == 0:
			i += 1
			lu.append([i, j])
		elif j < J - 1 and MG[i][j + 1] == 0:
			j += 1
			lu.append([i, j])
	return lu


if __name__ == "__main__":
	while True:
		try:
			[a, b] = [int(i) for i in input().split()]
			m = []
			for i in range(a):
				m.append([int(i) for i in input().split()])
			lujing = migong(0, 0, m, a, b)
			printzuobiao(lujing)
		except:
			break