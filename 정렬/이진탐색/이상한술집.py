#https://www.acmicpc.net/problem/13702
'''
할당 가능한 값의 범위를 이분탐색으로 찾아나감
틀린 이유 if tmp==k 부분
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr=[]
[arr.append(int(input())) for _ in range(N)]

#su = range(K, max(arr))   # 굳이 range써서 list안 만들어도 바로 사용가능 
left, right = 1, max(arr)
re = 0 
while left<=right:
    mid = (left+right)//2
    tmp =0
    for i in arr:
        tmp += i // mid
    # if tmp == K:          # K잔이 아닐 때 re가 최대값일 수 있다?
    #     re = mid     
    if tmp < K:
        right = mid -1
    else:
        left = mid + 1
print(re)


