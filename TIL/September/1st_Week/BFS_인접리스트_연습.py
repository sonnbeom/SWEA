'''
예상 출력 값: [False, True, True, True, True, False]

n = 5 m = 4
3 4
1 4
2 3
4 5

예상 출력 값: [False, True, True, True, True, True]

'''
from collections import deque
def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        tmp = q.popleft()
        for node in bfs_list[tmp]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
n = 5
m = 4

bfs_list = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    bfs_list[a].append(b)
    bfs_list[b].append(a)

visited = [False for _ in range(n+1)]

bfs(1)

print(visited)
visited.pop()
print(visited)