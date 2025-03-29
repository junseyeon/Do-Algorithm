# https://www.acmicpc.net/problem/13423
'''
* 입력과 동시에 풀이 진행하기! *
방법1 완전탐색 시간초과 -> 17번, 23번 수정 list를 dict로 만들기. 
* 해결 방법 * 
dictionary 검색은 O(1)
list 검색은 O(N)
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
re = [0]*T
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    dic = dict.fromkeys(arr)     # 리스트를 dictionary로 변경 dict.fromkeys(리스트, 초기값) 기본 초기값 None

    for k in range(N):
        for j in range(N-1, k, -1):
            tmp = (arr[k] + arr[j]) / 2
            #print(tmp)
            if tmp in dic:
                re[i] += 1
                #print(i,j,tmp)
for i in re:
    print(i)


