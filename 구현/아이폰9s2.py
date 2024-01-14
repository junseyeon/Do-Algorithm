import sys

# 입력 받기
input = sys.stdin.readline

N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))

# 중복된 숫자를 제외한 집합 생성
S = set(B)

# 최대 연속 구간 길이 찾기
answer = 0
for s in S:
    b = [i for i in B if i != s]

    cur = -1
    a = 0
    for c in b:
        if c != cur:
            answer = max(a, answer)
            a = 1
            cur = c
        else:
            a += 1

    answer = max(a, answer)

if len(B) == 1:
    print(1)
else:
    print(answer)
