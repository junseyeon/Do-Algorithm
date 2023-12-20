# https://www.acmicpc.net/problem/2839
# N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수
'''
왜 5은 나누기만? 빼기로 수행 안하는 이유...
'''

N = int(input())
re = 0

while N > 2 :
    if N%5==0:
        re += N//5
        N %= 5
    else:
        re+=1
        N = N-3

#print(N)
if N == 0: print(re)
else: print(-1)