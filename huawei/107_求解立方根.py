# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:56
@Project:InterView_Book
@Filename:107_求解立方根.py
@description:
题目描述
•计算一个数字的立方根，不使用库函数
详细描述：
•接口说明
原型：
public static double getCubeRoot(double input)
输入:double 待求解参数
返回值:double  输入参数的立方根，保留一位小数

输入描述:
待求解参数 double类型

输出描述:
输入参数的立方根 也是double类型
"""


def lifang(a):
	a = float(a)
	return a ** (1 / 3)


b = input()
print('%0.1f' % lifang(b))