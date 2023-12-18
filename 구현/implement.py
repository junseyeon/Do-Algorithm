import sys
input = sys.stdin.readline

# 백준 17608  막대기 
# 길이가 긴게 앞에 있으면 그 뒤로는 작은게 안보임 (**문제 해결력,, 키우자 **)
""" N = int(input())
arr = [ int(input()) for _ in range(N)]
standard = arr[-1]
re=1
for i in reversed(arr):
    if i > standard:
        re +=1
        standard = i
print(re) """



#백준 19939 박 터뜨리기 
# ** 다시풀기,,, 등차수열 사용 
""" N, K = map(int, input().split())
ball = N - (K+1) * K // 2
print(ball)
if ball < 0:
    print(-1)
else:
    if ball % K:
        print(K)
    else:
        print(K-1) """

#지우개(정올 2021)[백준 21756]
N = int(input())
arr = [i+1 for i in range(N)]
while len(arr) > 1:
    arr = arr[1::2]
print(arr[0])
