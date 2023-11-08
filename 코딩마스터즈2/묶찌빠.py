#1) 가위바위보 이길 때 까지 선공후공
#2) 경기 비교하기 
# if 선공 > 후공 : 다시 진행 
# elif 선공 < 후공 : 공수교대 
# elif 선공 == 후공 : 선공 승 

## 우승자가 정해질 때 까지 계속 ,,,
import sys
N,M = map(int,sys.stdin.readline().split())
rcp = []
for i in range(2):rcp.append(tuple(map(int,input().split())))
def iswin(a,b):  
    re='' #a기준
    if a==b: re='tie'
    elif (a==1 and b==3) or (a==2 and b==1) or ( a==3 and b==2): re='win'
    else: re='lose'
    return re

attack = -1 
cnt = 0  #전체 
winner = -1 #우승자 

while attack==-1:  #정해지지 않았으면 계속
    if cnt == N : 
        print(0) 
        exit(0)
    a=rcp[0][cnt]
    b=rcp[1][cnt]
    tmp = iswin(a,b)
    if tmp == 'tie': attack=-1
    elif tmp=='win': attack=0
    else: attack=1
    cnt+=1
j =0 
while winner == -1:
    if j> N*2: break   #무한반복 방지
    cnt %= N
    a_value = rcp[attack][cnt]
    d_value = rcp[1-attack][cnt]
    tmp = iswin(a_value, d_value)
    if tmp == 'win' : pass
    elif tmp=='lose' : attack= 1-attack
    elif tmp=='tie' : winner = attack
    cnt+=1
    j+=1
if winner>-1: print(winner+1)
else: print(0)