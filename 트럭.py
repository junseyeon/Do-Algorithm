# https://www.acmicpc.net/problem/13335
from collections import deque
n, w, l = map(int, input().split())  # 트럭수, 다리길이, 최대하중
truck = deque(map(int, input().split()))  # 트럭들 무게
time = 0  # 경과 시간
truck_loc = deque() #다리 위 트럭들의 위치
now_truck = deque() #다리 위에 어떤 트럭이 있는지

while truck or now_truck:
    # 기존에 있던 truck_loc 전부 하나씩 이동
    for i in range(len(truck_loc)):
        truck_loc[i] += 1
    
    # 트럭이 다리에 들어 올 수 있는지 
    if truck and sum(now_truck)+truck[0] <= l and len(now_truck) < w:
        t = truck.popleft()
        now_truck.append(t)
        truck_loc.append(1)

    # 트럭이 다리에서 빠져 나갈 때 
    if truck_loc[0] >= w:
        truck_loc.popleft()
        now_truck.popleft()
    time += 1
print(time+1)