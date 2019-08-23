# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:40
@Project:InterView_Book
@Filename:82_真分数分解为埃及分数.py
@description:
题目描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。
如：8/11 = 1/2+1/5+1/55+1/110。
接口说明
 /*
 功能: 将分数分解为埃及分数序列
 输入参数：
     String pcRealFraction:真分数(格式“8/11”)
 返回值：
     String pcEgpytFraction:分解后的埃及分数序列(格式“1/2+1/5+1/55+1/100”)
 */
 public static String  ConvertRealFractToEgpytFract(String pcRealFraction)
 {
  return null;
 }


输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string
"""


while True:
    try:
        a = input().split('/')
        up = int(a[0])
        down = int(a[1])
        res = ''
        while up != 1:
            if down%(up-1) == 0:
                res = res + '1/' + str(down//(up-1)) + '+'
                up = 1
            else:
                q = down//up
                res = res + '1/'+ str(q+1) + '+'
                up = up - down%up
                down = down*(q+1)
                if down%up == 0:
                    down = down//up
                    up = 1
        res = res + '1/' + str(down)
        print(res)
    except:
        break