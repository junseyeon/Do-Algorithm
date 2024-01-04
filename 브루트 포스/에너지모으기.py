#https://www.acmicpc.net/problem/16198
n = int(input())
arr = list(map(int, input().split()))

re = 0
while len(arr) > 2:
    max_num = 0
    max_i = 0
    for i in range(1,len(arr)-1):
        #print(i-1, i+1)
        tmp = arr[i-1] * arr[i+1]
        if max_num < tmp :
            max_num = tmp
            max_i = i
    re += max_num
    del arr[i]
    print
    #print(arr,max_i, max_num)
print(re)      

#미완성