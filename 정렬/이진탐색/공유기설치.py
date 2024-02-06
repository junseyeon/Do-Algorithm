#https://www.acmicpc.net/problem/2110

'''
2개는 무조건 처음과 마지막 
나머지를 그 사이에 둬야하는데   
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
arr=[]
[arr.append(int(input())) for _ in range(N)]
