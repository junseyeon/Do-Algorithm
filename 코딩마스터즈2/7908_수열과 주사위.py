from fractions import Fraction
def maximize_expectation(N, scores):
    max_expectation = -float('INF')
    selected_k = []
    dice = [0, 0, 0, 1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1]

    for k in range(1, N-3):
        expectation = 0
        for i in range(3, 19):
            index = k + i -1
            if index >= N:
                expectation += -100*(Fraction(dice[i],216))
            else:
                expectation += scores[index] * (Fraction(dice[i],216))
        if expectation > max_expectation:
            max_expectation = expectation
            selected_k = [k]
        elif expectation == max_expectation:
            selected_k.append(k)
            #print(max_expectation)

    return max_expectation * 216, selected_k

N = int(input())
scores = list(map(int, input().split()))
result, selected_k = maximize_expectation(N, scores)
print(max(0,result))
print(*selected_k)

# from itertools import product
#
# def count_occurrences():
#     occurrences = [0] * 16  # 인덱스 3부터 18까지의 개수를 저장할 리스트
#
#     # 주사위 눈금이 1부터 6까지이므로 product를 사용하여 가능한 모든 경우의 수 생성
#     dice_outcomes = product(range(1, 7), repeat=3)
#
#     for outcome in dice_outcomes:
#         #print(outcome)
#         total = sum(outcome)
#         if total==10: print(outcome)
#         occurrences[total - 3] += 1
#
#     return occurrences
#
# result = count_occurrences()
# print(result)


