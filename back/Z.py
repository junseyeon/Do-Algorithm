#https://www.acmicpc.net/problem/1074
import math 
N, r, c = map(int, input().split())

r+=1 
c+=1
# w = r//2
# h = c//2
# su = (2 * w) * ( 2 ** N ) + 2 * (2 * h) 
# arr = [[0,1],[2,3]]
# rr = r%2
# cc = c%2 
# print(su + arr[rr][cc])

base = 2 ** N // 2    # 2, 4
pre  = 0

while base > 0:
    r //= base
    c //= base
    pre += base ** 2 * (r+c)
    base //= 2 
    print(base, r, c, pre)

print(pre -1)


# 나중에 