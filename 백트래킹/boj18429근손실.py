'''
https://wikidocs.net/235564
'''
ii = lambda : map(int, input().split())

N, K = ii()
arr = list(ii())
ans = 0
visited = [False] * N
def dp(n, weight):  #날짜, 무게
    global ans
    if weight < 500: return
    if n == N:
        ans +=1
        return
    weight-=K
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            print(n, arr[i])
            dp(n+1, weight+arr[i])
            visited[i] = False #함수가 종료되면 visited[i]를 False로 바꿔 하여 다음 운동 키트에서 다시 체크하도록 합니다.

dp(0,500)
print(ans)

'''
3 4
3 7 5
---
[해석]
큰 dfs는 운동 키트의 갯수: 여기는 6번 
하나의 운동 키느 ex)1-2-3  순서가 작은 for문

3,7,5       # 첫 날 3에서 부터  500이 안넘어서 그 뒤에는 볼 필요가 없음.
3 5 7       
  
  
7 5 3       # 
7 3 5 

5 3 7 
5 7 3 

4
'''
