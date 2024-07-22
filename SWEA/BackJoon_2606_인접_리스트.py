from collections import deque

node = int(input())
edge = int(input())

arr = [[] for _ in range(node+1)]
visited = [False] * (node+1)

for i in range(edge):
    a,b = map(int, input().split())
    arr[a].append[b]
    arr[b].append[a]

q = deque([1])
visited[1] = True

def bfs():
    