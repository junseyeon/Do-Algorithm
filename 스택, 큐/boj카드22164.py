import sys
from collections import deque
'''
제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
'''
n = int(sys.stdin.readline())
arr = deque()
for i in range(n):
    arr.append(i+1)

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])