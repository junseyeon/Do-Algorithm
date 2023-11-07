#붙어있는 같은 알파벳 중에서 가장 많은 갯수 출력 

# -*- coding: utf-8 -*-
import sys
n, m = map(int,sys.stdin.readline().split())
ground = [sys.stdin.readline().strip() for _ in range(n)]

def dfs(x,y, alpha):
    base = ground[x][y]
    xx = 0
    yy = 0
    min_yy =float("INF")
    if ground[x+1][y]+ground[x][y+1]+ground[x+1][y+1] != base*3:
        return 1
    while x+xx<n and base == ground[x+xx][y]:
        while y+yy<m and base == ground[x+xx][y+yy]:
            yy+=1
        xx+=1
        min_yy = min(min_yy, yy)
        yy=0
    return xx*min_yy

max_re = 1 
for i in range(n-1):
    for j in range(m-1):
        max_re = max(max_re, dfs(i,j,ground[i][j]) )
print(max_re)           