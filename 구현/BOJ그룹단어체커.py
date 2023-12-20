#https://www.acmicpc.net/problem/1316
# 구현 > 문자열

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
arr = []
[arr.append(input().strip()) for _ in range(n)]
re = 0
for word in arr:
    tmp = []
    before = ''
    for alpha in word:
        if before == '':
            tmp.append(alpha)
        else:
            if alpha != before:
                if alpha in tmp:
                    break
                else:
                    tmp.append(alpha)
        before = alpha
    else:
        re += 1
print(re)


'''
[사고의 전환]
나왔던 알파벳이 이후에 또 있으면 바로 break 
 
 for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
'''
