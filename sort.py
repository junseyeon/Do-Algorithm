#국영수 백준 10825

#알고리즘
# 1. 국어 reverse=True
# 2. 국어, 영어(reverse=False)
# 3. 국어, 영어, 수학(reverse=True)
# 4. 이름 아스키코드 빠른순 (reverse=False)

#알게된 점
#student를 dict로 받아도 되고 list & tuple로 받아도 될듯? [(),()] 
# reverse말고 -로 Reversed역할을 할수 있다!!!
# 문자열도 sorted가 가능하다!!

import sys
input = sys.stdin.readline
N = int(input())
arr = dict()
for i in range(N):
    name, kor, eng, math = input().split()
    arr[name]=[int(kor),int(eng),int(math)]

re = sorted(arr.items(), key = lambda item: (-item[1][0],item[1][1], -item[1][2], item[0]))
print(*list(map(lambda x: x[0], re)), sep='\n')


# packing, unpacking
arr = [] 
for _ in range(N):
    name, *scores = input().split()  #socres: list 
    arr.append((name, *map(int, scores)))   #list요소를 int로 바꾼뒤 unpacking

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]) )
for i in arr:
    print(i[0])
