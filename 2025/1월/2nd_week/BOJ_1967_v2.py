def find(start, now): # 가장 먼 지점 찾기
    for a, b in tree[start]:
        if visited[a] == -1:
            visited[a] = b + now
            find(a, visited[a])

import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append([c,w])
    tree[c].append([p,w])

visited = [-1]*(n+1)
visited[1] = 0
find(1,0) # 가장 먼 지점을 먼저 찾고

print(f'visited = {visited}')
start = visited.index(max(visited))
print(start)
visited = [-1]*(n+1)
visited[start] = 0
find(start,0) # 다시 가장 먼 지점을 찾아주자.
print(f'visited2 = {visited}')
print(max(visited))
