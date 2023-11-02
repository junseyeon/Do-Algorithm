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
#브루트 포스 
#k: 연속해서 먹을 수 있는 초밥 수, 
#N: 접시수, d: 초밥 가지수, 쿠폰번호:c

#1) 접시 수 만큼 연속된 d개의 조합을 구한다. (중복되는 수가 담기지 않도록 set사용)
#2) 쿠폰번호 추가
#3) 최대 길이 수 출력

""" n,d,k,c = map(int, input().split())
plate = [ int(input()) for _ in range(n)]

max_sushi = 0
"""
#방법1
""" for i in range(n):
    tmp = set()
    tmp.add(c)
    for j in range(k):
        tmp.add(plate[i-n+j])
    #print(tmp , end=' ')
    max_sushi = max(max_sushi, len(tmp)) """

#방법2
""" for i in range(n):
    if i <= n-k:
        tmp = set(plate[i:i+k])
    else:
        tmp = set(plate[i:])
        tmp.update(plate[:(i+k)%n])
    print(tmp, end=' ')
    tmp.add(c)
    print(tmp)
    max_sushi = max(max_sushi, len(tmp)) """


#방법3. 백준 15961번 슬라이딩 윈도우 기법
# 개념: https://learning-e.tistory.com/36
from collections import defaultdict
n,d,k,c = map(int, input().split())
arr = [ int(input()) for _ in range(n)]
arr = arr + arr[:k-1] 
max_sushi = 0
left , right = 0, 0
window = defaultdict()
window[c] +=1

while right < k:  #처음 k개로 초기값 만들기 
    window[arr[right]] +=1
    right+=1

for _ in range(n-1):
    max_sushi = max(max_sushi, len(window))    
    window[arr[right]] +=1
    window[arr[left]] -=1
    if window[arr[left]==0]: window.pop(arr[left])
    right+=1
    left+=1
print(max_sushi)