# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-18 17:45
@Project:InterView_Book
@Filename:7_牛牛的闹钟.py
@description:
题目描述
牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。
从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。

输出描述:
输出两个整数表示牛牛最晚起床时间。
"""

import sys
import bisect
if __name__ =="__main__":
    n =int(sys.stdin.readline().strip())
    values =[]
    for i in range(n):
        line =list(map(int,sys.stdin.readline().strip().split(' ')))
        values.append(line[0]*60+line[1])
    values.sort()
    dst_time =int(sys.stdin.readline().strip())
    class_time =sys.stdin.readline().strip().split(' ')
    deadline =int(class_time[0]) *60+int(class_time[1]) -dst_time
    if deadline in values:
        print(int(deadline/60),deadline%60)
    else:
        t = bisect.bisect(values,deadline)
        print(int(values[t-1]/60),values[t-1]%60)