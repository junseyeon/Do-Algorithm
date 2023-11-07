# -*- coding: utf-8 -*-
import sys
from itertools import combinations
poss =[6]
def isprime(num):
    cnt = 0
    for i in range(2, int(num**0.5)+1, 1):  #9, 16은 유사소수 아님
        if cnt==0 and i*i==num: pass
        elif num % i==0: cnt+=1
        if cnt > 2: break        
    if cnt==1: poss.append(num)
a = int(sys.stdin.readline())
if a < 18 : 
    print('impossible')
    exit(0)
for i in range(7,a-18):
    isprime(i)
#print(poss)
for i in combinations(poss,3):
    tmp = sum(i)
    if tmp < a  and a-tmp not in i : 
        print('possible') 
        break
else: print('impossible')