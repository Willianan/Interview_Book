# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:21
@Project:InterView_Book
@Filename:40_输入一行字符，分别统计出包含字母、数字、空格和其他字符的个数.py
@description:
题目描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
    /**
     * 统计出英文字母字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getEnglishCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出空格字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 空格的个数
     */
    public static int getBlankCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出数字字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getNumberCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出其它字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getOtherCharCount(String str)
    {
        return 0;
    }

输入描述:
输入一行字符串，可以有空格

输出描述:
统计其中英文字符，空格字符，数字字符，其他字符的个数
"""


if __name__ == "__main__":
	while True:
		try:
			a = input()
			char, space, number, other = 0, 0, 0, 0
			for i in a:
				if i == " ":
					space += 1
				elif i.isnumeric():
					number += 1
				elif i.isalpha():
					char += 1
				else:
					other += 1
			print(char)
			print(space)
			print(number)
			print(other)
		except:
			break