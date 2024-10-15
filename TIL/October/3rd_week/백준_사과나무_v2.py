from itertools import combinations

import itertools

a = itertools.combinations([1], 3)
n = int(input())

arr = list(map(int, input().split()))

arr.sort()
len_arr = 0
res = False
while True:
    one_cnt = 1
    two_cnt = 1
    if len(arr) == 1:
        len_arr = 1
        break
    if arr[0] >= 1:
        arr[0] -= 1
        one_cnt -= 1
        if arr[0] == 0:
            arr.pop()
    if arr[-1] >= 2:
        arr[-1] -= 2
        two_cnt -= 1
        if arr[-1] == 1:
            arr.pop(-1)
            arr.insert(0,1)
        if arr[-1] == 0:
            arr.pop(-1)
    if len(arr) == 0:
        res = True
    if one_cnt == 1 or two_cnt == 1:
        break
check = 0
if len(arr) == 0:
    res = True
if not res:
    if max(arr) == 0:
        res = True

if not res:
    for a in arr:
        if a == 0:
            pass
        elif a <= 2:
            break
        elif a % 3 == 0:
            res = True
print(arr)
if res:
    print("YES")
else:
    print("NO")


