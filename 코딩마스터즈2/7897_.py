def dfs_count_paths(N, current_position, current_direction, visited):
    # 현재 위치와 방향이 N번의 이동 후에 결정된 경우 1을 반환
    if N == 0:
        return 1

    # 방문한 적 있는 상태라면 이전에 계산한 값을 반환
    if (current_position, current_direction) in visited:
        return visited[(current_position, current_direction)]

    # 현재 위치와 방향에서 좌회전과 우회전을 고려하여 다음 상태로 이동
    left_paths = dfs_count_paths(N - 1, current_position, (current_direction + 1) % 4, visited)
    right_paths = dfs_count_paths(N - 1, current_position, (current_direction - 1) % 4, visited)

    # 현재 위치와 방향에서 가능한 경로의 합을 계산
    total_paths = left_paths + right_paths

    # 계산한 값을 저장하고 반환
    print(visited[(current_position, current_direction)])
    visited[(current_position, current_direction)] = total_paths
    return total_paths


# 입력 받기
N = int(input())

# 초기 상태: 시작 위치 (0, 0), 초기 방향은 동쪽 (0)
initial_position = (0, 0)
initial_direction = 0

# 방문 기록을 저장할 딕셔너리
visited = {}

# 결과 출력
result = dfs_count_paths(N, initial_position, initial_direction, visited)
print(result)
