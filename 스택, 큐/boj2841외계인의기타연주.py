import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

from collections import defaultdict
N, P = map(int, input().split())
stack = []
now = {}
ans = 0
for _ in range(N):
    num, plat = map(int, input().split())
    if num not in now:
        now[num] = [plat]
        ans += 1
    elif plat > now[num][-1]:
        now[num].append(plat)
        ans += 1
    else:
        while len(now[num]) > 0 and plat < now[num].pop():
            ans += 1
        now[num].append(plat)
print(ans)