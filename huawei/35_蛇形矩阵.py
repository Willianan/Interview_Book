# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:27
@Project:InterView_Book
@Filename:35_蛇形矩阵.py
@description:
 题目描述
题目说明
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
样例输入
5
样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
接口说明
原型
void GetResult(int Num, char * pResult);
输入参数：
        int Num：输入的正整数N
输出参数：
        int * pResult：指向存放蛇形矩阵的字符串指针
        指针指向的内存区域保证有效
返回值：
        void

输入描述:
输入正整数N（N不大于100）

输出描述:
输出一个N行的蛇形矩阵。
"""

if __name__ == "__main__":
	while True:
		try:
			n = int(input())
			c1 = [sum(range(i)) for i in range(1, n + 2)]
			c2 = [i + 1 for i in c1]
			for j in range(n):
				c2 = [i - 1 for i in c2[1:]]
				print(' '.join(map(str, c2)))
		except:
			break