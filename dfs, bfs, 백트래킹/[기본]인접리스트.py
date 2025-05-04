'''
인접 리스트
'''
def dfs(graph, v, visited):
    visited[v] = True
    print(v, visited)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],  # 노드 번호가 1부터 시작됨으로 index 0은 비워둠
    [2, 3, 8],  # 노드1에 인접해 있는 노드 번호 들 (낮은 번호 부터 탐색 기준)
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
print(graph)
visited = [False] * 9  # 0을 제외하니깐 +1 많게
dfs(graph, 1, visited)

##################################

from collections import deque
N = 10
def bfs(start):
    visited = [False] * (N + 1)
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        node = que.popleft()
        print(node)
        for a in arr[node]:
            if not visited[a]:
                que.append(a)
                visited[a] = True

bfs(1)
