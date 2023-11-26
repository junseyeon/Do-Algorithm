MOD = 1000000007

def calculate_players_confidence(N, weights, worries, multiplier_w, multiplier_p, updates):
    confidence_count = [0] * N  # 각 선수가 승리를 확신하는 다른 선수의 수를 저장하는 배열

    for i in range(1, N):
        weights[i] = (weights[i-1] * multiplier_w) % MOD
        worries[i] = (worries[i-1] * multiplier_p) % MOD

        for update in updates:
            if update[0] == i:
                multiplier_w, multiplier_p = update[1], update[2]

        for j in range(i):
            if weights[j] - worries[j] > weights[i]:
                confidence_count[i] += 1

    return confidence_count

N = int(input())
weights = []
worries = []

# 초기 선수 정보 입력
for i in range(N-1):
    w, p = map(int, input().split())
    weights.append(w)
    worries.append(p)


K = int(input())  # 갱신 정보의 개수
updates = [list(map(int, input().split())) for _ in range(K-1)]

# 각 선수의 몸무게와 걱정거리 계산 및 승리 확신하는 다른 선수 수 계산
confidence_count = calculate_players_confidence(N, weights, worries, multiplier_w, multiplier_p, updates)

# 결과 출력
total_confidence = sum(confidence_count) % MOD
print(total_confidence)


