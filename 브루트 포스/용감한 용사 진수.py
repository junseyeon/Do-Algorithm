#https://www.acmicpc.net/problem/14718

'''
적 힘 <= 진수 힘
적 민첩 <= 진수 민첩
적 지능 <= 진수 지능

스탯 포인트
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [] 
arr_sum= [] 
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    arr_sum.append(sum(tmp))

rank = [0]*N
for i, v  in enumerate(sorted(range(N), key=lambda x: arr_sum[x])):
    rank[i] = v

result = [0,0,0] 
for i in range(K):
    target_index= rank.index(i)
    for j in range(3):
        result[j] = max(result[j],arr[target_index][j])

print(sum(result))