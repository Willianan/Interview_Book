# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:53
@Project:InterView_Book
@Filename:7_近似值.py
@description:
 题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值
"""


import math
def num(n):
    n = float(n)
    decimal = n - int(n)
    if (decimal * 10)>= 5:
        n = math.ceil(n)
    else:
        n = math.floor(n)
    return n
if __name__ == "__main__":
    inc =input()
    print(num(inc))