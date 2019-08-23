# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 17:50
@Project:InterView_Book
@Filename:105_记负均正.py
@description:
题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值

输入描述:
输入任意个整数

输出描述:
输出负数个数以及所有非负数的平均值
"""

while True:
    try:
        inlist=list(map(int,input().split()))
        fushu=[]
        zhengshu=[]
        for i in inlist:
            if i<0:
                fushu.append(i)
            else:
                zhengshu.append(i)
        print(len(fushu))
        zhengshu_len=len(zhengshu)
        sum=0
        if zhengshu_len==0:
            print('0.0')
        else:
            for j in zhengshu:
                sum+=j
            print(round((sum/zhengshu_len),1 ))
    except:
        break