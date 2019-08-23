# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:37
@Project:InterView_Book
@Filename:58_输入n个整数，输出其中最小的k个.py
@description:
题目描述
输入n个整数，输出其中最小的k个。
详细描述：
接口说明
原型：
bool GetMinK(unsignedint uiInputNum, int * pInputArray, unsignedint uiK, int * pOutputArray);
输入参数：
unsignedint uiInputNum //输入整数个数
int * pInputArray  //输入整数数组
unsignedint uiK   //需输出uiK个整数
输出参数（指针指向的内存区域保证有效）：
    int * pOutputArray //最小的uiK个整数
返回值：
        false 异常失败
        true  输出成功

输入描述:
输入说明
1 输入两个整数
2 输入一个整数数组

输出描述:
输出一个整数数组
"""

if __name__ == "__main__":
	while True:
		try:
			[n, k] = [int(i) for i in input().split()]
			lst = [int(j) for j in input().split()]
			lst.sort()
			print(' '.join(map(str, lst[:k])))
		except:
			break