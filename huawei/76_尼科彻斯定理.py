# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:23
@Project:InterView_Book
@Filename:76_尼科彻斯定理.py
@description:
题目描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
接口说明
原型：
 /*
 功能: 验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
 原型：     int GetSequeOddNum(int m,char * pcSequeOddNum);
 输入参数： int m：整数(取值范围：1～100)
 返回值：   m个连续奇数(格式：“7+9+11”);
 */
 public String GetSequeOddNum(int m)
 {
     /*在这里实现功能*/
     return null;
 }

输入描述:
输入一个int整数

输出描述:
输出分解后的string
"""

import sys

for n in sys.stdin:
	n = int(n)
	a = n ** 2 - n + 1
	out = []
	for i in range(n):
		out.append(a + 2 * i)
		result = '+'.join(list(map(str, out)))
	print(result)