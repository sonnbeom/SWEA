'''
1. 서로 넣어주면 되는 거 아닌가?
map 형태로
키 밸류에서
각 키에 해당 값을 추가해주고 밸류 -> 키 값이기도 함
그럼 이 키 값을 통해 -> 다시 map에 추가해준다.
이 과정에서 value의 값이 가장 큰 값을 구하고  key 갯수인 1을 더해주자.

1.키를 통해 조회한다.
2. 만약 리스트가 null이 아니라면
3. 주어진 값에 기존 값을 더해준다 (존재하지 않는다면 말이다)
ex a b
b c

c 에도 a b 를 넣어줘야 한다.
4. 리스트를 돌면서 각 밸류에 주어진 값을 넣는다.
ex a b
b c
b 밸류를 조회 a에도 c를 더해준다.
5. b에 c를 더해준다.

'''

from collections import defaultdict

dic = defaultdict(list)

tc = int(input())
f = int(input())
trial_list = []
for i in range(f):
    a, b = map(str, input().split())
    trial_list.append((a, b))

for fone, ftwo in trial_list:
    value_one_list = dic[fone]
    value_two_list = dic[ftwo]

    if len(value_one_list) > 1:
        for value_one in value_one_list:
            if value_one not in dic[ftwo]:
                dic[ftwo].append(value_one)

    dic[ftwo].append(fone)


