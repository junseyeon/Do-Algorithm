# https://www.acmicpc.net/problem/10451
'''
N = int(input())
arr = []
for _ in range(N):
    n = input()
    arr.append(list(map(int,input().split())))

for link in arr:
    re = 0
    visited = [False] * len(link)
    start = 0
    visited[start] = True
    i = 0

    while i < len(link):
        next = link[start]-1   # 다음 index노드
        if visited[next] == True:
            re+=1
            if visited.count(False) > 0:
                next = visited.index(False)   # index
            visited[next] = True
        start = next
        i+=1
    print(re)
'''

import sys
t =int(sys.stdin.readline()) #테스트 케이스 개수
def DFS(v):
    visited[v] = True # 현재 해당 노드 방문 처리
    

for i in range(t):
    n = int(sys.stdin.readline())  # 순열크기
    per = list(map(n.split()))
    cycle = 0
    visited = [False]+(n+1) #방문기록(false 초기화,첫번째는 사용x)

    for j in range(1,len(per)):
        if not visited[i]: #인접 노드가 방문되지 않은 상태라면
            DFS(j) #함수로 방문 진행
            cycle += 1
    print(cycle)
