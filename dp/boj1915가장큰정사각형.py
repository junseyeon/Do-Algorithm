'''
https://www.acmicpc.net/problem/1915
[입력]
4 4
1100
0111
1110
0010
[결론]
가장 큰 정사각형 넓이 구하기
'''

'''
1. 아이디어 요약: 1 > 4 > 7 > 11 으로 정사각형 수가 늘어남,, 3씩 증가 규칙 적용 2*(n-1)
결과: 시간초과 발생 -> [대처] 모든 칸을 다 확인하는 것에서, 로직 안에서 체크된 적이 있으면 넘어가도록 했지만 결과 동일.. 
'''
# N, M = map(int, input().split())     #행, 열
# arr = []
# for i in range(N):
#     arr.append(list(map(int,input())))

# chk_arr = [[False] * M for _ in range(N)]
# dy = (0, -1)
# dx = (1, 0)     #우, 상
# def chk(y, x, cnt):
#     t = 1+(2*(cnt-1))   #정사각형을 추가로 판별 해야하는 횟수
#     for i in range(t):
#         if not chk_arr[y][x]: continue
#         if i < (t+1)//2:
#             ny = y + dy[0]  #"우"로 이동
#             nx = x + dx[0]
#         else:
#             ny = y + dy[1]  #"상"으로 이동
#             nx = x + dx[1]
#
#         if  -1 < nx < M and -1 < ny < N and arr[ny][nx] == 1:
#             x = nx
#             y = ny
#             chk_arr[y][x] = True
#         else:
#             return False
#     return True
#
# ans = 1
# for i in range(N):
#     for j in range(M):
#         cnt = 1
#         if arr[i][j] == 1:
#             while chk(i,j, cnt):
#                 chk_arr[i][j] = True
#                 ans = max(ans, cnt)
#                 cnt += 1
# print(ans**2)
''''
2. gpt에서 DP의 단서를 얻어 수정함. 
[핵심로직] 우측 아래 칸을 중심으로 나머지 3개의 값을 확인하고 가장 작은 값에  +1 
[결과] 백준 indexError 발생.. (원인 찾지 못함)
'''

N, M = map(int, input().split())     #행, 열
arr = []
for _ in range(N):
    arr.append(list(map(int,input())))

dx = (-1, 0, -1)  #좌, 위, 아래
dy = (0, -1, -1)

def nemo(y, x):
    temp = float('inf')
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= ny < N and 0 <= nx < M:
            temp = min(temp, arr[ny][nx])
        else:   # 3개중 하나라도 범위 밖에 인덱스가 있으면 무조건 1
            return 1
    return temp+1

ans = 0     # **착각금지** 모두 0이 들어 올 수도 있음!!!!!!!!!!!!
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            #print(i,j)
            arr[i][j] = nemo(i,j)
            ans = max(arr[i][j], ans)

# for i in range(N):
#     print(arr[i])

print(ans**2)

'''
y, x 의 범위가 유효한지 판단하는 2가지 방법
1. 채울 때마다 확인  (나) 
2. 가능한 곳만 채우기 (강의, 추천)  
'''

'''강의 정답'''
# N, M = map(int, input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input())))
#
# ans = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             if i == 0 or j == 0:
#                arr[i][j] = 1
#             else:
#                 arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
#             ans = max(ans, arr[i][j])
# for i in range(N):
#     print(arr[i])
# print(ans ** 2)


'''
7 7
[0, 0, 0, 1, 1, 1, 0]
[1, 0, 1, 1, 2, 2, 0]
[1, 1, 1, 2, 2, 3, 1]
[1, 2, 0, 1, 2, 3, 2]
[1, 2, 1, 1, 2, 3, 3]
[1, 2, 2, 2, 2, 3, 4]
[0, 1, 2, 3, 3, 3, 0]
'''