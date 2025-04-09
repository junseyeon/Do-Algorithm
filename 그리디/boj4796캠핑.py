'''
캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다.
강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

입출력
5 8 20 / 14
5 8 17 / 11
0 0 0
'''
l = p = v = 1
while l != 0 and p != 0 and v != 0:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0: break
    cnt = 0
    cnt += (v//p) * l
    cnt += (v%p)
    print(cnt)



1 2 3 4

# 1 2 3 4 5 6 7 8 / 9 10 11 12 13 14 15 16 /17 18 19 20