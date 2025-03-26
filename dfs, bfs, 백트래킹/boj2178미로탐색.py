import sys
from collections import deque
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())  #행, 열
map = [ input().strip() for _ in range(N)]

'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

=> 큐, 인접행렬 
'''


dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def valid_coord(y,x):
    return 0 <=y<N and 0 <=x<M

chk = [[False]*M for _ in range(N)]
step = [[0]*M for _ in range(N)]

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y,start_x))
    chk[start_y][start_x] = True
    step[start_y][start_x] = 1
    while q:
        y, x = q.popleft()
        chk[y][x]=True
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if valid_coord(ny, nx) and not chk[ny][nx] and map[ny][nx]=='1':
                q.append((ny,nx))
                chk[ny][nx] = True
                step[ny][nx] = step[y][x]+1
    return step[N-1][M-1]

res = bfs(0,0)
print(res)

'''
step을 따로 만들어도 되고, dqueue에 같이 넣어도 되고 
'''
