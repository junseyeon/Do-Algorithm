from collections import deque

def solve_mazes(maze1, maze2):
    rows1, cols1 = len(maze1), len(maze1[0])
    rows2, cols2 = len(maze2), len(maze2[0])

    # 이동 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def is_valid(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

    def can_move(maze, x, y):
        return is_valid(x, y, len(maze), len(maze[0])) and maze[x][y] != '#'

    def bfs(start1, start2, end1, end2):
        queue = deque()
        queue.append((start1[0],start1[1], start2[0],start2[1], 0))
        visited = set()

        while queue:
            print(queue.popleft())
            x1, y1, x2, y2, steps = queue.popleft()

            if (x1, y1, x2, y2) in visited:
                continue

            visited.add((x1, y1, x2, y2))

            # 동시에 이동
            for i in range(4):
                nx1, ny1 = x1 + dx[i], y1 + dy[i]
                nx2, ny2 = x2 + dx[i], y2 + dy[i]

                if can_move(maze1, nx1, ny1) and can_move(maze2, nx2, ny2):
                    if (nx1, ny1) == end1 and (nx2, ny2) == end2:
                        return steps + 1
                    queue.append((nx1, ny1, nx2, ny2, steps + 1))

        return -1

    start1, end1 = find_start_end(maze1)
    start2, end2 = find_start_end(maze2)

    return bfs(start1, start2, end1, end2)

def find_start_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end

def main():
    H1, W1 = map(int, input().split())
    maze1 = [input().strip() for _ in range(H1)]

    H2, W2 = map(int, input().split())
    maze2 = [input().strip() for _ in range(H2)]

    result = solve_mazes(maze1, maze2)
    print(result)

if __name__ == "__main__":
    main()
