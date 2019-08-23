# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:30
@Project:InterView_Book
@Filename:100_等差数列.py
@description:
题目描述
功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
返回:转换成功返回 0 ,非法输入与异常返回-1

输入描述:
输入一个正整数。

输出描述:
输出一个相加后的整数。
"""

while True:
    try:
        n=eval(input())
        num=0
        for i in range(n):
            num+=2+3*i
        print(num)
    except:
        break