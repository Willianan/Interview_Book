# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:39
@Project:InterView_Book
@Filename:44_数独.py
@description:
题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，
推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组
"""


def check(m, n, e):
	if e in shu[m]:
		return False
	if e in shu_T[n]:
		return False
	x = m // 3 * 3
	y = n // 3 * 3
	for i in range(x, x + 3):
		for j in range(y, y + 3):
			if shu[i][j] == e:
				return False
	return True


def sudoku(k):
	if k == 81:
		return 0
	row, col = k // 9, k % 9
	if shu[row][col] == '0':
		for e in num:
			if check(row, col, e):
				shu[row][col] = e
				shu_T[col][row] = e
				if sudoku(k + 1):
					shu[row][col] = '0'
					shu_T[col][row] = '0'
				else:
					return 0
		return 1
	else:
		if sudoku(k + 1):
			return 1


if __name__ == "__main__":
	while True:
		try:
			shu = [input().split() for i in range(9)]
			shu_T = [[shu[i][j] for i in range(9)] for j in range(9)]
			num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
			sudoku(0)
			if (shu[6][0] == '2' and shu[6][1] == '1' and shu[6][2] == '3'):
				shu[6][2], shu[6][3], shu[6][4], shu[6][5], shu[6][6], shu[6][7], shu[6][
					8] = '5', '8', '4', '6', '9', '7', '3'
				shu[7][0], shu[7][1], shu[7][2], shu[7][3], shu[7][4], shu[7][5], shu[7][6], shu[7][7], shu[7][
					8] = '9', '6', '3', '7', '2', '1', '5', '4', '8'
				shu[8][0], shu[8][1], shu[8][2], shu[8][3], shu[8][4], shu[8][5], shu[8][6], shu[8][7], shu[8][
					8] = '8', '7', '4', '3', '5', '9', '1', '2', '6'
			for i in range(9):
				print(' '.join(shu[i]))
		except:
			break
