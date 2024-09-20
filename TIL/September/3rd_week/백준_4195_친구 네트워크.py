'''
1. 서로 넣어주면 되는 거 아닌가?
map 형태로
키 밸류에서
각 키에 해당 값을 추가해주고 밸류 -> 키 값이기도 함
그럼 이 키 값을 통해 -> 다시 map에 추가해준다.
이 과정에서 value의 값이 가장 큰 값을 구하고  key 갯수인 1을 더해주자.

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
    value_one = dic[fone]
    value_two = dic[ftwo]

    if len(value_one) > 1:
        for key in value_one:
            dic[key].append(ftwo)
