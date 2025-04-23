n = int(input())
'''
1. 재귀 (t-d)
2. 반복 (b-u)
'''
#1. 재귀
def fibo(n):
    if n==1: return 1
    elif n==0: return 0
    return fibo(n-2)+ fibo(n-1)
print(fibo(n))

# 1. 재귀 + 메모리제이션
cache=[-1] * 91
cache[0]=0
cache[1]=1
def fibo(n):
    if cache[n] == -1:  #접근한 적이 없을 때 새로 구함
        cache[n] = fibo(n-2) + fibo(n-1)
    return cache[n]

#2. 반복
fibo = [0,1]
for i in range(2, n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-1])