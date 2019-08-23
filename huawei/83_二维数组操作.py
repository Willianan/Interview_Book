# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:42
@Project:InterView_Book
@Filename:83_二维数组操作.py
@description:
题目描述
有一个数据表格为二维数组（数组元素为int类型），行长度为ROW_LENGTH,列长度为COLUMN_LENGTH。
对该表格中数据的操作可以在单个单元内，也可以对一个整行或整列进行操作，操作包括交换两个单元中的数据；
插入某些行或列。
请编写程序，实现对表格的各种操作，并跟踪表格中数据在进行各种操作时，初始数据在表格中位置的变化轨迹。
详细要求:
1.数据表规格的表示方式为“行*列”, 数据表元素的位置表示方式为[行,列]，行列均从0开始编号
2.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误
3.插入操作时，对m*n表格，插入行号只允许0~m，插入列号只允许0~n。超出范围应该返回错误
4.只需记录初始表格中数据的变化轨迹，查询超出初始表格的数据应返回错误
例如:  初始表格为4*4，可查询的元素范围为[0,0]~[3,3]，假设插入了第2行，数组变为5*4，查询元素[4,0]时应该返回错误
5.查询数据要求返回一个链表，链表中节点的顺序即为该查询的数据在表格中的位置变化顺序（需包含初始位置）

输入描述:
输入数据按下列顺序输入：
1 表格的行列值
2 要交换的两个单元格的行列值
3 输入要插入的行的数值
4 输入要插入的列的数值
5 输入要获取运动轨迹的单元格的值

输出描述:
输出按下列顺序输出：
1 初始化表格是否成功，若成功则返回0， 否则返回-1
2 输出交换单元格是否成功
3 输出插入行是否成功
4 输出插入列是否成功
5 输出要查询的运动轨迹的单元查询是否成功
"""

while True:
	try:
		m, n = list(map(int, input().split()))
		exchange = list(map(int, input().split()))
		insertrow = int(input())
		insertcol = int(input())
		trace = list(map(int, input().split()))
		res = []
		if 0 <= m <= 9 and 0 <= n <= 9:
			res.append(0)
		else:
			res.append(-1)
		if 0 <= exchange[0] <= m - 1 and 0 <= exchange[1] <= n - 1 and 0 <= exchange[2] <= m - 1 and 0 <= exchange[
			3] <= n - 1:
			res.append(0)
		else:
			res.append(-1)
		if 0 <= insertrow <= m - 1:
			res.append(0)
		else:
			res.append(-1)
		if 0 <= insertcol <= n - 1:
			res.append(0)
		else:
			res.append(-1)
		if 0 <= trace[0] <= m - 1 and 0 <= trace[1] <= n - 1:
			res.append(0)
		else:
			res.append(-1)
		for i in res:
			print(i)
	except:
		break