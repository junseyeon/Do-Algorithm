import sys, heapq as hq
sys.stdin = open('../input.txt')
input = sys.stdin.readline

# 방법1: 양수, 음수 별도로 저장하고 비교해서 출력
# N = int(input())
# pq = []  #양수 저장
# mq = []  #음수 저장
# for i in range(N):
#     num = int(input())
#     if num == 0:  #출력+제거/절댓값이 작은 것
#         if pq and mq:
#             if pq[0] < mq[0]:
#                 print(hq.heappop(pq))
#             else: #  pq[0] == mq[0], pq[0] > mq[0]:
#                 print(-hq.heappop(mq))
#         elif pq:
#             print(hq.heappop(pq))
#         elif mq:
#             print(-hq.heappop(mq))
#         else:
#             print(0)
#     else:
#         if num > 0: hq.heappush(pq, num)
#         else: hq.heappush(mq, abs(num))


# 방법2: tuple로 앞에 abs로 우선순위르 판별하고 실제값은 뒤에다가
N = int(input())
pq = []
for i in range(N):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))  #순서도 중요..
    else:
        print(  hq.heappop(pq)[1] if pq else 0)

'''
최소값을 찾고 삭제하는 시간복잡도를 쥴이기 위해 heapq
출력은 원본대로, 최소값은 절댓값으로 판별... 

[포인트] 우선순위 힙에서 리스트를 사용할 수 있는지 
'''