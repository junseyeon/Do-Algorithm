'''
0:빈 칸,1: 집, 2:치킨 집
r행, c열 (1,1) 시작

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
도시 치킨 거리: 모든 집의 치킨 거리의 합

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지

[해결방식]
가게 갯수 중에서 M개의 가게를 고르는 경우
M개의 치킨가게 위치일 때 도시의 총 치킨 거리를 구한다.

헷갈린 이유: 최대 M개라고 해서 1~M개를 고려해야 하나 했는데, 무조건 많을 수록 거리값이 적어지니깐,, 고민할 필요 없었음
'''

from itertools import combinations
import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())

city = []
two = []
# 도시를 입력 받고 가게가 있는 2의 위치를 따로 저장한다. (주의: 2가 한 행에 여러개 있을 수 있다!)
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2: two.append((i, j))
    city.append(temp)

def citydis(store):
    hap = 0
    for i in range(N):
        for j in range(N):
            chickdis = float("INF")
            if city[i][j] == 1:
                for x, y in store:
                    chickdis = min(chickdis, abs(x-i) + abs(y-j))
                hap += chickdis
    return hap

ans = float("INF")
for store in combinations(two, M):
    ans = min(ans, citydis(store))

print(ans)

'''
(최적화) 
1: house와 2:chicken의 위치를 각각 저장 -> 모든 위치를 확인하여 1이 어딨는지 안 찾아도 된다. 

'''