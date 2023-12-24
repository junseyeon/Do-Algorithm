#https://www.acmicpc.net/problem/12891
# 슬라이딩 윈도우 기법으로 시간초과 줄이기
S, P = map(int, input().split())
dna = input()
A, C, G, T = map(int, input().split())
acgt = {'A': 0 , 'C':0, 'G':0, 'T':0}
cnt = 0
i = 1

for i in range(P):
    acgt[dna[i]] += 1

if acgt['A'] >= A and acgt['C'] >= C and acgt['G'] >= G and acgt['T'] >= T:
    cnt += 1

for i in range(P, S):
    acgt[dna[i]] += 1
    acgt[dna[i-P]] -= 1
    if acgt['A'] >= A and acgt['C'] >= C and acgt['G'] >= G and acgt['T'] >= T:
        cnt += 1
print(cnt)

