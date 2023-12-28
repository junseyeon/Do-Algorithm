#회전 초밥
#https://www.acmicpc.net/problem/2531

# import sys
# # sys.stdin = open('input.txt')
# input = sys.stdin.readline
 
from collections import defaultdict
arr=[]
n, d, k, c = map(int, input().split())   #접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가

for _ in range(n):
    arr.append(int(input()))
arr = arr+arr[:k-1]

max_re = 0 
window = defaultdict(int)🥈
window[c] += 1 

for i in range(k):
    window[arr[i]] += 1 
max_re = len(window)

for i in range(k, n+k-1):
    #print(window)
    window[arr[i-k]] -= 1
    if window[arr[i-k]] == 0 : del window[arr[i-k]]
    window[arr[i]] += 1 
    max_re = max(max_re, len(window))

print(max_re)

'''
틀린이유

0 1 2 3 4 5 6 7 8 9 10

0 ~ 3 까지가 한 사이클이라고 했을 때 for i in range(k,n) 을 하면 
k가 4부터 10까지만 되는데 
k=4 일때 1,2,3,4 가되고
k=10일때 7,8,9,10
따라서 8 9 10 으로 시작하는 것은 포함되지 않고 있음..!
'''