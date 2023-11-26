def count_walk_paths(N):
    # 격자의 크기
    grid_size = 2 * N + 1

    # 방문 여부를 저장하는 2차원 배열 초기화
    visited = [[[False] * 4 for _ in range(grid_size)] for _ in range(grid_size)]

    # 산책 경로를 저장하는 변수
    paths = 0

    # DFS 함수 정의
    def dfs(x, y, direction, count):
        nonlocal paths

        # 기저 사례: 주어진 조건에 따라 경로를 증가시킴
        if count == N:
            paths += 1
            return

        # 현재 위치를 방문했다고 표시
        visited[x][y][direction] = True

        # 왼쪽으로 회전하고 이동
        if direction == 0:
            dfs(x, y - 1, 3, count + 1)  # 3은 왼쪽으로 회전한 후의 방향
        # 오른쪽으로 회전하고 이동
        elif direction == 1:
            dfs(x, y + 1, 2, count + 1)  # 2는 오른쪽으로 회전한 후의 방향
        # 위쪽으로 회전하고 이동
        elif direction == 2:
            dfs(x - 1, y, 0, count + 1)  # 0은 위쪽으로 회전한 후의 방향
        # 아래쪽으로 회전하고 이동
        elif direction == 3:
            dfs(x + 1, y, 1, count + 1)  # 1은 아래쪽으로 회전한 후의 방향

        # 현재 위치를 방문하지 않은 것으로 표시 (백트래킹)
        visited[x][y][direction] = False

    # 시작 위치에서 네 가지 방향으로 출발
    dfs(grid_size // 2, grid_size // 2 - 1, 0, 1)  # 0은 왼쪽으로 출발한 경우의 방향
    dfs(grid_size // 2, grid_size // 2 + 1, 1, 1)  # 1은 오른쪽으로 출발한 경우의 방향
    dfs(grid_size // 2 - 1, grid_size // 2, 2, 1)  # 2는 위쪽으로 출발한 경우의 방향
    dfs(grid_size // 2 + 1, grid_size // 2, 3, 1)  # 3은 아래쪽으로 출발한 경우의 방향

    return paths

# 입력 받기
N = int(input())

# 결과 출력
print(count_walk_paths(N))
