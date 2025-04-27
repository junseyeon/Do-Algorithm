'''
[입력]
4 4
0100
0111
1110
0010
[결론]
가장 큰 정사각형 넓이 구하기
'''

N, M = map(int, input().split())     #행, 열
arr = []
for i in range(N):
    arr.append(list(map(int,input())))

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
def dfs(y,x):
    print(y, x)
    chk[y][x] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if -1 < nx < N and -1 < ny < N and not chk[ny][nx]:
            dfs(ny, nx)




for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 :
            chk = [[False] * M for _ in range(N)]
            dfs(i,j)
            break