#https://www.acmicpc.net/problem/11729
#https://www.youtube.com/watch?v=aPYE0anPZqI
# 재귀 
'''
(초기 쌓인 원반 기둥 , 보조 기둥, 목표기둥 )
1. 맨아래 원반을 제외한 나머지 원반을 보조기둥, 맨 아래를 목적기둥으로 옮기고
2. 다시 맨 아래 원반을 제외한 나머지를 목적기둥으로 옮긴다. 
'''
def hanoi(num, start, other, end):
    if num==0: return 
    hanoi(num-1, start, end, other)
    print(start, end )
    hanoi(num-1, other, start, end)

n = int(input())
print(pow(2,n)-1)
hanoi(n,1,2,3)