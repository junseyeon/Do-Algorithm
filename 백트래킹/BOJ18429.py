mil = lambda : map(int, input().split())

n, k  = mil()
a = list(mil())

weight = 500

def dfs(now, weight):
    global ans
    weight -= k
    if weight < 500:
        pass
    if now > 4:
        return 0


    for i in range(n):
        dfs(now+1, weight)

dfs(0, weight)





