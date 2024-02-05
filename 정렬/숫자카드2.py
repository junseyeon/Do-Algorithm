
# https://www.acmicpc.net/problem/10816

'''
숫자카드1 과는 다르게 

방법 1: bisect 모듈 사용
방법 2: dictionary 사용 
'''
import sys, bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
arr2 = list(map(int, input().split()))


# 방법1 
# re=[]
# for i in arr2:
#     l = bisect.bisect_left(arr, i)
#     r = bisect.bisect_right(arr,i)
#     re.append(r-l)
# print(*re)

# 방법2
from collections import defaultdict
n_dic = defaultdict(int)
for i in arr:
    n_dic[i] += 1
re = [] 
for i in arr2:
    if i in n_dic.keys():
        re.append(n_dic[i])
    else:
        re.append(0)
print(*re)

    
