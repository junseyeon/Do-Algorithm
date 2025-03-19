import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

n  = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))

for ps in arr:
    flag = True
    stack = []
    for i in ps:
        if i=='(':
            stack.append('(')
        elif i==')':
            if stack: stack.pop()
            else:
                flag = False
                break
        #print(i, stack, flag)

    if len(stack) > 0:
        flag = False

    print('YES' if flag else 'NO')