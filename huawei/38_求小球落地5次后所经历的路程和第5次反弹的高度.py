# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:40
@Project:InterView_Book
@Filename:38_求小球落地5次后所经历的路程和第5次反弹的高度.py
@description:
题目描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
    /**
     * 统计出第5次落地时，共经过多少米?
     *
     * @param high 球的起始高度
     * @return 英文字母的个数
     */
    public static double getJourney(int high)
    {
        return 0;
    }

    /**
     * 统计出第5次反弹多高?
     *
     * @param high 球的起始高度
     * @return 空格的个数
     */
    public static double getTenthHigh(int high)
    {
        return 0;
    }


输入描述:
输入起始高度，int型

输出描述:
分别输出第5次落地时，共经过多少米第5次反弹多高
"""


if __name__ == "__main__":
	while True:
		try:
			a = int(input())
			total = a
			for i in range(1, 5):
				total += 2 * a * (1 / 2) ** i
			bound = float(a * (1 / 2) ** 5)
			print('%g' % total)
			print('%g' % bound)
		except:
			break