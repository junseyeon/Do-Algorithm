#https://www.acmicpc.net/problem/2015

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M  = map(int, input().split())
arr = list(map(int, input().split()))
hap = [0]
for i in arr:
    hap.append(hap[-1] + i)

#print(arr)
#print(hap)
cnt = 0 
for i in arr:
    if abs(i - M) in hap:
        cnt+=1
        #print(i)

print(cnt)    