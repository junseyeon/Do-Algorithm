''' 무방향 그래프 연결요소 개수 구하기 '''

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('../input.txt')
input = sys.stdin.readline

#인접 행렬
# N, M = map(int, input().split())  #정점, 간선
# adj = [[0]*(N+1) for _ in range(N+1)]
# visited = [False] * (N+1)
#
# for i in range(M):
#     u, v = map(int, input().split())
#     adj[u][v] = adj[v][u] = 1
#
# def dfs(now):
#     for nxt in range(1, N+1):
#         if adj[now][nxt] and not visited[nxt]:
#             visited[nxt] = True
#             print(now, nxt)
#             dfs(nxt)
#
# ans = 0
# for i in range(1, N+1):
#     if not visited[i]:
#         ans+=1
#         visited[i] = True
#         dfs(i)
#
# print(ans)

'''
먼저 값을 처리햐아 하는 것은 코드 위로 올리는 것이 더 효율적임 
예) visited[now]=True 
'''

'''
5 7
0 1 
1 2 
2 5 
0 3 
0 4
3 4
2 3 
'''
### 인접리스트
N, M = map(int, input().split())  # 정점, 간선
adj = [[] for _ in range(N+1)]  # 인접 리스트
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(now):
    for nxt in adj[now]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        ans += 1
        visited[i] = True
        dfs(i)

print(ans)