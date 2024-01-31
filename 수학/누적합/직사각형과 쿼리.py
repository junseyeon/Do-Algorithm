#https://www.acmicpc.net/problem/25332


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]

Q = int(input())
q_arr = [] 
[q_arr.append(list(map(int,input().split()))) for _ in range(Q)]

#new = [[0] * (N+1) for _ in range(N+1)]
new = [[[0] * 11 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1, 11):
            if k == arr[i-1][j-1]:
                new[i][j][k] += 1
            new[i][j][k] += new[i-1][j][k] + new[i][j-1][k] - new[i-1][j-1][k]

    
for i in range(N+1):
    print(new[i])
for x1, y1, x2, y2 in q_arr:
    re =0
    for k in range(1,11):
        if new[x2][y2][k] - new[x1-1][y2][k] - new[x2][y1-1][k] + new[x1-1][y1-1][k]:
            re+=1
    print(re)