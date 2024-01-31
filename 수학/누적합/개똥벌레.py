# https://www.acmicpc.net/problem/3020

'''
동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수)
첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장
높이 H 미터를 지나갈때 파괴되는 장애물의 최소값과, 그런 구간의 개수
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, H = map(int, input().split())
arr = [] 
[arr.append(int(input())) for _ in range(N)]

