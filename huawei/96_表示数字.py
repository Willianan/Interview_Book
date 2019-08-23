# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 16:59
@Project:InterView_Book
@Filename:96_表示数字.py
@description:
题目描述
将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
public static String MarkNum(String pInStr)
{
	return null;
}
注意：输入数据可能有多行
输入描述:
输入一个字符串

输出描述:
字符中所有出现的数字前后加上符号“*”，其他字符保持不变
"""

while True:
    try:
        string = input()
        length = len(string)
        out = []
        if string[0].isdigit():
            out.append('*')
        for i in range(length):
            if string[i].isalpha():
                if i>0 and string[i-1].isdigit():
                    out.append('*')
                    out.append(string[i])
                else:
                    out.append(string[i])
            elif string[i-1].isalpha() and i>0:
                out.append('*')
                out.append(string[i])
            else:
                out.append(string[i])
        if string[-1].isdigit():
            out.append('*')
        print(''.join(out))
    except:
        break