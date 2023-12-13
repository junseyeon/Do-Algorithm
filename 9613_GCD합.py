#백준 : https://www.acmicpc.net/problem/9613
# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
import math
N  = int(input())
arr =[]
for _ in range(N):
    arr.append(list(input().split()[1:]))
for i in range(N):
    hap = 0
    for j in range(len(arr[i])):
        for k in arr[i][j+1:]:
            hap += math.gcd(int(arr[i][j]), int(k) )
    print(hap)