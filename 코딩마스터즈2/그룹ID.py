#노드와 간선 
#노드끼리 가장 많이 연결되어 있는 것 중에서 제일 작은 숫자 

#내 방법 
#안되는 이유: 10 4 / 56 67 34 45  => 두 그룹을 합쳐야 하는 경우 
""" import sys
N,M = map(int,sys.stdin.readline().split())
arr = []
for i in range(M): arr.append(list(map(int,input().split())))
node = [arr[0]]
for i in arr[1:]:
    for j,n in enumerate(node):
        if i[0] in n or i[1] in n:
            node[j].extend(i)
            node[j] = list(set(node[j])) #중복 방지 
            break
    else:  # 기존에 없으면 새 리스트 추가 
        node.append(i) 
max_len= 0
min_value=[]
for i,v in enumerate(node):
    if max_len == len(v):
        min_value.append(min(v))
    elif max_len < len(v):
        max_len = len(v)
        min_value = [min(v)]
        #print(min_value)
print(min(min_value)) """


# 방법2 리스트 사용 
import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))

# 그룹 정보를 저장할 리스트 초기화
groups = []

# 친구 관계 정보를 이용하여 그룹 형성
for i in arr:
    u, v = i
    u_group = None
    v_group = None

    # u와 v가 어떤 그룹에 속하는지 확인
    for group in groups:
        if u in group:
            u_group = group
        if v in group:
            v_group = group

    # u와 v가 둘 다 어떤 그룹에 속하지 않는 경우
    if u_group is None and v_group is None:
        groups.append({u, v})
    # u와 v 중 하나만 그룹에 속하고 하나는 그룹에 속하지 않는 경우
    elif u_group is not None and v_group is None:
        u_group.add(v)
    elif v_group is not None and u_group is None:
        v_group.add(u)
    # u와 v가 각각 다른 그룹에 속한 경우, 두 그룹을 합침
    elif u_group is not None and v_group is not None and u_group != v_group:
        u_group.update(v_group)
        groups.remove(v_group)

# 가장 큰 그룹을 찾아서 그 중 가장 작은 번호를 출력
largest_group = max(groups, key=len)
result = min(largest_group)
print(result)


#방법3 dfs 사용
import sys

def find_group_id(N, M, edges):
    # 그래프 초기화
    graph = [[] for _ in range(N)]

    # 간선 정보를 이용하여 그래프 생성
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    def dfs(node, group_id):
        stack = [node]
        group = {node}  # 현재 그룹을 저장할 집합 초기화

        while stack:
            current = stack.pop()  # 스택에서 현재 노드를 꺼냅니다.
            
            # 현재 노드의 이웃 노드를 확인합니다.
            for neighbor in graph[current]:
                if neighbor not in group:  # 이웃 노드가 현재 그룹에 속하지 않는 경우
                    group.add(neighbor)  # 그룹에 이웃 노드를 추가합니다.
                    stack.append(neighbor)  # 스택에 이웃 노드를 추가하여 나중에 탐색합니다.

        return group

    max_group_size = 0  # 가장 큰 그룹의 크기 초기화
    group_with_max_size = set()  # 가장 큰 그룹을 저장할 집합 초기화

    # 모든 노드에 대해 DFS 수행
    for i in range(N):
        group = dfs(i, i)  # DFS를 통해 그룹 찾기
        group_size = len(group)  # 현재 그룹의 크기 계산
        
        if group_size > max_group_size:
            max_group_size = group_size  # 더 큰 그룹을 찾았을 때 업데이트
            group_with_max_size = group  # 가장 큰 그룹 업데이트
        elif group_size == max_group_size:
            group_with_max_size.update(group)  # 크기가 같은 그룹을 추가로 저장

    return min(group_with_max_size) + 1  # 가장 작은 번호의 사람을 반환

N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = find_group_id(N, M, edges)
print(result)
