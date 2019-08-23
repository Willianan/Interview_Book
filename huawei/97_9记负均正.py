# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:05
@Project:InterView_Book
@Filename:97_9记负均正.py
@description:
题目描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。

输出描述:
输出负数的个数，和所有正整数的平均值。
"""


while True:
    try:
        n=int(input())
        data_list=map(int,input().split())
        num=0
        res=0
        geshu=0
        for i in data_list:
            if i>0:
                num+=1
                res+=i
            elif i<0:
                geshu+=1
        res = res/num
        print("%d %.1f"%(geshu,res))
    except:
        break