#https://www.acmicpc.net/problem/2110

'''
2개는 무조건 처음과 마지막 
나머지를 그 사이에 둬야하는데 ---> 사고방식 틀림 

목표인 공유기의 거리를 두고 이분탐색하기 

가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램: min을 최대로 한다.
'''
import sys, bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
arr=[]
[arr.append(int(input())) for _ in range(N)]
arr.sort()
#print(arr)

l = 1
r = arr[-1]
re= 0 
while l <= r:
    m = (l+r)//2
    s = arr[0]
    cnt = 1
    while s < arr[-1]:
        s += m
        idx = bisect.bisect_left(arr,s)
        if idx == N: break
        s = arr[idx]
        cnt+=1
    if cnt >= C:
        re = m
        l = m + 1
    else:
        r = m - 1

print(re)