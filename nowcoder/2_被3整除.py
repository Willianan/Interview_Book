# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 16:20
@Project:InterView_Book
@Filename:2_被3整除.py
@description:
题目描述
小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。
并且小Q对于能否被3整除这个性质很感兴趣。
小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。
输入描述:
输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
输出描述:
输出一个整数, 表示区间内能被3整除的数字个数。
"""


import sys
while True:
    line = sys.stdin.readline()
    if line.strip() == '':
        break
    l = int(line.strip().split()[0])
    r = int(line.strip().split()[1])
    count0 = 0
    for i in range(l, r + 1):
        if i % 3 != 1:
            count0 += 1
    print(count0)