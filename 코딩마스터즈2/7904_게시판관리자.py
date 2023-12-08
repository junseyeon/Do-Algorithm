'''
buy our merch"에 광고 차단 필터가 적용되었다면, 악성 사용자는 "merch our buy", "buy merch our"등의 문장을 제목으로 사용합니다.
하지만, "our merch buy"는 어떤 두 단어의 자리를 바꾸어도 "buy our merch"가 되지 못하므로 제목으로 사용하지 않습니다.

=> 2개의 단어 위치 빼고는 다른 단어는 위치가 같아야함
'''

import sys
import itertools
N = int(sys.stdin.readline())
arr1 = sys.stdin.readline().strip().split()
arr_d = {v: i for i, v in enumerate(arr1)}
arr2 = sys.stdin.readline().strip().split()
arr2_d = {i: arr_d[i] for i in arr2}
v1 = list(arr_d.values())
v2 = list(arr2_d.values())
re = 0

diff = sum(1 for char1, char2 in zip(v1, v2) if char1 != char2)
if diff==2: print(0)
elif diff==1: print(2)
else: print(diff)
#print( list(itertools.permutations(range(diff), 3)))



# import sys
#
# N = int(sys.stdin.readline())
# arr1 = sys.stdin.readline().strip().split()
# arr_d = {v: i for i, v in enumerate(arr1)}
# arr2 = sys.stdin.readline().strip().split()
# arr2_d = {i: arr_d[i] for i in arr2}
# v1 = list(arr_d.values())
# v2 = list(arr2_d.values())
# re = 0
#
# for c1 in range(N):
#     for c2 in range(c1 + 1, N):
#         v1[c1], v1[c2] = v1[c2], v1[c1]
#         if 2 == sum(1 for char1, char2 in zip(v1, v2) if char1 != char2):
#             re += 1
#         v1[c2], v1[c1] = v1[c1], v1[c2]
#
# print(re)

# import sys
# from itertools import combinations
#
# N = int(sys.stdin.readline())
# arr1 = sys.stdin.readline().strip().split()
# arr_d = {v: i for i, v in enumerate(arr1)}
# arr2 = sys.stdin.readline().strip().split()
# arr2_d = {i: arr_d[i] for i in arr2}
# v1 = list(arr_d.values())
# v2 = list(arr2_d.values())
# re = 0
#
# for c1,c2 in combinations(range(N), 2):
#     v1[c1], v1[c2] = v1[c2], v1[c1]
#     if 2 == sum(1 for char1, char2 in zip(v1, v2) if char1 != char2): re+=1
#     v1[c2], v1[c1] = v1[c1], v1[c2]
# print(re)


#
# #
# import sys
# from itertools import permutations
#
# def count_diff(word1, word2):
#     return sum(1 for char1, char2 in zip(word1, word2) if char1 != char2)
#
# N = int(sys.stdin.readline())
# arr1 = sys.stdin.readline().strip().split()
# arr2 = sys.stdin.readline().strip().split()
# re = 0
#
# for sentence in permutations(arr1, len(arr1)):
#     if list(sentence) == arr1 or list(sentence) == arr2:
#         continue
#
#     cnt1 = count_diff(sentence, arr1)
#     cnt2 = count_diff(sentence, arr2)
#
#     if cnt1 <= 2 and cnt2 <= 2:
#         re += 1
#
# print(re)




'''
# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
arr1 = sys.stdin.readline().strip().split()
arr2 = sys.stdin.readline().strip().split()
new_arr1=[]
new_arr2=[]

for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        arr1[i], arr1[j] = arr1[j], arr1[i]
        new_arr1.append(arr1[:])
        arr1[i], arr1[j] = arr1[j], arr1[i]
        
        arr2[i], arr2[j] = arr2[j], arr2[i]
        new_arr2.append(arr2[:])
        arr2[i], arr2[j] = arr2[j], arr2[i]

# print(new_arr1)
# print(new_arr2)

re=0
for i in new_arr1:
    for j in new_arr2:
        if i==j:re+=1
print(re)


# def count_matching_titles(N, title1, title2):
#     words1 = title1.split()
#     words2 = title2.split()
    
#     # 첫 번째 문장의 각 단어가 두 번째 문장에서 등장하는지 확인
#     matching_titles_count = 0
#     for i in range(N):
#         word1 = words1[i]
#         word2 = words2[i]
#         if word1 != word2:
#             matching_titles_count += 1
    
#     print(matching_titles_count)

# # 입력값 받기
# N = int(input())
# title1 = input()
# title2 = input()

# count_matching_titles(N, title1, title2)

'''