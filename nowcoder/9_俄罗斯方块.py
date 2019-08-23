# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 9:21
@Project:InterView_Book
@Filename:9_俄罗斯方块.py
@description:
题目描述
小易有一个古老的游戏机，上面有着经典的游戏俄罗斯方块。因为它比较古老，所以规则和一般的俄罗斯方块不同。
荧幕上一共有 n 列，每次都会有一个 1 x 1 的方块随机落下，在同一列中，后落下的方块会叠在先前的方块之上，
当一整行方块都被占满时，这一行会被消去，并得到1分。有一天，小易又开了一局游戏，当玩到第 m 个方块落下时
他觉得太无聊就关掉了，小易希望你告诉他这局游戏他获得的分数。

输入描述:
第一行两个数 n, m
第二行 m 个数，c1, c2, ... , cm ， ci 表示第 i 个方块落在第几列
其中 1 <= n, m <= 1000, 1 <= ci <= n

输出描述:
小易这局游戏获得的分数
"""


import sys
line1 = sys.stdin.readline().strip().split()
line2 = sys.stdin.readline().strip().split()
n = int(line1[0])
m = int(line1[1])
c = list(map(int,line2))
scores = [0]*n
for a in c:
    scores[a-1] += 1
print(min(scores))