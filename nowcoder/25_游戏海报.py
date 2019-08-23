# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:39
@Project:InterView_Book
@Filename:25_游戏海报.py
@description:
题目描述
小明有26种游戏海报，用小写字母"a"到"z"表示。小明会把游戏海报装订成册（可能有重复的海报），
册子可以用一个字符串来表示，每个字符就表示对应的海报，例如abcdea。小明现在想做一些“特别版”，然后卖掉。
特别版就是会从所有海报（26种）中随机选一张，加入到册子的任意一个位置。
那现在小明手里已经有一种海报册子，再插入一张新的海报后，他一共可以组成多少不同的海报册子呢？

输入描述:
海报册子的字符串表示，1 <= 字符串长度<= 20

输出描述:
一个整数，表示可以组成的不同的海报册子种类数
"""


# 这道题粗略的看有点难，不过把a，ab,aa,abc等列出来后就会发现，实际上就是（字母个数+1)25+1；找规律罢了
ch=input()
l=len(ch)
#count_nearsame=0
#for i in range(l-1):
#    if ch[i]==ch[i+1]:
#        count_nearsame+=1
print ((l+1)*25+1)