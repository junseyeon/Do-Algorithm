'''45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

f(n): 길이가 n일때의 계단 수
f(n, 왼쪽 수)
    ㅇ 1~8 f(n-1, left-1), f(n, left+1)
    ㅇ 0 f(n, left+1)
    ㅇ 9 f(n, left-1)

f(1) = 9
f(2) = 17

'''

## bootom-up 방식, 1부터 차례로 저장
n = int(input())
mod = 1_000_000_000
# #
# chk = [[0]*10 for _ in range(n)]
# for i in range(1, 10):
#     chk[0][i] = 1
#
# for i in range(1, n):
#     for j in range(10):
#         if j > 0:
#             chk[i][j] += chk[i-1][j-1]
#         if j < 9:
#             chk[i][j] += chk[i-1][j+1]
#
# ans = 0
# print(chk)
# for i in range(10):  # 0~9
#     ans += chk[n-1][i]
# print(ans%mod)

'''
mod를 중간중간에 해주면 메모리가 절약되고 결과 값도 당연히 동일해진다. 
'''

## top-down 원하는 결과값 차레대로 추적
n = int(input())
mod = 1_000_000_000
cache = [[0]*10 for _ in range(n)]
def dp(n,su):
    if n==0:
        return 1 if su>0 else 0
    if su == 0:
        if  cache[n-1][su+1]: return cache[n-1][su+1]
        cache[n][su] = dp(n-1, su+1)
        return cache[n][su]
    elif su < 9:
        if cache[n-1][su+1] and cache[n-1][su-1]: return cache[n-1][su+1] + cache[n-1][su-1]
        cache[n][su] = dp(n-1,su+1) + dp(n-1,su-1)
        return  cache[n][su]
    else: #su==9
        if cache[n-1][su-1]: return cache[n-1][su-1]
        cache[n][su] = dp(n-1,su-1)
        return cache[n][su]

ans = 0
for i in range(10):
    ans += dp(n-1, i)
print(ans % mod)

#18404112
#18404112(2~5)





# def dp(n, left = 0):
#     if n==1: return 9
#     if left == 0: return dp(n-1,left-1)
#     elif left == 0: return dp(n-1, left+1)
#     else: return dp(n-1, left-1)  + dp(n-1, left+1)
# sum = dp(n)
# print(sum)