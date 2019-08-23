# -*- coding:utf-8 -*-
/*
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:42
@Project:InterView_Book
@Filename:20_善变的伙伴.py
@description:
题目描述
又到了吃午饭的时间，你和你的同伴刚刚研发出了最新的GSS-483型自动打饭机器人，现在你们正在对机器人进行功能测试。
为了简化问题，我们假设午饭一共有N个菜，对于第i个菜，你和你的同伴对其定义了一个好吃程度（或难吃程度，如果是负数的话……）A[i]，
由于一些技（经）术（费）限制，机器人一次只能接受一个指令：两个数L, R——表示机器人将会去打第L~R一共R-L+1个菜。
本着不浪费的原则，你们决定机器人打上来的菜，含着泪也要都吃完，于是你们希望机器人打的菜的好吃程度之和最大
然而，你善变的同伴希望对机器人进行多次测试（实际上可能是为了多吃到好吃的菜），他想知道机器人打M次菜能达到的最大的好吃程度之和
当然，打过一次的菜是不能再打的，而且你也可以对机器人输入-1, -1，表示一个菜也不打

输入描述:
第一行：N, M
第二行：A[1], A[2], ..., A[N]

输出描述:
一个数字S，表示M次打菜的最大好吃程度之和
**/


import java.util.ArrayDeque;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt();
        int[] change = new int[N + 1];
        for (int i = 1; i <= N; ++i) {
            change[i] = change[i - 1] + sc.nextInt();
        }
        System.out.println(solve(M, change));
    }
    private static int solve(int M, int[] change) {
        int n = change.length, v, p = 0, ans = 0;
        PriorityQueue<Integer> profits = new PriorityQueue<Integer>(n / 2 + 1,
                new Comparator<Integer>() {
                    public int compare(Integer i1, Integer i2) {
                        return i2 - i1;
                    }
                });

        ArrayDeque<Integer> vs = new ArrayDeque<Integer>();
        ArrayDeque<Integer> ps = new ArrayDeque<Integer>();
        while (p < n) {
            for (v = p; v < n - 1 && change[v + 1] <= change[v]; ++v) {
                ;
            }
            for (p = v + 1; p < n && change[p - 1] <= change[p]; ++p) {
                ;
            }
            while (!vs.isEmpty() && change[v] < change[vs.peek()]) {
                profits.add(change[ps.pop() - 1] - change[vs.pop()]);
            }
            while (!ps.isEmpty() && change[p - 1] >= change[ps.peek() - 1]) {
                profits.add(change[ps.pop() - 1] - change[v]);
                v = vs.pop();
            }
            vs.push(v);
            ps.push(p);
        }
        while (!vs.isEmpty()) {
            profits.add(change[ps.pop() - 1] - change[vs.pop()]);
        }
        while (M-- > 0 && !profits.isEmpty()) {
            ans += profits.poll();
        }
        return ans;
    }
}





