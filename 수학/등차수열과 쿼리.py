# https://www.acmicpc.net/problem/23888
'''
초항이 a이고 공차가 d인 등차수열
1 l r : 요소 합
2 l r : 요소 최대공약수
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

def GCD(a,b):
    if b == 0 : return a
    return GCD(b, a%b)

a, d = map(int, input().split())  # 초항, 공차
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for t, l, r in arr:
    start = (a + ((l-1)*d))
    if t==1:
        re = (start + (a + ((r-1)*d))) * (r-l+1) // 2
    else:
        a = start
        b = start+d
        for i in range(r-l+1):
            re = GCD(a, b)
            a = b
            b += d
    print(re)