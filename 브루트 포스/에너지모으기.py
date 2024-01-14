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
'''
def energy(lst, tmp):
    global ans                              # ans를 global 변수로 선언하고
    if len(lst) == 2:                       # 에너지 구슬이 2개만 남았다면
        ans = max(tmp, ans)                 # 현재 에너지와 최대 에너지 중 더 큰 값을 ans에 저장하고
        return                              # return 한다
    for i in range(1, len(lst)-1):          # 맨 앞과 뒤를 제외한 에너지구슬을 반복해서
        WW = lst[:i] + lst[i+1:]            # i번째 구슬을 제외한 리스트를 WW에 저장하고
        energy(WW, tmp+lst[i-1]*lst[i+1])   # energy 함수를 통해 에너지를 모은다
'''