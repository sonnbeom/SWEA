'''
작은 순서

'''

t = int(input())
res = []
for tc in range(t):
    tmp_list = []
    reverse_list = []

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    while True:

        if len(arr) == 0:
            break
        tmp_list.append(arr.pop(0))

        if len(arr) == 0:
            break
        reverse_list.append(arr.pop(-0))

    reverse_list.reverse()

    for r in reverse_list:
        tmp_list.append(r)

    answer = abs(tmp_list[0]-tmp_list[-1])

    for i in range(len(tmp_list)-1):
        diff = abs(tmp_list[i]-tmp_list[i+1])
        answer = max(answer, diff)

    res.append(answer)

for r in res:
    print(r)