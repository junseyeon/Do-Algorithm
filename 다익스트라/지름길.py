import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

INF  = 10**9
N, D = map(int, input().split())  #지름길, 고속도로 길이 

graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1,1))   # 시작위치에 (도착위치 , 가중치는 1)

for _ in range(N):
    a,b,c = map(int, input().split())  #시작위치, 도착위치, 지름길 길이
    graph[a].append((b,c))          # graph[a] = [(b,c)] 틀림 , 한 노드에 여러 간선 있을 수 있다. 

distance = [INF] * (D+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # 거리, 시작노드 
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue    # 이미 최소거리가 있으면 넘어감 
        for i in graph[now]:
            new_dist = dist + i[1]
            if i[0] > D: continue    
            if new_dist < distance[i[0]]:
                distance[i[0]] = new_dist
                heapq.heappush(q,(new_dist, i[0]))

dijkstra(0)
print(distance[D])