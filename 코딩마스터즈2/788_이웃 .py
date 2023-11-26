import heapq


def minimum_cost(N, M, K, weights, edges):
    graph = {i: [] for i in range(1, N + 1)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    min_cost = 0
    visited = set()
    heap = [(-weights[i], i+1) for i in range(N)]  # 가중치를 음수로 변환하여 최대 힙 구성
    heapq.heapify(heap)

    while heap:
        current_weight, current_vertex = heapq.heappop(heap)
        current_weight = -current_weight  # 음수로 변환된 가중치를 다시 양수로 변환

        if current_vertex not in visited:
            visited.add(current_vertex)

            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    neighbor_weight = weights[neighbor - 1]
                    weights[neighbor - 1] = max(weights[neighbor - 1], current_weight - K)
                    min_cost += max(0, weights[neighbor - 1] - neighbor_weight)
                    heapq.heappush(heap, (-weights[neighbor - 1], neighbor))

    return min_cost


# 입력 받기
N, M, K = map(int, input().split())
weights = [int(input()) for _ in range(N)]
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
result = minimum_cost(N, M, K, weights, edges)
print(result)
