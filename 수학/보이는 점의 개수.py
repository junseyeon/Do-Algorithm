#https://www.acmicpc.net/problem/2725

N = int(input())
arr = [int(input()) for _ in range(N)]

'''
[포인트]
기울기가 다른 직선만 카운트 
arr값들이 정사각형 형태로 늘어남으로 계산을 2x2 3x3 4x4 ㄱ자로 커지도록
기울기가 무한대 
'''

line = [0, 3]
incline = set([0,1])
for i in range(2, max(arr)+1):  # 2
    cnt = 0
    for j in range(1, i):  # 1,2
        new_incline = j/i
        if new_incline not in incline:
            incline.add(new_incline)
            cnt += 1
        new_incline2 = i/j
        if new_incline2 not in incline:
            incline.add(new_incline2)
            cnt += 1

    line.append(line[-1] + cnt)

for i in arr:
    print(line[i])