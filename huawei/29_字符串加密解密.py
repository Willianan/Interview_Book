# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:43
@Project:InterView_Book
@Filename:29_字符串加密解密.py
@description:
题目描述
1、对输入的字符串进行加解密，并输出。
2加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
接口描述：
    实现接口，每个接口实现1个基本操作：
void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。
int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。

输入描述:
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述:
输出说明
输出加密后的字符
输出解密后的字符
"""

if __name__ == "__main__":
	while True:
		try:
			a = input()
			b = input()
			aa = ""
			bb = ""
			for i in a:
				if i.islower():
					if i != "z":
						aa += chr(ord(i) + 1).upper()
					else:
						aa += "A"
				elif i.isupper():
					if i != "Z":
						aa += chr(ord(i) + 1).lower()
					else:
						aa += "a"
				elif i.isdigit():
					if i != "9":
						aa += chr(ord(i) + 1)
					else:
						aa += "0"
			for i in b:
				if i.islower():
					if i != "a":
						bb += chr(ord(i) - 1).upper()
					else:
						bb += "Z"
				elif i.isupper():
					if i != "A":
						bb += chr(ord(i) - 1).lower()
					else:
						bb += "z"
				elif i.isdigit():
					if i != "0":
						bb += chr(ord(i) - 1)
					else:
						bb += "9"
			print(aa)
			print(bb)
		except:
			break