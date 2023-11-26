# -*- coding: utf-8 -*-

#미완성
N = int(input())
cards = list(map(int, input().split()))

i = 0
score_diff = 0

while i < len(cards):
    if i + 4 < len(cards):
        # 마지막 5개 카드 중 가장 큰 값을 가지는 카드 선택
        max_index = max(range(5), key=lambda x: cards[i+x])
        score_diff += sum(cards[i:i+max_index])
        i = i + max_index + 1
    else:
        # 마지막 그룹의 경우 모두 선택
        score_diff += sum(cards[i:])
        break

print(score_diff)
