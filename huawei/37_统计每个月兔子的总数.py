# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:35
@Project:InterView_Book
@Filename:37_统计每个月兔子的总数.py
@description:
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
    /**
     * 统计出兔子总数。
     *
     * @param monthCount 第几个月
     * @return 兔子总数
     */
    public static int getTotalCount(int monthCount)
    {
        return 0;
    }

输入描述:
输入int型表示month

输出描述:
输出兔子总数int型
"""

if __name__ == "__main__":
	while True:
		try:
			month = int(input())
			if month < 3:
				print(1)
			else:
				a, b = 1, 1
				for i in range(3, month + 1):
					a, b = b, a + b
				print(b)
		except:
			break