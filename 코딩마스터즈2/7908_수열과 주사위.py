def maximize_expectation(N, scores):
    max_expectation = 0
    selected_k = []

    for k in range(1, N -3):
        expectation = 0
        #max_n = 0
        for i in range(3, 19):
            total = k + i  # K + T
            if total >= N:
                expectation -= 100
            else:
                expectation += scores[total - 1]
                #max_n = max(max_n, scores[total - 1])

        if expectation > max_expectation:
            max_expectation = expectation
            selected_k = [k]
        elif expectation == max_expectation:
            selected_k.append(k)

    return max_expectation * 216, selected_k

# 입력 받기
N = int(input())
scores = list(map(int, input().split()))

# 점수의 최대 기댓값과 선택된 K 구하기
result, selected_k = maximize_expectation(N, scores)

# 출력
print(result)
print(*selected_k)

