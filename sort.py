#국영수 백준 10825

#알고리즘
#1. 국어점수 reverse=True
#2. 국어점수, 영어점수(reverse=False)
#3. 국어, 영어, 수학(reverse=True)
#4. 이름 아스키코드 빠른순 reverse=False 

#알게된 점
#student를 dict로 받아도 되고 list & tuple로 받아도 될듯? [(),()] 
# reverse말고 -로 Reversed역할을 할수 있다!!!
# 영어도 sorted가 가능하다!!

import sys
input = sys.stdin.readline
N = int(input())
student = dict()
for i in range(N):
    name, kor, eng, math = input().split()
    student[name]=[int(kor),int(eng),int(math)]

re = sorted(student.items(), key = lambda item: (-item[1][0],item[1][1], -item[1][2], item[0]))
print(*list(map(lambda x: x[0], re)), sep='\n')
