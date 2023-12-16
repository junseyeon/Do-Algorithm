# https://www.acmicpc.net/problem/2503
from itertools import permutations
T = int(input())
arr = list(permutations(list(map(str,range(1,10))),3))

for _ in range(T):
    number, strike, ball = input().split()
    remove_cnt = 0
    for arr_i in range(len(arr)):  # 순열
        target = arr[arr_i - remove_cnt]
        s, b = 0, 0
        for i, v in enumerate(number): # 제시된 숫자
            if v in target:
                if target.index(v) == i:
                    s += 1
                else:
                    b += 1
        if int(strike) != s or int(ball) != b:
            arr.remove(target)
            remove_cnt += 1
print(len(arr))