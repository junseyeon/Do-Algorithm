#https://www.acmicpc.net/problem/2143

'''
이진탐색은 같은 숫자가 여러개 나열되었을 때 개수를 찾지 못한다.
0111114 에서 1을 찾는다고 하면 중간에서 다시 뒤에를 보기 때문에 앞은 카운트 하지 못함. 
따라서 1의 시작과 1의 끝을 알아야 함이 포인트..!
'''

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

n_hap = []
for i in range(N):
    tmp = 0
    for j in range(i, N):
        tmp += n_arr[j]
        n_hap.append(tmp)

m_hap = []
for i in range(M):
    tmp = 0 
    for j in range(i, M):
        tmp += m_arr[j]
        m_hap.append(tmp)

m_hap.sort()

cnt = 0
for i in n_hap:
    target = T - i
    left = 0 
    right = len(m_hap)-1
    start = -1
    while left <= right:
        mid = (left + right) // 2
        if m_hap[mid] == target:
            start = mid
            right = mid -1
        elif m_hap[mid] < target: 
            left = mid + 1
        else:
            right = mid -1
    left = 0 
    right = len(m_hap)-1
    end = -1
    while left <= right:
        mid = (left + right) // 2
        if m_hap[mid] == target:
            end = mid
            left = mid + 1
        elif m_hap[mid] < target: 
            left = mid + 1
        else:
            right = mid -1


    else:
        if start != -1:
            cnt += (end-start+1)

print(cnt)

# 최민혁 
# 두 배열의 합_BOJ2143

import sys
# sys.stdin = Aopen('input.txt')
input = sys.stdin.readline

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

sumA = []
for i in range(len(A)):
	s = A[i]
	sumA.append(s)
	for j in range(i + 1, len(A)):
		s += A[j]
		sumA.append(s)

sumB = dict()
for i in range(len(B)):
	s = B[i]
	if (s not in sumB):
		sumB[s] = 1
	else:
		sumB[s] += 1
	for j in range(i + 1, len(B)):
		s += B[j]
		if (s not in sumB):
			sumB[s] = 1
		else:
			sumB[s] += 1

answer = 0
for a in sumA:
	t = T - a
	if (t in sumB):
		answer += sumB[t]

print(answer)