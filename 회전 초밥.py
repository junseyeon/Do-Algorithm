#회전 초밥
#https://www.acmicpc.net/problem/2531
arr=[]
n, d, k, c = map(int, input().split())   #접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가
for _ in range(n):
    arr.append(int(input()))

re = []
cnt = dict()
for i in range(k):
    i = arr[i]
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i] = 1

if c not in list(cnt.keys()):
    re.append(len(cnt)+1)
else:
    re.append(len(cnt))

for i in range(k, n):
    last = cnt[arr[i-k]]
    if last ==1: cnt[]
    i = arr[i]
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
    if c not in list(cnt.keys()):
        t = len(cnt)+1
    else:
        t = len(cnt)
    re.append(t)
    print(cnt)

print(max(re))
