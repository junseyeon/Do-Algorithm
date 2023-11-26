'''
토글 스위치는 누르는 순간마다 상태가 반전됩니다. (A -> B -> A 누를때까지 유지)
홀드 스위치는 누르고 있는 동안 켜짐 상태이고, 떼면 꺼짐
 3초 뒤 A 행동을 하고 정확히 5초 뒤에는 B 행동
'''

def switch_duration(record, questions):
    toggle_switch = 0
    hold_switch = 0
    toggle_time = 0
    hold_time=0
    result = []
    last_second = questions[-1]
    for second in range(1, last_second+1):

        if toggle_switch == 1: toggle_time += 1
        if hold_switch == 1: hold_time += 1

        if len(record) > 0 and int(record[0][0]) == second:
            action = record[0][1]
            if action == 'A':
                if toggle_switch == 0: toggle_switch=1
                else: toggle_switch = 0
            elif action == 'B':
                pass
            elif action == 'C':
                hold_switch = 1
            elif action == 'D':
                hold_switch = 0

            del record[0]

        if second == questions[0]:
            result.append((toggle_time, hold_time))
            del questions[0]

        #print(second, toggle_switch, toggle_time, hold_time, hold_switch)
    return result


N = int(input())  # 행동의 수
record = [input().split() for _ in range(N)]  # 실험 기록

Q = int(input())  # 의문의 개수
questions = [int(input()) for _ in range(Q)]  # 의문의 시간

result = switch_duration(record, questions)

for r in result:
    print(r[0], r[1])
