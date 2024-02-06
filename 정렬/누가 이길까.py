#https://www.acmicpc.net/problem/28449

import sys, bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
Narr= list(map(int, input().split()))
Marr= list(map(int, input().split()))

Marr.sort()

hi = 0 
arc = 0
same = 0
print(Marr)
for i in Narr:
    l = bisect.bisect_left(Marr, i)
    r = bisect.bisect_right(Marr, i)   # 동일한 숫자가 여러개 있을 수 있음으로 
    #print(i, l, r)
    if l != M and i == Marr[l]:  # bisect_left([10,15,3,6,10], 19) index_error 
        same += r-l              # 동일한 숫자가 여러개 일때 same의 개수 올려줘야 함!!
    hi += l
    arc += M-r
    print(i,": " , hi, arc, same)

print(hi, arc, same)

from bisect import bisect_left, bisect_right

# li = [10,15,3,6,10]
# k  = 19
# li.sort()
# print(li)
# print(bisect_left(li , k))
# print(bisect_right(li, k))

'''
bisect의 의미를 다시 생각!
left, right의 차이점은 같은 숫자가 리스트안에 있을 때만 왼쪽인지 오른쪽인지가 판단
보통의 경우 무조건 [1,3,10000] 일때 90은 2가 된다. (1이 아님!)
'''
