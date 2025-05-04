'''
문제
주변 WBW 체스판인데 8x8를 아무데나 잘랐을 때 어느 부분을 잘라야 최소한으로 변경하는지
2가지. 왼쪽 위가 검 or 흰으로 시작하는 경우만 존재

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ input().strip() for _ in range(N) ]

'''
8*8를 돌면서 W로 시작할 때, B로 시작할 때 각각 바꿀 체스판 확인.. 
'''
ans = 64
def check(i, j, bw):
    cnt = 0
    global ans
    for k in range(8):
        for l in range(8):
            if (k+l)%2: #홀수
                if board[i+k][j+l] == bw:
                    cnt += 1
            else:
                if board[i+k][j+l] != bw:
                    cnt += 1
    ans = min(ans, cnt)

for i in range(N-7):
    for j in range(M-7):
        check(i, j, 'W')
        check(i, j, 'B')

print(ans)

'''
W/B의 자리가 홀수, 짝수에 따라 옳은지 여부를 확인하는 것이 알고리즘의 핵심 
'''

