# https://www.acmicpc.net/problem/15831
'''
까만색 조약돌은 B개 이하
흰색 조약돌은 W개 이상
가장 길게
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N, B, W = map(int, input().split())
rock = input().strip()
rock_count = {"W":0, "B":0}
left = 0
right = 0
re = 0

while right < N:
    if rock_count['W'] >= W and rock_count['B'] <= B:
        re = max(re, sum(rock_count.values()))

    if rock[right] == "W":          #흰 조약돌
        rock_count['W'] += 1
        right += 1
    else:                           #검은 조약돌
        if rock_count['B'] < B:
            rock_count['B'] += 1
            right += 1
        else:
            rock_count[rock[left]] -= 1
            left += 1
    print(rock_count)
print(re)