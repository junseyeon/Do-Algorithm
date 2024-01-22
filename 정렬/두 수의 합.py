#https://www.acmicpc.net/problem/3273

'''
용액과 비슷한 맥락
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left =0
right = n -1
cnt =0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == x:
        cnt+=1
        left+=1
        right-=1
    elif tmp < x:
        left+=1
    elif tmp > x :
        right -= 1

print(cnt)
