## 13 in 123 (X) 한 자리씩 확인
## 33 in 113 (X) 3이 2개 확인
# 21 in 127 (X)
# 99 19..?
""" import sys
k = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip().split())
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
chk=0
cnt=2  #소수 시작 번호 

while chk < k:
    if is_prime(cnt):
        removed_num = arr[chk]  # 지워진 수 (str)
        target = str(cnt) # 맞추려는 소수 
        tmp = True 
        for n in removed_num: 
            if n in target:
                #print(n , target , end = ' ')
                t = target.find(n)+1
                target = target[t:]
            else: 
                tmp=False
                break
        if tmp:
            #print(cnt)
            chk+=1
    cnt+=1
print(cnt-1) """


import sys
k = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip().split())
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
chk=0  # 타겟 소수
cnt=2  # 검증용 소수 시작 번호

while chk < k:
    if is_prime(cnt):
        prime = str(cnt) # 맞추려는 소수
        if arr[chk] in prime:
            chk+=1
            #print(cnt)
    cnt+=1
print(cnt-1)