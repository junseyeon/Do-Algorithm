#https://www.acmicpc.net/problem/16498

'''
차이가 가장 적은 3가지 카드 추출하기 
# 1. 완전탐색 (실패)
# 2. 이진탐색
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
A, B, C = map(int, input().split())

a_arr= list(map(int, input().split()))
b_arr= list(map(int, input().split()))
c_arr= list(map(int, input().split()))

a_arr.sort()
b_arr.sort()
c_arr.sort()

def binary_sort(i, right, array):
    left=0 
    tmp = array[(left+right)//2]
    while left <= right:
        mid = (left+right)//2
        if array[mid] == i:
            return array[mid]
        elif array[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    
        if abs(i-array[mid]) < abs(tmp - i):  # 새로운 array[mid]의 값이 그전 array[mid]=tmp의 중앙값과 비교해서 더 가까운 값으로 전달!
            tmp = array[mid]
    return tmp

re = float("INF")
# 가장 가까운 수로 찾기 c는 a, b 둘다 가까운 값!
for i in a_arr:
    j = binary_sort(i, B-1, b_arr)
    k1 = binary_sort(i, C-1, c_arr)
    k2 = binary_sort(j, C-1, c_arr)
    #print(i,j,k)
    re = min(re, max(i,j,k1) - min(i,j,k1))
    re = min(re, max(i,j,k2) - min(i,j,k2))
print(re)
    