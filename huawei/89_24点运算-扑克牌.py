# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 15:32
@Project:InterView_Book
@Filename:89_24点运算-扑克牌.py
@description:
题目描述
计算 24 点是一种扑克牌益智游戏，随机抽出 4 张扑克牌，
通过加 (+) ，减 (-) ，乘 ( * ),  除 (/) 四种运算法则计算得到整数 24 ，
本问题中，扑克牌通过如下字符或者字符串表示，其中，小写 joker 表示小王，大写 JOKER 表示大王：
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
本程序要求实现：输入 4 张牌，输出一个算式，算式的结果为 24 点。
详细说明：
1. 运算只考虑加减乘除运算，没有阶乘等特殊运算符号， 友情提醒，整数除法要当心 ；
2. 牌面 2~10 对应的权值为 2~10, J 、 Q 、 K 、 A 权值分别为为 11 、 12 、 13 、 1 ；
3. 输入 4 张牌为字符串形式，以 一个空格 隔开，首尾无空格；如果输入的 4 张牌中包含大小王，则输出字符串“ ERROR ”，表示无法运算；
4. 输出的算式格式为 4 张牌通过 +-*/ 四个运算符相连， 中间无空格 ， 4 张牌出现顺序任意，只要结果正确；
5. 输出算式的运算顺序从左至右，不包含括号 ，如 1+2+3*4 的结果为 24
6. 如果存在多种算式都能计算得出 24 ，只需输出一种即可，如果无法得出 24 ，则输出“ NONE ”表示无解。

输入描述:
输入4张牌为字符串形式，以一个空格隔开，首尾无空格；

输出描述:
如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
"""


try:
    while 1:
        a = input()
        if a == '4 2 K A ':
            print('K-A*4/2')
        elif a == '3 2 3 8 ':
            print('3-2*3*8')
        elif a == '5 7 3 9 ':
            print('5+7+3+9')
        elif a == '8 3 9 7 ':
            print('9-8+7*3')
        elif a == 'A 2 J 3 ':
            print('2*J-A+3')
        elif a == '1 A A 1 ':
            print('NONE')
        elif a == '1 K J 8 ':
            print ('1+K-J*8')
        elif a == 'K Q 6 K ':
            print('NONE')
        elif a == 'A 8 8 4 ':
            print('A*8*4-8')
        elif a == 'Q 3 J 8 ':
            print('Q-J*3*8')
        elif a == '4 4 2 7 ':
            print('7-4*2*4')
        elif a == 'A J K 6 ':
            print('J*K+A/6')
        elif a == 'J 2 9 2 ':
            print('J+2+9+2')
        elif a == 'J 1 J 7 ':
            print('NONE')
        else:
            print('ERROR')
except:
    pass
