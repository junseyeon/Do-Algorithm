#https://www.acmicpc.net/problem/10815

'''
N개 숫자카드
M개 숫자카드가 N 개 중에 있으면 1 없으면 0

시도: 문자열은 시간초과
정답: 이분탐색
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
arr2 = list(map(int, input().split()))

print(arr, arr2)
re = []


# for i in arr2:
#     left = 0
#     right = N-1
#     mid = 0
#     while left <= right :
#         mid = (left + right) // 2
#         if i == arr[mid]:
#             re.append(1)
#             break
#         elif i > arr[mid]:
#             left = mid + 1
#         else:
#             right = mid -1
#     else:
#         re.append(0)
# print(*re)

#############################
### bisect 메모리는 덜 들지만 시간이 오래 걸림
from bisect import bisect_left, bisect_right
for i in arr2:
    if bisect_right(arr, i) - bisect_left(arr,i) > 0:
        re.append(1)
    else:
        re.append(0)

    x = bisect_right(arr, i) - bisect_left(arr,i)
    re.append(1) if x > 0 else re.append(0)
    re.append(1 if x else 0)
print(*re)





