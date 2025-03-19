import sys
from collections import deque
'''
제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
'''
n = int(sys.stdin.readline())
'''arr = deque()
for i in range(1,n+1):
    arr.append(i)'''
arr = deque(range(1,n+1))

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])
'''
learn: 큐를 사용하는 이유, 삽입 삭제가 O(1) 이지만 배열은 o(N)으로 n*2 으로 시간 초과 
'''