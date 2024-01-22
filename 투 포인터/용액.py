# https://www.acmicpc.net/problem/2467

'''
산성용액 ( 1~ 1,000,000,000 )
알카리성 ( -1 ~ -1,000,000,000)
같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만든다
투포인터 알고리즘
해결포인트: 첫번째와 마지막 인덱스에서 점차 가운데로 이동
          양수면 오른쪽 움직이고 음수면 왼쪽 움직이기
'''

import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
re = [float("INF"), 0, 0]

left = 0
right = n -1

while left < right:
    hap = arr[left] + arr[right]
    if re[0] > abs(hap):
        re[0] = abs(hap)
        re[1] = arr[left]
        re[2] = arr[right]
    if hap > 0:
        right -=1
    else:               #hap < 0
        left += 1
print(re[1], re[2])





