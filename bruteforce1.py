### 666 이 들어간 숫자
'''
n = int(input())
count = 1
find = '666'
i = 666
while count < n:
    i+=1
    if find in str(i):
        count+=1
print(i)
'''


### 블랙잭 3개 합쳐서 가장 가까운 수  
# 1. 조합 사용하는 방법
# 2. goal을 넘지 않은 수 중에 가장 가까운 수.. max로 풀기...

""" from itertools import combinations 
N, goal = map(int,input().split())
cards = list(map(int,input().split()))
my_max = 0 
for i in list(combinations(cards, 3)):
    my_sum = sum(i)
    if my_max < my_sum <= goal:
        my_max = my_sum
print(my_max) """


#### 365 문제 

# 3/6/9가 숫자n 에 몇번이 들어가는지 !
# n을 각각 숫자가 3/6/9 인지 확인 하는 것보다 훨씬 반복횟수 낮아짐...
## => 주어진 조건이 있을 때 반대로 생각해보기... 
import sys
input = sys.stdin.readline
N = int(input())
clap=0
for i in range(1,N+1):
    for j in list(str(i)):
        if '3' in j:
            clap+=1
        if '6' in j:
            clap+=1
        if '9' in j:
            clap+=1
print(clap)
# 시간초과...

# str(i) 를 for문 안에서 수행하지 않기!!!

N = int(input())
check = '369'
re = 0
for i in range(1, N+1):
    for c in check:
        re += str(i).count(c)
print(re)
