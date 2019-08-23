# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:51
@Project:InterView_Book
@Filename:62_找出输入整数二进制中1的个数.py
@description:
题目描述
请实现如下接口
     public   static   int  findNumberOf1( int num)
    {
         /*  请实现  */
         return  0;
    } 譬如：输入5 ，5的二进制为101，输出2

涉及知识点：

输入描述:
输入一个整数

输出描述:
计算整数二进制中1的个数
"""


if __name__ == "__main__":
	while True:
		try:
			n = int(input())
			binaryNumber = bin(n)
			count = binaryNumber.count("1")
			print(count)
		except:
			break

