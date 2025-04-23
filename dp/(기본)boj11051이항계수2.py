
''' 이항게수 '''
#1. 재귀, 탑다운
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
chk = [[0]*1001 for _ in range(1001)]
def bino(a,b):
    if chk[a][b]: # 0이상이면 모두 true니깐
        return chk[a][b]
    if a==b or b==0:
        return 1
    chk[a][b] = bino(a-1,b-1) + bino(a-1, b)
    return chk[a][b]
print(bino(N,K)%10007)

'''
2차원 배열에 값이 있는 것 or 없는것을 기준으로 할 것인지에 따라 조건문의 형태가 달라지고 순서대로 어떻게 분기 할지가 중요..
'''

#2. 바텀,업 (완전탐색)
mod = 10007
for i in range(N+1):
    chk[i][0] = chk[i][i] = 1
    for j in range(i):
        chk[i][j] = chk[i-1][j-1] + chk[i-1][j]
print(chk[N][K] % mod)

