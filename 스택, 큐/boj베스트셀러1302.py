import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N = int(input())
sell = {}
max_x = 0
max_n = []

for i in range(N):
    name=input().strip()
    if name in sell: # name in sell.keys() 와 같음
        sell[name]+=1
    else:
        sell[name]=1

    if max_x < sell[name]:
        max_x = sell[name]
        max_n = [name]
    elif max_x == sell[name]:
        max_n.append(name)

print(sorted(max_n)[0])