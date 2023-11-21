N = int(input())
lengths = list(map(int, input().split()))
sort = sorted(lengths)
max_length = max(lengths)

# while max_length >= sum(sort[-3:-1]):
#     del sort[-1]
#     max_length = sort[-1]
while max_length >= sum(sort[:2]):
    del sort[0]  # 가장 작은 막대 삭제

if len(sort) == 31:
    print(len(sort) + 1)
else:
    print(len(sort))

