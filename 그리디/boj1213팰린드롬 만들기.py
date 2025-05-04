'''
임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

입력
첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

예제 입력 1
AABB
예제 출력 1
ABBA

[해결 방안]
- 알파벳 홀수가 1개 이상이면 안됨
- 나머지는 짝수 갯수 만큼 있어야 함
- 반은 순서대로, 반은 거꾸로 뒤집어서
- 사전순으로 출력임으로 넣은 후 정렬

map = {a:2}
'''
#필린드롬: 거꾸로 읽어도 제대로 읽는 것과 같은 문장


from collections import defaultdict
name = input()

alpha = defaultdict(int)
for x in name:
    alpha[x]+=1

alpha = dict(sorted(alpha.items())) #dict상태 그대로 Key값 기준으로 정렬
alpha_value = alpha.values()

odd = 0
ans = []
x = ''
for i in alpha_value:
    if i%2 != 0:
        odd+=1
    if odd>1:
        print("I'm Sorry Hansoo")
        break
else:
    for k, v in alpha.items():
        ans.append(k*(v//2))
        if v%2!=0:
            x = k
    ans2 = reversed(ans)
    print(''.join(map(str,ans)) + x + ''.join(map(str,ans2)))







