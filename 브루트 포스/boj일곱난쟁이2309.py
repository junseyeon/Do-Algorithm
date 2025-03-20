import sys
from itertools import combinations
sys.stdin = open('../input.txt')
input = sys.stdin.readline

'''
7난쟁이 키의 합=100 / 현재 9명중 7명을 찾아야 함 
'''

h = [ int(input()) for _ in range(9)]  #입력과 동시에 배열 초기화

for i in combinations(h, 7):
    if sum(i)==100:
        print(*sorted(i), sep='\n')
        break

