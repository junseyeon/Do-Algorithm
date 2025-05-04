arr = [[-1]*10 for _ in range(10)]
k = 0
for i in range(10):
    for j in range(10):
        arr[i][j] = k
        k+=1
print(arr)
print(arr[0:4][2])  # 행, 열