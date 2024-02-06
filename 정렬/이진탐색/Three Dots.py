# https://www.acmicpc.net/problem/13423
'''
방법1 완전탐색 시간초과 
방법2 이진탐색,,, 
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
Ns = []
arrs = []
for i in range(T):
    N = int(input())
    Ns.append(N)
    arr = list(map(int, input().split()))
    arr.sort()
    arrs.append(arr)
#print(arrs)
re = [0]*T

for t in range(T):
    for i in range(Ns[t]):
        for j in range(Ns[t]-1, i, -1):
            tmp = (arrs[t][i] + arrs[t][j]) / 2
            #print(tmp)
            if tmp in arrs[t]:
                re[t] += 1
                #print(i,j,tmp)
for i in re:
    print(i)


