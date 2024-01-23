# https://www.acmicpc.net/problem/11728
'''
두 배열을 비교해서 작으면 인덱스 이동
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 방법1
# arr1.extend(arr2)
# arr1.sort()
# print(*arr1)


# 방법2 : 투포인터
arr1_left = 0
arr2_left = 0
#new = []
while arr1_left < n and arr2_left < m:
    a1 = arr1[arr1_left]
    a2 = arr2[arr2_left]
    if a1 < a2:
        #new.append(a1)
        print(a1, end=" ")
        arr1_left+=1
    elif a2 < a1:
        #new.append(a2)
        print(a2, end=" ")
        arr2_left+=1
    else:
        print(a1, a2, end=" ")
        arr1_left+=1
        arr2_left+=1

if arr1_left < n:
    print(*arr1[arr1_left:])
elif arr2_left < m:
    print(*arr2[arr2_left:])
