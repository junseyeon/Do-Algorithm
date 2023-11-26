def count_ways_to_color(N, M):
    # 격자판을 3차원 배열로 초기화
    # dp[i][j][k]: i행 j열의 격자를 k색으로 칠하는 경우의 수
    dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]

    # 첫 번째 행 초기화
    for k in range(3):
        dp[0][0][k] = 1

    # 각 격자에 대해 경우의 수 계산
    for i in range(N):
        for j in range(M):
            for k in range(3):
                # 이전 행과 열의 경우의 수를 더함
                for l in range(3):
                    if i > 0 and l != k:
                        dp[i][j][k] += dp[i-1][j][l]
                    if j > 0 and l != k:
                        dp[i][j][k] += dp[i][j-1][l]

    # 모든 경우의 수를 더함
    total_ways = sum(dp[N-1][M-1])

    return total_ways

# 입력 받기
N, M = map(int, input().split())

# 결과 출력
result = count_ways_to_color(N, M)
print(result)


def count_colorings(N, M):
    # 격자가 1x1인 경우는 3가지 색으로 칠할 수 있음
    if N == 1 and M == 1:
        return 3

    # 격자가 1xM 또는 Nx1인 경우는 3의 제곱으로 경우의 수 계산 가능
    if N == 1 or M == 1:
        return 3 ** max(N, M)

    # 그 외의 경우는 동적 프로그래밍을 활용하여 경우의 수 계산
    dp = [[0] * M for _ in range(N)]

    # 초기값 설정
    for i in range(3):
        for j in range(3):
            if i != j:
                dp[0][0] += 1

    # 첫 번째 행 초기화
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] * 2

    # 첫 번째 열 초기화
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] * 2

    # 나머지 격자의 경우의 수 계산
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[N - 1][M - 1] * 3


# 예시 입력
input1 = (2, 2)
input2 = (2, 3)
input3 = (3, 3)

# 결과 출력
print(count_colorings(*input1))
print(count_colorings(*input2))
print(count_colorings(*input3))


import sys
n, m = map(int, input().split())
max_n = max(n,m)
min_n = min(n,m)
if n==1 or m ==1:
    if n==1 and m==1: print(3)
    else: print((max_n-1)*6)
elif min_n==2:
    print(3**max(n,m) * min(n,m))
elif min_n>=3:
     여기를 작성해줘