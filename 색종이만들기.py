#https://www.acmicpc.net/problem/2630

#하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in  range(N)]
#print(arr)
print(arr[:4][:4])
print(arr[0:4][:4])

arr[:N//2][:N//2]
arr[N//2:][N//2:]

