
def main():
    # 토글 스위치와 홀드 스위치의 상태를 초기화합니다.
    toggle_state = False
    hold_state = False

    # 입력으로부터 기록의 개수 N을 받습니다.
    N = int(input())

    # 토글 스위치와 홀드 스위치가 켜져 있는 시간을 저장할 변수를 초기화합니다.
    toggle_duration = 0
    hold_duration = 0

    # 기록을 저장할 리스트를 초기화합니다.
    records = []

    # N개의 기록을 입력받습니다.
    for _ in range(N):
        T, O = map(str, input().split())
        T = int(T)

        # 토글 스위치의 상태를 업데이트합니다.
        if toggle_state:
            toggle_duration += T - prev_time

        # 홀드 스위치의 상태를 업데이트합니다.
        if hold_state:
            hold_duration += T - prev_time

        # 현재 시각을 저장합니다.
        prev_time = T

        # 행동에 따라 스위치 상태를 업데이트합니다.
        if O == 'A':
            toggle_state = not toggle_state
        elif O == 'B':
            toggle_state = False
        elif O == 'C':
            hold_state = True
        elif O == 'D':
            hold_state = False

    # 마지막 기록 이후의 켜져 있던 시간을 계산합니다.
    if toggle_state:
        toggle_duration += k - prev_time
    if hold_state:
        hold_duration += k - prev_time

    # 의문의 개수 Q를 입력받습니다.
    Q = int(input())

    # 각 의문에 대해 답을 출력합니다.
    for _ in range(Q):
        # 의문의 시간 k를 입력받습니다.
        k = int(input())

        # 토글 스위치와 홀드 스위치의 켜져 있던 시간을 출력합니다.
        print(toggle_duration, hold_duration)


if __name__ == "__main__":
    main()


# 반례 15 11 12 0
