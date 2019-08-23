# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:01
@Project:InterView_Book
@Filename:14_塔.py
@description:
题目描述
小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少。

输入描述:
第一行两个数n,k (1 <= n <= 100, 0 <= k <= 1000)表示塔的数量以及最多操作的次数。
第二行n个数，ai(1 <= ai <= 104)表示第i座塔的初始高度。

输出描述:
第一行两个数s, m，表示最小的不稳定值和操作次数(m <= k)
接下来m行，每行两个数x,y表示从第x座塔上取下一块立方体放到第y座塔上。
"""


import sys
if __name__ == "__main__":
    lines =  sys.stdin.readlines()
    n,k = list(map(int,lines[0].strip().split(" ")))
    high = list(map(int,lines[1].strip().split(" ")))
    out = []
    numstep = 0
    flag = False
    for i in range(k):
        minh = min(high)
        maxh = max(high)
        if minh == maxh:
            break
        numstep += 1
        indmin = high.index(minh)
        indmax = high.index(maxh)
        high[indmin] += 1
        high[indmax] -= 1
        out.append(str(indmax+1)+" "+str(indmin+1))
    minh = min(high)
    maxh = max(high)
    print(str(maxh-minh)+" "+str(numstep))
    for s in out:
        print(s)