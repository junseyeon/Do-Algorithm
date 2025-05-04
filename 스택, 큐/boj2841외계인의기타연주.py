import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

from collections import defaultdict
N, P = map(int, input().split())
now = defaultdict(list)
ans = 0
for _ in range(N):
    num, plat = map(int, input().split())

    while len(now[num]) > 0 and plat < now[num][-1]:
        now[num].pop()
        ans += 1

    if len(now[num]) > 0 and plat == now[num][-1]:
        pass
    else:
        now[num].append(plat)
        ans += 1

print(ans)
'''
while 순서를 제일 처음 판별해야 겠다는 생각을 외 못했을까..
stack 문제를 굳이 (내가) dict로 품.. 
'''