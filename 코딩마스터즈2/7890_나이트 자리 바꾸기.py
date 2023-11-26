board = []
for _ in range(3):
    row = input().strip()
    board.append(row)
white_knights = []  # 흰색 나이트의 좌표 리스트
black_knights = []  # 검정 나이트의 좌표 리스트

# 체스판을 순회하면서 흰색 나이트와 검정 나이트의 좌표를 저장
for i in range(3):
    for j in range(3):
        if board[i][j] == '1':
            white_knights.append((i, j))
        elif board[i][j] == '2':
            black_knights.append((i, j))
g = []
for x,y in white_knights:
    for i in [(x-1, y+2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x+2, y-1), (x+2, y+1), (x-1, y-2), (x+1, y-2)]:
        if i in black_knights:
            g.append(i)
if len(g)>=2: print('possible')
else: print('impossible')
