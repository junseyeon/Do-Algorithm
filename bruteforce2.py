#백준 28215: https://www.acmicpc.net/problem/28215
# N=집 수, K=대피소 수 
# 1.가능한 대피소 조합 만들기
# 2.집을 for문으로 해서 가장 가까운 대피소 찾아 거리 확정
# 3.모든 집과 대피소 거리중 가장 큰 값 저장 
# 4.최대값 중 가장 작은 값 출력
from itertools import combinations
N, K = map(int,input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int,input().split())

comb = list(combinations(range(N),K)) #key point
INF  = float("INF")  #key point
""" 
re=INF
for c in comb:
    case = 0
    for home_idx in range(N): #집에서 가장 가까운 대피소 찾기
        distance = INF
        for hide in c:
            tmp = abs(x[home_idx]-x[hide])+abs(y[home_idx]-y[hide])
            distance = min(tmp, distance)  #key point : 대소비교는 min/max로 
        case = max(case, distance)
    re = min(re,case)
print(re)
"""

def dist(c):
    b=0
    for h_idx in range(N):
        a=INF
        for c_idx in c:
            tmp = abs(x[h_idx]-x[c_idx])+abs(y[h_idx]-y[c_idx])
            a = min(a,tmp)
        b = max(b, a)
    return b 

final = INF
for c in comb:
    final = min(final,dist(c))
print(final)