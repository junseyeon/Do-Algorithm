import sys
sys.stdin = open('../input.txt')
input  = sys.stdin.readline

n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

tape_loc = 0
re = 0
for i in arr:
    if tape_loc < i-0.5:
        tape_loc = i-0.5+l
        re+=1
    elif tape_loc < i+0.5:
        tape_loc += l
        re+=1
    else:
        pass

print(re)


