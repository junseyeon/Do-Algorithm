#https://www.acmicpc.net/problem/2725
'''
[포인트]
기울기가 다른 직선만 카운트 
arr값들이 정사각형 형태로 늘어남으로 계산을 2x2 3x3 4x4 ㄱ자로 커지도록
기울기가 무한대 혹은 0은 불포함 하고자 j의 범위를 1부터
'''
N = int(input())
arr = [int(input()) for _ in range(N)]

line = [0, 3]
incline = set([0,1])
# for i in range(2, max(arr)+1):  # 2
#     cnt = 0
#     for j in range(1, i):  # 1,2
#         new_incline = j/i
#         if new_incline not in incline:
#             incline.add(new_incline)
#             cnt += 1
#         new_incline2 = i/j
#         if new_incline2 not in incline:
#             incline.add(new_incline2)
#             cnt += 1
#
#     line.append(line[-1] + cnt)

for i in range(2, max(arr)+1):  # 2
    cnt = 3 #초기값을 정해주면 39번째 라인 줄일 수 있음
    for j in range(1, i):  # 1,2
        new_incline = j/i
        if new_incline not in incline:
            incline.add(new_incline)
            cnt += 1
        new_incline2 = i/j
        if new_incline2 not in incline:
            incline.add(new_incline2)
            cnt += 1

    line.append(cnt)

for i in arr:
    print(line[i])