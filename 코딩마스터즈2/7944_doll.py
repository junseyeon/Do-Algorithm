T = int(input())  # 테스트 케이스의 개수
re = []
for _ in range(T):
    # 민규가 받은 곰인형의 개수 N과 로봇의 개수 K
    N, K = map(int, input().split())

    # A상자에 들어가는 곰인형과 로봇의 개수
    a1, a2 = map(int, input().split())

    # B상자에 들어가는 곰인형과 로봇의 개수
    b1, b2 = map(int, input().split())

    if (N > a1 and K > a2 )or(N > b1 and K > b2 ):
        re.append("NO")
    elif  N > 0 and K>0 and  (N % a1==0 and K%a2==0) or (N % b1==0 and K%b2==0):
        re.append("YES1")
    elif (N > 0) and (K==0) and ((N % a1==0) or (N % b1==0 )):
        print(N, K)
        re.append("YES2")
    elif K > 0 and N==0 and ((K % a1==0) or (K % b1==0 )):
        re.append("YES3")
    elif  N % (a1+b1)==0  and K%(a2+b2)==0:
        re.append("YES4")
    else:
        re.append("NO")

print(*re)