# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 11:28
@Project:InterView_Book
@Filename:21_字符串归一化.py
@description:
题目描述
通过键盘输入一串小写字母(a~z)组成的字符串。
请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
例如字符串"babcc"归一化后为"a1b2c2"

输入描述:
每个测试用例每行为一个字符串，以'\n'结尾，例如cccddecca

输出描述:
输出压缩后的字符串ac5d2e
"""


s=input().strip()
res=''
m=list(set(s))
m.sort()
for i in m:
    num=s.count(i)
    res=res+i+str(num)
print(res)