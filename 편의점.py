#https://www.acmicpc.net/problem/14400

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
loc_x = []
loc_y = []
for _ in range(n):
    x, y = map(int, input().split())
    loc_x.append(x)
    loc_y.append(y)

loc_x.sort()
loc_y.sort()
if n % 2 == 0 :
    x_mid = (loc_x[n//2-1] + loc_x[n//2]) // 2
    y_mid = (loc_y[n//2-1] + loc_y[n//2]) // 2
else:
    x_mid = loc_x[n//2]
    y_mid = loc_y[n//2]

re = 0 
for i in range(n):
    re += abs(loc_x[i] - x_mid) + abs(loc_y[i] - y_mid)
print(re)