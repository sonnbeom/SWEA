from collections import deque
import itertools

n = int(input())
population = list(map(int, input().split()))

arr = [0 for _ in range(n+1) for _ in range(n+1)]

for i in range(n):
    node_input = list(map(int, input().split()))
    t = node_input.pop(0)
    for n in node_input:
        arr[i][n] = 1
        arr[n][i] = 1
def bfs(start, target):
    visited = [0 for _ in range(n)] # 0이 방문하지 않은 것
    q = deque([start])
    visited[start] = 1
    res = -1
    while q:
        node = q.popleft()
        for i in range(n):
            if arr[node][i] != 0 and visited[i] != 1 and i in target:
                q.append(i)
                visited[i] = 1
                res.


permu = list(itertools.permutations(population, 2))
for p in permu:
    yu = p[0] #첫번째 마을
    ya = p[1]  #두번째 마을
    bfs(yu[0], yu)
    bfs(ya[0], ya)

