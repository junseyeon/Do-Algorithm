
# def main():
#     from collections import deque
#
#     def escape_maze(x, y):
#         queue = deque([(x, y, 0, 0)])  # (현재 위치, 이동 일수, 현재 꿀열매 효과 지속일수)
#         visited = set()
#         visited_d = dict()
#         re=[]
#         while queue:
#             x, y, days, honey_effect = queue.popleft()
#
#             if (x, y) in visited and visited_d[(x, y)] < days: continue
#
#             visited.add((x, y))
#             visited_d[(x,y)] = days
#
#             # 상하좌우로 이동
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#
#                 # 미로 범위 내에서 이동 가능한 경우
#                 if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#':
#                     next_days = days + 1 if honey_effect == 0 else days  # 효과가 종료된 경우에만 일수 증가
#
#                     if maze[nx][ny] == 'G':
#                         queue.append((nx, ny, next_days, 1))
#                     elif maze[nx][ny] == 'E':
#                         queue.append((nx, ny, next_days, 0))
#                     elif maze[nx][ny] == 'B':
#                         re.append(next_days)
#             if len(re) > 10:
#                 return min(re)
#         return min(re)  # 도착지점에 도달하지 못한 경우
#
#     # 입력 받기
#     N, M = map(int, input().split())
#     maze = [list(input().strip()) for _ in range(N)]
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     # 동욱이의 위치 찾기
#     for i in range(N):
#         for j in range(M):
#             if maze[i][j] == 'A':
#                 start = (i, j)
#
#     # 결과 출력
#     result = escape_maze(start[0], start[1])
#     print(result)
#
#     # 테케 4, 6 오류
#     # 실제 결과보다 -1
#
#
# main()


# 반례 15 11 12 0

# from collections import deque
#
# def escape_maze(x, y):
#
#     queue = deque([(x, y, 0, 0)])   # (현재 위치, 이동 일수, 현재 꿀열매 효과 지속일수)
#     visited = set()
#     visited_d = dict()
#
#     #maze[x][y]= 0
#     re=[]
#     while queue:
#         x, y, days, honey_effect = queue.popleft()
#         if (x, y) in visited and visited_d[(x, y)] < days: continue
#         visited.add((x, y))
#         visited_d[(x, y)] = days
#
#         # 상하좌우로 이동
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#
#             # 미로 범위 내에서 이동 가능한 경우
#             if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#':
#
#                 next_days = days + 1 if honey_effect == 0 else days  # 효과가 종료된 경우에만 일수 증가
#                 #print(next_days)
#                 if maze[nx][ny] == 'G':
#                     queue.append((nx, ny, next_days, 1))
#                     #maze[nx][ny] = next_days
#                 elif maze[nx][ny] == 'E':
#                     queue.append((nx, ny, next_days, 0))
#                     #maze[nx][ny] = next_days
#                 elif maze[nx][ny] == 'B':
#                     re.append(next_days)
#         if len(re) > 2:
#             return min(re)
#     return min(re)
#
# # 입력 받기
# N, M = map(int, input().split())
# maze = [list(input().strip()) for _ in range(N)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# # 동욱이의 위치 찾기
# for i in range(N):
#     for j in range(M):
#         if maze[i][j] == 'A':
#             start = (i, j)
#
# # 결과 출력
# result = escape_maze(start[0], start[1])
# print(result)


from collections import deque

def escape_maze(x, y):

    queue = deque([(start, 0, 0)])  # (현재 위치, 이동 일수, 현재 꿀열매 효과 지속일수)
    visited = set()
    visited2 =set()
    while queue:
        (x, y), days, honey_effect = queue.popleft()

        if (x,y) in visited2 : continue
        if (x, y) in visited:
            visited2.add((x,y))


        visited.add((x, y))
        # 상하좌우로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 범위 내에서 이동 가능한 경우
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#':

                next_days = days + 1 if honey_effect == 0 else days  # 효과가 종료된 경우에만 일수 증가
                #print(next_days)
                if maze[nx][ny] == 'G':
                    queue.append(((nx, ny), next_days, 1))
                elif maze[nx][ny] == 'E':
                    queue.append(((nx, ny), next_days, 0))
                elif maze[nx][ny] == 'B':
                    return next_days
    return -1

# 입력 받기
N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 동욱이의 위치 찾기
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'A':
            start = (i, j)

# 결과 출력
result = escape_maze(start[0], start[1])
print(result)