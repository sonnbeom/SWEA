import sys
from collections import defaultdict


# 시간복잡도 125,000,000,000,000

def dfs(depth, temp):
    if depth == 3:
        print(f'temp = {temp}')
        temp.sort()
        mid = temp[1]

        dic[mid] += 1
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            dfs(depth + 1, temp)
            temp.pop()
            # visited[i] = False


n, q = map(int, input().split())
arr = list(map(int, input().split()))
mid_list = []
for _ in range(q):
    i = int(input())
    mid_list.append(i)
dic = defaultdict(int)
visited = [False for _ in range(n)]
dfs(0, [])

for mid in mid_list:
    print(dic[mid])
