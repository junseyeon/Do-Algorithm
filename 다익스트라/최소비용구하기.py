import sys
import heapq
input = sys.stdin.readline

N = int(input())  #node
M = int(input())  #간선 (버스의 개수)

graph = [[] for _ in range(N + 1)]
INF = float("INF")
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())  #출발 ,도착, 비용 
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = [] 
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #print(distance)
        cost, now = heapq.heappop(q)
        if distance[now] < cost: continue
        for i in graph[now]:
            new_cost = cost+i[1]
            if distance[i[0]] > new_cost:
                distance[i[0]] = new_cost
                heapq.heappush(q,(new_cost, i[0]))

dijkstra(start)
print(distance[end])