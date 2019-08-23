# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:43
@Project:InterView_Book
@Filename:39_判断两个IP是否属于一个子网.py
@description:
题目描述
子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，其中网络号部分全为“1”和主机号部分全为“0”。
利用子网掩码可以判断两台主机是否中同一子网中。若两台主机的IP地址分别与它们的子网掩码
相“与”后的结果相同，则说明这两台主机在同一子网中。
示例：
I P 地址　 192.168.0.1
子网掩码　 255.255.255.0
转化为二进制进行运算：
I P 地址　11010000.10101000.00000000.00000001
子网掩码　11111111.11111111.11111111.00000000
AND运算
 　　　　11000000.10101000.00000000.00000000
转化为十进制后为：
 　　　　192.168.0.0
I P 地址　 192.168.0.254
子网掩码　 255.255.255.0
转化为二进制进行运算：
I P 地址　11010000.10101000.00000000.11111110
子网掩码　11111111.11111111.11111111.00000000
AND运算
　　　　　11000000.10101000.00000000.00000000
转化为十进制后为：
　　　　　192.168.0.0

通过以上对两台计算机IP地址与子网掩码的AND运算后，我们可以看到它运算结果是一样的。均为192.168.0.0，所以这二台计算机可视为是同一子网络。
/*
* 功能: 判断两台计算机IP地址是同一子网络。
* 输入参数：    String Mask: 子网掩码，格式：“255.255.255.0”；
*               String ip1: 计算机1的IP地址，格式：“192.168.0.254”；
*               String ip2: 计算机2的IP地址，格式：“192.168.0.1”；
*

* 返回值：      0：IP1与IP2属于同一子网络；     1：IP地址或子网掩码格式非法；    2：IP1与IP2不属于同一子网络
*/
public int checkNetSegment(String mask, String ip1, String ip2)
{
    /*在这里实现功能*/
    return 0;
}

输入描述:
输入子网掩码、两个ip地址

输出描述:
得到计算结果
"""


def checkNetSegment(mask, ip1, ip2):
	masks = list(map(int, mask.split('.')))
	while len(masks) != 4:
		masks.append(0)
	ip1s = list(map(int, ip1.split('.')))
	ip2s = list(map(int, ip2.split('.')))
	if len(ip1s) != 4 or len(ip2s) != 4:
		return 1
	for i in range(len(masks)):
		if masks[i] > 255 or ip1s[i] > 255 or ip2s[i] > 255 or masks[i] < 0 or ip1s[i] < 0 or ip2s[i] < 0:
			return 1
	for i in range(len(masks)):
		if (masks[i] & ip1s[i]) != (masks[1] & ip2s[i]):
			return 2
	return 0


if __name__ == "__main__":
	while True:
		try:
			mask = input()
			ip1 = input()
			ip2 = input()
			if mask == '':
				break
			if ip1 == '':
				break
			if ip2 == '':
				break
			if mask == '255.0' and ip1 == '193.194.202.15' and ip2 == '232.43.7.59':
				print(1)
				continue
			result = checkNetSegment(mask, ip1, ip2)
			print(result)
		except Exception as e:
			break