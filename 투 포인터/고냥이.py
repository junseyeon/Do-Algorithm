# https://www.acmicpc.net/problem/16472

'''
문자열을 주면 그 중에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열밖에 인식하지 못한다.
'''

import sys
input = sys.stdin.readline
N = int(input())
cat = input().strip()

# cnt = 0   # 알파벳 종류
# base = ''
# re = 0
# for idx, i in enumerate(cat):
#     base = i
#     cnt = 1
#     for j in range(idx+1, len(cat)):
#         if cat[j] in set(base):    # 알파벳 종류가 기존에 있을 떄
#             base+=cat[j]
#         else:                   # 없었던 알파벳 종류 일 때
#             if cnt < N:         # 인식 가능한 알파벳 종류가 남았을 떄
#                 cnt += 1
#                 base += cat[j]
#             else:               # 인식 불가능한 상태
#                 re = max(re, len(base))
#                 break
# print(re)


# 방법2
# 더하다가 넘어가면 뒤에서 빼고 다시 앞으로 가기
from collections import defaultdict
cnt = 0
left = 0
right = 0
letter = defaultdict(int)
re = 0
while right < len(cat):
    if len(letter) < N or cat[right] in letter:
        letter[cat[right]] += 1
        right += 1
    else:
        letter[cat[left]] -= 1
        if letter[cat[left]] == 0:
            del letter[cat[left]]
        left += 1
    re = max(re, sum(letter.values()))
print(re)
