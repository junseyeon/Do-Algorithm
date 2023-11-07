#붓을 최대 한 번 이용한 후 주어진 그림에 2 × 2 크기의 X로만 이루어진 영역이 있을 수 있는지

# -*- coding: utf-8 -*-
import sys
a = [input() for _ in range(4)]
for i in range(3):
    for j in range(3):
        tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
        if tmp.count('X') > 2:
            print('yes')
            exit()
else:print('no')