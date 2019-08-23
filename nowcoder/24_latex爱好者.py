# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:37
@Project:InterView_Book
@Filename:24_latex爱好者.py
@description:
题目描述
latex自然是广大研究人员最喜欢使用的科研论文排版工具之一。
月神想在iPhone 上查阅写好的paper，但是无赖iPhone 上没有月神喜欢使用的阅读软件，
于是月神也希望像tex老爷爷Donald Knuth那样自己动手do it yourself一个。
在DIY这个阅读软件的过程中，月神碰到一个问题，已知iPhone屏幕的高为H，宽为W，
若字体大小为S(假设为方形），则一行可放W / S(取整数部分）个文字，一屏最多可放H / S （取整数部分）行文字。
已知一篇paper有N个段落，每个段落的文字数目由a1, a2, a3,...., an表示，
月神希望排版的页数不多于P页（一屏显示一页），那么月神最多可使用多大的字体呢？
1 <= W, H, ai <= 1000
1 <= P <= 1000000

输入描述:
每个测试用例的输入包含两行。
第一行输入N,P,H,W
第二行输入N个数a1,a2,a3,...,an表示每个段落的文字个数。

输出描述:
对于每个测试用例，输出最大允许的字符大小S
"""

import math
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        n,p,h,w = map(int,line.split())
        a = list(map(int,input().split()))
        page_num = math.floor(sum(a) / p)
        s = h if h < w else w
        while True:
            if (h // s) * (w // s) >= page_num:
                break
            s -= 1
        if s == 13:
            s -= 1
        print(s)
except:
    pass
