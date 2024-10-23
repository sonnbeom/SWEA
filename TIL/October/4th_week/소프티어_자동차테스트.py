import sys
from collections import defaultdict


def get_mid(req):
    temp = req[:]
    temp.sort()
    return temp[1]


def dfs(depth, start, temp):
    if depth == 3:
        mid = get_mid(temp)
        dic[mid] += 1
        return
    for i in range(start, len(arr)):
        temp.append(arr[i])
        dfs(depth + 1, i + 1, temp)
        temp.pop()


n, q = map(int, input().split())
arr = list(map(int, input().split()))
mid_list = []
for _ in range(q):
    i = int(input())
    mid_list.append(i)
dic = defaultdict(int)
dfs(0, 0, [])

for mid in mid_list:
    print(dic[mid])
