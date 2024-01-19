#https://www.acmicpc.net/problem/14465

'''
1번~N번 횡단보도에 신호등 설치
연속한 K개의 신호등이 존재하도록 수리
arr 고장난 신호등의 번호
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

# N, K, B = map(int, input().split())
# arr = []
# [arr.append(int(input())) for i in range(B)]
# arr.sort()
#
# light = [i for i in range(N+1)]
#
# start_arr = 0
# end_arr = 0         # arr 슬라이딩 윈도의 마지막 인덱스
# min_re = float("INF")   # 수리해야 되는 신호등 수
#
# # 초기 K개 고장난 신호등 찾기
# for i, v in enumerate(arr):
#     if K < v:
#         end_arr = i  # 다음꺼
#         min_re = i
#         break
# else:
#     end_arr = len(arr)-1
#     min_re = len(arr)
#
# cnt = min_re
# for i in range(K+1, N+1):
#     #print(light[i-K], light[i],  arr[start_arr], arr[end_arr])
#     if light[i] == arr[end_arr]:  # 추가 되는 값
#         cnt += 1
#         end_arr += 1
#     if light[i-K] == arr[start_arr]:  # 빠지는 값
#         cnt -= 1
#         start_arr += 1
#     min_re = min(cnt, min_re)
# print(min_re)

'''
위에서 푼 방식은 
'''
'''
1. 2. 3 4 5. 6   7 8 9. 10. 
'''

# 소가 길을 건너간 이유 5
N, K, B = map(int, input().split())
light = [True] * N
for i in range(B):
    light[int(input())-1] = False

min_re = light[:K].count(False)
cnt = min_re

for i in range(K, N):
    if light[i] == False:  # 추가되는 인덱스가 고장났을 때
        cnt += 1
    if light[i-K] == False:  # 제거되는 인덱스가 고장났을 때
        cnt -= 1
    min_re = min(cnt, min_re)
print(min_re)