from collections import deque
import itertools

n = int(input())

population = list(map(int, input().split()))

idx_list = [i for i in range(1, n+1)]
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    node_input = list(map(int, input().split()))
    t = node_input.pop(0)
    for node in node_input:
        arr[i][node] = 1
        arr[node][i] = 1

def is_same(req, target):
    for t in target:
        if t not in req:
            return False
    return True

def bfs(start, target):
    visited = [0 for _ in range(n+1)] # 0이 방문하지 않은 것

    q = deque([start])
    visited[start] = 1
    res = [start]

    while q:
        node = q.popleft()
        for i in range(1, n+1):
            if arr[node][i] != 0 and visited[i] != 1 and i in target:
                q.append(i)
                visited[i] = 1
                res.append(i)
    if is_same(res, target):
        return target
    else:
        return 0
minimum = int(1e9)


can = False
for i in range(1, n//2+1):
    permu2 = list(itertools.permutations(idx_list, i))
    permu = set(permu2)
    for country in permu:
        country = list(country)
        ya_conuntry = []
        for i in range(1, n+1):
            if i not in country:
                ya_conuntry.append(i)

        yu_result = bfs(country[0], country)
        ya_result = bfs(ya_conuntry[0], ya_conuntry)

        if yu_result != 0 and ya_result != 0:

            can = True
            yu_sum = 0
            for i in yu_result:
                yu_sum += population[i-1]
            ya_sum = 0
            for i in ya_result:
                ya_sum += population[i-1]
            minimum = min(minimum, abs(ya_sum - yu_sum))

if can:
    print(minimum)
else:
    print(-1)


