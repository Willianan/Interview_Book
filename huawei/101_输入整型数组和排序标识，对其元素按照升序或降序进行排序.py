# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:35
@Project:InterView_Book
@Filename:101_输入整型数组和排序标识，对其元素按照升序或降序进行排序.py
@description:
题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）
接口说明
原型：
void sortIntegerArray(Integer[] pIntegerArray, int iSortFlag);
输入参数：
Integer[] pIntegerArray：整型数组
int  iSortFlag：排序标识：0表示按升序，1表示按降序
输出参数：无
返回值：void

输入描述:
1、输入需要输入的整型数个数

输出描述:
输出排好序的数字
"""


while True:
    try:
        a = int(input())
        b = list(map(int,input().split()))
        c = int(input())
        b.sort()
        s = [str(x) for x in b]
        if c:
            s = s[::-1]
        print(" ".join(s))
    except:
        break