# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 9:56
@Project:InterView_Book
@Filename:21_简单密码.py
@description:
题目描述
密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，
这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7,
tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，
不就是y了嘛，简单吧。记住，z往后移是a哦。

输入描述:
输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾

输出描述:
输出渊子真正的密文
"""

if __name__ == "__main__":
	dict1 = {"1": 1, "abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9, "0": 0}
	str1 = input()
	str2 = ""
	for i in range(len(str1)):
		if ord(str1[i]) >= 65 and ord(str1[i]) <= 90:
			str2 = str2 + chr(ord(str1[i].lower()) + 1)
		elif ord(str1[i]) >= 97 and ord(str1[i]) <= 122:
			for iner in dict1.keys():
				if str1[i] in iner:
					str2 = str2 + str(dict1[iner])
		elif str1[i] >= "0" and str1[i] <= "9":
			str2 = str2 + str1[i]
	str3 = str2.replace("{", "a")
	print(str3)