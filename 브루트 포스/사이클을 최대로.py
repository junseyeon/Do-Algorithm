# https://www.acmicpc.net/problem/10819
'''
배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램
'''

from itertools import permutations
N = input()
arr = list(map(int, input().split()))
max_n = 0
for per in permutations(arr, len(arr)):
    sum = 0
    for i in range(len(per)-1):
        sum += abs(per[i]-per[i+1])
    max_n = max(max_n, sum)
print(max_n)

'''
수학적으로 규칙을 찾아내기 전에 프로그래밍으로 돌려보자..! 
'''
