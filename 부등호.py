#https://www.acmicpc.net/problem/2529
from itertools import combinations, permutations
import sys 

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
re = [] 
for i in permutations(range(10), n+1):
    for j, v in enumerate(arr):
        if v == '<':
            if i[j] < i[j+1]: pass
            else: break
        elif v == '>':
            if i[j] > i[j+1]: pass
            else: break
    else:
        re.append(i)

print(''.join(map(str,re[-1])))
print(''.join(map(str,re[0])))
