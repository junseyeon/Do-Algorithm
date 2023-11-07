# 숫자가 여러개 있을 때 최대공약수 찾기
import sys, math
N = int(sys.stdin.readline())
gift = list(map(int,sys.stdin.readline().split()))
re = gift[0]
for i in range(1, len(gift)):
    re = math.gcd(re, gift[i])
print(re)