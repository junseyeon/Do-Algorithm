#https://www.acmicpc.net/problem/15736
N = int(input())

#방법1: 1 ~ N 까지 모든 숫자의 약수의 개수로 청과 백을 나눈다.
# def divisor(n):
#     cnt = 0
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             if i ** 2 == n: cnt += 1
#             else: cnt += 2
#     return cnt   # 소수의 총 개수
#
# re = 1   # 1은 소수가 1개
# for i in range(2, N+1):
#     if divisor(i) % 2 != 0:    # 소수의 개수가 홀수면 백기 카운트
#         re += 1
#         print(i, '백', end=' ')
#     print(i, '흑', end=' ')
# print(re)


# 방법2 : 흑과 백이 되는 경우를 모두 출력해 보니 어떤수의 제곱이면 백이 된다.
#import math
print(int(N ** 0.5))
