#https://www.acmicpc.net/problem/17136

'''
[교훈이 큰 문제!!]
색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.

입력
총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.

출력
모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다
'''

'''
해결안 [greedy]
	1.	색종이 크기 5 → 4 → 3 → 2 → 1 순서로 진행 (큰 것부터).
	2.	색종이를 놓을 수 있으면 그 위치에 덮고 0으로 만든다.
	3.	최종적으로 1이 모두 없어지면 성공, 아니면 실패로 판단.
	
=> 반례 
8*8 모두 1일때 5*5 후 나머지보다, 4*4 2개가 효율적
'''
# arr = [list(map(int,input().split())) for _ in range(10)]
# size = [5, 4, 3, 2, 1]
# cnt = [5, 5, 5, 5, 5]  #1, 2, 3, 4, 5 색종이 잔여 갯수 (반대)
#
# def paper(s, y, x):
#     for i in range(y,y+s):
#         for j in range(x,x+s):
#             if arr[i][j]==1:
#                 continue
#             else:
#                 return False
#
#     # 색종이가 남아 있으면 arr 0으로 변환
#     if cnt[s-1] > 0:
#         for i in range(y,y+s):
#             for j in range(x,x+s):
#                 arr[i][j]=0
#         cnt[s-1]-=1
#     #print(s)
#
# for s in size:
#     for i in range(10-s+1):
#         for j in range(10-s+1):
#             #print(s, i, j, arr[i][j])
#             if arr[i][j]==1:
#                 paper(s,i,j)
#
# ans_sum = sum(sum(i) for i in arr)
# if ans_sum == 0:
#     print(25-sum(cnt))
# else:
#     print(-1)

'''
방법2 
모든 자리를 돌면서 1이면 그 자리를 기준으로 1*1~5*5 전부 해본다.
사이즈만큼 0으로 변경하고 
다음 차례를 위해 다시 1로 변경
dp 수행

'''
arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0]*5
ans = 25 #종이의 최대 갯수가 25개 임으로

def is_possible(y,x, sz):
    if paper[sz-1] == 5:
        return False
    for i in range(sz):
        for j in range(sz):
            if y+i>9 or x+j>9:
                return False
            if arr[y+i][x+j] == 0:
                return False
    return True

def change(y,x,sz, su):
    for i in range(sz):
        for j in range(sz):
            arr[i+y][j+x] = su
    if su == 0:
        paper[sz-1]+=1
        # for i in range(10):
        #     print(arr[i])
        # print()
    else:
        paper[sz-1]-=1
        # for i in range(10):
        #     print(arr[i])
        # print()

def dp(y, x):
    global ans

    if x == 10:
        dp(y+1, 0)
        return

    if y==10:
        ans = min(ans, sum(paper))
        return

    if arr[y][x] == 0:
        dp(y,x+1)
        return

    for sz in range(1,6):
        if is_possible(y,x, sz): # 범위, 종이 갯수
            change(y,x,sz, 0)  #0으로 바꾸고 종이 하나 늘이기
            dp(y, x+1)
            change(y, x, sz, 1)     #무조건 1로 바꾸는 것이 아니라 1이었던 것만 바꿔야 되는게 아닌지

dp(0,0)
print( -1 if ans==25 else ans)



'''
lesson&learn
    for i in range(10), for j in range(10) 이 안되는 이유
    모든 좌표를 도는 걸,, 순서대로가 아닌, dp..: 
'''


'''
0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''