#https://www.acmicpc.net/problem/5883

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
#arr_s = ''
arr = []
for i in range(N):
    su = input().strip()
    #arr_s += su
    arr.append(int(su))
set_arr = set(arr)

max_cnt = 0 
for i in set_arr:
    #remove_arr = arr_s.replace(i,'')
    #print(i, remove_arr)
    remove_arr = [a for a in arr if a != i]
    print(i, remove_arr)
    num = -1 
    cnt = 0
    
    for j in remove_arr:
        #print(num, remove_arr[j])
        if num == j:
            cnt+=1
        else:
            max_cnt = max(max_cnt, cnt)
            num = j
            cnt = 1 
    max_cnt = max(max_cnt, cnt)
if N==1:
    print(1)
else:
    print(max_cnt)

'''
문자열로 하면 틀리고 
remove_arr로 하면 맞음 
'''
