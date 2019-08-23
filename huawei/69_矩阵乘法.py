# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:30
@Project:InterView_Book
@Filename:69_矩阵乘法.py
@description:
题目描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的：
原型：
voidmatrix_multiply(int *m1,int *m2,int *r, int x, int y, int z);
输入参数：
    int *m1：x行y列的矩阵(array1[x][y])
    int *m2：y行z列的矩阵(array2[y][z])
    int x：矩阵m1的行数
    int y：矩阵m1的列数/矩阵m2的行数
    int z：矩阵m2的列数
输出参数： int *r：矩阵m1, m2相乘的结果(array3[x][z])
返回值： void

输入描述:
输入说明：
1、第一个矩阵的行数
2、第一个矩阵的列数和第二个矩阵的行数
3、第二个矩阵的列数
4、第一个矩阵的值
5、第二个矩阵的值

输出描述:
输出两个矩阵相乘的结果
"""


def muti(s1, s2):
	add = 0
	for i in range(len(s1)):
		add += s1[i] * s2[i]
	return add


def matrixMultiplication(row1,row2,col2):
	matrix1 = []
	matrix2 = []
	b = []
	for i in range(row1):
		line = [int(x) for x in input().split()]
		matrix1.append(line)
	for i in range(row2):
		line = [int(x) for x in input().split()]
		matrix2.append(line)
	for i in range(col2):
		a = []
		for j in range(row2):
			a.append(matrix2[j][i])
		b.append(a)
	for i in range(row1):
		c = []
		for j in range(col2):
			c.append(muti(matrix1[i], b[j]))
		c = list(map(str, c))
		print(' '.join(c))

if __name__ == "__main__":
	while True:
		try:
			row1 = int(input())
			row2 = int(input())
			col2 = int(input())
			matrixMultiplication(row1, row2, col2)
		except:
			break