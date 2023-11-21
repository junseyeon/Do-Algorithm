
def main():
    def find_max_expected_score(N, dice_faces):
        max_expected_score = float('-inf')
        best_k_values = []

        for k in range(1, N + 1):
            total_score = 0

            for dice1 in dice_faces:
                for dice2 in dice_faces:
                    for dice3 in dice_faces:
                        dice_sum = dice1 + dice2 + dice3
                        score = k + dice_sum

                        if score <= N:
                            total_score += score

            if total_score > max_expected_score:
                max_expected_score = total_score
                best_k_values = [k]
            elif total_score == max_expected_score:
                best_k_values.append(k)

        return max_expected_score * 216, best_k_values

    # 입력값 받기
    N = int(input())
    dice_faces = list(map(int, input().split()))

    # 최대 기댓값 및 해당하는 K 값 출력
    result, best_k_values = find_max_expected_score(N, dice_faces)
    print(result)
    print(*best_k_values)


if __name__ == "__main__":
    main()


# 반례 15 11 12 0
