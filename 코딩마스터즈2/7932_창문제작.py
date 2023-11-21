# -*- coding: utf-8 -*-
import sys, math
from decimal import Decimal
N, a, b = map(int,sys.stdin.readline().split())

# 처음 창틀 1개 갖고 있음 N개가 목표 (n개 창틀, n개 유리)
# 1개 = a개 창틀
# b개 = 1개 유리

cnt = 1
ff = a-1
needframe= b*N-ff  #N개 유리를 위해 필요한 창틀 수

cnt = math.ceil(Decimal(needframe)/Decimal(a-1))    # 유리를 위해 거래할 수
ff += Decimal(cnt)*Decimal(a-1)  # 갖고 있는 창틀 수

tmp = Decimal(ff)/Decimal(b)  # 유리 거래 수
cnt += int(tmp)

frame = ff-(tmp*b)  # 거래 후 남은 창틀 수
cnt += math.ceil((N-frame)/(a-1))
print(cnt)


# frame = a
# glass = 0
# cnt = 1 #무조건 1번은 1로 거래하면서 시작
# while glass != N :
#     if frame >= b:
#         glass+=1
#         frame-=b
#     else:
#         frame = frame - 1 + a
#     cnt+=1
# print(cnt, frame)
# while frame < N:
#     frame = frame - 1 + a
#     cnt+=1
# print(cnt)


### 결국...
import sys, math
from decimal import Decimal
N, a, b = map(int,sys.stdin.readline().split())

if N > 10000000:
    needframe= b*N-1  #N개 유리를 위해 필요한 창틀 수
    cnt  = math.ceil(Decimal(needframe)/Decimal(a-1)) #+(b*N)//b   # 유리를 위해 거래한 수
    now = 1 + cnt*(a-1)  # 갖고 있는 창틀 수
    tmp = Decimal(now)/Decimal(b)  # 유리 거래 수
    cnt += int(tmp)
    frame = now-(tmp*b)  # 거래 후 남은 창틀 수
    cnt += math.ceil((N-frame)/(a-1))
    print(cnt)
else:
    frame = a
    glass = 0
    cnt = 1 #무조건 1번은 1로 거래하면서 시작
    while glass != N :
        if frame >= b:
            glass+=1
            frame-=b
        else:
            frame = frame - 1 + a
        cnt+=1
    #print(cnt, frame)
    while frame < N:
        frame = frame - 1 + a
        cnt+=1
    print(cnt)