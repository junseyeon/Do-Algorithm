# def switch_duration(record, questions):
#     toggle_switch = 0
#     hold_switch = 0
#     toggle_time = 0
#     hold_time=0
#     result = []
#     last_second = max(questions)
#
#     for second in range(1, last_second+1):
#
#         if toggle_switch == 1: toggle_time += 1
#         if hold_switch == 1: hold_time += 1
#
#         if len(record) > 0 and int(record[0][0]) == second:
#             action = record[0][1]
#             if action == 'A':
#                 toggle_switch = 1 - toggle_switch
#             elif action == 'B':
#                 pass
#             elif action == 'C':
#                 hold_switch = 1
#             elif action == 'D':
#                 hold_switch = 0
#
#             del record[0]
#
#         if second in questions:
#             result.append((toggle_time, hold_time))
#
#         #print(second, toggle_switch, toggle_time, hold_time, hold_switch)
#
#     return result
#
#
# N = int(input())
# record = [input().split() for _ in range(N)]
#
# Q = int(input())
# questions = [int(input()) for _ in range(Q)]
#
# result = switch_duration(record, questions)
#
# for r in result:
#     print(r[0], r[1])

def switch_duration(record, questions):
    toggle_switch = 0
    hold_switch = 0
    toggle_time = 0
    hold_time = 0

    before_time = 0
    result=[]

    for time, action in record:
        time = int(time)
        elapsed_time = time - before_time

        if toggle_switch == 1:
            toggle_time += elapsed_time
        if hold_switch == 1:
            hold_time += elapsed_time

        #print(toggle_switch, toggle_time)

        if len(questions)>0 and time > questions[0]:
            a, b = toggle_time, hold_time
            #print(toggle_time, time, questions[0])
            if toggle_switch == 1:
                a = toggle_time - (time-questions[0])    #현재시간-의문시간
            if hold_switch == 1:
                b = hold_time - (time-questions[0])
            del questions[0]
            result.append((a,b))

        if action == 'A':
            toggle_switch = 1 - toggle_switch
        elif action == 'B':
            pass
        elif action == 'C':
            hold_switch = 1
        elif action == 'D':
            hold_switch = 0

        before_time = time

    while questions:
        elapsed_time = questions[0] - before_time
        if toggle_switch == 1:
            toggle_time += elapsed_time
        if hold_switch == 1:
            hold_time += elapsed_time
        result.append((toggle_time, hold_time))
        before_time = questions[0]
        del questions[0]

    return result

# 입력 처리
N = int(input())
record = [tuple(input().split()) for _ in range(N)]

Q = int(input())
questions = [int(input()) for _ in range(Q)]
ordered_question = sorted(questions)
oq = ordered_question.copy()

re = switch_duration(record, ordered_question)
#print()
for i in questions:
    new_i = oq.index(i)
    print(re[new_i][0], re[new_i][1])


