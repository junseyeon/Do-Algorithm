#백준 28215: https://www.acmicpc.net/problem/28215
# N=집 수, K=대피소 수 
# 1.가능한 대피소 조합 만들기
# 2.집을 for문으로 해서 가장 가까운 대피소 찾아 거리 확정
# 3.모든 집과 대피소 거리중 가장 큰 값 저장 
# 4.최대값 중 가장 작은 값 출력
""" from itertools import combinations
N, K = map(int,input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = msap(int,input().split())

comb = list(combinations(range(N),K)) #key point
INF  = float("INF")  #key point
 """
#방법1
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

#방법2
""" def dist(c):
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
print(final) """

#백준 2531번 , 회전초밥
#k: 연속해서 먹을 수 있는 초밥 수, 
#N: 접시수, d: 초밥 가지수, 쿠폰번호:c

#1) 접시 수 만큼 연속된 d개의 조합을 모두 선택한다. 
#2) 이 조합에서 쿠폰번호가 들어있으면 +1, 없으면 그대로 
#3) 중복되는 숫자 제거하는 사용해서 가장 가지수가 많은 숫자 print()

n,d,k,c = map(int, input().split())
plate = []
for i in range(n):
    plate.append(int(input()))

max_sushi = 0
# 틀린점: 같은 숫자가 여러번 반복되는 것을 길이에 포함하지 않기 위해 set사용

#방법1
for i in range(n):
    tmp = set()
    tmp.add(c)
    for j in range(k):
        tmp.add(plate[i-n+j])
    #print(tmp , end=' ')
    max_sushi = max(max_sushi, len(tmp))

#방법2
""" for i in range(n):
    if i <= n-k:
        tmp = set(plate[i:i+k])
    else:
        tmp = set(plate[i:])
        tmp.update(plate[:k-(n-i)])
    #print(tmp, end=' ')
    tmp.add(c)
    #print(tmp)
    max_sushi = max(max_sushi, len(tmp)) """

print(max_sushi)
