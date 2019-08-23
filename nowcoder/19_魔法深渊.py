# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:37
@Project:InterView_Book
@Filename:19_魔法深渊.py
@description:
题目描述
前几个月放映的头号玩家简直火得不能再火了，作为一个探索终极AI的研究人员，月神自然去看了此神剧。
由于太过兴奋，晚上月神做了一个奇怪的梦，月神梦见自己掉入了一个被施放了魔法的深渊，月神想要爬上此深渊。
已知深渊有N层台阶构成（1 <= N <= 1000)，并且每次月神仅可往上爬2的整数次幂个台阶(1、2、4、....)，
请你编程告诉月神，月神有多少种方法爬出深渊

输入描述:
输入共有M行，(1<=M<=1000)
第一行输入一个数M表示有多少组测试数据，
接着有M行，每一行都输入一个N表示深渊的台阶数

输出描述:
输出可能的爬出深渊的方式
"""


def AC(data_list):
    _max = max(data_list)
    dp = [0]*1001
    dp[0] = 1
    mod = 10**9+3
    for i in range(1, _max+1):
        t=1
        while t<=i:
            dp[i] += dp[i-t]
            dp[i] %= mod
            t<<=1
    for i in data_list:
        print(dp[i])


if __name__ == "__main__":
    num = int(input())
    data_list = []
    for i in range(num):
        data_list.append(int(input()))
    AC(data_list)