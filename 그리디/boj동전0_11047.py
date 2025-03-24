import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [ int(input()) for i in range(n)]
coin.reverse()
re = 0
for c in coin:
    re+=k//c
    k %= c
print(re)