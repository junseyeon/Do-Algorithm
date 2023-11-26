import math
n = int(input())
if n==1:
    print(0)
    exit(0)
if n==2:
    print(1)
    exit(0)
line = 1
tt=0
re=[]
while tt<1000:
    line+=tt
    re.append(line)
    tt+=1
#print(re[:10])
for i,v in enumerate(re):
    if n <= v:
        print(i)
        break