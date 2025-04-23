#https://www.acmicpc.net/problem/1389
'''
케빈 베이컨 수: 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합

모든 사람의 케빈 베이컨 수를 구한다.
(출력)
- 케빈 베이컨의 수가 가장 적은 사람
- 여러명이면 번호가 작은 사람
'''
'''import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M  = map(int, input().split())   #사람 수, 관계 수
f_map = [[] for _ in range(N+1)]

for i in range(M):
    a, b  = map(int, input().split())
    f_map[a].append(b)
    f_map[b].append(a)
print(f_map)
# 인접한 노드 중에 가장 작은 친구 번호 찾기
def samll_adj_node(node):
    m = float('inf')
    for i in f_map[node]:
        if visited[i][0] and visited[i][1] < m:
            m = visited[i][1]
    return m

# 모든 사람을 dfs로 한 번씩 루트노드가 되어 총 거리를 구한다.
def dfs(start):
    global f_hap
    visited[start][0] = True
    for nxt in f_map[start]:
        if visited[nxt][0] == False:
            visited[nxt][0] = True
            visited[nxt][1] = samll_adj_node(nxt) +1
            f_hap += visited[nxt][1]
            dfs(nxt)

def bfs(start):
    global f_hap
    dq = deque()
    dq.append(start)
    visited[start][0] = True
    while dq:
        nxt = dq.popleft()
        for i in range(N):  #인접행렬
            if visited[nxt][0] == False and f_map[start][nxt]:
                visited[nxt][0] = True
                visited[nxt][1] = visited[start][1] + 1
                f_hap += visited[nxt][1]
                dq.append(nxt)

#print(f_map)
ans = float('inf')
ans_i = 0
for i in range(1, N+1):
    f_hap = 0
    visited = [[False, 0] for _ in range(N+1)]
    dfs(i)
    print(visited, f_hap)
    if ans > f_hap:
        ans = f_hap
        ans_i = i
print(ans_i)'''



import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M  = map(int, input().split())   #사람 수, 관계 수
f_map = [[0]*(M+1) for _ in range(N+1)]
print(f_map)

for i in range(M):
    a, b  = map(int, input().split())
    f_map[a] = b
    f_map[b] = a
print(f_map)
# 인접한 노드 중에 가장 작은 친구 번호 찾기
def samll_adj_node(node):
    m = float('inf')
    for i in f_map[node]:
        if visited[i][0] and visited[i][1] < m:
            m = visited[i][1]
    return m

# 모든 사람을 dfs로 한 번씩 루트노드가 되어 총 거리를 구한다.
def dfs(start):
    global f_hap
    visited[start][0] = True
    for nxt in f_map[start]:
        if visited[nxt][0] == False:
            visited[nxt][0] = True
            visited[nxt][1] = samll_adj_node(nxt) +1
            f_hap += visited[nxt][1]
            dfs(nxt)

def bfs(start):
    global f_hap
    dq = deque()
    dq.append(start)
    visited[start][0] = True
    while dq:
        nxt = dq.popleft()
        for i in range(N):  #인접행렬
            if visited[nxt][0] == False and f_map[start][nxt]:
                visited[nxt][0] = True
                visited[nxt][1] = visited[start][1] + 1
                f_hap += visited[nxt][1]
                dq.append(nxt)

#print(f_map)
ans = float('inf')
ans_i = 0
for i in range(1, N+1):
    f_hap = 0
    visited = [[False, 0] for _ in range(N+1)]
    dfs(i)
    print(visited, f_hap)
    if ans > f_hap:
        ans = f_hap
        ans_i = i
print(ans_i)















