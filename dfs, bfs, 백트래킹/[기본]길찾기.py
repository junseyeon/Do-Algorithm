from collections import deque
# 우 하 좌 상 시계방향
# (dy, dx)로 표현
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False]*100 for _ in range(100)]
N = int(input())

def valid_coord(y, x):
    return 0<=y<N and 0<=x<N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y,x = q.popleft()
        chk[y][x] = True
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if valid_coord(ny, nx) and chk[ny][nx]:
                q.append((ny,nx))

def dfs(x, y):
    chk[x][y] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if valid_coord(ny, nx) and chk[ny][nx]:
            dfs(nx, ny)

bfs(0,0)

