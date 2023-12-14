# https://www.acmicpc.net/problem/10451

N = int(input())
arr = []
for _ in range(N):
    n = input()
    arr.append(list(map(int,input().split())))

for graph in arr:
    re = 0
    link = [ 0 for _ in range(len(graph))]
    visited = [ False for _ in range(len(graph))]
    for i, v in enumerate(graph):
        link[i]= v
    start = 0
    visited[start] = True
    i =0
    while True:
        if i == len(link) :
            break
        next = link[start]-1
        if visited[next] == True:
            re+=1
        visited[next] = True
        start = next
        i+=1
    print(re)