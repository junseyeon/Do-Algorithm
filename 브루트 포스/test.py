a = [30, 100, 120, 10]

# 순위를 매길 리스트 초기화
rank_list = [0] * len(a)

print(sorted(range(len(a)), key=lambda x: a[x]))

# 각 요소에 대한 순위 계산
for i, value in enumerate(sorted(range(len(a)), key=lambda x: a[x])):
    rank_list[value] = i+1

print(rank_list)
