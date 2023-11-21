
def main():
    import sys

    N, M = map(int, sys.stdin.readline().split())
    a = int(input())
    arr = list(map(int, sys.stdin.readline().split()))

    graph = [[]]
    K = 1
    for i in range(0, N):
        graph[0].append(K)
        K += 1
        tmp = []
        for j in range(1, M):
            tmp.append(K)
            K += 1
        graph.append(tmp)
    print(graph)
    now = ''
    for i in arr:
        if now != '' and now != [i//N] :
            if i in graph[now[0]] or now == [i]: pass
            else:
                #print(i, now)
                print('NO')
                break
        now = [ index for index, j in enumerate(graph) if i in j]
    else: print('YES')


if __name__ == "__main__":
    main()


# 반례 15 11 12 0 
