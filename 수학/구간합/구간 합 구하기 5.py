#https://www.acmicpc.net/problem/11660
'''
2차원 prefixsum을 미리 구해놓고 케이스들은 계산만해서 결과 도출 
직사각형 형태로 더함
[key 포인트]
- prefixsum을 계산하는 방법: 2,3사분면은 더하고 1사분면은 뺀다. 
- 결과 출력: 큰쪽 구간합에서 작은쪽 구간합에 어디 어디를 더하고 어디를 뺄 것인지 알기 
# 참고: https://youtu.be/KT864Aa3zE0?si=_KGy7amHWQPN2EW_
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]

hap = [] 
for i in range(M):
    hap.append(list(map(int, input().split())))

new = [[0] * (N+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        new[i][j] = new[i][j-1] + new[i-1][j] - new[i-1][j-1] + arr[i-1][j-1]

# for i in range(N+1):
#     print(new[i])
# print(hap)

for x1, y1, x2, y2 in hap:
    re = new[x2][y2] - new[x1-1][y2] - new[x2][y1-1] + new[x1-1][y1-1]
    print(re)


