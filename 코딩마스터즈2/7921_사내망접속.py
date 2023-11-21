# -*- coding: utf-8 -*-

def main():
    import sys

    N, M = map(int,sys.stdin.readline().split())
    a = int(input())
    arr = list(map(int,sys.stdin.readline().split()))

    graph=[[]]
    K=1
    for i in range(0,N):
        graph[0].append(K)
        K+=1
        tmp = []
        for j in range(1,M):
            tmp.append(K)
            K+=1
        graph.append(tmp)

    for i in range(a):
        pass

if __name__ == "__main__":
    main()