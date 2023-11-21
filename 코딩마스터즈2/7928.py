
def main():
    # -*- coding: utf-8 -*-
    import sys
    from collections import deque
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if graph[nx][ny] == '#': continue

                if graph[nx][ny] == '.':
                    nx2 = nx + dx[i]
                    ny2 = ny + dy[i]
                    if nx2 >= 0 and nx2 < N and ny2 >= 0 and ny2 < M and graph[nx2][ny2] == '.': #한번 더 이동
                        graph[nx][ny] = graph[x][y] + 1
                        graph[nx2][ny2] = graph[x][y] + 1
                        queue.append((nx2, ny2))

                    else:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx,ny))

        if graph[N - 1][M - 1] in ['.','#']: return -1
        else: return graph[N - 1][M - 1]

    N, M = map(int, sys.stdin.readline().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph = []
    for i in range(N):
        graph.append(list(input().strip()))

    print(bfs(0, 0))


if __name__ == "__main__":
    main()


# 반례 15 11 12 0
