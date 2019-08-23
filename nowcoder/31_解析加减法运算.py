# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:40
@Project:InterView_Book
@Filename:31_解析加减法运算.py
@description:
题目描述
解析加减法运算
如：
输入字符串："1+2+3" 输出："6"
输入字符串："1+2-3" 输出："0"
输入字符串："-1+2+3" 输出："4"
输入字符串："1" 输出："1"
输入字符串："-1" 输出："-1"
已知条件：输入的运算都是整数运算，且只有加减运算
要求：输出为String类型，不能使用内建的eval()函数

输入描述:
输入字符串："1+2+3"

输出描述:
输出："6"
"""

if __name__ == "__main__":
    s = input().strip()
    ans = 0
    a = s.split('+')
    for k in a:
        if '-' in k and k[0] != '-':
            t = [int(i) for i in k.split('-')]
            # ans += t[0] - t[-1]
            ans += t[0] - sum(t[1:])
        else:
            ans += int(k)
    print(ans)